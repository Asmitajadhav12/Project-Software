Rubik’s Cube Solver Robot

This project is an automated Rubik’s Cube solver built using a Teensy 4.1 microcontroller, stepper motors, and a web-based interface.
It combines embedded programming, hardware design, and solving algorithms to demonstrate how robotics can be applied to a classic puzzle.

Features

A browser-based interface hosted on the Teensy, allowing users to configure the cube’s state.

Validation checks to prevent impossible cube configurations.

Six stepper motors that control the rotation of each cube face.

Adjustable stepper speed for reliable performance.

Efficient cube-solving logic based on the Kociemba two-phase algorithm.

Project Structure
rubiks-cube-solver-robot/
├─ firmware/
│  ├─ Cube_Solver.ino
│  ├─ Find_IP_Address.ino
│  └─ libraries.txt
├─ hardware/
│  ├─ Electronics_Schematic.pdf
│  └─ 3D_Parts/   # STL files go here
├─ docs/          # project report, block diagram, flowchart
├─ images/        # setup photos, UI screenshots, demo.gif
└─ README.md

Hardware

The robot is built around the Teensy 4.1 with an Ethernet kit.
It uses six NEMA-17 stepper motors paired with TMC2208 drivers to rotate each face of the cube.
A 24V power supply with a 5V step-down regulator powers the system, and the mechanical structure is made from 3D-printed parts such as motor mounts, cube adapters, and support frames.

Software

The project is developed in the Arduino IDE with the following key libraries:

AccelStepper – for controlling stepper motors

CubeCentral – for running the web-based user interface

CubeSolver – implementing the Kociemba two-phase algorithm for cube solving

How to Run

Connect the power supply to the drivers and the Teensy, ensuring all grounds are common.

Upload Find_IP_Address.ino to the Teensy and check the Serial Monitor for the assigned IP address.

Update this IP address in Cube_Solver.ino and upload it.

Open the IP in a web browser, configure the cube state, and press “Solve” to let the robot complete the solution.

Notes

If a motor rotates in the wrong direction, reverse the wiring of one motor phase.

If the cube jams or slips during operation, lower the motor speed, adjust the cube’s tension, or use retainer clips for stability.

Future Work

Potential improvements include:

Replacing Ethernet with Wi-Fi for easier connectivity.

Using smarter motor control profiles to reduce slippage.

Adding camera-based color detection to automate cube state entry.

Author

Asmita Jadhav
