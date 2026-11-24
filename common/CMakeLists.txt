set(SOURCES
    InputFile.cpp
    Config.cpp
    Runner.cpp
    TestHarness.cpp
)

add_library(Common ${SOURCES})
target_include_directories(Common PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_link_libraries(Common PUBLIC GTest::gtest)
target_compile_features(Common PUBLIC cxx_std_23)
