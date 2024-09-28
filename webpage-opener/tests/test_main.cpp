#include <gtest/gtest.h>
#include "../../vcpkg/buildtrees/fmt/src/11.0.2-463dc5ff21.clean/test/gtest/gtest/gtest.h"

// Entry point for Google Test
int main(int argc, char** argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
