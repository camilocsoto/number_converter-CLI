from interface import ConvertInt

class Decimal_hexadecimal(ConvertInt):

    def next_transform(self, num_to_transform:str) -> str:
        # decimal to hexadecimal
        dividendo = int(num_to_transform.split('.')[0]) # borra la mantisa
        residuo = ''
        while dividendo > 0: # evalúa la parte entera
            if dividendo < 16: # evalúa los últimos 2 digitos
                if dividendo >= 10: #con letras
                    residuo+=self.transformation_table(str(dividendo))
                residuo+=str(dividendo)
                break 
            
            modulo = dividendo %16
            if modulo >= 10 and modulo <=15:
                residuo+=self.transformation_table(str(modulo)) #con letras
            else:
                residuo += str(modulo) #sin letras
            dividendo = dividendo//16 # sin mantiza     
        hexadecimal = residuo[::-1] #invierte el orden
        
        # mantisa 
        if '.' in num_to_transform:
            index = num_to_transform.index('.')
            mantisa = int(num_to_transform[index+1:]) #get the mantissa
            while mantisa > 0: # evalúa la parte entera
                if mantisa < 16: # evalúa los últimos 2 digitos
                    if mantisa >= 10: #con letras
                        residuo+=self.transformation_table(str(mantisa))
                    residuo+=str(mantisa)
                    break 
                
                modulo = mantisa %16
                if modulo >= 10 and modulo <=15:
                    residuo+=self.transformation_table(str(modulo)) #con letras
                else:
                    residuo += str(modulo) #sin letras
                mantisa = mantisa//16 # sin mantiza     
        mantisa_hexadecimal = residuo[::-1] #invierte el orden
        return f'{hexadecimal}.{mantisa_hexadecimal}'
    
    def reverse_transform(self, num_to_transform:str) -> str:
        # hexadecimal to decimal
        if '.' in num_to_transform:
            hexad, mantisa = num_to_transform.split('.')
        entire = 0
        n=0
        while len(hexad) != 0:
            if hexad[-1].isnumeric(): # get last num 
                digit= int(hexad[-1]) 
            else: # convert letters to nums
                digit = int(self.transformation_table(hexad[-1])) 
            entire+= digit*(16**n)
            hexad = hexad[:-1] # del last num
            n+=1
        
        # mantissa
        n=0
        mantisa_dec=0
        while len(mantisa) != 0:
            if mantisa[-1].isnumeric(): # get last num 
                digit= int(mantisa[-1]) 
            else: # convert letters to nums
                digit = int(self.transformation_table(mantisa[-1])) 
            mantisa_dec+= digit*(16**n)
            mantisa = mantisa[:-1] # del last num
            n+=1
        return f'{entire}.{mantisa_dec}'
            
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