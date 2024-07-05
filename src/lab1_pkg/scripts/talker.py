#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from ackermann_msgs.msg import AckermannDriveStamped 


class TalkerNode(Node): 
    def __init__(self):
        super().__init__("talker")
        # Test VI  
        # Declare parameters with default value
        self.declare_parameter('v', 1.0)
        self.declare_parameter('d', 0.5)
        # self.v_ = 1.0
        # self.d_ = 0.5
        self.publisher_ = self.create_publisher(AckermannDriveStamped, "drive", 10)
        # self.timer_ = self.create_timer(0.5, self.publish_info)
        self.get_logger().info("Talker has been started")

    def publish_info(self):
        msg = AckermannDriveStamped ()
        # msg.drive.speed = self.v_
        # msg.drive.steering_angle = self.d_
        # to publish as fast as possible
        while rclpy.ok():
            # update for dynamic change
            msg.drive.speed = self.get_parameter('v').get_parameter_value().double_value
            msg.drive.steering_angle = self.get_parameter('d').get_parameter_value().double_value
            self.publisher_.publish(msg)
    
 
 
def main(args=None):
    rclpy.init(args=args)
    node = TalkerNode() 
    # rclpy.spin(node)
    
    try:
        node.publish_info()
    except KeyboardInterrupt:
        pass  # Handle Ctrl+C gracefully
    
    node.destroy_node()
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
