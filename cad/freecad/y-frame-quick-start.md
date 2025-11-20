# Y-Frame Assembly Quick Start Guide

This guide walks you through creating the Y-frame assembly in FreeCAD. The Y-frame forms the foundation of the router sled system.

## What You'll Build

The Y-frame assembly includes:
- Two 96" steel tubes (2×3, 14 gauge, vertical orientation)
- Two 2200mm SBR20 linear rails mounted on tube tops
- Eight M12 leveling feet (four per tube)
- Two lumber end caps (2×4 trimmed to fit)
- Connection plates (steel-to-lumber joints)

## Before You Start

**Time estimate:** 2-3 hours for first assembly

**Have ready:**
- FreeCAD installed (you have this)
- Design spec: `docs/plans/2025-11-19-freecad-model-design.md`
- Steel tube dimensions: 2" × 3" (50.8 × 76.2 mm), 14 gauge (2.1 mm wall)
- Rail specs: SBR20-2200mm with 40mm hole spacing

**What you'll learn:**
- Creating parametric models with spreadsheets
- Using sketches and constraints
- Creating linear patterns for hole arrays
- Building assemblies from parts

## Step 1: Create New File and Setup

### Create the File

1. Launch FreeCAD
2. File → New
3. File → Save As → Navigate to `cad/freecad/`
4. Name: `y-frame-assembly.FCStd`
5. Save

### Create Parameters Spreadsheet

1. Click the Spreadsheet workbench (top toolbar)
2. Spreadsheet → Create spreadsheet
3. Rename it to "Parameters" (right-click in tree → Rename)
4. Double-click "Parameters" to open it

### Enter Parameters

Enter these values in the spreadsheet:

| Cell | Name | Value | Units | Description |
|------|------|-------|-------|-------------|
| A1 | `y_tube_length` | 2438.4 | mm | 96 inches |
| A2 | `y_rail_length` | 2200 | mm | Linear rail length |
| A3 | `tube_width` | 50.8 | mm | 2 inches |
| A4 | `tube_height` | 76.2 | mm | 3 inches |
| A5 | `tube_wall_thickness` | 2.1 | mm | 14 gauge |
| A6 | `rail_hole_spacing` | 40 | mm | SBR20 standard |
| A7 | `rail_first_hole_offset` | 20 | mm | From rail end |
| A8 | `m6_hole_diameter` | 6 | mm | For rivnuts |
| A9 | `m12_hole_diameter` | 12 | mm | For leveling feet |

**Tips:**
- Enter values in column B
- Use descriptive names in column A
- FreeCAD will reference these as `Parameters.A1`, `Parameters.A2`, etc.

### Assign Aliases (Important!)

For each parameter row:
1. Right-click the cell (e.g., B1)
2. Select "Properties..."
3. In the "Alias" field, enter the name from column A (e.g., `y_tube_length`)
4. Click OK
5. Repeat for all parameters

Now you can reference parameters as `<<Parameters.y_tube_length>>` in sketches.

**Save your work:** File → Save

## Step 2: Create Steel Tube Part

### Switch to Part Design

1. Click Part Design workbench (top toolbar)
2. Click "Create body" button (or Part Design → Create body)
3. Rename body to "SteelTube_96in" (right-click in tree → Rename)

### Create Tube Cross-Section Sketch

1. With SteelTube_96in selected, click "Create sketch"
2. Select XY plane
3. Click OK

### Draw Outer Rectangle

1. Click Rectangle tool (in Sketcher toolbar)
2. Click near origin to start
3. Click to complete rectangle
4. Press Esc to exit tool

### Constrain Outer Rectangle

1. Click one vertical edge
2. Click Constrain Vertical Distance (toolbar)
3. Enter: `<<Parameters.tube_height>>` (include the << >>)
4. Click OK
5. Click one horizontal edge
6. Click Constrain Horizontal Distance
7. Enter: `<<Parameters.tube_width>>`
8. Click OK

### Center Rectangle on Origin

1. Click rectangle's bottom-left corner point
2. Hold Ctrl and click the origin point
3. Click Coincident constraint (toolbar)
   - This pins corner to origin

### Draw Inner Rectangle (Wall Thickness)

1. Click Rectangle tool
2. Draw a smaller rectangle inside the first
3. Press Esc

### Constrain Inner Rectangle

Calculate inner dimensions:
- Inner width = outer width - (2 × wall thickness)
- Inner height = outer height - (2 × wall thickness)

1. Click inner vertical edge
2. Constrain Vertical Distance
3. Enter: `<<Parameters.tube_height>> - 2 * <<Parameters.tube_wall_thickness>>`
4. Click inner horizontal edge
5. Constrain Horizontal Distance
6. Enter: `<<Parameters.tube_width>> - 2 * <<Parameters.tube_wall_thickness>>`

### Center Inner Rectangle

1. Click Symmetry constraint (toolbar)
2. Click outer rectangle's bottom-left corner
3. Click inner rectangle's bottom-left corner
4. Click outer rectangle's top-right corner
5. Press Esc

The inner rectangle centers automatically within the outer rectangle.

### Close Sketch

1. Click "Close" in Sketcher toolbar
2. The sketch should be fully constrained (green in tree)

**Save your work**

### Extrude Tube to Length

1. Select the sketch in tree (should be called "Sketch")
2. Click "Pad" tool (Part Design toolbar)
3. In Pad dialog:
   - Type: Dimension
   - Length: `<<Parameters.y_tube_length>>`
   - Check "Symmetric to plane" if you want (optional)
4. Click OK

You now have a 96" hollow tube!

**Save your work**

## Step 3: Add Leveling Feet Holes

Leveling feet mount to the bottom of the tube (four holes per tube).

### Create Leveling Feet Sketch

1. Select a face on the **bottom** of the tube (the 2×3 face)
2. Click "Create sketch" (Part Design toolbar)
3. The selected face becomes your sketch plane

### Position First Hole

1. Click Circle tool
2. Click to place circle (approximate location)
3. Press Esc

### Constrain First Hole

1. Click circle
2. Constrain Radius: `<<Parameters.m12_hole_diameter>> / 2`
3. Click circle center point
4. Click one edge of the rectangular face
5. Constrain distance from edge: `25.4` mm (1 inch from end)
6. Constrain distance from other edge: `<<Parameters.tube_width>> / 2` (centered)

### Create Linear Pattern for 4 Holes

1. Click circle
2. Tools → Linear pattern (or click Linear pattern tool)
3. Direction: Along length of tube
4. Occurrences: 4
5. Spacing: Calculate manually or use: `<<Parameters.y_tube_length>> / 4`
   - For 96" tube: approximately 609.6 mm spacing
6. Click OK

You should see 4 circles evenly spaced along the tube bottom.

### Close Sketch

Click "Close" in Sketcher toolbar.

### Create Holes (Pocket)

1. Select the sketch with 4 circles
2. Click "Pocket" tool (Part Design toolbar)
3. Type: Through All
4. Click OK

You now have 4 M12 holes for leveling feet!

**Save your work**

## Step 4: Add Rail Mounting Holes

Linear rails mount to the **top** of the tube. The SBR20 rails have holes every 40mm.

### Calculate Number of Holes

For a 2200mm rail with 40mm spacing and 20mm offset:
- Number of holes ≈ (2200 - 2×20) / 40 + 1 ≈ 55 holes

We'll use FreeCAD's linear pattern to create these.

### Create Rail Mounting Sketch

1. Select the **top** face of the tube (opposite side from leveling feet)
2. Click "Create sketch"

### Position First Hole

1. Click Circle tool
2. Place circle near one end
3. Press Esc

### Constrain First Hole

1. Click circle
2. Constrain Radius: `<<Parameters.m6_hole_diameter>> / 2` (3mm radius)
3. Click circle center
4. Constrain distance from end edge: `<<Parameters.rail_first_hole_offset>>`
5. Constrain distance from side edge: `<<Parameters.tube_width>> / 2` (centered)

### Create Linear Pattern

1. Click circle
2. Tools → Linear pattern
3. Direction: Along tube length
4. Occurrences: Calculate: `(<<Parameters.y_rail_length>> - 2 * <<Parameters.rail_first_hole_offset>>) / <<Parameters.rail_hole_spacing>> + 1`
   - Or enter manually: ~55 holes
5. Spacing: `<<Parameters.rail_hole_spacing>>` (40mm)
6. Click OK

You should see a line of circles along the tube top.

### Close Sketch and Create Holes

1. Close sketch
2. Select the sketch
3. Click "Pocket" tool
4. Type: Through All
5. Click OK

You now have all rail mounting holes!

**Save your work**

## Step 5: Create Second Tube

You need two identical tubes for the Y-frame.

### Duplicate the Part

1. Right-click "SteelTube_96in" body in tree
2. Select "Duplicate selected object"
3. Rename the copy to "SteelTube_96in_Second"

### Position Second Tube

1. Select "SteelTube_96in_Second"
2. In Properties panel (View tab), set Placement:
   - Position: X = 0, Y = 1000, Z = 0 (or adjust spacing as needed)
   - This separates the two tubes for visualization

**Save your work**

## Step 6: Add Linear Rails (Simplified)

Linear rails sit on top of the tubes. We'll create simplified representations.

### Create Rail Body

1. Click "Create body" (Part Design workbench)
2. Rename to "LinearRail_Y_2200mm"

### Create Rail Sketch

1. With LinearRail selected, click "Create sketch"
2. Select XY plane
3. Draw 20mm × 20mm square (SBR20 = 20mm × 20mm profile)
4. Constrain dimensions to 20mm × 20mm
5. Close sketch

### Extrude Rail

1. Select sketch
2. Click "Pad"
3. Length: `<<Parameters.y_rail_length>>` (2200mm)
4. Click OK

### Position Rail on Tube

1. Select LinearRail body
2. In Properties → Placement, position it on top of first tube:
   - X: center on tube width
   - Y: 0
   - Z: on top of tube (tube height)

### Duplicate for Second Rail

1. Duplicate LinearRail body
2. Rename to "LinearRail_Y_2200mm_Second"
3. Position on second tube

**Save your work**

## Step 7: Add Leveling Feet (Simplified)

Create simplified representations of the M12 leveling feet.

### Create Leveling Foot Body

1. Create new body
2. Rename to "LevelingFoot_M12"

### Create Foot Sketch

1. Create sketch on XY plane
2. Draw circle with 25mm radius (approximate foot pad size)
3. Close sketch
4. Pad to 10mm height (foot pad thickness)

### Create Threaded Shaft

1. Create new sketch on top of foot pad
2. Draw 6mm radius circle (M12 thread ≈ 12mm diameter)
3. Close sketch
4. Pad to 100mm length (adjustment range)

### Position First Foot

Position the foot to align with the first M12 hole in the tube.

### Duplicate for Remaining Feet

Create 8 total feet (4 per tube), positioning each at the M12 hole locations.

**Tip:** You can create one foot, then use the Clone tool or Linear Pattern to create the array.

**Save your work**

## Step 8: Organize and Verify

### Organize the Tree

Your tree should look like:
```
y-frame-assembly
├── Parameters (Spreadsheet)
├── SteelTube_96in (Body)
│   ├── Sketch (tube cross-section)
│   ├── Pad (extrude)
│   ├── Sketch001 (leveling feet holes)
│   ├── Pocket (leveling feet)
│   ├── Sketch002 (rail mounting holes)
│   └── Pocket001 (rail mounting)
├── SteelTube_96in_Second (Body)
├── LinearRail_Y_2200mm (Body)
├── LinearRail_Y_2200mm_Second (Body)
└── LevelingFoot_M12 (Bodies, 8 total)
```

### Verify Parameters Work

Test the parametric model:
1. Open Parameters spreadsheet
2. Change `y_tube_length` from 2438.4 to 2000
3. Right-click document → Recompute
4. Verify tube shortened and holes adjusted
5. Change back to 2438.4
6. Recompute

If everything updates correctly, your parametric model works!

### Check Dimensions

Measure key features:
1. Select an edge or face
2. View → Measure distance
3. Verify against specifications

**Save your work**

## Step 9: Add Lumber End Caps (Optional)

The 2×4 lumber end caps connect to the tube ends. These are simple rectangular extrusions.

### Create End Cap Body

1. Create new body: "LumberEndCap_2x4"
2. Create sketch on XY plane
3. Draw rectangle:
   - Full section: 38mm × 89mm (actual 2×4 dimensions)
   - Trimmed section: 38mm × 64mm (to fit inside tube)
4. Create stepped profile showing trim
5. Extrude to ~100mm length

### Position End Caps

Position at tube ends where connection plates will join steel to lumber.

## Next Steps

You've completed the Y-frame assembly foundation! Next:

1. **Review your work:**
   - All parameters working correctly?
   - Holes positioned accurately?
   - File saved and stable?

2. **Create X-gantry assembly:**
   - Follow similar process
   - 40" tubes instead of 96"
   - X-axis rails (1000mm)
   - Slide block mounting points

3. **Generate technical drawings:**
   - Use TechDraw workbench
   - Create fabrication views showing hole positions
   - Add dimensions and callouts

4. **Build master assembly:**
   - Link Y-frame, X-gantry, and router mount
   - Show complete system
   - Check clearances and motion

## Troubleshooting

**Sketch won't close or has errors:**
- Check all constraints are applied correctly
- Look for over-constrained geometry (red in tree)
- Verify parameter references use correct syntax: `<<Parameters.name>>`

**Pad or Pocket fails:**
- Ensure sketch is fully constrained
- Check that the sketch plane makes sense for the operation
- Verify length/depth values are positive

**Parameters don't update:**
- Right-click document → Recompute
- Edit → Refresh document
- Check alias names match references exactly

**FreeCAD crashes or freezes:**
- Save frequently (every 5-10 minutes)
- Keep backup files
- Restart FreeCAD if it becomes sluggish
- Reduce complexity if needed (fewer holes for testing)

## Tips for Success

1. **Save frequently** - FreeCAD can crash
2. **Name everything** - Future you will thank you
3. **Use parameters** - Don't hard-code dimensions
4. **Test parameter changes** - Verify parametric model works
5. **Keep it simple** - Don't over-detail at first
6. **Take breaks** - This is complex work

## Resources

**FreeCAD Documentation:**
- Part Design workbench: https://wiki.freecad.org/Part_Design_Workbench
- Sketcher: https://wiki.freecad.org/Sketcher_Workbench
- Spreadsheet: https://wiki.freecad.org/Spreadsheet_Workbench

**Project Documentation:**
- Design spec: `docs/plans/2025-11-19-freecad-model-design.md`
- Build plan: `docs/plans/2025-11-18-build-plan.md`
- Project overview: `Router Sled Slab Flattening.md`

Good luck building your Y-frame assembly!
