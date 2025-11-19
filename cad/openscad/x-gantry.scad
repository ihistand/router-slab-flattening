// X-Gantry Assembly for Router Sled
// 40" x 8" box frame with 2x3 steel tubes, cross-braces, and X-rails

// All dimensions in millimeters

// Steel tube dimensions
tube_length = 40 * 25.4;  // 1016mm
tube_width = 2 * 25.4;    // 50.8mm
tube_height = 3 * 25.4;   // 76.2mm
tube_wall = 2;            // 14 gauge ≈ 2mm

// Cross-brace dimensions
cross_brace_length = 8 * 25.4;  // 203.2mm

// Rail dimensions
rail_width = 20;  // SBR20
rail_height = 20;
rail_length = 1000;  // 1000mm rails

// Router plate dimensions
plate_width = 10 * 25.4;   // 254mm
plate_length = 12 * 25.4;  // 304.8mm
plate_thickness = 0.5 * 25.4;  // 12.7mm (1/2")

// Router dimensions (approximate Bosch 1617EVS)
router_diameter = 6 * 25.4;  // 152.4mm
router_height = 8 * 25.4;    // 203.2mm

// Colors
steel_color = [0.6, 0.6, 0.7];
rail_color = [0.3, 0.3, 0.3];
plate_color = [0.9, 0.9, 0.95, 0.7];  // Translucent acrylic
router_color = [0.2, 0.3, 0.4];

module steel_tube(length) {
    color(steel_color)
    difference() {
        // Outer tube
        cube([tube_width, tube_height, length]);
        // Inner hollow
        translate([tube_wall, tube_wall, -1])
        cube([tube_width - 2*tube_wall, tube_height - 2*tube_wall, length + 2]);
    }
}

module t_plate() {
    // Simplified T-plate (3" x 4" x 1/4")
    plate_width = 3 * 25.4;   // 76.2mm
    plate_length = 4 * 25.4;   // 101.6mm
    plate_thickness = 0.25 * 25.4;  // 6.35mm

    color([0.5, 0.5, 0.55])
    // Simplified as flat plate (actual T-shape would be more complex)
    cube([plate_width, plate_length, plate_thickness]);
}

module l_bracket() {
    bracket_thickness = 3;
    bracket_width = 50;
    bracket_length1 = 40;
    bracket_length2 = 40;

    color([0.3, 0.3, 0.35])
    union() {
        cube([bracket_width, bracket_thickness, bracket_length1]);
        cube([bracket_width, bracket_length2, bracket_thickness]);
    }
}

module x_rail() {
    color(rail_color)
    cube([rail_width, rail_height, rail_length]);
}

module x_rail_slide_block() {
    // SBR20UU slide block
    block_length = 60;
    block_width = 34;
    block_height = 28;

    color([0.2, 0.2, 0.25])
    cube([block_width, block_height, block_length]);
}

module z_bracket() {
    // Simplified Z-bracket
    bracket_thickness = 5;
    bracket_height = 40;
    bracket_width = 50;

    color([0.35, 0.35, 0.4])
    union() {
        // Horizontal base
        cube([bracket_width, bracket_thickness, bracket_width]);
        // Vertical leg
        cube([bracket_width, bracket_height, bracket_thickness]);
    }
}

module router_plate() {
    color(plate_color)
    difference() {
        // Plate
        cube([plate_width, plate_thickness, plate_length]);
        // Router mounting hole (simplified)
        translate([plate_width/2, -1, plate_length/2])
        cylinder(h=plate_thickness+2, d=4*25.4, $fn=64);
    }
}

module router() {
    color(router_color)
    union() {
        // Router body (cylinder)
        rotate([90, 0, 0])
        cylinder(h=router_height, d=router_diameter, $fn=64);

        // Router bit (simplified)
        translate([0, -router_height, 0])
        rotate([90, 0, 0])
        cylinder(h=50, d=12, $fn=32);
    }
}

// Complete X-Gantry Assembly
module x_gantry_assembly() {
    // First 40" tube (front)
    translate([0, 0, 0])
    rotate([0, 0, 90])
    steel_tube(tube_length);

    // Second 40" tube (back, spaced 8" apart)
    translate([0, 0, cross_brace_length])
    rotate([0, 0, 90])
    steel_tube(tube_length);

    // Left cross-brace (8")
    translate([0, 0, 0])
    rotate([0, 90, 0])
    steel_tube(cross_brace_length);

    // Right cross-brace (8")
    translate([tube_length - tube_width, 0, 0])
    rotate([0, 90, 0])
    steel_tube(cross_brace_length);

    // L-brackets at corners (4 total, bottom face)
    // Front left
    translate([-5, -40, -5])
    rotate([0, 0, 0])
    l_bracket();

    // Front right
    translate([tube_length - 45, -40, -5])
    rotate([0, 0, 0])
    l_bracket();

    // Rear left
    translate([-5, -40, cross_brace_length - tube_width + 5])
    rotate([0, 0, 0])
    l_bracket();

    // Rear right
    translate([tube_length - 45, -40, cross_brace_length - tube_width + 5])
    rotate([0, 0, 0])
    l_bracket();

    // X-rails (1000mm, mounted on top of tubes)
    // Front rail
    translate([tube_length/2 - rail_length/2, tube_height, tube_width/2 - rail_width/2])
    rotate([0, 90, 0])
    x_rail();

    // Rear rail
    translate([tube_length/2 - rail_length/2, tube_height, cross_brace_length - tube_width/2 - rail_width/2])
    rotate([0, 90, 0])
    x_rail();

    // X-rail slide blocks (4 total, 2 per rail)
    // Front rail blocks
    translate([250, tube_height, tube_width/2 - 17])
    rotate([0, 90, 0])
    x_rail_slide_block();

    translate([700, tube_height, tube_width/2 - 17])
    rotate([0, 90, 0])
    x_rail_slide_block();

    // Rear rail blocks
    translate([250, tube_height, cross_brace_length - tube_width/2 - 17])
    rotate([0, 90, 0])
    x_rail_slide_block();

    translate([700, tube_height, cross_brace_length - tube_width/2 - 17])
    rotate([0, 90, 0])
    x_rail_slide_block();

    // Z-brackets (4 total, attached to slide blocks)
    // Front left
    translate([240, tube_height + 28, 15])
    z_bracket();

    // Front right
    translate([690, tube_height + 28, 15])
    z_bracket();

    // Rear left
    translate([240, tube_height + 28, cross_brace_length - 65])
    z_bracket();

    // Rear right
    translate([690, tube_height + 28, cross_brace_length - 65])
    z_bracket();

    // Router plate (mounted on Z-brackets)
    translate([tube_length/2 - plate_width/2, tube_height + 68, cross_brace_length/2 - plate_length/2])
    router_plate();

    // Router (mounted on plate)
    translate([tube_length/2, tube_height + 68 + plate_thickness + router_diameter/2, cross_brace_length/2])
    router();

    // T-plates at corners (shown for reference, simplified position)
    // These would be at Y-rail slide block interface in full assembly
    // Shown here slightly offset for visibility
    translate([-10, -50, 15])
    rotate([90, 0, 0])
    t_plate();
}

// Render the assembly
x_gantry_assembly();

// Add reference annotations (as comments for documentation)
// Frame dimensions: 40" (1016mm) x 8" (203mm) box
// Internal dimensions: 36" x 8" (914mm x 203mm)
// Rail spacing: 8" (203mm) center-to-center
// Rail travel: 39.4" (1000mm)
// Router plate: 10" x 12" x 1/2" (254mm x 305mm x 12.7mm)
// Height adjustment: 3" (76mm) via T-plate repositioning
