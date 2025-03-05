from interface import ConvertInt

class Binary_octal(ConvertInt):
    # binary to octal
    def next_transform(self, num_to_transform:str) -> str:
        # binary to octal
        if '.' in num_to_transform:
            binary, mantisa = num_to_transform.split('.')
        else:
            binary = num_to_transform
        #real part
        octal = ''
        while len(binary) != 0:
            last3nums = binary[-3:]
            if len(last3nums) == 3: # 3 números
                octal+= self.transform_table(last3nums) 
            elif len(last3nums) == 2:
                last3nums = "0" + last3nums
                octal+= self.transform_table(last3nums)
            elif len(last3nums) == 1:
                last3nums = "00" + last3nums
                octal+= self.transform_table(last3nums)
            # borra los últimos 3 números
            binary = binary[:-3]
        octal = octal[::-1] # invierte el orden
        # mantissa part
        mantisa_octal = ''
        while len(mantisa) != 0:
            last3nums = mantisa[-3:]
            if len(last3nums) == 3: # 3 números
                mantisa_octal+= self.transform_table(last3nums) 
            elif len(last3nums) == 2:
                last3nums = "0" + last3nums
                mantisa_octal+= self.transform_table(last3nums)
            elif len(last3nums) == 1:
                last3nums = "00" + last3nums
                mantisa_octal+= self.transform_table(last3nums)
            # borra los últimos 3 números
            mantisa = mantisa[:-3]
        mantisa_octal = mantisa_octal[::-1]
        return f'{octal}.{mantisa_octal}'
    
    def reverse_transform(self, num_to_transform:str) -> str:
        # octal to binary
        if '.' in num_to_transform:
            octal, mantisa = num_to_transform.split('.')
        # real part
        binary = ''
        while len(octal) != 0:
            digit= octal[0]
            binary+= self.transform_table(digit)
            octal = octal[1:] # elimina el primer numero
    
        # mantissa part
        mantisa_binary = ''
        while len(mantisa) != 0:
            digit= mantisa[0]
            mantisa_binary+= self.transform_table(digit)
            mantisa = mantisa[1:] # elimina el primer numero
            
        return f'{binary}.{mantisa_binary}'
    
    def transform_table(self, num_to_transform:str) -> str:
        match num_to_transform:
            case "0": return "000" # octal to binary
            case "1": return "001"
            case "2": return "010"
            case "3": return "011"
            case "4": return "100"
            case "5": return "101"
            case "6": return "110"
            case "7": return "111"
            case "000": return "0" # binary to octal
            case "001": return "1"
            case "010": return "2"
            case "011": return "3"
            case "100": return "4"
            case "101": return "5"
            case "110": return "6"
            case "111": return "7"
            case _: raise ValueError(f"grupo {num_to_transform} no válido.")

