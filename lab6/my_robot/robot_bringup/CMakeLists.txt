cmake_minimum_required(VERSION 3.5)

project(robot_bringup)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

install(
  PROGRAMS
    robot_bringup/robot_lazer_stop.py  # Путь к вашему Python-скрипту
  DESTINATION lib/${PROJECT_NAME}   # Устанавливаем его в папку lib/<имя_проекта>
)

install(
  PROGRAMS
    robot_bringup/robot_depth_stop.py  # Путь к вашему Python-скрипту
  DESTINATION lib/${PROJECT_NAME}   # Устанавливаем его в папку lib/<имя_проекта>
)

# Install project launch files
install(
  DIRECTORY
    launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

# Install project configuration files
install(
  DIRECTORY
    config/
  DESTINATION share/${PROJECT_NAME}/config
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
