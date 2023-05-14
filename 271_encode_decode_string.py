class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        """
        enc_str = ""
        for i in strs:
            enc_str += str(len(i))
            enc_str += "#"
            enc_str += str(i)
        print(enc_str)
        return enc_str
    
    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        dic = {}
        decode = []
        
        for i in range(len(s)):
            if s[i].isdigit() and s[i+1] == "#":
                decode.append(s[i+2:i+2+int(s[i])])
        return decode

# Your Codec object will be instantiated and called as such:

strs =["C#","&","~Xp|F","R4QBf9g=_"]
codec = Codec()
codec.decode(codec.encode(strs))