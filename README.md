2D Occupancy Grid Mapping using Overhead Infrastructure Cameras

Overview
This project aims to develop a system for accurate and real-time 2D occupancy grid mapping of indoor environments using a network of RGB cameras positioned overhead. The mapped environment will be used for Autonomous Mobile Robot (AMR) navigation, leveraging infrastructure cameras instead of onboard sensors like LiDAR or depth cameras.
Project Scope and Goals
Scope:

    Integrate 4 RGB cameras in a 2x2 matrix configuration in the Gazebo simulation environment.
    Acquire images at 640x480 resolution from simulated cameras.
    Implement multi-camera calibration to align and calibrate Field of Views (FoVs).
    Develop algorithms to fuse images from multiple cameras into a composite 2D occupancy grid map.
    Generate a 2D occupancy grid map in .pgm format (512x512 resolution) suitable for integration with ROS navigation stack.

Goals:

    Create an accurate and dimensionally correct composite map of the environment.
    Benchmark accuracy against the ground truth map from Gazebo.
    Measure computational latency on an Intel i5 (10th Gen) CPU.
    Provide documentation, source code, and algorithms for evaluation.

Setup Instructions
Prerequisites:

    Ubuntu 20.04 with ROS2 Foxy installed.
    Gazebo simulation environment setup.
    Python 3.x environment.

Steps:

    Setting up ROS2 Environment:
        Install ROS2 Foxy and necessary packages.
        Create a ROS2 workspace and download required simulation packages.

    Integrating Cameras in Gazebo:
        Download the provided "infraCam.zip" and extract it into the Gazebo models directory.
        Modify configuration files to include the new camera models.

    Running Simulation:
        Launch the Gazebo simulation environment with the added cameras.
        Verify the visibility of overhead camera topics using ros2 topic list.

    Acquiring Camera Data:
        Use ROS2 Python scripts to subscribe to camera topics and acquire images.
        Ensure to source ROS2 environment (source /opt/ros/foxy/setup.bash) before running scripts.

    Mapping and Evaluation:
        Implement algorithms to process camera images, calibrate FoVs, and fuse images into a composite 2D occupancy grid map.
        Evaluate the accuracy of the generated map against key-point distances in the simulated environment.
        Measure computational latency using provided procedures.

Evaluation Criteria

    Accuracy: Compare average, minimum, and maximum errors of the composite map against ground truth distances.
    Computational Complexity: Measure and optimize computational latency on an Intel i5 CPU.
    Novelty and Practicality: Assess the uniqueness and efficiency of the solution in comparison to existing methods.

Deliverables

    Detailed documentation including project solution, approach, algorithm descriptions, and comparison to state-of-the-art.
    Composite 2D occupancy grid map in .pgm format.
    Error estimates and accuracy measurements of the map.
    Computational latency measurements and optimization details.
    Source code and algorithms for review and evaluation.
