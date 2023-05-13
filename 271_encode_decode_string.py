class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        enc_str = ""
        for i in strs:
            enc_str += str(len(i))
            enc_str += "#"
            enc_str += str(i)
        print(enc_str)
        return enc_str
    
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        dec_str = []

        i = 0

        while  i < len(s):
            if s[i].isdigit() and i < len(s)-1:
                num = ""
                runner = i
                while runner < len(s) and s[runner]!= "#" and s[runner].isdigit():
                    num += s[runner]
                    runner +=1
                if s[runner] =="#":
                    temp = ""
                    print(temp)
                    for j in range(runner+1, runner + int(num)+ 1):
                        temp+= s[j]
                    print(temp)
                    dec_str.append(temp)
                    i += runner + int(num)+ 1
            else:
                i+=1

        return dec_str

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))