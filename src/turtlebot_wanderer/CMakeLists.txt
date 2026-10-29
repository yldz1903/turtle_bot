cmake_minimum_required(VERSION 3.8)
project(turtlebot_wanderer)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(turtlesim REQUIRED)
find_package(geometry_msgs REQUIRED)

# Python düğümünü ros2 run ile çalışacak şekilde lib/<paket> altına kur
install(PROGRAMS scripts/wanderer DESTINATION lib/${PROJECT_NAME})

ament_package()
