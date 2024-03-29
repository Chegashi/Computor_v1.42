#!/bin/sh
green='\033[0;32m'
NC='\033[0m'
echo "${green}./computor.py '5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0'${NC}"
./computor.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
echo "${green}./computor.py '5 * X^0 + 4 * X^1 = 4 * X^0'${NC}"
./computor.py "5 * X^0 + 4 * X^1 = 4 * X^0"
echo "${green}./computor.py '8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0'${NC}"
./computor.py "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
echo "${green}./computor.py '5 * X^5 = 5 * X^5'${NC}"
./computor.py "5 * X^5 = 5 * X^5"
echo "${green}./computor.py '8 * X^4 = 4 * X^0'${NC}"
./computor.py "8 * X^4 = 4 * X^0"
echo "${green}./computor.py '8 * X^0 = 4 * X^0'${NC}"
./computor.py "8 * X^0 = 4 * X^0"
echo "${green}./computor.py '7 * X^1 + 4 * X^1 = 5 * X^0'${NC}"
./computor.py "7 * X^1 + 4 * X^1 = 5 * X^0"
echo "${green}./computor.py '1 * X^1 + 1 * X^0 = 3 * X^2 + 31 * X^1 5 * X^0'${NC}"
./computor.py "1 * X^1 + 1 * X^0 = 3 * X^2 + 31 * X^1 5 * X^0"
echo "${green}./computor.py '1 * X^1 + 1 * X^0 = 5 * X^2 + 11 * X^1 + 6 * X^0'${NC}"
./computor.py "1 * X^1 + 1 * X^0 = 5 * X^2 + 11 * X^1 + 6 * X^0"
echo "${green}./computor.py '0 * X^1 + 1 * X^0 = 3 * X^2 + 3 * X^1 + 5 * X^0'${NC}"
./computor.py "0 * X^1 + 1 * X^0 = 3 * X^2 + 3 * X^1 + 5 * X^0"