import struct
from rich import print
import numpy as np
format_string = '>f'
my_variable = 10
packed_data = struct.pack(format_string, my_variable)
bytes_str = ''

for byte in packed_data:
    byte_str = format(byte, '08b')
    bytes_str += byte_str

def fractional_binary(binary:str) -> float:
    value=np.float128(1)
    for position, byte in enumerate(binary):
        value+=int(byte)*(2**(-position-1))  
    return value
sign_bit = bytes_str[0]
exponent_bits = bytes_str[1:9]
exponent=int(exponent_bits,2)-127
fraction_bits = bytes_str[9:]
fraction=fractional_binary(fraction_bits)
print(f"{my_variable} em representação Float32 =")
print(f"[red]{sign_bit}[/red][green]{exponent_bits}[/green][bright_yellow]{fraction_bits}[/bright_yellow]")
print('')
print(f"Sinal 1-bit: [red]{sign_bit}[/red] {'(positivo)' if sign_bit else 'negativo'}")
print('')
print(f"Expoente 8-bits: [green]{exponent_bits}= {exponent+127}-127=[/green]{exponent}")
print('')
print(f"Fracionário 23-bits [bright_yellow]{fraction_bits}[/bright_yellow] = {fraction}")
print("----------------")
print(f"{my_variable}=(Float-32)[bright_yellow]{fraction}[/bright_yellow]*(2^[green]{exponent}[/green])={fraction*np.power(2,exponent)}")