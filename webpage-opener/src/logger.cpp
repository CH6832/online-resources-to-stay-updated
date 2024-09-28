// logger.cpp

#include "../includes/logger.hpp"

using namespace std;

// Constructor that opens the log file
Logger::Logger(const string& filename) {
    logFile.open(filename, ios::app); // Open in append mode
    if (!logFile.is_open()) {
        cerr << "Error: Could not open log file: " << filename << endl;
    }
}

// Destructor that closes the log file
Logger::~Logger() {
    if (logFile.is_open()) {
        logFile.close();
    }
}

// Log a message with the specified log level
void Logger::log(LogLevel level, const string& message) {
    lock_guard<mutex> lock(mtx); // Ensure thread safety
    if (logFile.is_open()) {
        logFile << getCurrentTime() << " [" << logLevelToString(level) << "] " << message << endl;
    }
}

// Get the current time as a string
string Logger::getCurrentTime() {
    auto now = chrono::system_clock::now();
    time_t now_time = chrono::system_clock::to_time_t(now);
    return ctime(&now_time); // Convert to string
}

// Convert log level to string
string Logger::logLevelToString(LogLevel level) {
    switch (level) {
    case APPINFO:    return "APPINFO";
    case APPWARNING: return "APPWARNING";
    case APPERROR:   return "APPERROR";
    default:      return "APPUNKNOWN";
    }
}
