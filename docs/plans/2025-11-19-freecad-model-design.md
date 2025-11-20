# FreeCAD Model Design for Router Sled System

**Date:** 2025-11-19
**Author:** Ivan Histand
**Status:** Design Complete, Ready for Implementation

## Purpose

This document specifies the FreeCAD model structure for the router sled slab flattening system. The model provides both 3D visualization and technical fabrication drawings.

## Design Goals

The FreeCAD model delivers three capabilities:

1. **3D Visualization** - Shows complete assembly with accurate clearances and fit
2. **Fabrication Drawings** - Provides precise hole locations and dimensions for drilling
3. **Parametric Flexibility** - Allows dimension changes through spreadsheet parameters

## File Organization

### Directory Structure

```
cad/freecad/
├── y-frame-assembly.FCStd          # Base frame (96" tubes, Y-rails, feet)
├── x-gantry-assembly.FCStd         # Moving carriage (40" tubes, X-rails)
├── router-mount-assembly.FCStd     # Router plate and Z-brackets
├── master-assembly.FCStd           # Complete system assembly
└── drawings/
    ├── y-frame-fabrication.FCStd   # Y-frame drilling patterns
    ├── x-gantry-fabrication.FCStd  # X-gantry drilling patterns
    └── assembly-views.FCStd        # Isometric and exploded views
```

### Assembly File Responsibilities

**y-frame-assembly.FCStd** contains:
- Two 96" steel tubes (2×3, 14 gauge)
- Two lumber end caps (2×4 trimmed to fit)
- Two SBR20-2200mm linear rails
- Eight M12 leveling feet
- Connection plates (steel-to-lumber joints)

**x-gantry-assembly.FCStd** contains:
- Two 40" steel tubes (2×3, 14 gauge)
- Two SBR20-1000mm linear rails
- Four SBR20UU slide blocks (Y-rail connection)
- Optional 8" vertical bracing tubes

**router-mount-assembly.FCStd** contains:
- Acrylic router base plate
- Four Z-brackets (plate-to-gantry mounting)
- Bosch 1617EVS router (simplified representation)

**master-assembly.FCStd** contains:
- Links to all three assembly files
- Shows complete system in operating configuration

## Parametric Design

### Spreadsheet Parameters

Each assembly file includes a "Parameters" spreadsheet. This spreadsheet drives all critical dimensions.

**Y-Frame Parameters:**
```
y_tube_length = 2438.4 mm (96 inches)
y_rail_length = 2200 mm
tube_width = 50.8 mm (2 inches)
tube_height = 76.2 mm (3 inches)
tube_wall_thickness = 2.1 mm (14 gauge)
rail_hole_spacing = 40 mm (SBR20 standard)
rail_first_hole_offset = 20 mm (from rail end)
leveling_foot_spacing = calculated (tube_length / 4)
```

**X-Gantry Parameters:**
```
x_tube_length = 1016 mm (40 inches)
x_rail_length = 1000 mm
gantry_frame_height = 203.2 mm (8 inches, optional bracing)
rail_hole_spacing = 40 mm
slide_block_mounting_width = per SBR20UU specifications
```

**Router Mount Parameters:**
```
plate_width = measured from Bosch 1617EVS base
plate_thickness = TBD (likely 6.35 mm or 12.7 mm acrylic)
z_bracket_spacing = 4 brackets around router perimeter
```

### Parameter Usage

Change a parameter value in the spreadsheet, and FreeCAD updates all dependent geometry automatically. For example, changing `y_tube_length` from 2438.4 mm to 2000 mm adjusts:
- Tube extrusion length
- Leveling foot positions
- End cap placement
- Linear rail mounting holes

## Component Modeling Strategy

### Detail Levels by Component Type

**Full Detail Components:**
- SBR20UU slide blocks (accurate dimensions affect gantry height)
- M12 leveling feet (accurate pad size and adjustment range)
- Linear rails (precise mounting hole patterns)

**Simplified Components:**
- Rivnuts: simple cylinders showing installed position
- M6/M12 screws: cylinder with hex head, no threads
- Connection plates: flat plates with hole patterns

**Symbolic Components:**
- Wood screws: construction geometry or simple cylinders
- Lumber end caps: basic rectangular extrusions

### Steel Tube Modeling

Steel tubes form the structural core. Model them using the Part Design workbench:

1. Create rectangular sketch (2" × 3" outer dimensions)
2. Create offset inner sketch (subtract wall thickness)
3. Extrude to tube length (driven by parameter)
4. Orient vertically (narrow edge up/down)
5. Add mounting holes using Linear Pattern feature

### Linear Rail Mounting Holes

Linear rails mount to steel tube top faces. The hole pattern follows SBR20 specifications:

**Hole Pattern Definition:**
- First hole: 20 mm from rail end
- Spacing: 40 mm center-to-center
- Hole diameter: 6 mm (for M6 rivnuts)
- Pattern length: driven by rail length parameter

Use FreeCAD's Linear Pattern feature to create the array. When you change `rail_hole_spacing` or `rail_length`, the pattern updates automatically.

### Hardware Modeling

**Rivnuts:**
- Model as simple cylinders
- Diameter: 6 mm (M6) or 12 mm (M12)
- Length: shows installed depth in tube wall
- No threads required

**Socket Head Cap Screws:**
- Cylinder body (6 mm or 12 mm diameter)
- Hex socket head (simplified, no actual socket detail)
- Length: appropriate for joint thickness

**Leveling Feet:**
- Accurate foot pad diameter and shape
- Threaded shaft (simplified cylinder)
- Adjustment range shown in assembly

## Technical Drawings

### Y-Frame Fabrication Drawing

**Purpose:** Shows exact hole positions for drilling Y-frame tubes before assembly.

**Drawing Content:**
- Top view of 96" steel tube
- All hole positions dimensioned from one end (0" reference)
- Two drawing sheets:
  - Sheet 1: Full length view with overall dimensions
  - Sheet 2: Detail view of rail mounting hole pattern

**Callouts:**
- M6 hole: 6 mm diameter (for rail mounting rivnuts)
- M12 hole: 12 mm diameter (for leveling feet)
- Note: "Drill holes before paint application"
- Note: "Install rivnuts per manufacturer specifications"

### X-Gantry Fabrication Drawing

**Purpose:** Shows hole positions for X-gantry tubes.

**Drawing Content:**
- Top view of 40" steel tubes
- X-axis rail mounting holes (M6, 6 mm)
- Slide block attachment points (where gantry connects to Y-rails)
- Router plate Z-bracket positions

**Dimensioning:**
- Dimension from center or edge (whichever provides clarity)
- Show hole spacing and total distances
- Include critical clearances

### Assembly Views Drawing

**Purpose:** Shows how parts fit together and assembly sequence.

**Drawing Content:**
- Isometric view of complete system
- Exploded view showing assembly order:
  1. Y-frame with leveling feet installed
  2. Y-rails mounted to frame
  3. X-gantry attached to Y-rail slide blocks
  4. X-rails mounted to gantry
  5. Router mount assembly added
- Side elevation showing working height and clearances
- Bill of materials table listing major components

**Assembly Sequence Notes:**
- Install leveling feet before placing frame
- Mount Y-rails to frame tubes (verify alignment)
- Attach slide blocks to gantry before mounting on Y-rails
- Check all axes move freely before mounting router

## Drawing Standards

All technical drawings use these conventions:

**Title Block:**
- Project name: Router Sled Slab Flattening System
- Drawing title: [specific to sheet]
- Date: [generation date]
- Author: Ivan Histand
- Scale: noted on each view

**Dimensions:**
- Use metric (millimeters) as primary units
- Show inch equivalents in parentheses where helpful
- Dimension from fixed references (ends, centers)
- Show both individual spacings and cumulative totals

**Notes:**
- Material specifications (2×3 steel tube, 14 gauge)
- Finish specifications (latex enamel paint)
- Assembly instructions where critical
- Hole tolerance if required

## Implementation Notes

### Linear Rail Specifications

SBR20 rails have standard mounting hole patterns, but verify your actual rails before drilling. Measure the following:

- Distance from rail end to first hole
- Hole-to-hole spacing
- Total number of holes
- Hole diameter

Adjust the `rail_hole_spacing` and `rail_first_hole_offset` parameters if your measurements differ from the standard 40 mm spacing.

### Modeling Workflow

Build the model in this order:

1. **Y-frame assembly** (foundation)
   - Steel tubes with parameters
   - Mounting hole patterns
   - Leveling feet
   - Linear rails

2. **X-gantry assembly** (moving parts)
   - Steel tubes
   - Rail mounting holes
   - Slide blocks
   - X-axis rails

3. **Router mount assembly** (router attachment)
   - Acrylic plate
   - Z-brackets
   - Router representation

4. **Master assembly** (complete system)
   - Link all assemblies
   - Verify clearances
   - Check motion range

5. **Fabrication drawings** (documentation)
   - Y-frame holes
   - X-gantry holes
   - Assembly views

### FreeCAD Workbenches

Use these workbenches for different tasks:

- **Part Design** - Create solid parts (tubes, plates, brackets)
- **Sketcher** - Define 2D profiles and hole patterns
- **Spreadsheet** - Define parameters
- **Assembly** - Combine parts into assemblies
- **TechDraw** - Generate technical drawings

### File Dependencies

The master assembly file links to the three sub-assembly files. When you modify a sub-assembly and save it, the master assembly updates automatically when opened.

Keep all files in the same directory structure to maintain links. If you move files, update the links in the master assembly.

## Quality Checks

Before using the model for fabrication, verify:

**Dimensional Accuracy:**
- Measure key dimensions in FreeCAD against specifications
- Verify tube lengths match purchased materials
- Check rail lengths match ordered parts

**Hole Patterns:**
- Count holes in model against calculated quantity
- Verify spacing matches parameters
- Check first and last hole positions

**Clearances:**
- Slide blocks clear steel tubes during full travel
- Router bit has adequate clearance below gantry
- Leveling feet provide sufficient height adjustment

**Assembly Feasibility:**
- Parts can be assembled in the order shown
- No interference between components
- Fasteners accessible for installation

## Next Steps

After completing this design phase:

1. Create FreeCAD directory structure
2. Build Y-frame assembly (foundation model)
3. Build X-gantry assembly
4. Build router mount assembly
5. Create master assembly with links
6. Generate fabrication drawings
7. Verify all dimensions against BOM
8. Print drawings for fabrication reference

## References

- **Design Specification:** `Router Sled Slab Flattening.md`
- **Build Plan:** `docs/plans/2025-11-18-build-plan.md`
- **BOM:** Listed in CLAUDE.md
- **SBR20 Specifications:** VEVOR product documentation
