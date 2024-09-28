// logger.hpp

#pragma once

#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include <ctime>
#include <mutex>

class Logger {
public:
    enum LogLevel {
        APPINFO,
        APPWARNING,
        APPERROR
    };

    Logger(const std::string& filename);
    ~Logger();

    void log(LogLevel level, const std::string& message);

private:
    std::ofstream logFile;
    std::mutex mtx;

    std::string getCurrentTime();
    std::string logLevelToString(LogLevel level);
};
