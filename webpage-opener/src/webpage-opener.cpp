// webpage-opener.cpp : Defines the entry point for the application.
//

#include <boost/asio.hpp>
#include <boost/asio/ip/tcp.hpp>
#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/xml_parser.hpp>
#include <libxml/parser.h>
#include <libxml/tree.h>
#include <windows.h>
#include <iostream>
#include <cstdlib>
#include "../includes/webpage-opener.hpp"
#include "../includes/resources.h"
#include "../includes/logger.hpp"
#include <shellapi.h>

using namespace std;

Logger logger("webpage-opener.log");

void LoadEmbeddedResource() {
    HMODULE hModule = GetModuleHandle(nullptr);
    HRSRC hRes = FindResource(hModule, MAKEINTRESOURCE(IDR_DATA_XML), RT_RCDATA);

    if (hRes) {
        HGLOBAL hData = LoadResource(hModule, hRes);
        DWORD size = SizeofResource(hModule, hRes);
        const char* data = static_cast<const char*>(LockResource(hData));

        cout << "Embedded data size: " << size << "\n";
        logger.log(Logger::APPINFO, "Embedded data size: " + to_string(size));
        cout.write(data, size);
    }
    else {
        logger.log(Logger::APPERROR, "Resource not found.");
        cerr << "Resource not found.\n";
    }
}

void openURL(const string& url) {
    // Use a local character buffer to avoid unnecessary string allocation
    #ifdef _WIN32
        // Use ShellExecute to open URLs on Windows
        ShellExecuteA(NULL, "open", url.c_str(), NULL, NULL, SW_SHOWNORMAL);
    #else
        // Use xdg-open on Linux
        string command = "xdg-open " + url;
        system(command.c_str());
    #endif

    // Log that the URL was opened
    logger.log(Logger::APPINFO, "Opened URL: " + url);
}

void openURLsInElement(const string& elementName) {
    // CPU Profiling
    auto start = chrono::high_resolution_clock::now();
    
    // Load the XML document
    xmlDocPtr doc = xmlReadFile("data.xml", nullptr, 0);
    if (doc == nullptr) {
        logger.log(Logger::APPERROR, "Could not find root element");
        cerr << "Error: could not parse file data.xml\n";
        return;
    }

    // Get the root element
    xmlNodePtr rootElement = xmlDocGetRootElement(doc);
    if (rootElement == nullptr) {
        cerr << "Error: could not find root element\n";
        xmlFreeDoc(doc);
        return;
    }

    // Find the specified element by name
    xmlNodePtr targetElement = nullptr;
    for (xmlNodePtr curNode = rootElement->children; curNode != nullptr; curNode = curNode->next) {
        if (curNode->type == XML_ELEMENT_NODE && xmlStrcmp(curNode->name, BAD_CAST elementName.c_str()) == 0) {
            targetElement = curNode;
            break;
        }
    }

    if (!targetElement) {
        cerr << "Error: specified element not found\n";
        logger.log(Logger::APPERROR, "Specified element not found: " + elementName);
        xmlFreeDoc(doc);
        return;
    }

    // Create a vector to hold the threads
    vector<thread> threads;

    // Iterate over the "url" elements inside the target element
    for (xmlNodePtr curNode = targetElement->children; curNode != nullptr; curNode = curNode->next) {
        if (curNode->type == XML_ELEMENT_NODE && xmlStrcmp(curNode->name, BAD_CAST "url") == 0) {
            xmlChar* urlContent = xmlNodeGetContent(curNode);
            if (urlContent) {
                string url(reinterpret_cast<const char*>(urlContent));
                logger.log(Logger::APPINFO, "Preparing to open URL: " + url);

                // Create a new thread to open the URL
                threads.emplace_back(openURL, url);

                xmlFree(urlContent); // Free the URL content after creating the thread
            }
        }
    }

    // Wait for all threads to finish
    for (auto& thread : threads) {
        if (thread.joinable()) {
            thread.join();
        }
    }

    // Free the XML document
    xmlFreeDoc(doc);

    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = end - start;
    cout << "openURLsInElement took " << elapsed.count() << " seconds.\n";

    Logger::APPINFO("openURLsInElement took " + to_string(elapsed.count()) + " seconds.");
}

int main(int argc, char* argv[]) {
    #pragma GCC optimize("O3") // Suggest optimization level O3 for this function

    if (argc < 2) {
        cerr << "Usage: " << argv[0] << " <element>\n";
        logger.log(Logger::APPERROR, "Usage: " + string(argv[0]) + " <element>");
        return 1;
    }

    string elementName = argv[1];
    logger.log(Logger::APPINFO, "Received element name: " + elementName);

    openURLsInElement(elementName);
    logger.log(Logger::APPINFO, "Finished processing for element: " + elementName);

    return 0;
}
