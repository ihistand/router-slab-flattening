# FreeCAD Models for Router Sled

This directory contains the FreeCAD parametric models for the router sled slab flattening system.

## File Organization

```
freecad/
├── y-frame-assembly.FCStd          # Base frame (96" tubes, Y-rails, feet)
├── x-gantry-assembly.FCStd         # Moving carriage (40" tubes, X-rails)
├── router-mount-assembly.FCStd     # Router plate and Z-brackets
├── master-assembly.FCStd           # Complete system assembly
├── drawings/
│   ├── y-frame-fabrication.FCStd   # Y-frame drilling patterns
│   ├── x-gantry-fabrication.FCStd  # X-gantry drilling patterns
│   └── assembly-views.FCStd        # Isometric and exploded views
├── README.md                       # This file
└── y-frame-quick-start.md         # Step-by-step guide to build Y-frame
```

## Getting Started

Start with the Y-frame assembly as it forms the foundation:

1. Read `y-frame-quick-start.md` for step-by-step instructions
2. Open FreeCAD and create `y-frame-assembly.FCStd`
3. Follow the guide to build the parametric model
4. Move to X-gantry assembly once Y-frame is complete

## Model Design

See `docs/plans/2025-11-19-freecad-model-design.md` for complete design specifications including:
- Parametric approach and spreadsheet definitions
- Component modeling strategy and detail levels
- Technical drawing requirements
- Quality checks and verification steps

## Key Concepts

### Parametric Parameters

Each assembly uses a Spreadsheet to define critical dimensions. Change a parameter and all dependent geometry updates automatically.

Example Y-frame parameters:
- `y_tube_length` = 2438.4 mm (96")
- `y_rail_length` = 2200 mm
- `rail_hole_spacing` = 40 mm

### Detail Levels

**Full Detail:** SBR20UU slide blocks, M12 leveling feet, linear rails
**Simplified:** Rivnuts (cylinders), screws (cylinder + hex head)
**Symbolic:** Wood screws, basic geometry only

### Assembly Links

The master assembly links to sub-assemblies. When you modify and save a sub-assembly, the master assembly updates automatically when opened.

## FreeCAD Workbenches

You'll use these workbenches:

- **Part Design** - Create solid parts (tubes, plates, brackets)
- **Sketcher** - Define 2D profiles and hole patterns
- **Spreadsheet** - Define parameters
- **Assembly** - Combine parts into assemblies (or use A2plus addon)
- **TechDraw** - Generate technical drawings

## Build Order

Build the models in this sequence:

1. **Y-frame assembly** (foundation) ← Start here
2. **X-gantry assembly** (moving parts)
3. **Router mount assembly** (router attachment)
4. **Master assembly** (complete system)
5. **Fabrication drawings** (documentation)

## Tips for Success

### Before You Start

- Read the quick-start guide completely before opening FreeCAD
- Have the design specification open for reference
- Save your work frequently (FreeCAD can crash)
- Use descriptive names for parts and features

### While Modeling

- Set up the Parameters spreadsheet first
- Reference parameters in sketches (don't hard-code dimensions)
- Name your sketches and features clearly
- Use symmetry and patterns where possible
- Save after completing each major feature

### Verification

Before moving to the next assembly:
- Check all dimensions against specifications
- Verify hole counts and spacing
- Test parameter changes (change a value, check updates)
- Save and close, then reopen to verify file integrity

## Common Issues

**Parameter not updating:**
- Right-click spreadsheet → Recompute
- Edit → Refresh document
- Save, close, and reopen file

**FreeCAD crashes:**
- Save frequently
- Keep backups of working files
- Restart FreeCAD if it becomes sluggish

**Assembly links broken:**
- Keep all files in same directory structure
- Use relative paths when linking
- Update links if you move files

## Resources

**Design Documentation:**
- `docs/plans/2025-11-19-freecad-model-design.md` - Complete design spec
- `docs/plans/2025-11-18-build-plan.md` - Physical build plan
- `Router Sled Slab Flattening.md` - Project overview

**FreeCAD Help:**
- Official wiki: https://wiki.freecad.org/
- Tutorials: https://wiki.freecad.org/Tutorials
- Forum: https://forum.freecad.org/

**Part Specifications:**
- VEVOR SBR20 rails: Product documentation
- Bosch 1617EVS: Router manual and base dimensions
- Steel tube: 2×3 rectangular, 14 gauge specifications
