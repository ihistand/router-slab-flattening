#!/usr/bin/env python3
"""
Generate SVG technical drawing for Y-Frame assembly
Shows top view with dimensions and rivnut hole positions
"""

import svgwrite
from svgwrite import cm, mm

# Dimensions in inches (will convert to mm for SVG)
Y_TUBE_LENGTH = 95  # inches
Y_TUBE_WIDTH = 2    # inches
Y_TUBE_HEIGHT = 3   # inches
LUMBER_LENGTH = 38  # inches
LUMBER_WIDTH = 3.5  # inches (actual 2x4)

# Conversion
INCH_TO_MM = 25.4
SCALE = 20  # pixels per inch for drawing

def inch_to_px(inches):
    """Convert inches to pixels for drawing"""
    return inches * SCALE

def create_y_frame_top_view():
    """Create top view of Y-frame with dimensions"""

    # Drawing size (in mm for SVG, but we'll work in scaled pixels)
    width_px = inch_to_px(Y_TUBE_LENGTH + 10)
    height_px = inch_to_px(LUMBER_LENGTH + Y_TUBE_WIDTH * 2 + 10)

    dwg = svgwrite.Drawing(
        'y-frame-top-view.svg',
        size=(f'{width_px}px', f'{height_px}px'),
        profile='full'
    )

    # Define styles
    dwg.defs.add(dwg.style('''
        .frame { fill: lightgray; stroke: black; stroke-width: 2; }
        .lumber { fill: burlywood; stroke: black; stroke-width: 2; }
        .dimension-line { stroke: red; stroke-width: 1; fill: none; }
        .dimension-text { font-family: Arial; font-size: 14px; fill: red; }
        .label-text { font-family: Arial; font-size: 12px; fill: black; }
        .rivnut-hole { fill: none; stroke: blue; stroke-width: 1; }
        .center-line { stroke: gray; stroke-width: 1; stroke-dasharray: 5,5; }
    '''))

    # Offset for margins
    offset_x = inch_to_px(5)
    offset_y = inch_to_px(5)

    # Draw first 95" tube (left side)
    tube1_x = offset_x
    tube1_y = offset_y
    tube1_width = inch_to_px(Y_TUBE_WIDTH)
    tube1_height = inch_to_px(Y_TUBE_LENGTH)

    dwg.add(dwg.rect(
        insert=(tube1_x, tube1_y),
        size=(tube1_width, tube1_height),
        class_='frame'
    ))

    # Draw second 95" tube (right side)
    tube2_x = offset_x + inch_to_px(Y_TUBE_WIDTH) + inch_to_px(LUMBER_LENGTH)
    tube2_y = offset_y
    tube2_width = inch_to_px(Y_TUBE_WIDTH)
    tube2_height = inch_to_px(Y_TUBE_LENGTH)

    dwg.add(dwg.rect(
        insert=(tube2_x, tube2_y),
        size=(tube2_width, tube2_height),
        class_='frame'
    ))

    # Draw front lumber cross-brace (38")
    lumber1_x = offset_x + inch_to_px(Y_TUBE_WIDTH)
    lumber1_y = offset_y
    lumber1_width = inch_to_px(LUMBER_LENGTH)
    lumber1_height = inch_to_px(LUMBER_WIDTH)

    dwg.add(dwg.rect(
        insert=(lumber1_x, lumber1_y),
        size=(lumber1_width, lumber1_height),
        class_='lumber'
    ))

    # Draw rear lumber cross-brace (38")
    lumber2_x = offset_x + inch_to_px(Y_TUBE_WIDTH)
    lumber2_y = offset_y + inch_to_px(Y_TUBE_LENGTH) - inch_to_px(LUMBER_WIDTH)
    lumber2_width = inch_to_px(LUMBER_LENGTH)
    lumber2_height = inch_to_px(LUMBER_WIDTH)

    dwg.add(dwg.rect(
        insert=(lumber2_x, lumber2_y),
        size=(lumber2_width, lumber2_height),
        class_='lumber'
    ))

    # Add dimension lines

    # Overall length dimension (95")
    dim_y = offset_y + tube1_height + inch_to_px(2)
    dwg.add(dwg.line(
        start=(tube1_x, dim_y),
        end=(tube1_x + tube1_width, dim_y),
        class_='dimension-line'
    ))
    dwg.add(dwg.text(
        '95.00"',
        insert=(tube1_x + tube1_width/2, dim_y - 5),
        class_='dimension-text',
        text_anchor='middle'
    ))

    # Overall width dimension (38" + 2×2" tubes)
    dim_x = offset_x + tube2_x + tube2_width + inch_to_px(1)
    dwg.add(dwg.line(
        start=(dim_x, tube1_y),
        end=(dim_x, tube1_y + inch_to_px(Y_TUBE_WIDTH + LUMBER_LENGTH + Y_TUBE_WIDTH)),
        class_='dimension-line'
    ))
    dwg.add(dwg.text(
        f'{Y_TUBE_WIDTH + LUMBER_LENGTH + Y_TUBE_WIDTH:.2f}"',
        insert=(dim_x + 10, offset_y + inch_to_px((Y_TUBE_WIDTH + LUMBER_LENGTH + Y_TUBE_WIDTH)/2)),
        class_='dimension-text'
    ))

    # Inside dimension (38")
    dim_x_inside = offset_x + inch_to_px(Y_TUBE_WIDTH/2)
    dwg.add(dwg.line(
        start=(tube1_x + tube1_width, offset_y + inch_to_px(Y_TUBE_LENGTH/2)),
        end=(tube2_x, offset_y + inch_to_px(Y_TUBE_LENGTH/2)),
        class_='dimension-line'
    ))
    dwg.add(dwg.text(
        '38.00" (inside)',
        insert=(tube1_x + tube1_width + inch_to_px(LUMBER_LENGTH/2), offset_y + inch_to_px(Y_TUBE_LENGTH/2) - 10),
        class_='dimension-text',
        text_anchor='middle'
    ))

    # Mark leveling feet positions (approximate)
    foot_positions = [10, 30, 50, 70, 90]  # inches along tube
    for pos in foot_positions:
        # Left tube
        cx = tube1_x + tube1_width/2
        cy = offset_y + inch_to_px(pos)
        dwg.add(dwg.circle(
            center=(cx, cy),
            r=3,
            class_='rivnut-hole'
        ))
        dwg.add(dwg.text(
            'M12',
            insert=(cx + 10, cy + 5),
            class_='label-text'
        ))

        # Right tube
        cx = tube2_x + tube2_width/2
        dwg.add(dwg.circle(
            center=(cx, cy),
            r=3,
            class_='rivnut-hole'
        ))

    # Add title and notes
    dwg.add(dwg.text(
        'Y-FRAME TOP VIEW',
        insert=(offset_x, offset_y - inch_to_px(2)),
        style='font-family: Arial; font-size: 20px; font-weight: bold;'
    ))

    dwg.add(dwg.text(
        'Scale: 1:1 at 20px/inch',
        insert=(offset_x, offset_y - inch_to_px(1)),
        style='font-family: Arial; font-size: 12px;'
    ))

    # Add material notes
    notes_x = offset_x + inch_to_px(Y_TUBE_WIDTH + LUMBER_LENGTH + Y_TUBE_WIDTH + 3)
    notes_y = offset_y

    notes = [
        'MATERIALS:',
        '- Steel tubes: 2×3, 14g, 95" long (2 qty)',
        '- Lumber: 2×4, 38" long (2 qty)',
        '- L-brackets: 8 qty (2 per corner)',
        '- M12 leveling feet: 8 qty (4 per tube)',
        '- M6 rivnuts: ~60 qty (for Y-rails)',
        '',
        'NOTES:',
        '- Tubes oriented vertically (3" height)',
        '- Inside spacing: 38.00"',
        '- Leveling feet spaced ~20" apart',
        '- Y-rails mount on top (not shown)',
    ]

    for i, note in enumerate(notes):
        dwg.add(dwg.text(
            note,
            insert=(notes_x, notes_y + i * 15),
            style='font-family: Arial; font-size: 11px;'
        ))

    return dwg

if __name__ == '__main__':
    print("Generating Y-Frame top view drawing...")
    dwg = create_y_frame_top_view()
    dwg.save()
    print("Saved: y-frame-top-view.svg")
    print(f"Dimensions: {dwg.attribs['width']} x {dwg.attribs['height']}")
