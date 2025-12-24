red = int(input())
green = int(input())
blue = int(input())

red_hex = hex(red)[2:].upper().zfill(2)
green_hex = hex(green)[2:].upper().zfill(2)
blue_hex = hex(blue)[2:].upper().zfill(2)

rgb_code = f"#{red_hex}{green_hex}{blue_hex}"

print(rgb_code)