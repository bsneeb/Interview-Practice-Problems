#include <iostream>

/**
 * @brief Draws a rhombus of height s entered in terminal.
 *
 * @return int
 */

int main()
{
    int s, i, j;
    std::cout << "Enter the size of rhombus: " << std::endl;
    std::cin >> s;

    for (i = 0; i < s; i++)
    {
        for (j = 0; j < i; j++)
        {
            std::cout << " ";
        }
        for (j = 0; j < s; j++)
        {
            std::cout << "*";
        }
        std::cout << "" << std::endl;
    }

    return 0;
}
