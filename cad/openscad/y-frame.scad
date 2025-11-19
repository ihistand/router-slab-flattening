// Y-Frame Assembly for Router Sled
// 95" x 38" frame with 2x3 steel tubes, lumber cross-braces, and leveling feet

// All dimensions in millimeters
// Inches to mm conversion: multiply by 25.4

// Steel tube dimensions
tube_length = 95 * 25.4;  // 2413mm
tube_width = 2 * 25.4;    // 50.8mm
tube_height = 3 * 25.4;   // 76.2mm
tube_wall = 2;            // 14 gauge ≈ 2mm

// Lumber dimensions
lumber_length = 38 * 25.4;  // 965.2mm
lumber_width = 3.5 * 25.4;  // 88.9mm (actual 2x4 width)
lumber_height = 1.5 * 25.4; // 38.1mm (actual 2x4 height)

// Leveling feet
foot_diameter = 12;  // M12 threads
foot_length = 50;    // Approximate visible length

// Rail dimensions
rail_width = 20;  // SBR20
rail_height = 20;
rail_length = 2200;  // 2200mm rails

// Colors
steel_color = [0.6, 0.6, 0.7];
wood_color = [0.8, 0.6, 0.4];
rail_color = [0.3, 0.3, 0.3];

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

module lumber_cross_brace() {
    color(wood_color)
    cube([lumber_width, lumber_height, lumber_length]);
}

module leveling_foot() {
    color([0.4, 0.4, 0.4])
    union() {
        // Threaded shaft
        cylinder(h=foot_length, d=foot_diameter, $fn=24);
        // Foot pad
        translate([0, 0, -10])
        cylinder(h=10, d=foot_diameter*2.5, $fn=32);
    }
}

module l_bracket() {
    // Simplified L-bracket representation
    bracket_thickness = 3;
    bracket_width = 50;
    bracket_length1 = 40;
    bracket_length2 = 40;

    color([0.3, 0.3, 0.35])
    union() {
        // Horizontal leg
        cube([bracket_width, bracket_thickness, bracket_length1]);
        // Vertical leg
        cube([bracket_width, bracket_length2, bracket_thickness]);
    }
}

module y_rail() {
    color(rail_color)
    cube([rail_width, rail_height, rail_length]);
}

module y_rail_slide_block() {
    // SBR20UU slide block
    block_length = 60;
    block_width = 34;
    block_height = 28;

    color([0.2, 0.2, 0.25])
    cube([block_width, block_height, block_length]);
}

// Complete Y-Frame Assembly
module y_frame_assembly() {
    // First 95" tube (left side)
    translate([0, 0, 0])
    rotate([0, 0, 90])
    steel_tube(tube_length);

    // Second 95" tube (right side, spaced 38" apart)
    translate([lumber_length, 0, 0])
    rotate([0, 0, 90])
    steel_tube(tube_length);

    // Front cross-brace
    translate([0, tube_height/2 - lumber_height/2, 0])
    rotate([0, 0, 0])
    lumber_cross_brace();

    // Rear cross-brace
    translate([0, tube_height/2 - lumber_height/2, tube_length - lumber_width])
    rotate([0, 0, 0])
    lumber_cross_brace();

    // L-brackets at corners (8 total - simplified representation)
    // Front left top
    translate([-5, tube_height, -5])
    rotate([90, 0, 0])
    l_bracket();

    // Front right top
    translate([lumber_length - 45, tube_height, -5])
    rotate([90, 0, 0])
    l_bracket();

    // Rear left top
    translate([-5, tube_height, tube_length - lumber_width + 5])
    rotate([90, 0, 0])
    l_bracket();

    // Rear right top
    translate([lumber_length - 45, tube_height, tube_length - lumber_width + 5])
    rotate([90, 0, 0])
    l_bracket();

    // Leveling feet (8 total, 4 per tube)
    feet_positions = [250, 650, 1050, 1450, 1850];  // Approximate spacing along 95"

    for (pos = feet_positions) {
        // Left tube feet
        translate([tube_width/2, -foot_length + 5, pos])
        rotate([0, 0, 0])
        leveling_foot();

        // Right tube feet
        translate([lumber_length + tube_width/2, -foot_length + 5, pos])
        rotate([0, 0, 0])
        leveling_foot();
    }

    // Y-rails (2200mm, mounted on top of tubes)
    // Left rail
    translate([tube_width/2 - rail_width/2, tube_height, (tube_length - rail_length)/2])
    y_rail();

    // Right rail
    translate([lumber_length + tube_width/2 - rail_width/2, tube_height, (tube_length - rail_length)/2])
    y_rail();

    // Slide blocks (4 total, 2 per rail, positioned for visibility)
    // Left rail blocks
    translate([tube_width/2 - 17, tube_height, 400])
    y_rail_slide_block();

    translate([tube_width/2 - 17, tube_height, 1600])
    y_rail_slide_block();

    // Right rail blocks
    translate([lumber_length + tube_width/2 - 17, tube_height, 400])
    y_rail_slide_block();

    translate([lumber_length + tube_width/2 - 17, tube_height, 1600])
    y_rail_slide_block();
}

// Render the assembly
y_frame_assembly();

// Add reference annotations (as comments for documentation)
// Frame dimensions: 95" (2413mm) x 38" (965mm) x 3" (76mm) height
// Rail spacing: 38" (965mm) center-to-center
// Rail travel: 86.6" (2200mm)
// Leveling feet: M12, 8 total, ~1.5" adjustment range
