#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImageListener(Node):

    def __init__(self):
        super().__init__('image_listener')
        self.subscription1 = self.create_subscription(
            Image,
            '/overhead_camera/overhead_camera1/image_raw',
            self.listener_callback1,  # Changed to listener_callback1
            10)
        self.subscription2 = self.create_subscription(
            Image,
            '/overhead_camera/overhead_camera2/image_raw',
            self.listener_callback2,
            10)
        self.bridge = CvBridge()

    def listener_callback1(self, msg):  # Changed function name to listener_callback1
        self.get_logger().info('Receiving image from camera 1')
        cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        cv2.imshow("Camera Image 1", cv_image)
        cv2.waitKey(1)

    def listener_callback2(self, msg):
        self.get_logger().info('Receiving image from camera 2')
        cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        cv2.imshow("Camera Image 2", cv_image)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = ImageListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

