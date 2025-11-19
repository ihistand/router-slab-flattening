#!/usr/bin/env python3
"""
Generate 1:1 scale drilling templates for rivnut holes
Can be printed and used as physical templates for marking holes
"""

import svgwrite
from svgwrite import mm

# Dimensions in millimeters (for 1:1 printable template)
INCH_TO_MM = 25.4

# Hole sizes
M6_DRILL_DIA = 5  # mm (for M6 rivnut)
M12_DRILL_DIA = 13  # mm (for M12 rivnut)

def create_corner_rivnut_template():
    """
    Create drilling template for X-gantry corner (8 M6 holes per corner)
    Scale 1:1 for direct printing and use as template
    """

    # Template size (A4 paper size in mm)
    width_mm = 210
    height_mm = 297

    dwg = svgwrite.Drawing(
        'corner-rivnut-drilling-template.svg',
        size=(f'{width_mm}mm', f'{height_mm}mm'),
        profile='full'
    )

    # Define styles
    dwg.defs.add(dwg.style('''
        .drill-hole { fill: none; stroke: black; stroke-width: 0.5mm; }
        .center-mark { stroke: red; stroke-width: 0.3mm; }
        .dimension-line { stroke: blue; stroke-width: 0.3mm; fill: none; }
        .title-text { font-family: Arial; font-size: 16px; font-weight: bold; }
        .label-text { font-family: Arial; font-size: 10px; }
        .instruction-text { font-family: Arial; font-size: 9px; }
    '''))

    # Starting position for template
    start_x = 30  # mm
    start_y = 40  # mm

    # Hole pattern for one corner (4 top + 4 bottom, mirrored arrangement)
    # Top holes (clustered near corner)
    top_holes = [
        (0, 0),      # Hole 1
        (10, 0),     # Hole 2
        (0, 10),     # Hole 3
        (10, 10),    # Hole 4
    ]

    # Bottom holes (offset from top, on opposite face)
    # In reality these would be on the bottom face, but shown offset for clarity
    bottom_holes = [
        (25, 0),     # Hole 5
        (35, 0),     # Hole 6
        (25, 10),    # Hole 7
        (35, 10),    # Hole 8
    ]

    # Title
    dwg.add(dwg.text(
        'X-GANTRY CORNER RIVNUT DRILLING TEMPLATE',
        insert=(width_mm/2*mm, 15*mm),
        class_='title-text',
        text_anchor='middle'
    ))

    # Subtitle
    dwg.add(dwg.text(
        'Scale 1:1 - Print at 100% (NO SCALING)',
        insert=(width_mm/2*mm, 25*mm),
        class_='label-text',
        text_anchor='middle',
        style='fill: red;'
    ))

    # Draw TOP face holes
    dwg.add(dwg.text(
        'TOP FACE (4 holes)',
        insert=(start_x*mm, (start_y - 10)*mm),
        class_='label-text',
        style='fill: green; font-weight: bold;'
    ))

    for i, (dx, dy) in enumerate(top_holes, 1):
        cx = (start_x + dx) * mm
        cy = (start_y + dy) * mm

        # Drill hole circle (5mm diameter for M6)
        dwg.add(dwg.circle(
            center=(cx, cy),
            r=M6_DRILL_DIA/2*mm,
            class_='drill-hole'
        ))

        # Center crosshair
        crosshair_len = 8  # mm
        dwg.add(dwg.line(
            start=((start_x + dx - crosshair_len/2)*mm, cy),
            end=((start_x + dx + crosshair_len/2)*mm, cy),
            class_='center-mark'
        ))
        dwg.add(dwg.line(
            start=(cx, (start_y + dy - crosshair_len/2)*mm),
            end=(cx, (start_y + dy + crosshair_len/2)*mm),
            class_='center-mark'
        ))

        # Label
        dwg.add(dwg.text(
            f'T{i}',
            insert=((start_x + dx)*mm, (start_y + dy + 15)*mm),
            class_='label-text',
            text_anchor='middle',
            style='fill: green;'
        ))

    # Draw BOTTOM face holes
    dwg.add(dwg.text(
        'BOTTOM FACE (4 holes)',
        insert=((start_x + 25)*mm, (start_y - 10)*mm),
        class_='label-text',
        style='fill: blue; font-weight: bold;'
    ))

    for i, (dx, dy) in enumerate(bottom_holes, 1):
        cx = (start_x + dx) * mm
        cy = (start_y + dy) * mm

        # Drill hole circle
        dwg.add(dwg.circle(
            center=(cx, cy),
            r=M6_DRILL_DIA/2*mm,
            class_='drill-hole'
        ))

        # Center crosshair
        dwg.add(dwg.line(
            start=((start_x + dx - crosshair_len/2)*mm, cy),
            end=((start_x + dx + crosshair_len/2)*mm, cy),
            class_='center-mark'
        ))
        dwg.add(dwg.line(
            start=(cx, (start_y + dy - crosshair_len/2)*mm),
            end=(cx, (start_y + dy + crosshair_len/2)*mm),
            class_='center-mark'
        ))

        # Label
        dwg.add(dwg.text(
            f'B{i}',
            insert=((start_x + dx)*mm, (start_y + dy + 15)*mm),
            class_='label-text',
            text_anchor='middle',
            style='fill: blue;'
        ))

    # Dimension lines (10mm spacing between holes)
    # Horizontal dimension
    dim_y = start_y + 25
    dwg.add(dwg.line(
        start=(start_x*mm, dim_y*mm),
        end=((start_x + 10)*mm, dim_y*mm),
        class_='dimension-line'
    ))
    dwg.add(dwg.text(
        '10mm',
        insert=((start_x + 5)*mm, (dim_y - 2)*mm),
        class_='label-text',
        text_anchor='middle',
        style='fill: blue;'
    ))

    # Vertical dimension
    dim_x = start_x + 50
    dwg.add(dwg.line(
        start=(dim_x*mm, start_y*mm),
        end=(dim_x*mm, (start_y + 10)*mm),
        class_='dimension-line'
    ))
    dwg.add(dwg.text(
        '10mm',
        insert=((dim_x + 3)*mm, (start_y + 5)*mm),
        class_='label-text',
        style='fill: blue;'
    ))

    # Instructions
    instructions_y = start_y + 50
    instructions = [
        'INSTRUCTIONS:',
        '1. Print this page at 100% scale (NO SCALING OR "FIT TO PAGE")',
        '2. Verify scale: Measure printed dimension - should be exactly 10mm',
        '3. Cut out template along outer edges',
        '4. Position template on tube corner (align with tube edges)',
        '5. Mark hole centers using center crosshairs',
        '6. Center punch marked positions before drilling',
        '7. Drill 5mm holes for M6 rivnuts',
        '8. Repeat for all 4 corners (16 holes per tube, 32 total)',
        '',
        'NOTES:',
        '- Top face holes: For T-plate mounting (adjustable height)',
        '- Bottom face holes: For L-bracket mounting',
        '- Use lockwashers on T-plate bolts (allows reconfiguration)',
        '- Use Loctite 242 on L-bracket bolts (permanent)',
        '',
        'DRILL SPECIFICATIONS:',
        '- Hole size: 5mm (for M6 rivnuts)',
        '- Depth: Through wall thickness (~2mm)',
        '- Tool: Standard twist drill bit',
        '- Speed: Medium (800-1200 RPM)',
        '- Safety: Wear eye protection, secure workpiece',
    ]

    for i, line in enumerate(instructions):
        dwg.add(dwg.text(
            line,
            insert=(10*mm, (instructions_y + i * 5)*mm),
            class_='instruction-text'
        ))

    # Scale verification bar (exactly 100mm)
    scale_bar_y = height_mm - 30
    dwg.add(dwg.line(
        start=(20*mm, scale_bar_y*mm),
        end=(120*mm, scale_bar_y*mm),
        style='stroke: black; stroke-width: 2mm;'
    ))
    dwg.add(dwg.text(
        'SCALE CHECK: This bar should measure exactly 100mm',
        insert=(70*mm, (scale_bar_y - 5)*mm),
        class_='label-text',
        text_anchor='middle',
        style='fill: red; font-weight: bold;'
    ))

    # End marks at 0 and 100mm
    dwg.add(dwg.line(start=(20*mm, (scale_bar_y - 5)*mm), end=(20*mm, (scale_bar_y + 5)*mm), style='stroke: black; stroke-width: 1mm;'))
    dwg.add(dwg.line(start=(120*mm, (scale_bar_y - 5)*mm), end=(120*mm, (scale_bar_y + 5)*mm), style='stroke: black; stroke-width: 1mm;'))

    dwg.add(dwg.text('0mm', insert=(20*mm, (scale_bar_y + 10)*mm), class_='label-text', text_anchor='middle'))
    dwg.add(dwg.text('100mm', insert=(120*mm, (scale_bar_y + 10)*mm), class_='label-text', text_anchor='middle'))

    return dwg

def create_leveling_foot_template():
    """Create template for M12 leveling feet holes on Y-frame"""

    width_mm = 210
    height_mm = 150  # Smaller template

    dwg = svgwrite.Drawing(
        'leveling-foot-drilling-template.svg',
        size=(f'{width_mm}mm', f'{height_mm}mm'),
        profile='full'
    )

    dwg.defs.add(dwg.style('''
        .drill-hole { fill: none; stroke: black; stroke-width: 0.5mm; }
        .center-mark { stroke: red; stroke-width: 0.3mm; }
        .title-text { font-family: Arial; font-size: 16px; font-weight: bold; }
        .label-text { font-family: Arial; font-size: 10px; }
        .instruction-text { font-family: Arial; font-size: 9px; }
    '''))

    # Title
    dwg.add(dwg.text(
        'LEVELING FEET DRILLING TEMPLATE (M12)',
        insert=(width_mm/2*mm, 15*mm),
        class_='title-text',
        text_anchor='middle'
    ))

    dwg.add(dwg.text(
        'Scale 1:1 - Print at 100% (NO SCALING)',
        insert=(width_mm/2*mm, 25*mm),
        class_='label-text',
        text_anchor='middle',
        style='fill: red;'
    ))

    # Single hole template (repeat 8 times on frame)
    center_x = 50
    center_y = 50

    # Drill hole
    dwg.add(dwg.circle(
        center=(center_x*mm, center_y*mm),
        r=M12_DRILL_DIA/2*mm,
        class_='drill-hole'
    ))

    # Center crosshair
    crosshair_len = 20
    dwg.add(dwg.line(
        start=((center_x - crosshair_len/2)*mm, center_y*mm),
        end=((center_x + crosshair_len/2)*mm, center_y*mm),
        class_='center-mark'
    ))
    dwg.add(dwg.line(
        start=(center_x*mm, (center_y - crosshair_len/2)*mm),
        end=(center_x*mm, (center_y + crosshair_len/2)*mm),
        class_='center-mark'
    ))

    # Label
    dwg.add(dwg.text(
        f'Ø{M12_DRILL_DIA}mm',
        insert=(center_x*mm, (center_y + 20)*mm),
        class_='label-text',
        text_anchor='middle'
    ))

    # Instructions
    instructions_y = 80
    instructions = [
        'INSTRUCTIONS:',
        '1. Print at 100% scale (verify with scale bar below)',
        '2. Position template on BOTTOM edge of Y-frame tube',
        '3. Mark centers at: 10", 30", 50", 70", 90" from tube end',
        '4. Drill 13mm holes for M12 rivnuts',
        '5. Install M12 rivnuts using rivnut tool',
        '6. Thread M12 leveling feet into rivnuts',
        '',
        'SPECIFICATIONS:',
        '- Hole diameter: 13mm (for M12 rivnuts)',
        '- Quantity: 8 holes total (4 per tube)',
        '- Spacing: Approximately 20" apart',
        '- Position: Bottom edge, centered on 2" width',
    ]

    for i, line in enumerate(instructions):
        dwg.add(dwg.text(
            line,
            insert=(10*mm, (instructions_y + i * 4.5)*mm),
            class_='instruction-text'
        ))

    # Scale bar
    scale_bar_y = height_mm - 20
    dwg.add(dwg.line(
        start=(30*mm, scale_bar_y*mm),
        end=(130*mm, scale_bar_y*mm),
        style='stroke: black; stroke-width: 2mm;'
    ))
    dwg.add(dwg.text(
        'SCALE CHECK: 100mm',
        insert=(80*mm, (scale_bar_y - 5)*mm),
        class_='label-text',
        text_anchor='middle',
        style='fill: red;'
    ))

    return dwg

if __name__ == '__main__':
    print("Generating drilling templates...")

    print("  1. Corner rivnut template (M6)...")
    dwg1 = create_corner_rivnut_template()
    dwg1.save()
    print("     Saved: corner-rivnut-drilling-template.svg")

    print("  2. Leveling foot template (M12)...")
    dwg2 = create_leveling_foot_template()
    dwg2.save()
    print("     Saved: leveling-foot-drilling-template.svg")

    print("\nDone! Print templates at 100% scale for 1:1 use.")
    print("IMPORTANT: Verify scale with printed scale bars before drilling.")
