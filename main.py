hewan = ['Kuda', 'Kelinci', 'Kambing', 'Unta', 'Domba']
deleteHewan = ['Kelinci', 'Kambing', 'Unta']

print("Hewan : ", hewan)
print("Hewan Yang Dihapus : ", deleteHewan)

iterator = iter(hewan)
for h in list(iterator):
    for i in deleteHewan:
        if i == h:
            hewan.remove(h)
            break

print("Output hewan : ", hewan)