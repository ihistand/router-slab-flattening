# Router Sled for Slab Flattening - Design Document

**Date:** November 18, 2025
**Author:** Ivan Histand
**Status:** Final Design - Ready for Implementation

## Overview

This document details the complete design for a manual router sled system to flatten hardwood slabs up to 3' × 8' × 4" thick. The system uses steel tube framing, linear rails, and a Bosch 1617EVS router on a two-axis gantry platform.

## Design Goals

- Flatten slabs from 1" to 5" thickness
- Accommodate slabs up to 36" wide × 96" long
- Disassemble completely for storage
- Adjust to level on cement floor
- Operate manually (no motors)

## System Architecture

### Frame Structure

The router sled consists of a Y-frame base supporting an X-gantry carriage. The Y-frame sits on the floor and spans over the workpiece. The X-gantry bolts to Y-rail slide blocks and carries the router plate assembly.

**Y-Frame (Base):**
- Two parallel 95" steel tubes (2×3, 14g) oriented vertically
- 38" lumber cross-braces connect tube ends at 90° angles
- Eight M12 leveling feet support the frame (four per side)
- Two 2200mm SBR20 linear rails mount to tube tops
- Provides 86.6" of Y-axis travel

**X-Gantry (Moving Carriage):**
- Box frame with 8" × 36" internal dimensions
- Two 40" steel tubes (2×3, 14g) spaced 8" apart
- Two 8" cross-braces at frame ends (cut from 16" leftover tube)
- Two 1000mm SBR20 linear rails mount to tube tops
- Provides 39.4" of X-axis travel

### Motion System

The system provides two-axis motion through linear rails and slide blocks:

1. **Y-Axis Motion:** X-gantry travels along Y-rails (86.6" range)
2. **X-Axis Motion:** Router plate travels along X-rails (39.4" range)

All motion is manual. Operators push the gantry and router plate by hand during surfacing operations.

### Height Adjustment System

The system handles 1" to 5" slabs through three adjustment mechanisms:

**Leveling Feet:** M12 adjustable feet provide 1.5" range for floor leveling
**Router Height:** Bosch 1617EVS depth adjustment provides 2" range
**Gantry Position:** Two mounting positions 3" apart extend range

**Total Adjustment Range:** 6.5" (exceeds 4" requirement with margin)

## Detailed Components

### Y-Frame Construction

**Main Structure:**

Two 95" steel tubes (2×3 rectangular, 14g, 0.075" wall) form parallel rails. Orient tubes vertically (2" face horizontal, 3" face vertical) for maximum rigidity. Space tubes 38" apart (inside dimension).

**End Cross-Braces:**

Two 38" pieces of 2×4 lumber connect tube ends at 90° angles. Each corner uses two L-brackets (8 total):
- One L-bracket on top face of joint
- One L-bracket on bottom face of joint
- Each bracket: one leg bolts to steel tube (M6 rivnuts), other leg screws into lumber (wood screws)

**Leveling System:**

Eight M12 adjustable feet attach to bottom of steel tubes (four per tube). Install M12 rivnuts in tube walls. Distribute feet along length for stable support. Adjust feet to level frame on cement floor.

**Y-Rail Installation:**

Two 2200mm SBR20 linear rails mount to top surface of steel tubes using clamp-mark-drill method:
1. Clamp rail in position on tube
2. Mark hole locations through rail mounting slots
3. Drill marked holes
4. Install M6 rivnuts
5. Bolt rail using M6 socket head cap screws with Loctite 242

Approximately 30 rivnuts required per rail (60 total for Y-axis).

### X-Gantry Construction

**Box Frame:**

Two 40" steel tubes (2×3, 14g) run parallel, spaced 8" apart (inside dimension). Two 8" cross-braces (cut from 16" leftover tube) connect the 40" tubes at each end, creating a rigid box with 8" × 36" internal dimensions.

**Corner Connections:**

Each of four corners uses one T-plate and one L-bracket:

**T-Plate (Top Face):**
- Flat steel plate (3" × 4" × 1/4")
- Bolts to Y-rail slide block (4 M6 bolts)
- Bolts to 40" gantry tube top (4 M6 bolts into rivnuts)
- Bolts to 8" cross-brace top (4 M6 bolts into rivnuts)

**L-Bracket (Bottom Face):**
- Bolts to 40" gantry tube bottom (4 M6 bolts into rivnuts)
- Bolts to 8" cross-brace bottom (4 M6 bolts into rivnuts)

**Per-Corner Fasteners:**
- 24 M6 bolts (16 with lockwashers for height adjustment, 8 to slide blocks)
- 16 M6 rivnuts

**Total X-Gantry Fasteners:**
- 4 T-plates (3" × 4" × 1/4" steel)
- 4 L-brackets
- 96 M6 bolts
- 64 M6 rivnuts

**Height Adjustment:**

Install 8 M6 rivnuts at each corner (4 on top, 4 on bottom of 2" horizontal face) for 32 rivnuts total. T-plates bolt to either top or bottom rivnut set:
- **High position:** Tubes bolt to bottom of T-plates (tubes rest on top)
- **Low position:** Tubes bolt to top of T-plates (tubes hang 3" lower)

Use lockwashers (not Loctite) on height adjustment bolts to permit reconfiguration.

**X-Rail Installation:**

Two 1000mm SBR20 linear rails mount to top surface of 40" gantry tubes using the same clamp-mark-drill method as Y-rails. Use M6 rivnuts and socket head cap screws with Loctite 242.

### Router Plate Assembly

**Acrylic Plate:**

10" × 12" × 1/2" acrylic provides the router mounting surface. This thickness prevents flex under router weight and cutting forces. Size the plate to fit between Z-bracket positions with margin for fastener holes.

**Mounting System:**

Four Z-brackets connect the router plate to four X-rail slide blocks (SBR20UU):
- One Z-bracket per slide block
- One bracket leg bolts to slide block
- Perpendicular bracket leg bolts through acrylic plate
- Provides stable four-point support

**Router Installation:**

Mount Bosch 1617EVS to acrylic plate using router's standard base plate mounting pattern. Router depth adjustment provides 2" of height range.

### Optional Accessories

**Dust Collection:**

Aftermarket dust collection boot for Bosch 1617EVS connects to shop vacuum. Mounts to router, collects chips at source. Manage hose routing to avoid restricting gantry motion.

**Ergonomic Handles:**

Add handles to X-gantry tubes for comfortable pushing during operation. Design mounting points for wooden dowels, cabinet pulls, or 3D-printed custom handles. Install after initial testing to determine optimal positions.

## Complete Bill of Materials

### Steel Components

| Component | Quantity | Size | Status | Notes |
|-----------|----------|------|--------|-------|
| Y-frame tubes | 2 | 95" × 2×3, 14g | PURCHASED | Pre-painted |
| X-gantry tubes | 2 | 40" × 2×3, 14g | PURCHASED | Pre-painted |
| X-gantry cross-braces | 2 | 8" × 2×3, 14g | ON HAND | Cut from 16" leftover |
| T-plates (gantry mounting) | 4 | 3" × 4" × 1/4" | TO PURCHASE | Connect Y-slides to X-gantry |
| L-brackets (Y-frame corners) | 8 | Heavy-duty steel | TO PURCHASE | Two per corner |
| L-brackets (X-gantry corners) | 4 | Steel | TO PURCHASE | Bottom face only |

### Lumber & Acrylic

| Component | Quantity | Size | Status | Notes |
|-----------|----------|------|--------|-------|
| Y-frame cross-braces | 2 | 38" × 2×4 | TO PURCHASE | Connects Y-frame ends |
| Router base plate | 1 | 10" × 12" × 1/2" acrylic | TO PURCHASE | 1/2" thickness critical |

### Linear Motion (All Purchased)

| Component | Quantity | Size | Status | Travel |
|-----------|----------|------|--------|--------|
| Y-axis rails + blocks | 2 rails + 4 blocks | SBR20-2200mm | PURCHASED | 86.6" |
| X-axis rails + blocks | 2 rails + 4 blocks | SBR20-1000mm | PURCHASED | 39.4" |

### Router System

| Component | Quantity | Status | Notes |
|-----------|----------|--------|-------|
| Bosch 1617EVS router | 1 | PURCHASED | Fixed base, 2" depth adjustment |
| Router bit | 1 | PURCHASED | Slab surfacing bit |
| Z-brackets | 4 | PURCHASED | Router plate to X-rails |

### Fasteners (All Purchased)

| Component | Quantity | Status | Application |
|-----------|----------|--------|-------------|
| M5 rivnuts | 100 | PURCHASED | Spare/future use |
| M5 socket head cap screws | 100 | PURCHASED | Spare/future use |
| M6 rivnuts | 100 | PURCHASED | Rails, gantry, cross-braces |
| M6 socket head cap screws | 100 | PURCHASED | Rails, gantry, cross-braces |
| M12 rivnuts | 10 | PURCHASED | Leveling feet |
| Wood screws | As needed | ON HAND | L-brackets to lumber |
| Pocket screws | As needed | ON HAND | Lumber joints (if needed) |
| Lockwashers (M6) | 64 | TO PURCHASE | Gantry height adjustment bolts |

### Hardware & Tools

| Component | Quantity | Status | Notes |
|-----------|----------|--------|-------|
| M12 adjustable leveling feet | 8 | PURCHASED | BokWin, 1.5" adjustment |
| Rivnut installation tool | 1 | PURCHASED | M5, M6, M12 |
| Loctite 242 | 1 bottle | ON HAND | Blue threadlocker |
| Pocket screw jig | 1 | ON HAND | For lumber assembly |
| Hand drill & bits | 1 set | ON HAND | Rivnut hole drilling |
| Level | 1 | ON HAND | Frame leveling |
| 3D printer | 1 | ON HAND | End caps, shims, custom parts |

### Optional Accessories (Future)

| Component | Status | Purpose |
|-----------|--------|---------|
| Dust collection boot (Bosch 1617EVS) | TO PURCHASE | Chip collection |
| Ergonomic handles | TO FABRICATE | Operator comfort |

## Assembly Sequence

### Phase 1: Y-Frame Assembly

1. **Prepare lumber cross-braces**
   - Cut two 38" pieces from 2×4 lumber
   - Ensure ends are square

2. **Install corner L-brackets**
   - Position lumber between steel tube ends
   - Install 8 L-brackets (2 per corner: top and bottom)
   - Drill and install M6 rivnuts in tube ends
   - Screw bracket legs into lumber with wood screws
   - Creates 95" × 38" rectangular frame

3. **Install leveling feet**
   - Mark positions for 8 feet (4 per tube, distributed along length)
   - Drill holes for M12 rivnuts in tube bottom edges
   - Install M12 rivnuts
   - Thread leveling feet into rivnuts

4. **Level the frame**
   - Place frame on cement floor
   - Adjust M12 feet until frame is level in both axes
   - Use quality level for accuracy

5. **Install Y-rails** (First rail already complete)
   - Clamp first rail in position (verify alignment)
   - Second rail: clamp, mark holes through mounting slots, drill, install M6 rivnuts
   - Bolt both rails with M6 socket head cap screws and Loctite 242
   - Verify rails are parallel and slide blocks move smoothly

### Phase 2: X-Gantry Assembly

1. **Prepare cross-braces**
   - Cut 16" leftover tube into two 8" pieces
   - Deburr cut ends

2. **Drill rivnut holes**
   - Mark rivnut positions on all four corners (8 holes per corner: 4 top, 4 bottom)
   - Drill holes for M6 rivnuts
   - Install 64 M6 rivnuts total (16 per corner)

3. **Assemble box frame**
   - Position 40" tubes 8" apart
   - Place 8" cross-braces at ends
   - Install 4 L-brackets on bottom face (one per corner)
   - Bolt brackets to tubes and cross-braces with M6 bolts and Loctite 242
   - Verify frame is square

4. **Install X-rails**
   - Clamp rails in position on top of 40" tubes
   - Mark holes, drill, install M6 rivnuts
   - Bolt rails with M6 socket head cap screws and Loctite 242
   - Verify rails are parallel and slide blocks move smoothly

### Phase 3: Gantry-to-Frame Connection

1. **Choose height position**
   - For thick slabs (4-5"): Use low position (tubes on top of T-plates)
   - For thin slabs (1-2"): Use high position (tubes hanging from T-plates)

2. **Install T-plates**
   - Position X-gantry assembly on Y-rail slide blocks
   - Bolt T-plates to slide blocks (4 M6 bolts per plate)
   - Bolt T-plates to 40" gantry tubes (4 M6 bolts with lockwashers)
   - Bolt T-plates to 8" cross-braces (4 M6 bolts with lockwashers)
   - Verify gantry moves smoothly along Y-rails

### Phase 4: Router Plate Installation

1. **Prepare acrylic plate**
   - Cut 10" × 12" × 1/2" acrylic to size
   - Mark and drill holes for Z-bracket mounting
   - Mark and drill holes for router base mounting
   - Deburr all holes

2. **Mount Z-brackets**
   - Bolt one leg of each Z-bracket to X-rail slide block
   - Bolt perpendicular leg through acrylic plate
   - Use four Z-brackets total (one per slide block)
   - Ensure plate is level and centered

3. **Mount router**
   - Attach Bosch 1617EVS to acrylic plate using standard mounting pattern
   - Verify router is secure and perpendicular to plate

### Phase 5: Testing and Adjustment

1. **Motion testing**
   - Move gantry along full Y-axis travel (86.6")
   - Move router plate along full X-axis travel (39.4")
   - Verify smooth motion with no binding
   - Check for adequate clearance in all positions

2. **Height range verification**
   - Test router at lowest position (low gantry + lowered router)
   - Test router at highest position (high gantry + raised router)
   - Verify 1" to 5" slab range is achievable

3. **Leveling verification**
   - Recheck frame level after assembly
   - Adjust M12 feet as needed

### Phase 6: Optional Accessories (Future)

1. **Dust collection** (when purchased)
   - Install dust boot on Bosch 1617EVS
   - Connect shop vacuum hose
   - Test hose routing during motion

2. **Ergonomic handles** (after initial use)
   - Determine optimal handle positions based on operation
   - Design and fabricate or 3D print mounting brackets
   - Install handles on X-gantry tubes

## Critical Assembly Notes

### Rivnut Installation

- Use proper rivnut tool to avoid stripping threads
- Clean and deburr all holes before installation
- Ensure tube walls are flat and free of paint at rivnut locations
- Test fit screws before final assembly

### Linear Rail Alignment

- Rails must be parallel and coplanar for smooth motion
- Use the clamp-mark-drill method (proven on first Y-rail)
- Small misalignments cause binding and poor surface finish
- Verify slide blocks move freely before bolting rails permanently

### Thread Locking Strategy

**Use Loctite 242 (blue) for:**
- All rail mounting screws
- Cross-brace L-bracket bolts
- Any fastener that should not be adjusted

**Use lockwashers for:**
- Gantry height adjustment bolts (T-plate connections)
- Any connection requiring reconfiguration

### Leveling Procedure

1. Use quality level (digital recommended)
2. Level both X and Y axes
3. Recheck periodically (cement may settle)
4. Verify level after any frame adjustment

### Safety Considerations

- Secure all fasteners before powering router
- Verify acrylic plate thickness supports router weight
- Test all motions without router power before cutting
- Wear hearing and eye protection during operation
- Ensure adequate ventilation or dust collection

## Design Rationale

### Steel Tube Selection (2×3, 14g)

**Benefits:**
- Good strength-to-weight ratio for this application
- 14g walls support rivnut installation
- Vertical orientation maximizes rigidity
- Pre-painted finish reduces preparation work

**Vertical Orientation:**
- 3" vertical dimension provides maximum resistance to bending
- 2" horizontal dimension adequate for rail mounting and connections
- Natural height increment (3") serves as gantry adjustment range

### SBR20 Linear Rails

**Benefits:**
- Common size with good availability and cost
- Four bearing blocks per axis provide stability
- 20mm rail diameter supports router weight and cutting forces
- VEVOR offers good value for hobbyist applications

**Rail Selection:**
- 2200mm Y-rails: Adequate for 96" slabs with margin
- 1000mm X-rails: Covers 36" slab width plus router travel

### M6 Fasteners for Rails

**Benefits:**
- Standard size for SBR20 rail mounting holes
- Adequate clamping force for secure rail attachment
- Rivnuts in 14g steel provide sufficient pull-out strength
- Socket head cap screws allow low-profile installation

### Modular/Disassemblable Design

**Benefits:**
- Accommodates garage/shop space constraints
- Permits seasonal storage
- Allows future modifications and upgrades
- L-bracket and bolt connections disassemble easily

**Critical Connections:**
- Y-frame corners: 8 L-brackets (removable)
- Gantry to Y-rails: 4 T-plates (removable, adjustable)
- All fasteners are bolts or screws (no welds)

### Workpiece Support (Floor-Mounted)

**Benefits:**
- Maximizes slab capacity (no table size constraint)
- Leverages M12 leveling feet for height adjustment
- Simple setup (slab rests directly on floor)
- Cement floor provides stable, flat reference

**Considerations:**
- Floor must be reasonably level (leveling feet compensate)
- Slab must be clean on bottom surface
- May want sacrificial surface under slab to protect cement

## Maintenance and Operation

### Pre-Operation Checklist

- Verify frame is level
- Check that all fasteners are tight
- Lubricate linear rails per manufacturer specifications
- Test gantry and router motion for smooth operation
- Ensure router bit is sharp and properly secured
- Connect dust collection if installed

### Operation Guidelines

- Support slab on level surface (cement floor or platform)
- Set gantry height for slab thickness
- Adjust router depth for desired cut depth (shallow passes recommended)
- Push gantry steadily and smoothly
- Let router reach full speed before engaging workpiece
- Make multiple shallow passes rather than single deep cut

### Maintenance Schedule

**After Each Use:**
- Clean sawdust from rails and slide blocks
- Wipe down acrylic plate
- Check for loose fasteners

**Monthly (or every 20 hours of use):**
- Lubricate linear rails and slide blocks
- Verify frame level
- Check router bit sharpness
- Inspect all fasteners

**Annually:**
- Disassemble for deep cleaning
- Inspect rivnuts for pull-out
- Check acrylic plate for cracks
- Verify rail alignment

## Future Enhancements

### CNC Conversion (Advanced)

Add stepper motors and control system for automated surfacing:
- Y-axis motor and lead screw
- X-axis motor and lead screw
- Z-axis motor for router depth
- Limit switches for homing
- Controller (GRBL, Mach3, or similar)

### 3D-Printed Components

Design and print custom parts:
- End caps for steel tube (protective, finished appearance)
- Shims for fine rail alignment
- Cable management clips
- Router bit storage holders
- Dust port adapters

### Enhanced Dust Collection

Improve chip removal:
- Custom shroud around bit (3D printed or fabricated)
- Multiple vacuum ports
- Magnetic dust shoe for quick attachment/removal

### Digital Readout (DRO)

Add measurement scales:
- Linear scales on X and Y axes
- Digital display for precise positioning
- Useful for repeatable cuts and patterns

### Workpiece Hold-Down

Prevent slab movement during surfacing:
- Cam clamps at slab edges
- Vacuum hold-down system
- Featherboards for pressure

## Conclusion

This design provides a robust, adjustable router sled for flattening hardwood slabs from 1" to 5" thick and up to 36" × 96" in size. The modular construction permits disassembly for storage, while the height adjustment system handles a wide range of slab thicknesses. The proven clamp-mark-drill method for rail installation ensures accurate alignment with accessible tools.

The design emphasizes:
- **Simplicity:** Uses readily available components and standard tools
- **Rigidity:** Steel tube frame and linear rails provide stable platform
- **Flexibility:** Multiple height positions and manual operation
- **Practicality:** Disassembles for storage, assembles on cement floor

Next steps: detailed build plan with step-by-step instructions, technical drawings (OpenSCAD 3D models and SVG fabrication templates), and parts procurement.

---

**Document History:**
- 2025-11-18: Initial design (brainstorming session with Claude Code)
