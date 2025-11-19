#!/usr/bin/env python3
"""
Generate SVG technical drawing for X-Gantry assembly
Shows top view with dimensions and rivnut hole positions
"""

import svgwrite

# Dimensions in inches
X_TUBE_LENGTH = 40  # inches
X_TUBE_WIDTH = 2    # inches
X_TUBE_HEIGHT = 3   # inches
CROSS_BRACE_LENGTH = 8  # inches

# Conversion
SCALE = 40  # pixels per inch for drawing (larger scale for detail)

def inch_to_px(inches):
    """Convert inches to pixels for drawing"""
    return inches * SCALE

def create_x_gantry_top_view():
    """Create top view of X-gantry with dimensions and rivnut positions"""

    # Drawing size
    width_px = inch_to_px(X_TUBE_LENGTH + 10)
    height_px = inch_to_px(CROSS_BRACE_LENGTH + X_TUBE_WIDTH * 2 + 10)

    dwg = svgwrite.Drawing(
        'x-gantry-top-view.svg',
        size=(f'{width_px}px', f'{height_px}px'),
        profile='full'
    )

    # Define styles
    dwg.defs.add(dwg.style('''
        .frame { fill: lightgray; stroke: black; stroke-width: 2; }
        .dimension-line { stroke: red; stroke-width: 1; fill: none; }
        .dimension-text { font-family: Arial; font-size: 14px; fill: red; }
        .label-text { font-family: Arial; font-size: 11px; fill: black; }
        .rivnut-hole { fill: blue; stroke: navy; stroke-width: 1; }
        .rivnut-hole-top { fill: lime; stroke: green; stroke-width: 1; }
        .rivnut-hole-bottom { fill: cyan; stroke: blue; stroke-width: 1; }
    '''))

    # Offset for margins
    offset_x = inch_to_px(5)
    offset_y = inch_to_px(5)

    # Draw first 40" tube (front)
    tube1_x = offset_x + inch_to_px(X_TUBE_WIDTH)
    tube1_y = offset_y
    tube1_width = inch_to_px(X_TUBE_LENGTH)
    tube1_height = inch_to_px(X_TUBE_WIDTH)

    dwg.add(dwg.rect(
        insert=(tube1_x, tube1_y),
        size=(tube1_width, tube1_height),
        class_='frame'
    ))

    # Draw second 40" tube (rear, spaced 8" apart)
    tube2_x = offset_x + inch_to_px(X_TUBE_WIDTH)
    tube2_y = offset_y + inch_to_px(X_TUBE_WIDTH) + inch_to_px(CROSS_BRACE_LENGTH)
    tube2_width = inch_to_px(X_TUBE_LENGTH)
    tube2_height = inch_to_px(X_TUBE_WIDTH)

    dwg.add(dwg.rect(
        insert=(tube2_x, tube2_y),
        size=(tube2_width, tube2_height),
        class_='frame'
    ))

    # Draw left cross-brace (8")
    brace1_x = offset_x
    brace1_y = offset_y + inch_to_px(X_TUBE_WIDTH)
    brace1_width = inch_to_px(X_TUBE_WIDTH)
    brace1_height = inch_to_px(CROSS_BRACE_LENGTH)

    dwg.add(dwg.rect(
        insert=(brace1_x, brace1_y),
        size=(brace1_width, brace1_height),
        class_='frame'
    ))

    # Draw right cross-brace (8")
    brace2_x = offset_x + inch_to_px(X_TUBE_WIDTH) + inch_to_px(X_TUBE_LENGTH)
    brace2_y = offset_y + inch_to_px(X_TUBE_WIDTH)
    brace2_width = inch_to_px(X_TUBE_WIDTH)
    brace2_height = inch_to_px(CROSS_BRACE_LENGTH)

    dwg.add(dwg.rect(
        insert=(brace2_x, brace2_y),
        size=(brace2_width, brace2_height),
        class_='frame'
    ))

    # Mark rivnut positions at corners (8 per corner: 4 top + 4 bottom)
    # We'll show top rivnuts as green, bottom as cyan for clarity

    corner_positions = [
        # (x_center, y_center, label)
        (brace1_x + inch_to_px(X_TUBE_WIDTH/2), brace1_y + inch_to_px(0.5), 'Corner 1 (FL)'),
        (brace2_x + inch_to_px(X_TUBE_WIDTH/2), brace1_y + inch_to_px(0.5), 'Corner 2 (FR)'),
        (brace1_x + inch_to_px(X_TUBE_WIDTH/2), brace1_y + inch_to_px(CROSS_BRACE_LENGTH - 0.5), 'Corner 3 (RL)'),
        (brace2_x + inch_to_px(X_TUBE_WIDTH/2), brace1_y + inch_to_px(CROSS_BRACE_LENGTH - 0.5), 'Corner 4 (RR)'),
    ]

    for cx, cy, label in corner_positions:
        # Draw 4 top rivnuts (green) in a small pattern
        for i, (dx, dy) in enumerate([(- 0.2, -0.2), (0.2, -0.2), (-0.2, 0.2), (0.2, 0.2)]):
            dwg.add(dwg.circle(
                center=(cx + inch_to_px(dx), cy + inch_to_px(dy)),
                r=2,
                class_='rivnut-hole-top'
            ))

        # Draw 4 bottom rivnuts (cyan) slightly offset
        for i, (dx, dy) in enumerate([(-0.6, -0.2), (-0.6, 0.2), (-1.0, -0.2), (-1.0, 0.2)]):
            dwg.add(dwg.circle(
                center=(cx + inch_to_px(dx), cy + inch_to_px(dy)),
                r=2,
                class_='rivnut-hole-bottom'
            ))

        # Label
        dwg.add(dwg.text(
            label,
            insert=(cx, cy - inch_to_px(0.5)),
            class_='label-text',
            text_anchor='middle'
        ))

    # Add dimensions

    # Overall length (40")
    dim_y = offset_y + tube2_y + tube2_height + inch_to_px(1)
    dwg.add(dwg.line(
        start=(tube1_x, dim_y),
        end=(tube1_x + tube1_width, dim_y),
        class_='dimension-line'
    ))
    dwg.add(dwg.text(
        '40.00"',
        insert=(tube1_x + tube1_width/2, dim_y + 15),
        class_='dimension-text',
        text_anchor='middle'
    ))

    # Internal height (8")
    dim_x = offset_x - inch_to_px(1)
    dwg.add(dwg.line(
        start=(dim_x, brace1_y),
        end=(dim_x, brace1_y + brace1_height),
        class_='dimension-line'
    ))
    dwg.add(dwg.text(
        '8.00"',
        insert=(dim_x - 10, brace1_y + brace1_height/2),
        class_='dimension-text',
        text_anchor='end'
    ))

    # Internal width (36")
    internal_width = X_TUBE_LENGTH - X_TUBE_WIDTH * 2
    dim_y_internal = offset_y + inch_to_px(X_TUBE_WIDTH/2)
    dwg.add(dwg.line(
        start=(tube1_x, dim_y_internal),
        end=(tube1_x + tube1_width, dim_y_internal),
        class_='dimension-line'
    ))
    dwg.add(dwg.text(
        f'{internal_width:.1f}" (internal)',
        insert=(tube1_x + tube1_width/2, dim_y_internal - 5),
        class_='dimension-text',
        text_anchor='middle'
    ))

    # Add title
    dwg.add(dwg.text(
        'X-GANTRY TOP VIEW',
        insert=(offset_x, offset_y - inch_to_px(2)),
        style='font-family: Arial; font-size: 20px; font-weight: bold;'
    ))

    dwg.add(dwg.text(
        'Scale: 1:1 at 40px/inch (enlarged for detail)',
        insert=(offset_x, offset_y - inch_to_px(1)),
        style='font-family: Arial; font-size: 12px;'
    ))

    # Add legend and notes
    legend_x = offset_x
    legend_y = offset_y + inch_to_px(CROSS_BRACE_LENGTH + X_TUBE_WIDTH * 2 + 2)

    # Legend circles
    dwg.add(dwg.circle(center=(legend_x, legend_y), r=3, class_='rivnut-hole-top'))
    dwg.add(dwg.text('M6 rivnut (TOP face)', insert=(legend_x + 10, legend_y + 5), class_='label-text'))

    dwg.add(dwg.circle(center=(legend_x, legend_y + 20), r=3, class_='rivnut-hole-bottom'))
    dwg.add(dwg.text('M6 rivnut (BOTTOM face)', insert=(legend_x + 10, legend_y + 25), class_='label-text'))

    # Material notes
    notes_x = offset_x + inch_to_px(X_TUBE_LENGTH/2)
    notes_y = legend_y

    notes = [
        'MATERIALS:',
        '- Steel tubes: 2×3, 14g, 40" long (2 qty)',
        '- Steel tubes: 2×3, 14g, 8" long (2 qty) [cut from 16"]',
        '- T-plates: 3"×4"×1/4" steel (4 qty)',
        '- L-brackets: 4 qty (bottom corners only)',
        '- M6 rivnuts: 64 qty (8 per corner × 4 corners + rails)',
        '- M6 lockwashers: 48 qty (for height adjustment)',
        '',
        'NOTES:',
        '- Internal dimensions: 36" × 8"',
        '- Each corner: 8 rivnuts (4 top + 4 bottom)',
        '- Top rivnuts: T-plate mounting (adjustable height)',
        '- Bottom rivnuts: L-bracket mounting',
        '- X-rails mount on top (not shown)',
    ]

    for i, note in enumerate(notes):
        dwg.add(dwg.text(
            note,
            insert=(notes_x, notes_y + i * 14),
            style='font-family: Arial; font-size: 10px;'
        ))

    return dwg

if __name__ == '__main__':
    print("Generating X-Gantry top view drawing...")
    dwg = create_x_gantry_top_view()
    dwg.save()
    print("Saved: x-gantry-top-view.svg")
    print(f"Dimensions: {dwg.attribs['width']} x {dwg.attribs['height']}")
