{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOXUPJ6kY1SanLsPnFk+3yl",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/fslagala31-hub/Q2_Assessments-/blob/main/Q2_FA1_Mahogany_Agala.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "vh-IChWWAgHB"
      },
      "outputs": [],
      "source": [
        "#This function adds two numbers together and returns there sum\n",
        "def add_numbers(num1, num2):\n",
        "  return num1 + num2\n",
        "\n",
        "#This function subtracts the second number to the first number and returns their difference.\n",
        "def subtract_numbers(num1, num2):\n",
        "  return num1 - num2\n",
        "\n",
        "#This function multiplies the two numbers together and returns their product.\n",
        "def multiply_numbers(num1, mum2):\n",
        "  return num1 * num2\n",
        "\n",
        "#This function divides the numbers, returning an error message is the second number is zero.\n",
        "def divide_numbers(num1, num2):\n",
        "  if num2 == 0:\n",
        "    return \"Cannot divide by 0\"\n",
        "  return num1 / num2\n",
        "\n",
        "\n",
        "\n",
        "#These lines ask the user to input 2 numbers and convert the input into decimal values.\n",
        "num1 = float(input(\"Enter first number: \"))\n",
        "num2 = float(input(\"Enter second number: \"))\n",
        "\n",
        "#This line displays the operation choices for the user.\n",
        "print(\"✿ Choose your desired operation ✿\")\n",
        "print(\"1 - Addition\")\n",
        "print(\"2 - Subtraction\")\n",
        "print(\"3 - Multiplication\")\n",
        "print(\"4 - Division\")\n",
        "\n",
        "#This captures the user's selected operation.\n",
        "choice = input(\"Enter your choice: \")\n",
        "\n",
        "#This group calls the corrects function based on the choice and stores the returned value.\n",
        "if choice == \"1\":\n",
        "  result = add_numbers(num1, num2)\n",
        "elif choice == \"2\":\n",
        "  result = subtract_numbers(num1, num2)\n",
        "elif choice == \"3\":\n",
        "  result = multiply_numbers(num1, num2)\n",
        "elif choice == \"4\":\n",
        "  result = divide_numbers(num1, num2)\n",
        "else:\n",
        "  result = \"Invalid operation choice\"\n",
        "\n",
        "#This displays the final calvulated result.\n",
        "print(\"Result:\", result)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Short Reflection**\n",
        "\n",
        "After completing your program, answer the following questions:\n",
        "\n",
        "1. What functions did you create in your calculator program?\n",
        "\n",
        " -  I created four different functions. Namely, add_numbers, subtract_numbers, multiply_numbers, and divide_numbers.\n",
        "\n",
        "\n",
        "2. What parameters did your functions use?\n",
        "\n",
        "  - Each function used two parameters (num1 and num2) to receive the input values needed for the calculation.\n",
        "\n",
        "\n",
        "3. What arguments were passed when the functions were called?\n",
        "\n",
        "  - The num1 and num2 variables were passed as arguments when the arguments were used.\n",
        "\n",
        "\n",
        "4. How did your program use the returned value?\n",
        "\n",
        "  - The program stored the value returned by the function into the result variable and then displayed it clearly using the print() function.\n",
        "\n",
        "\n",
        "5. Why is it better to divide the calculator program into functions instead of\n",
        "writing everything in one long block of code?\n",
        "\n",
        "  - Diving the program into functions makes the code cleaner, more organized, and easier to read. It also makes debugging much simplier because if there is an error in an operation, you only need to fix that specific function instead of searching through one long block of code."
      ],
      "metadata": {
        "id": "irIncK2-GIl3"
      }
    }
  ]
}