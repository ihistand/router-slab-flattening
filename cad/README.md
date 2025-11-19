# Router Sled CAD Files

This directory contains 3D models and 2D technical drawings for the router sled project.

## Directory Structure

```
cad/
├── openscad/          # 3D models (OpenSCAD format)
├── svg/               # 2D technical drawings (SVG format)
└── README.md          # This file
```

## OpenSCAD 3D Models

**Requirements:** OpenSCAD (free, open-source 3D modeling software)
- Download: https://openscad.org/downloads.html

**Files:**
- `y-frame.scad` - Y-frame assembly (95" × 38" base frame)
- `x-gantry.scad` - X-gantry assembly (40" × 8" moving carriage)
- `complete-assembly.scad` - Full router sled system

**Usage:**
1. Install OpenSCAD
2. Open `.scad` files in OpenSCAD
3. Press F5 to preview, F6 to render
4. Export to STL for 3D printing (if needed for custom brackets)
5. Use built-in camera controls to rotate and inspect

**Viewing Tips:**
- Mouse drag: Rotate view
- Shift + Mouse drag: Pan view
- Scroll wheel: Zoom
- View → Axes: Show coordinate system
- View → Show Edges: Toggle edge display

## SVG Technical Drawings

**Requirements:** Python 3 with svgwrite library
- Install: `pip install svgwrite`

**Generator Scripts:**
- `generate_y_frame_drawing.py` - Y-frame top view with dimensions
- `generate_x_gantry_drawing.py` - X-gantry top view with rivnut positions
- `generate_drilling_template.py` - 1:1 scale drilling templates (printable)

**To Generate SVG Files:**

```bash
cd cad/svg
python generate_y_frame_drawing.py
python generate_x_gantry_drawing.py
python generate_drilling_template.py
```

**Output Files:**
- `y-frame-top-view.svg` - Y-frame dimensional drawing
- `x-gantry-top-view.svg` - X-gantry dimensional drawing with hole patterns
- `corner-rivnut-drilling-template.svg` - Corner hole template (M6, print 1:1)
- `leveling-foot-drilling-template.svg` - Leveling feet template (M12, print 1:1)

**Viewing SVG Files:**
- Web browser (Chrome, Firefox, Safari)
- Inkscape (free vector graphics editor)
- Adobe Illustrator
- Any SVG-compatible viewer

## Using Drilling Templates

The drilling templates are designed to be printed at **1:1 scale** and used as physical templates for marking hole positions.

**Printing Instructions:**
1. Open SVG file in web browser
2. Print using browser's print function
3. **CRITICAL:** Set print scale to 100% (NO SCALING or "Fit to Page")
4. Verify scale: Measure the printed scale bar
   - Should measure exactly 100mm (3.937")
   - If not exact, adjust printer settings and reprint

**Using Templates:**
1. Cut out printed template
2. Position on workpiece (tube surface)
3. Mark hole centers using center crosshairs
4. Center punch marked positions
5. Drill holes per specifications

**Template Specifications:**
- **Corner Rivnut Template:** 8× M6 holes per corner (5mm drill bit)
- **Leveling Foot Template:** Single M12 hole (13mm drill bit), repeat 8× on frame

## Dimension Reference

### Y-Frame
- Overall: 95" × 38" (2413mm × 965mm)
- Tube size: 2×3, 14 gauge
- Rail travel: 86.6" (2200mm)
- Leveling feet: 8× M12, ~20" spacing

### X-Gantry
- Overall: 40" × 8" (1016mm × 203mm)
- Internal: 36" × 8" (914mm × 203mm)
- Tube size: 2×3, 14 gauge
- Rail travel: 39.4" (1000mm)
- Height adjustment: 3" (76mm) via repositioning

### Router Plate
- Size: 10" × 12" × 1/2" (254mm × 305mm × 12.7mm)
- Material: Acrylic
- Mounting: 4× Z-brackets to X-rail slide blocks

## Modifications

All CAD files are text-based and easily editable:
- **OpenSCAD:** Edit `.scad` files with any text editor
- **SVG Python Scripts:** Modify Python scripts to change dimensions, layout, or annotations

## Export Formats

### From OpenSCAD:
- STL (for 3D printing)
- OFF (mesh format)
- AMF (additive manufacturing)
- DXF (2D projection for laser cutting)

### From SVG:
- PDF (print-ready documents)
- PNG (raster images, various resolutions)
- DXF (via Inkscape for CAD import)

## Notes

- All dimensions in technical drawings match the design document
- OpenSCAD models are parametric - edit variables at top of files to adjust dimensions
- SVG drawings use color coding:
  - Red: Dimensions
  - Black: Frame outlines
  - Blue: Rivnut holes / Bottom face
  - Green: Top face rivnuts
- Scale bars included on all printable templates for verification

## Questions or Issues

Refer to:
- `docs/plans/2025-11-18-router-sled-design.md` - Complete design specifications
- `docs/plans/2025-11-18-build-plan.md` - Step-by-step assembly instructions
- `CLAUDE.md` - Project overview and context
