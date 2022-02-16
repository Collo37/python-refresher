#while loops

collins_is_programmer = True
collins_has_energy = True
energy_level = 100

while(collins_is_programmer and collins_has_energy):
    energy_level -= 10
    print("Collins still has energy")
    if(energy_level == 0):
        collins_has_energy = False
        print("Collins no longer has energy")

