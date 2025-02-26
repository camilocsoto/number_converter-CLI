from interface import ConvertInt

class Decimal_hexadecimal(ConvertInt):

    def next_transform(self, num_to_transform:str) -> str:
        # decimal to hexadecimal
        dividendo = int(num_to_transform)
        residuo = ''
        while dividendo > 0: # parte entera
            if dividendo < 16:
                if dividendo >= 10: #con letras
                    residuo+=self.transformation_table(str(dividendo))
                residuo+=str(dividendo)
                break # falta la mantiza!            
            
            modulo = dividendo %16
            if modulo >= 10 and modulo <=15:
                residuo+=self.transformation_table(str(modulo)) #con letras
            else:
                residuo += str(modulo) #sin letras
            dividendo = dividendo//16 # sin mantiza     

        hexadecimal = residuo[::-1] #invierte el orden
        return hexadecimal
    
    def reverse_transform(self, num_to_transform:str) -> str:
        # hexadecimal to decimal
        hexad = num_to_transform
        decimal = 0
        n=0
        while len(hexad) != 0:
            if hexad.isnumeric(): # get last num 
                digit= int(hexad[-1]) 
            else: # convert letters to nums
                digit = int(self.transformation_table(hexad[-1])) 
            decimal+= digit*(16**n)
            hexad = hexad[:-1] # del last num
            n+=1
        return str(decimal)
        
    
    def transformation_table(self, num_to_transform:str) -> str:
        match num_to_transform:
            case "10": return "A"
            case "11": return "B"
            case "12": return "C"
            case "13": return "D"
            case "14": return "E"
            case "15": return "F"
            case "A": return "10"
            case "B": return "11"
            case "C": return "12"
            case "D": return "13"
            case "E": return "14"
            case "F": return "15"
            case _: return f"{num_to_transform} not valid"
            