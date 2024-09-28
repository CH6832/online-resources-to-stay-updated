// wepage-opener.h : Include file for standard system include files,
// or project specific include files.

#pragma once

#include <iostream>
#include <string>
#include <vector>
/**
 * @file webpage-opener.h
 * @brief Header file for the Webpage Opener project.
 *
 * This header file includes standard system headers and declarations
 * for the Webpage Opener application. It provides the necessary
 * includes for input/output operations and any other project-specific
 * includes that may be required.
 *
 * Future additions to this file might include:
 * - Function declarations
 * - Class definitions
 * - Additional headers as needed for the project.
 */

 /**
  * @brief Opens a URL in the system's default web browser.
  *
  * This function takes a URL string and opens it in the system's
  * default web browser. The implementation varies depending on
  * the operating system.
  *
  * @param url The URL to be opened.
  */
void openURL(const std::string& url);

/**
 * @brief Opens URLs specified in an XML file.
 *
 * This function takes the name of an XML element and opens all URLs
 * found within that element in the system's default web browser.
 *
 * @param elementName The name of the XML element containing URL nodes.
 */
void openURLsInElement(const std::string& elementName);