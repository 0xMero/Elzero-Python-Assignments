# Assignment 1
# Given: "eeeeE llllLl lllzzZzzzz eroe operationr pollo"
# Required: write regex to match the results in Ass-1.jpg
# Solution: \w\s

# Assignment 2
# Given: "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"
# Required: write regex to match the results in Ass-2.jpg
# Solution: L(\w{6})

# Assignment 3
# Given: 
"""
    +(0100) 600-1234
    +(0100) 60-1234
    (0100) 6000-1234
    01006001234
    0100 600 1234
    (0100) 600-1
    (0100) 600-12
"""
# Required: write regex to match the results in Ass-3.jpg
# Solution: (\+?\(\d{4}\)\s\d{2,4}-\d{4})

# Assignment 4
# Given: 
"""
    http://www.elzero.org:8888/link.php
    https://elzero.org:8888/link.php
    http://www.elzero.com/link.py
    https://elzero.com/link.py
    http://www.elzero.net
    https://elzero.net
"""
# Required: write regex to match the results in Ass-4.jpg
# Solution: (https?://(www\.)?\w+\.(\w+)(:?\d*)/.+)

# Assignment 5
# Required: write regex to match the results in Ass-5.jpg with 5 different ways
# Given
"""
    http
    https
    abcd
    abcd
"""
# Solution 1: https?
# Solution 2: [h-t]
# Solution 3: [h-t]s?
# Solution 4: \w+ps?
# Solution 5: \w+t{2}.+