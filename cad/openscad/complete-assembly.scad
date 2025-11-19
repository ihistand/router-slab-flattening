// Complete Router Sled Assembly
// Combines Y-frame and X-gantry with proper positioning

// Import component modules (if using separate files, otherwise include inline)
// For standalone use, this file includes all modules inline

// All dimensions in millimeters

// === SHARED DIMENSIONS ===
tube_width = 2 * 25.4;    // 50.8mm
tube_height = 3 * 25.4;   // 76.2mm
tube_wall = 2;            // 14 gauge ≈ 2mm

// Y-frame dimensions
y_tube_length = 95 * 25.4;  // 2413mm
y_lumber_length = 38 * 25.4;  // 965.2mm
y_rail_length = 2200;

// X-gantry dimensions
x_tube_length = 40 * 25.4;  // 1016mm
x_cross_brace_length = 8 * 25.4;  // 203.2mm
x_rail_length = 1000;

// Colors
steel_color = [0.6, 0.6, 0.7];
wood_color = [0.8, 0.6, 0.4];
rail_color = [0.3, 0.3, 0.3];
plate_color = [0.9, 0.9, 0.95, 0.7];

// === MODULES ===

module steel_tube(length) {
    color(steel_color)
    difference() {
        cube([tube_width, tube_height, length]);
        translate([tube_wall, tube_wall, -1])
        cube([tube_width - 2*tube_wall, tube_height - 2*tube_wall, length + 2]);
    }
}

module y_frame_base() {
    lumber_width = 3.5 * 25.4;
    lumber_height = 1.5 * 25.4;

    // First tube
    translate([0, 0, 0])
    rotate([0, 0, 90])
    steel_tube(y_tube_length);

    // Second tube
    translate([y_lumber_length, 0, 0])
    rotate([0, 0, 90])
    steel_tube(y_tube_length);

    // Cross-braces
    color(wood_color) {
        translate([0, tube_height/2 - lumber_height/2, 0])
        cube([lumber_width, lumber_height, y_lumber_length]);

        translate([0, tube_height/2 - lumber_height/2, y_tube_length - lumber_width])
        cube([lumber_width, lumber_height, y_lumber_length]);
    }
}

module y_rails() {
    rail_width = 20;
    rail_height = 20;

    color(rail_color) {
        // Left rail
        translate([tube_width/2 - rail_width/2, tube_height, (y_tube_length - y_rail_length)/2])
        cube([rail_width, rail_height, y_rail_length]);

        // Right rail
        translate([y_lumber_length + tube_width/2 - rail_width/2, tube_height, (y_tube_length - y_rail_length)/2])
        cube([rail_width, rail_height, y_rail_length]);
    }
}

module x_gantry(position_on_y) {
    // Position is Z coordinate along Y-rails where gantry sits

    // Offset for centering gantry on Y-frame
    x_offset = y_lumber_length/2 - x_tube_length/2;

    translate([x_offset, tube_height + 28, position_on_y]) {
        // Front tube
        translate([0, 0, 0])
        rotate([0, 0, 90])
        steel_tube(x_tube_length);

        // Rear tube
        translate([0, 0, x_cross_brace_length])
        rotate([0, 0, 90])
        steel_tube(x_tube_length);

        // Cross-braces
        translate([0, 0, 0])
        rotate([0, 90, 0])
        steel_tube(x_cross_brace_length);

        translate([x_tube_length - tube_width, 0, 0])
        rotate([0, 90, 0])
        steel_tube(x_cross_brace_length);

        // X-rails
        rail_width = 20;
        rail_height = 20;

        color(rail_color) {
            translate([x_tube_length/2 - x_rail_length/2, tube_height, tube_width/2 - rail_width/2])
            rotate([0, 90, 0])
            cube([rail_width, rail_height, x_rail_length]);

            translate([x_tube_length/2 - x_rail_length/2, tube_height, x_cross_brace_length - tube_width/2 - rail_width/2])
            rotate([0, 90, 0])
            cube([rail_width, rail_height, x_rail_length]);
        }
    }
}

module router_assembly(x_position, y_position) {
    // Position on X-gantry (x_position along X-rails, y_position along Y-rails)

    plate_width = 10 * 25.4;
    plate_length = 12 * 25.4;
    plate_thickness = 0.5 * 25.4;

    router_diameter = 6 * 25.4;
    router_height = 8 * 25.4;

    x_offset = y_lumber_length/2 - x_tube_length/2;

    // Calculate absolute position
    translate([x_offset + x_position - plate_width/2, tube_height + 28 + tube_height + 68, y_position - plate_length/2]) {
        // Router plate
        color(plate_color)
        difference() {
            cube([plate_width, plate_thickness, plate_length]);
            translate([plate_width/2, -1, plate_length/2])
            cylinder(h=plate_thickness+2, d=4*25.4, $fn=64);
        }

        // Router
        translate([plate_width/2, plate_thickness + router_diameter/2, plate_length/2]) {
            color([0.2, 0.3, 0.4]) {
                rotate([90, 0, 0])
                cylinder(h=router_height, d=router_diameter, $fn=64);

                translate([0, -router_height, 0])
                rotate([90, 0, 0])
                cylinder(h=50, d=12, $fn=32);
            }
        }
    }
}

// === COMPLETE ASSEMBLY ===

// Set gantry position (Z coordinate along Y-axis, 0 to ~2200mm)
gantry_y_position = 1000;  // Center position

// Set router position (X coordinate along X-axis, relative to gantry center)
router_x_position = x_tube_length/2;  // Center position

module complete_router_sled() {
    // Y-frame base
    y_frame_base();

    // Y-rails
    y_rails();

    // X-gantry (positioned on Y-rails)
    x_gantry(gantry_y_position);

    // Router assembly (positioned on X-gantry)
    router_assembly(router_x_position, gantry_y_position);

    // Reference work piece (optional, shown for scale)
    show_workpiece = true;
    if (show_workpiece) {
        workpiece_width = 36 * 25.4;
        workpiece_length = 96 * 25.4;
        workpiece_thickness = 4 * 25.4;

        translate([y_lumber_length/2 - workpiece_width/2, -workpiece_thickness - 60, y_tube_length/2 - workpiece_length/2])
        color([0.7, 0.5, 0.3, 0.5])
        cube([workpiece_width, workpiece_thickness, workpiece_length]);
    }
}

// Render
complete_router_sled();

// === VIEWING NOTES ===
// - Use OpenSCAD's view controls to rotate and inspect the assembly
// - Gantry position can be adjusted by changing gantry_y_position variable
// - Router position can be adjusted by changing router_x_position variable
// - Workpiece visibility can be toggled with show_workpiece variable

// === DIMENSIONS SUMMARY ===
// Overall footprint: 95" x 38" (2413mm x 965mm)
// Working envelope: ~86" x 39" (2186mm x 991mm)
// Height: Variable with adjustment (1" to 5" slab capacity)
// Frame weight: Approximately 60-80 lbs assembled
