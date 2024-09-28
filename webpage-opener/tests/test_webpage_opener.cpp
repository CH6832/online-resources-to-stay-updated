#include "../includes/webpage-opener.hpp"
#include <gtest/gtest.h>

// Mock function to replace URL opening for testing
void openURL(const std::string& url) {
    // Simulate URL opening by just logging for testing purposes
    std::cout << "Opening URL: " << url << std::endl;
}

// Test for parsing and opening URLs
TEST(WebpageOpenerTest, OpenURLsInElement) {
    std::string xmlContent = "<root><element><url>http://example.com</url></element></root>";
    std::string elementName = "element";

    // Mock XML loading instead of reading from file (assumes function is refactored to accept XML string)
    EXPECT_NO_THROW(openURLsInElement(elementName));

    // Expected output
    // Check that openURL was called with the correct URLs
}
