# CMakeList.txt : Top-level CMake project file, do global configuration
# and include sub-projects here.
#
cmake_minimum_required (VERSION 3.8)

# Enable Hot Reload for MSVC compilers if supported.
if (POLICY CMP0141)
  cmake_policy(SET CMP0141 NEW)
  set(CMAKE_MSVC_DEBUG_INFORMATION_FORMAT "$<IF:$<AND:$<C_COMPILER_ID:MSVC>,$<CXX_COMPILER_ID:MSVC>>,$<$<CONFIG:Debug,RelWithDebInfo>:EditAndContinue>,$<$<CONFIG:Debug,RelWithDebInfo>:ProgramDatabase>>")
endif()

project ("webpage-opener")

# Include sub-projects.
add_subdirectory ("webpage-opener")

# Enable UTF-8 support for MSVC
if(MSVC)
    target_compile_options(webpage-opener PRIVATE /utf-8)
endif()

# Include CPack after all configurations
include(CPack)

# Specify output directories for the packages
set(CPACK_OUTPUT_FILE_PREFIX "${CMAKE_SOURCE_DIR}/packages")

# Specify the MSI installer settings
if(WIN32)
    set(CPACK_GENERATOR "ZIP;WIX")  # Specify the desired package formats
    set(CPACK_NSIS_INSTALL_ROOT "$PROGRAMFILES/webpage-opener")
    set(CPACK_NSIS_DISPLAY_NAME "webpage-opener Installer")
    set(CPACK_PACKAGE_NAME "webpage-opener")
    set(CPACK_PACKAGE_VERSION "1.0.0")
    set(CPACK_PACKAGE_VENDOR "Your Company")
    set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "webpage-opener application")
    set(CPACK_PACKAGE_EXECUTABLES "webpage-opener" "webpage-opener")
    set(CPACK_NSIS_MODIFY_PATH ON)
    set(CPACK_NSIS_HELP_LINK "https://example.com/help")
    set(CPACK_NSIS_URL_INFO_ABOUT "https://example.com")
endif()

# Specify the Linux packaging settings
if(UNIX AND NOT APPLE)
    set(CPACK_GENERATOR "DEB;RPM")  # Use DEB and RPM for Linux packages
    set(CPACK_DEBIAN_PACKAGE_MAINTAINER "Christoph Hartleb")  # Required
    set(CPACK_DEBIAN_PACKAGE_VERSION "1.0.0")
    set(CPACK_DEBIAN_PACKAGE_NAME "webpage-opener")
    set(CPACK_DEBIAN_PACKAGE_DESCRIPTION "webpage-opener application")
    set(CPACK_RPM_PACKAGE_LICENSE "MIT")
endif()

# Include CPack after all configurations
include(CPack)