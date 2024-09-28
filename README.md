# Webpage Opener


## Table of Contents
- [Webpage Opener](#webpage-opener)
  - [Table of Contents](#table-of-contents)
  - [What is the Project Created For?](#what-is-the-project-created-for)
  - [How It Was Created](#how-it-was-created)
    - [Design Patterns](#design-patterns)
    - [Architectural Style](#architectural-style)
  - [Features](#features)
  - [Content overview](#content-overview)
  - [How to open the Project](#how-to-open-the-project)
  - [How to Run the Project](#how-to-run-the-project)
  - [How to Debug the Project](#how-to-debug-the-project)
  - [How to Test the Project](#how-to-test-the-project)
    - [Prerequisites](#prerequisites)
    - [Steps to Run Tests in Visual Studio](#steps-to-run-tests-in-visual-studio)
    - [Command Line Testing](#command-line-testing)
    - [Adding New Tests](#adding-new-tests)
  - [What Resources are Used to Create the Project?](#what-resources-are-used-to-create-the-project)
  - [License](#license)
  - [Copyright](#copyright)

## What is the Project Created For?

The **Webpage Opener** project is designed to provide a simple command-line tool that reads a specified XML file containing URLs and opens them in the default web browser. This tool is useful for automating the process of opening multiple web pages quickly, making it ideal for developers and testers who need to access several resources in a short time.

## How It Was Created

The project was created using **CMake**, a cross-platform build system that simplifies the build process for C++ projects. The source code is organized into multiple files, including the main application logic, header files, and resource files (such as XML data). The project uses libraries like **libxml2** for XML parsing and **fmt** for formatted output.

### Design Patterns

The **Webpage Opener** project follows several core design patterns to ensure modularity, maintainability, and scalability:

1. **Singleton Pattern**:
   - The logging system is designed as a singleton, ensuring that there is only one instance of the logger available throughout the application. This prevents resource contention and ensures that all logs are centralized.

2. **Facade Pattern**:
   - The `openURLsInElement()` function acts as a facade by abstracting the complexity of parsing the XML, extracting URLs, and opening them in the system’s default browser. This pattern simplifies the interface for the client code, allowing it to interact with the system at a higher level without needing to understand the underlying complexity.

3. **Command Pattern**:
   - The function responsible for opening URLs follows the command pattern, encapsulating the action of opening a URL as a command. This provides flexibility for future extensions, such as queueing or delaying the execution of commands.

4. **Factory Method** (Planned for future extensions):
   - A potential extension of this project could involve using a factory method to create platform-specific URL openers. This would allow the system to dynamically select the appropriate URL opening strategy based on the operating system (e.g., Windows vs. Linux).

### Architectural Style

The project follows a **Modular Monolithic** architecture. This approach divides the project into clear, independent modules (e.g., logging, XML parsing, and URL handling), while still maintaining a single cohesive system. Each module is responsible for a distinct piece of functionality, but they all work together within the same application.

The **separation of concerns** is a key principle in this architecture, ensuring that different responsibilities (like file handling, URL parsing, logging, etc.) are handled by distinct components. This makes the codebase more maintainable and easier to extend in the future.

## Features

- **XML Parsing**: Utilizes `libxml2` for robust XML parsing, enabling seamless extraction of URLs from XML files.
- **Cross-Platform Support**: Built using CMake, ensuring compatibility across Windows and Linux environments.
- **Command-Line Interface**: Provides a simple command-line interface for user interaction, making it easy to specify which XML file to process.
- **Logging**: Implements a logging system to track operations, making debugging and monitoring easier.
- **Dynamic Library Linking**: Links necessary libraries dynamically, reducing the executable size and allowing for easier updates to dependencies.
- **Performance Tuning**: Utilizes compiler pragmas for performance tuning, optimizing the execution of critical sections of the code.
- **Compiler Optimization**: Applies various compiler optimization flags to enhance the overall performance of the application during the build process.
- **Multithreading**: Leverages multithreading to improve performance, allowing multiple URLs to be opened simultaneously.
- **Unit Testing with Google Test**: Implements extensive unit tests using the Google Test framework to ensure the reliability and correctness of the code.

## Content overview

    .
    ├── .vs/ - visula studio specific settings
    ├── out/ - contains binary files and releavant metadata
    ├── vcpkg - package manager with third-party libraries
    ├── webpage-opener - source code
    ├── CMakeLists.txt - cmake source code
    ├── CMakePresets.json - cmake configurations
    ├── LICENSE - license text
    └──README.md - project information

## How to open the Project

0. **Clone the Repository:**
   To open the project, you first need to clone the repository from GitHub (or wherever it's hosted):
   ```bash
   git clone https://github.com/CH6832/webpage-opener.git
   cd webpage-opener
   ```

1. **Open with Visual Studio:**
   - Open **Visual Studio Community Edition**.
   - Click on `File` -> `Open` -> `CMake...` and select the folder containing the project.

2. **Open with Visual Studio:**
   - Open **Visual Studio Code**.
   - Click on `File` -> `Open Folder` and select the folder containing the project.

3. **Other IDEs**
   - There are other IDEs that could handle the project:
     - **Eclipse IDE for C and C++ Developers**
     - **Codeblocks**
     - **Apache Netbeans IDE**
     - ...

## How to Run the Project

0. **Build the Project:**
   - Ensure the project is built by selecting `Build` -> `Build Solution` from the menu.
   - This will generate the executable in the output directory (typically found under `out/build/x64-debug`).

1. **Run the Executable:**
   - You can run the executable directly from the command line:
      ```bash
      cd webpage-opener/out/build/x64-release/webpage-opener
      ./webpage-opener.exe
      ```

## How to Debug the Project

0. **Set Up Debug Configuration:**
   - Open the project in Visual Studio.
   - Right-click on the main CmakeLists.txt and click on `Open Debug and Launch Settings`.
   - An examples looks like this:
      ```bash
      {
      "version": "0.2.1",
      "defaults": {},
      "configurations": [
         {
            "type": "default",
            "project": "CMakeLists.txt",
            "projectTarget": "webpage-opener.exe (webpage-opener\\webpage-opener.exe)",
            "name": "webpage-opener.exe (webpage-opener\\webpage-opener.exe)",
            "args": [
            "finance"
            ]
         }
      ]
      }
      ```

1. **Start Debugging:**
   - Set breakpoints in the code by clicking in the margin next to the line numbers.
   - Press `F5` to start debugging or select `Debug` -> `Start Debugging` from the menu.

## How to Test the Project

The project includes unit tests to ensure the functionality of the `webpage-opener` tool. We use **Google Test** as the testing framework. Below are the steps to run and manage the tests using **Microsoft Visual Studio Community Edition**.

### Prerequisites

Before running tests, ensure that you have:
1. **Google Test** installed via **vcpkg** (set up as a static library).
2. A properly configured `CMakeLists.txt` file, which includes the test executable.

### Steps to Run Tests in Visual Studio

1. **Open the Project in Visual Studio**:
   - Open **Visual Studio Community Edition**.
   - Click on `File` -> `Open` -> `CMake...` and select the project folder containing `CMakeLists.txt`.

2. **Configure vcpkg in CMake**:
   - Ensure that **vcpkg** is integrated with Visual Studio. If it's not done yet, follow these steps:
     - Go to `Tools` -> `Options` -> `CMake` -> `CMake Toolchain File`.
     - Set the toolchain file to `vcpkg` path, for example:
       ```
       <path_to_vcpkg>\scripts\buildsystems\vcpkg.cmake
       ```

3. **Build the Project**:
   - In Visual Studio, make sure the project is set to the `Debug` configuration.
   - Click `Build` -> `Build All` or use the `Ctrl + Shift + B` shortcut to build both the main executable and the test executable (e.g., `webpage-opener`).
   - This will generate the `webpage-opener` executable and the unit test executable (`webpage-opener`).

4. **Run the Tests**:
   - In the **Test Explorer** window of Visual Studio, you should see the list of Google Test unit tests that were discovered.
   - If **Test Explorer** is not visible, go to `Test` -> `Windows` -> `Test Explorer` to open it.
   - From the **Test Explorer**, click `Run All` to run all the tests or selectively run individual tests.
   - Visual Studio will compile the tests and display the results directly in the **Test Explorer** window.

### Command Line Testing

You can also run tests via the command line if you prefer:

1. **Build the Test Executable**:
   - Navigate to your project's build directory:
     ```bash
     cd out/build/x64-debug
     ```

2. **Run the Test Executable**:
   - Run the test executable (`webpage-opener.exe`) to see the test results:
     ```bash
     ./webpage-opener.exe
     ```

3. **Run Tests with CTest**:
   - After building, you can also use `ctest` to run the tests:
     ```bash
     ctest
     ```

### Adding New Tests

To add new tests:
1. Create additional test files in the `test/` directory (e.g., `test/test_new_feature.cpp`).
2. Follow the same pattern for writing tests, using **Google Test**'s macros like `TEST()`, `ASSERT_EQ()`, `EXPECT_TRUE()`, etc.
3. Make sure to add new test files to the `CMakeLists.txt` under the `add_executable(webpage-opener)` section.

## What Resources are Used to Create the Project?

* C++
  * [CPlusPlus](https://cplusplus.com/)
  * [Microsoft C++, C, and Assembler documentation](https://learn.microsoft.com/en-us/cpp/?view=msvc-170)
  * [C++ Programming Language](https://devdocs.io/cpp/)
  * [C++ - The Standard](https://isocpp.org/std/the-standard)
  * [GoogleTest User's Guide](http://google.github.io/googletest/)
  * [libxml2](http://xmlsoft.org/html/)
* CMake
  * [CMake Documentation and Community](https://cmake.org/documentation/)
* Markdwon
  * [Basic syntax](https://www.markdownguide.org/basic-syntax/)
  * [Complete list of github markdown emojis](https://dev.to/nikolab/complete-list-of-github-markdown-emoji-markup-5aia)
  * [Awesome template](http://github.com/Human-Activity-Recognition/blob/main/README.md)
  * [.gitignore file](https://git-scm.com/docs/gitignore)
* Editor
  * [Visual Studio Code](https://code.visualstudio.com/)
* Commandline tools
  * [Build Command-Line Interfaces With Python's argparse](https://realpython.com/command-line-interfaces-python-argparse/)
  * [Master the Art of Command Line: Your Ultimate Guide to Developing Powerful Tools](https://hackernoon.com/master-the-art-of-command-line-your-ultimate-guide-to-developing-powerful-tools)
  * [Command Line Interface Guidelines](https://clig.dev/)
  * [Building a Network Command Line Interface in Go](https://tutorialedge.net/golang/building-a-cli-in-go/)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Copyright

See the [COPYRIGHT](COPYRIGHT) file for copyright and licensing details.
