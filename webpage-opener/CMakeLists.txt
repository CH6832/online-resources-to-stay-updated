# CMakeLists.txt : CMake project for webpage-opener, include source and define project specific logic here.

cmake_minimum_required(VERSION 3.10)

# Project name
project(webpage-opener)

# Add source to this project's executable.
add_executable(webpage-opener "src/webpage-opener.cpp" "includes/webpage-opener.hpp" "resources/resources.rc" "src/logger.cpp" "includes/logger.hpp" "tests/test_webpage_opener.cpp" "tests/test_main.cpp" "tests/test_openURLs.cpp")

# Set the VCPKG root and toolchain file
set(VCPKG_ROOT "${CMAKE_SOURCE_DIR}/vcpkg")
# set(CMAKE_TOOLCHAIN_FILE "${VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake")
set(CMAKE_PREFIX_PATH "${VCPKG_ROOT}/installed/x64-windows")

# Include directories
include_directories(${CMAKE_SOURCE_DIR}/includes)

# Set C++ standard
set_property(TARGET webpage-opener PROPERTY CXX_STANDARD 20)

# Set compiler optimization flags based on build type
if(CMAKE_BUILD_TYPE STREQUAL "Release")
    # Optimization flags for Release
    message(STATUS "Setting optimization flags for Release build.")
    if(MSVC)
        target_compile_options(webpage-opener PRIVATE /O2)  # Full optimization for MSVC
    else()
        target_compile_options(webpage-opener PRIVATE -O3)   # Full optimization for GCC/Clang
    endif()
elseif(CMAKE_BUILD_TYPE STREQUAL "Debug")
    # Optimization flags for Debug (typically none)
    message(STATUS "Debug build - optimization flags will be minimal.")
    if(MSVC)
        target_compile_options(webpage-opener PRIVATE /Od)  # No optimization for MSVC
    else()
        target_compile_options(webpage-opener PRIVATE -O0)   # No optimization for GCC/Clang
    endif()
endif()

# Define paths for libraries based on the platform
if(WIN32)
    # Specify the paths to the libraries and includes for Windows
    set(LIB_PATH "${CMAKE_SOURCE_DIR}/vcpkg/installed/x64-windows/lib")
    set(INCLUDE_PATH "${CMAKE_SOURCE_DIR}/vcpkg/installed/x64-windows/include")
    set(BIN_PATH "${CMAKE_SOURCE_DIR}/vcpkg/installed/x64-windows/bin")


    # Add include directories
    include_directories(${INCLUDE_PATH})

    # Specify the paths to the libraries
    set(LIBXML2_LIB_PATH "${LIB_PATH}/libxml2.lib")
    set(LIBICONV_LIB_PATH "${LIB_PATH}/iconv.lib")
    set(FMT_LIB_PATH "${LIB_PATH}/fmt.lib")
    set(GTEST_LIB_PATH "${LIB_PATH}/gtest.lib")
    set(GTEST_MAIN_LIB_PATH "${LIB_PATH}/gtest_main.lib")

    # Link against Windows libraries
    target_link_libraries(webpage-opener PRIVATE ${FMT_LIB_PATH} ${LIBXML2_LIB_PATH} ${LIBICONV_LIB_PATH} ${GTEST_LIB_PATH} ${GTEST_MAIN_LIB_PATH})

    # Copy data.xml to the output directory
    add_custom_command(TARGET webpage-opener POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_if_different
        "${CMAKE_SOURCE_DIR}/webpage-opener/resources/data.xml" 
        $<TARGET_FILE_DIR:webpage-opener>/data.xml
    )

    # Copy DLLs to the output directory
    add_custom_command(TARGET webpage-opener POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_if_different
        "${BIN_PATH}/fmt.dll" $<TARGET_FILE_DIR:webpage-opener>
    )

    add_custom_command(TARGET webpage-opener POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_if_different
        "${BIN_PATH}/libxml2.dll" $<TARGET_FILE_DIR:webpage-opener>
    )

    add_custom_command(TARGET webpage-opener POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_if_different
        "${BIN_PATH}/liblzma.dll" $<TARGET_FILE_DIR:webpage-opener>
    )

    add_custom_command(TARGET webpage-opener POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_if_different
        "${BIN_PATH}/iconv-2.dll" $<TARGET_FILE_DIR:webpage-opener>
    )

    add_custom_command(TARGET webpage-opener POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_if_different
        "${Boost_LIBRARY_DIRS}/*.dll" $<TARGET_FILE_DIR:webpage-opener>
    )

    # Enable Google Test
    enable_testing()


    # Copy data.xml to the output directory
    #add_custom_command(TARGET webpage-opener POST_BUILD
    #   COMMAND ${CMAKE_COMMAND} -E copy_if_different
    #   "${CMAKE_SOURCE_DIR}/webpage-opener/resources/data.xml" $<TARGET_FILE_DIR:webpage-opener>/data.xml
    #)
elseif(UNIX)  # This will match Linux/Unix systems
    # Specify the paths to the libraries and includes for UNIX
    set(LIB_PATH "${CMAKE_SOURCE_DIR}/vcpkg/installed/x64-linux/lib")
    set(INCLUDE_PATH "${CMAKE_SOURCE_DIR}/vcpkg/installed/x64-linux/include")

    # Add include directories
    include_directories(${INCLUDE_PATH})

    # Specify the paths to the libraries
    set(LIBXML2_LIB_PATH "${LIB_PATH}/libxml2.so")
    set(LIBICONV_LIB_PATH "${LIB_PATH}/libiconv.so")
    set(FMT_LIB_PATH "${LIB_PATH}/libfmt.so")
    set(BOOST_LIB_PATH "${LIB_PATH}/libboost_system.so")  # Example for Boost.System
    set(BOOST_FILESYSTEM_LIB_PATH "${LIB_PATH}/libboost_filesystem.so")  # Example for Boost.Filesystem

    add_custom_command(TARGET webpage-opener POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy
    ${CMAKE_SOURCE_DIR}/webpage-opener/resources/data.xml
    $<TARGET_FILE_DIR:webpage-opener>/data.xml)

    # Link against UNIX libraries
    target_link_libraries(webpage-opener PRIVATE ${FMT_LIB_PATH} ${LIBXML2_LIB_PATH} ${LIBICONV_LIB_PATH} ${BOOST_LIB_PATH} ${BOOST_FILESYSTEM_LIB_PATH} ${Boost_LIBRARIES})

    # Copy data.xml to the output directory
    add_custom_command(TARGET webpage-opener POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_if_different
        "${CMAKE_SOURCE_DIR}/webpage-opener/resources/data.xml" $<TARGET_FILE_DIR:webpage-opener>/data.xml
    )
endif()

# Include the resource file
set(RESOURCE_FILE "${CMAKE_SOURCE_DIR}/webpage-opener/resources/resources.rc")
if(EXISTS ${RESOURCE_FILE})  # Check if the file exists before adding it
    target_sources(webpage-opener PRIVATE ${RESOURCE_FILE})
else()
    message(FATAL_ERROR "Resource file not found: ${RESOURCE_FILE}")
endif()

# Optional: If you have CMake configuration files in share
set(SHARE_PATH "${CMAKE_SOURCE_DIR}/vcpkg/installed/x64-windows/share")
list(APPEND CMAKE_PREFIX_PATH "${SHARE_PATH}")

# TODO: Add tests and install targets if needed.
