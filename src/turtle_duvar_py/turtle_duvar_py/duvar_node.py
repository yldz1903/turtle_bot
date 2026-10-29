"""Duvardan kaçan kaplumbağa düğümü.

- /turtle1/pose konusunu dinler (x, y)
- /turtle1/cmd_vel ile kaplumbağayı ileri sürer
- x veya y, min_limit'ten küçük ya da max_limit'ten büyükse dönerek yön değiştirir
- Konumu saniyede bir get_logger().info() ile yazar
- Hız ve sınır değerleri ROS parametresidir (bonus)
"""
import math

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class DuvarNode(Node):
    def __init__(self):
        super().__init__('duvar_node')

        # Parametreler (bonus)
        self.declare_parameter('linear_speed', 2.0)
        self.declare_parameter('angular_speed', 4.0)
        self.declare_parameter('min_limit', 1.0)
        self.declare_parameter('max_limit', 10.0)

        self.pose = None
        self.sub = self.create_subscription(
            Pose, '/turtle1/pose', self.pose_callback, 10)
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        # Konumu saniyede bir yazdır
        self.log_timer = self.create_timer(1.0, self.log_callback)

        self.get_logger().info('duvar_node başladı.')

    @staticmethod
    def normalize(angle):
        """Açıyı -pi ile +pi arasına getir."""
        return math.atan2(math.sin(angle), math.cos(angle))

    def pose_callback(self, msg):
        self.pose = msg

        linear = self.get_parameter('linear_speed').value
        angular = self.get_parameter('angular_speed').value
        lo = self.get_parameter('min_limit').value
        hi = self.get_parameter('max_limit').value

        cmd = Twist()
        if msg.x < lo or msg.x > hi or msg.y < lo or msg.y > hi:
            # Duvara yakın: merkeze doğru dön
            center = (lo + hi) / 2.0
            target = math.atan2(center - msg.y, center - msg.x)
            diff = self.normalize(target - msg.theta)
            cmd.linear.x = linear / 2.0
            cmd.angular.z = angular if diff >= 0.0 else -angular
        else:
            cmd.linear.x = linear
        self.pub.publish(cmd)

    def log_callback(self):
        if self.pose is not None:
            self.get_logger().info(
                f'Konum: x={self.pose.x:.2f}, y={self.pose.y:.2f}')


def main(args=None):
    rclpy.init(args=args)
    node = DuvarNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            node.pub.publish(Twist())
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
