temperature_val = [16, 12, 11, 9, 13, 15]

for kel_val in temperature_val:
    Cel_temp_val = kel_val - 273.15
    far_temp_val = 1.8*Cel_temp_val + 32
    print(f"Farenheight value of {kel_val} is {round(far_temp_val)}")
    print(f"Celsius value of {kel_val} is {Cel_temp_val}")

# The above code converts temperature values from kelvin to celsius and farenheit

