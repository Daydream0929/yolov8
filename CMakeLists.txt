cmake_minimum_required(VERSION 3.9)
project(yolov8_pose_mnn)

set(CMAKE_CXX_STANDARD 17)

find_package(OpenCV REQUIRED)

# MNN include directory (default: /usr/local/include)
include_directories(
    ./include
    )

# libMNN.so directory 
link_directories(
    ./lib/x86
    )

add_executable(yolov8_pose_mnn main.cpp src/yolov8_pose_mnn.cpp)
target_link_libraries(yolov8_pose_mnn MNN ${OpenCV_LIBS})
