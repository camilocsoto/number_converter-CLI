from interface import ConvertInt

class Octal_decimal(ConvertInt):

    def next_transform(self, num_to_transform:str) -> str:
        # octal to decimal
        octal = num_to_transform
        decimal = 0
        n=0
        while len(octal) != 0:
            digit= int(octal[-1]) # get last num
            decimal+= digit*(8**n)
            octal = octal[:-1] # del last num
            n+=1
        return str(decimal)
        
    
    def reverse_transform(self, num_to_transform:str) -> str:
        # decimal to octal
        dividendo = int(num_to_transform)
        residuo = ''
        while dividendo > 0: # parte entera
            if dividendo < 8:
                residuo+=str(dividendo)
                break # falta la mantiza!
            residuo += str(dividendo % 8)
            dividendo = dividendo//8
        octal = residuo[::-1]
        return octal
    
