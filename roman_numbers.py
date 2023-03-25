def roman_numerals_to_int(roman_numeral): 
    nums = {'I': 1, 
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            }
    for i in roman_numeral:
        if i not in list(nums.keys()): return None 
    result = 0
    buffer = ("", 0)
    for i,j in enumerate(roman_numeral,0):
        if ((buffer[0] == "") or ((buffer[0][-1] == j) and (str(nums.get(j))[0] != '5'))) and ((buffer[0].count(j) <= 2) or j == 'M' ): # условие заполнение буффера (например: I,II,X,XX и тд)
            if (len(buffer[0]) == 2) and j!='M':
                result += buffer[1] + nums.get(j)
                buffer = (buffer[0]+j, 0)
            elif (len(buffer[0]) < 2) or j=='M':
                buffer = (buffer[0]+j, buffer[1]+nums.get(j))
            else:
                return None
        elif (len(buffer[0]) == 1) and (nums.get(buffer[0][0]) < nums.get(j) and str(nums.get(buffer[0][-1]))[0] != '5'): #условие записи числа и обнуления буфера (IV, XL)
            result += nums.get(j) - buffer[1]
            buffer = ("", 0)
        elif buffer[0] != "" and (nums.get(buffer[0][-1]) > nums.get(j)): #условие записи числа VI, VII, VIII
            result += buffer[1]
            buffer = (j, nums.get(j))
        else:
            return None
    result += buffer[1]
    return result


if __name__ == "__main__":
    print(roman_numerals_to_int("MMXXIV"))
    print(roman_numerals_to_int("MMMCMXCIX"))

