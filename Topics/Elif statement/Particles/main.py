particle_spin = str(input())
particle_charge = str(input())

if particle_spin == "1":
    print("Photon Boson")
elif particle_spin == "1/2":
    if particle_charge == "-1/3":
        print("Strange Quark")
    elif particle_charge == "2/3":
        print("Charm Quark")
    elif particle_charge == "-1":
        print("Electron Lepton")
    elif particle_charge == "0":
        print("Neutrino Lepton")
    else:
        print("Unknown particle")
else:
    print("Unknown particle")



