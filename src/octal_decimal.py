from interface import ConvertInt

class Octal_decimal(ConvertInt):

    def next_transform(self, num_to_transform:str) -> str:
        # octal to decimal
        if '.' in num_to_transform:
            octal, mantisa = num_to_transform.split('.')            
        else:
            octal = num_to_transform
        # real
        decimal = 0
        n=0
        while len(octal) != 0:
            digit= int(octal[-1]) # get last num
            decimal+= digit*(8**n)
            octal = octal[:-1] # del last num
            n+=1
            
        # mantisa
        mantisa_decimal = 0
        n=0
        while len(mantisa) != 0:
            digit= int(mantisa[-1]) # get last num
            mantisa_decimal+= digit*(8**n)
            mantisa = mantisa[:-1] # del last num
            n+=1

        return f'{decimal}.{mantisa_decimal}'
        
    
    def reverse_transform(self, num_to_transform:str) -> str:
        # decimal to octal
        if '.' in num_to_transform:
            dividendo, mantisa = num_to_transform.split('.')
            dividendo, mantisa = int(dividendo), int(mantisa)
        else:
            dividendo = int(num_to_transform)
        #real
        residuo_real = ''
        while dividendo > 0: # parte entera
            if dividendo < 8:
                residuo_real+=str(dividendo)
                break # falta la mantiza!
            residuo_real += str(dividendo % 8)
            dividendo = dividendo//8
        residuo_real = residuo_real[::-1]
        
        #mantisa
        residuo_mantisa = ''
        while mantisa > 0: # parte entera
            if mantisa < 8:
                residuo_mantisa+=str(mantisa)
                break # falta la mantiza!
            residuo_mantisa += str(mantisa % 8)
            mantisa = mantisa//8
        residuo_mantisa = residuo_mantisa[::-1]
        
        return f'{residuo_real}.{residuo_mantisa}'
    
