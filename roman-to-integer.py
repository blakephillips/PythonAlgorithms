#Given a roman numeral, convert it to an integer.


class Solution:
    def romanToInt(self, s: str) -> int:
        
        #Map of integer values for each roman value
        romanValues = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        
        #Map of values that have a special case for the previous value
        previousRomanValues = {
            "V":"I",
            "X":"I",
            "L":"X",
            "C":"X",
            "D":"C",
            "M":"C",
        }
        romanInteger = 0
        previousValue = ""
        for c in s:
            if c in romanValues:
                currentValue = romanValues[c]
                
                if c in previousRomanValues and len(previousValue) > 0:
                    if previousRomanValues[c] == previousValue:
                        currentValue -= (romanValues[previousValue] *2) # *2 because it was previously added to the total
                
                romanInteger += currentValue
                previousValue = c
        
        
        return romanInteger

                
            