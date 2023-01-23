def roman(num):

    roman_map = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII",
               8: "VIII", 9: "IX", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

    result = ""
    remainder = num

    for i in sorted(roman_map.keys(), reverse=True):# 2
        print(i)
        if remainder > 0:
            multiplier = i
            roman_digit = roman_map[i]

            times = remainder // multiplier         # 3
            remainder = remainder % multiplier      # 4
            result += roman_digit * times           # 4

    return result


print(roman(1553))
