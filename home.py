from company import Driver, Bus, Trip

# Drivers
david = Driver("Apolo David", "Male", "Kibuli", "0763243343")
amos = Driver("Amos Peters", "Male", "Kawempe", "075337322")
Fatmah = Driver("Fatmah Musa", "Female", "Nakawa", "0786552622")

# Buses
executive = Bus("UBQ 897A", "Toyota", 20, "2024-10-05")
executive.assign_driver(amos)
executive.assign_driver(david)
executive.assign_driver(Fatmah)

print(executive.get_bus_drivers())

common = Bus("UBP 348G", "Isuzu", 30, "2025-10-05")


# Trips
kampala_masaka = Trip("T001", "2024-10-07", "Kampala", "Masaka")
kampala_jinja = Trip("T001", "2024-10-07", "Kampala", "Jinja")

kampala_masaka.assign_bus(common)
kampala_jinja.assign_bus(common)


