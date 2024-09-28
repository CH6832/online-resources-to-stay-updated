#include <gtest/gtest.h>
#include "../includes/webpage-opener.hpp"

TEST(WebpageOpenerTest, TestOpenURLs) {
    std::string elementName = "testElement";
    // Call the function and assert expectations
    ASSERT_NO_THROW(openURLsInElement(elementName));
}
