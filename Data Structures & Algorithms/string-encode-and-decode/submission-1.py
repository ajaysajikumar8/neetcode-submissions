# The Pattern — Length-Prefix Framing

class Solution:

    def encode(self, strs: List[str]) -> str:
        res_string = ""
        for item in strs: 
            delimiter =  str(len(item)) + "#"
            res_string += delimiter + item
        return res_string

    def decode(self, s: str) -> List[str]:
        i = 0
        result_list = []
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            str_length = int(s[i : j])
            item = s[j+1:j+1+str_length]
            result_list.append(item)
            i = j + 1 + str_length
        return result_list
