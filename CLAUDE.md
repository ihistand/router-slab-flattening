# CLAUDE.md - Router Sled Slab Flattening Project

This file provides guidance to Claude Code when working with this hardware project.

## Project Owner

**Ivan Histand** - Sr Data Architect / Maker
Email: ihistand@rotoplas.com

**Profiles**:
- [GitHub](https://github.com/ihistand)
- [GitLab](https://gitlab.com/ihistand)
- [LinkedIn](https://linkedin.com/in/ihistand)

## Project Overview

**Type**: Hardware / Woodworking CNC Project
**Purpose**: Router sled system for flattening large hardwood slabs up to 3' × 8' × 4" thick
**Status**: Design/Planning Phase

This project involves building a precision CNC-style router sled using steel tube framing, linear rails, and a Bosch router. The system features:
- Y-axis frame: 95" (2200mm linear rails)
- X-axis gantry: 40" (1000mm linear rails)
- Adjustable leveling feet for cement floor installation
- Modular design for disassembly and storage

## Bill of Materials

### Structural Components

**Steel Framing** (Purchased - Pre-cut and Painted):
- Material: 2×3 rectangular steel tube, 14 gauge, latex enamel painted
- Original: 24' tube cut by vendor into:
  - 2× 96" pieces (Y-frame rails)
  - 2× 40" pieces (X-gantry base)
  - 1× 16" piece (leftover for gantry framing)
- Additional use: 16" piece can be cut into 8" sections for gantry frame

**Lumber**:
- 2×4 lumber (Y-frame end caps)
- Note: Trim ends to 2×3 to fit inside steel tube

### Linear Motion System

**Y-Axis Linear Rails** (Purchased):
- VEVOR SBR20-2200mm Linear Guide Rail Set
- Quantity: 2 rails (86.6" / 2200mm)
- Includes: 4× SBR20UU slide blocks
- Link: [VEVOR Y-Rails](https://www.vevor.com/linear-guide-rail-c_10531/vevor-linear-guide-rail-set-sbr20-2200mm-2-pcs-86-6-in-2200-mm-sbr20-guide-rails-and-4-pcs-sbr20uu-slide-blocks-linear-rails-and-bearings-kit-for-automated-machines-diy-project-cnc-router-machines-p_010322688456)

**X-Axis Linear Rails** (Purchased):
- VEVOR SBR20-1000mm Linear Guide Rail Set
- Quantity: 2 rails (39.4" / 1000mm)
- Includes: 4× SBR20UU slide blocks
- Link: [VEVOR X-Rails](https://www.vevor.com/linear-guide-rail-c_10531/vevor-linear-guide-rail-set-sbr20-1000mm-2-pcs-39-4-in-1000-mm-sbr20-guide-rails-and-4-pcs-sbr20uu-slide-blocks-linear-rails-and-bearings-kit-for-automated-machines-diy-project-cnc-router-machines-p_010358112362)

### Leveling System

**Leveling Feet** (Purchased):
- BokWin M12 Thread Adjustable Feet
- Quantity: 8 total (4 per Y-rail)
- Link: [Amazon M12 Leveling Feet](https://www.amazon.com/dp/B08T1T19FH?ref=ppx_pop_mob_ap_share)

### Router Components

**Router** (Purchased):
- Bosch 1617EVS Fixed Base Router
- Link: [Amazon Bosch Router](https://a.co/d/ec7WP3W)

**Router Bit** (Purchased):
- Link: [Amazon Router Bit](https://a.co/d/gaS5NHb)

**Router Mounting Plate** (NOT YET PURCHASED):
- Material: Acrylic
- Purpose: Mount router to X-gantry using Z-brackets

### Fasteners and Hardware

**M5 Hardware** (Purchased):
- Rivnuts: 100× M5 ([Amazon](https://a.co/d/bvDlL4k))
- Socket head cap screws: 100× M5 ([Amazon](https://a.co/d/2fvpGeN))

**M6 Hardware** (Purchased):
- Rivnuts: 100× M6
- Socket head cap screws: 100× M6 ([Amazon](https://a.co/d/jiaw68P))
- Required quantity: ~60 rivnuts per Y-rail (30 per rail × 2 rails)

**M12 Hardware** (Purchased):
- Rivnuts: 10× M12 (for leveling feet)

**Wood Hardware**:
- Wood screws (for steel-to-lumber connections)
- Pocket screws and jig (for lumber frame assembly)

### Tools and Supplies

**On Hand**:
- Rivnut installation tool ([Amazon](https://a.co/d/2H824TW))
- Hand drill
- Drill bits
- Level
- Loctite 242 (thread locker)
- 3D printer (for custom end caps and shims)

## Assembly Architecture

### Frame Orientation
- All 2×3 steel tube oriented **vertically** (narrow edge facing up/down)
- This provides maximum rigidity for the frame

### Y-Frame Assembly (Base Frame)
```
Component: Y-Frame Rails
- 2× 95" steel tubes (2×3, 14g)
- 2× 2×4 lumber end pieces (trimmed to 2×3 at connection points)
- Connection method: Flat steel plates
  - Plates to steel tube: M6 rivnuts
  - Plates to lumber: Wood screws
- Result: Rectangular box frame, 95" × ~40"

Y-Linear Rail Mounting:
- 2× 2200mm SBR20 rails
- Attach to top face of Y-frame steel tubes
- Connection: M6 rivnuts + socket head cap screws
- Quantity: 30 rivnuts per rail = 60 total for Y-axis

Leveling Feet:
- 8× M12 adjustable feet (4 per rail)
- Attach to bottom of Y-frame steel tubes
- Connection: M12 rivnuts in steel tube
```

### X-Gantry Assembly (Moving Carriage)
```
Component: X-Gantry Frame
- 2× 40" steel tubes (2×3, 14g)
- Optional: 2× 8" steel tube pieces (cut from 16" leftover) for framing
- Connection: TBD (likely rivnuts + flat plates or Z-brackets)

X-Linear Rail Mounting:
- 2× 1000mm SBR20 rails
- Attach to X-gantry steel tubes
- Connection: M6 rivnuts + socket head cap screws

Gantry to Y-Rail Connection:
- X-gantry bolts to Y-rail slide blocks (SBR20UU)
- Connection method: Flat plates or Z-brackets + rivnuts

Router Mounting:
- Acrylic router base plate
- Attach to X-gantry using 4× Z-brackets
- Bosch 1617EVS router mounts to acrylic plate
```

### Connection Methods

**Steel-to-Steel**:
- M6 rivnuts installed in steel tube
- M6 socket head cap screws
- Loctite 242 recommended

**Steel-to-Lumber**:
- Flat steel plates as interface
- Rivnuts in steel, wood screws into lumber
- Lumber trimmed to fit inside steel tube profile

**Linear Rail Mounting**:
- M6 rivnuts in steel tube (spaced per rail mounting holes)
- M6 socket head cap screws through rail into rivnuts
- Critical: Maintain rail alignment for smooth motion

## Design Specifications

### Workpiece Capacity
- Maximum slab dimensions: 3' wide × 8' long × 4" thick
- Material: Hardwood slabs

### Frame Dimensions
- Y-axis (length): 95" external frame, 86.6" rail travel
- X-axis (width): 40" external frame, 39.4" rail travel
- Z-axis (height): Determined by router base mounting

### Installation Requirements
- Surface: Cement floor
- Level requirement: Adjustable via M12 leveling feet
- Storage: Must be fully disassemblable

### Materials Finish
- Steel: Latex enamel paint (pre-applied by vendor)
- Purpose: Corrosion protection for garage/shop environment

## Critical Assembly Notes

1. **Rivnut Installation**:
   - Use proper rivnut tool to avoid stripping threads
   - Ensure steel tube walls are clean and deburred
   - Test fit screws before final assembly

2. **Linear Rail Alignment**:
   - Rails must be parallel and coplanar
   - Use precision straightedge and dial indicator if available
   - Small misalignments cause binding and poor surface finish

3. **Leveling**:
   - Use quality level (digital recommended)
   - Level both X and Y axes before first use
   - Recheck level periodically (cement floor may settle)

4. **Router Safety**:
   - Secure all fasteners with Loctite 242
   - Verify acrylic plate thickness supports router weight
   - Test all motions without router power before cutting

## Project Files

### Current Files
- `Router Sled Slab Flattening.md` - Master design specification
- `CLAUDE.md` - This file (project guide for Claude Code)

### Recommended Additional Files
- `assembly-instructions.md` - Step-by-step assembly guide
- `cut-list.md` - Detailed cutting and drilling plans
- `bom-tracking.md` - Purchase status and part numbers
- `cad/` - CAD drawings (if created)
- `photos/` - Assembly progress photos
- `3d-prints/` - STL files for custom brackets and shims

## Design Decisions and Rationale

### Why 2×3 Steel Tube (14 gauge)?
- Good strength-to-weight ratio for this application
- 14 gauge walls support rivnut installation
- Vertical orientation maximizes rigidity
- Pre-painted finish reduces prep work

### Why SBR20 Linear Rails?
- Common size with good availability
- Four bearing blocks per axis provide stability
- 20mm rail supports router weight and cutting forces
- Vevor provides good value for hobbyist applications

### Why M6 Fasteners for Rails?
- Standard size for SBR20 rail mounting holes
- Provides adequate clamping force
- Rivnuts in 14 gauge steel have sufficient pull-out strength

### Why Modular/Disassemblable Design?
- Garage/shop space constraints
- Seasonal storage requirements
- Future modifications and upgrades

## Future Enhancements

### Potential Upgrades
- Add stepper motors for CNC control
- Install limit switches for homing
- Create dust collection shroud
- Design featherboards for workpiece hold-down
- Add measurement scales or DRO (Digital Read Out)

### 3D Printed Components
- End caps for steel tube
- Shims for linear rail alignment
- Cable management clips
- Router bit storage
- Dust port adapters

## Troubleshooting

### Common Issues

**Gantry Binding**:
- Check linear rail alignment
- Verify all slide blocks move freely
- Clean rails and lubricate per manufacturer specs
- Check for frame twist (verify level)

**Vibration**:
- Verify all fasteners tight
- Check router bit is properly secured
- Reduce router speed
- Take shallower cuts

**Uneven Surface Finish**:
- Check rails for debris
- Verify gantry is perpendicular to Y-rails
- Ensure router bit is sharp
- Check for play in slide blocks

**Leveling Feet Won't Hold**:
- Tighten M12 lock nuts
- Check floor for severe irregularities
- Consider larger foot pads for concrete texture

## Resources

### Suppliers
- **VEVOR**: Linear rails and motion components
- **Amazon**: Fasteners, rivnuts, tools
- **Local Metal Supply**: Steel tube (already purchased)
- **Local Hardware**: Lumber, wood screws

### Reference Materials
- VEVOR linear rail installation guides
- Bosch 1617EVS router manual
- SBR20 bearing block specifications
- Rivnut installation best practices

## Contact

For questions about this project:
- **Ivan Histand**: ihistand@rotoplas.com
- **GitHub**: [@ihistand](https://github.com/ihistand)

## Notes

This is a personal maker project, separate from professional data engineering work. The design emphasizes practicality, ease of assembly, and use of readily available components.
