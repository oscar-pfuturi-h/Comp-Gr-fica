#ifndef _UTILS_
#define _UTILS_

#include <glad/glad.h>
#include <glfw/glfw3.h>
#include <string>

std::string readShaderSource(const char* filePath);

void printShaderLog(GLuint shader);

void printProgramLog(int prog);

bool checkOpenGLError();

GLuint createShaderProgram(const GLchar* vertShaderPath, const GLchar* fragShaderPath);

void init(GLFWwindow* window);

void display(GLFWwindow* window, double currentTime);

#endif