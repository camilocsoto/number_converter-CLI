from dataclasses import dataclass
from binary_octal import Binary_octal
from decimal_hexadecimal import Decimal_hexadecimal
from octal_decimal import Octal_decimal 

@dataclass
class ConvertService:
    in_type: int      # 1: binario, 2: octal, 3: decimal, 4: hexadecimal
    request: str      # Número a convertir
    out_type: int     # Tipo de dato deseado para la conversión
    response: str = ""  # resultado de la conversión

    def exec_strategy(self) -> str:
        """
        Ejecuta la conversión encadenando los pasos necesarios en la "escalera":
        - Si se va de un tipo inferior a uno superior (ej.: binario → octal → decimal),
          se usa `next_transform` en cada paso.
        - Si se va de un tipo superior a uno inferior (ej.: hexadecimal → decimal → octal),
          se usa `reverse_transform` en cada paso.
          
        Los mapeos de tipos son:
            1 → binario
            2 → octal
            3 → decimal
            4 → hexadecimal
        """
        # validación
        type_names = {1: "binario", 2: "octal", 3: "decimal", 4: "hexadecimal"}
        if self.in_type not in type_names or self.out_type not in type_names:
            raise ValueError("Tipos inválidos. Usa 1 (binario), 2 (octal), 3 (decimal) o 4 (hexadecimal).")
        
        # mismo tipo de conversion
        if self.in_type == self.out_type:
            self.response = self.request
            return self.response

        # Valor que irá cambiando con cada conversión
        current_value = self.request

        # Conversión ascendente (por ejemplo, de binario a hexadecimal)
        if self.in_type < self.out_type:
            for step in range(self.in_type, self.out_type):
                if step == 1 and step + 1 == 2:
                    # Convertir de binario a octal
                    converter = Binary_octal()
                    current_value = converter.next_transform(current_value)
                elif step == 2 and step + 1 == 3:
                    # Convertir de octal a decimal
                    converter = Octal_decimal()
                    current_value = converter.next_transform(current_value)
                elif step == 3 and step + 1 == 4:
                    # Convertir de decimal a hexadecimal
                    converter = Decimal_hexadecimal()
                    current_value = converter.next_transform(current_value)
                else:
                    raise ValueError("Conversión no soportada en la escalera.")
        
        # Conversión descendente (por ejemplo, de hexadecimal a binario)
        else:
            # Se recorre la escalera en sentido inverso
            for step in range(self.in_type, self.out_type, -1):
                if step == 2 and step - 1 == 1:
                    # Convertir de octal a binario
                    converter = Binary_octal()
                    current_value = converter.reverse_transform(current_value)
                elif step == 3 and step - 1 == 2:
                    # Convertir de decimal a octal
                    converter = Octal_decimal()
                    current_value = converter.reverse_transform(current_value)
                elif step == 4 and step - 1 == 3:
                    # Convertir de hexadecimal a decimal
                    converter = Decimal_hexadecimal()
                    current_value = converter.reverse_transform(current_value)
                else:
                    raise ValueError("Conversión no soportada en la escalera.")
        print(f"conversion -> {current_value}")
        self.response = current_value
        return self.response


if __name__ == '__main__':
    print(f"{'='*5} Bienvenido a la calculadora conversora.{'='*5} \n Usa puntos (.) no comas (,)")
    in_user = int(input("1 → binario \n 2 → octal \n 3 → decimal \n 4 → hexadecimal \n digíta el tipo de número que vas a insertar: "))
    out_user= int(input("\n 1 → binario \n 2 → octal \n 3 → decimal \n 4 → hexadecimal \n Digíta el tipo de número que quieres obtener: "))
    user_request = input("\n Digita el número a convertir: ")
    operation = ConvertService(in_type=in_user, request=user_request, out_type=out_user)
    operation.exec_strategy()
