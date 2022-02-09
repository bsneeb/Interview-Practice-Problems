#include <iostream>

/**
 * @brief Draws a diamond. Enter desired width in the terminal.
 * (Symmetric with odd numbers)
 *
 */
void drawDiamond()
{
    int i, j, k, r;

    std::cout << "Enter height of the diamond: " << std::endl;
    std::cin >> r;

    for (i = 0; i < r; i++)
    {
        if (i <= r / 2)
        {
            for (k = r / 2; k > i; k--)
            {
                printf(" ");
            }
            for (j = 0; j <= i * 2; j++)
            {
                printf("*");
            }
        }
        else
        {
            for (k = r / 2; k < i; k++)
            {
                printf(" ");
            }
            for (j = 0; j < ((r - i) * 2) - 1; j++)
            {
                printf("*");
            }
        }
        printf("\n");
    }
}

int main()
{
    drawDiamond();
    return 0;
}
