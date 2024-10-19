def hargaAkhir(a, barang, VIP, negeri, hari):
    if VIP == True:
        if barang == "elektronik":
            if hari == "Jumat" or hari == "Sabtu":
                if negeri == "luar negeri":
                    return int(((a-(a*0.3))-((a-(a*0.3))*0.05))+(((a-(a*0.3))*0.05)*0.2))
                elif negeri == "dalam negeri":
                    return int(((a-(a*0.3))-((a-(a*0.3))*0.05))+(((a-(a*0.3))*0.05)*0.1))
            elif hari == "Minggu":
                if negeri == "luar negeri":
                    return int(((a-(a*0.3))+((a-(a*0.3))*0.05))+(((a-(a*0.3))*0.05)*0.2))
                elif negeri == "dalam negeri":
                    return int(((a-(a*0.3))+((a-(a*0.3))*0.05))+(((a-(a*0.3))*0.05)*0.1))
            else:
                if negeri == "luar negeri":
                    return int((a-(a*0.3))+((a-(a*0.3))*0.2))
                elif negeri == "dalam negeri":
                    return int((a-(a*0.3))+((a-(a*0.3))*0.1))
        elif barang == "pakaian":
            if hari == "Jumat" or "Sabtu":
                if negeri == "luar negeri":
                    return int(((a-(a*0.2))-((a-(a*0.2))*0.05))+(((a-(a*0.2))*0.05)*0.2))
                elif negeri == "dalam negeri":
                    return int(((a-(a*0.2))-((a-(a*0.2))*0.05))+(((a-(a*0.2))*0.05)*0.1))
            elif hari == "Minggu":
                if negeri == "luar negeri":
                    return int(((a-(a*0.2))+((a-(a*0.2))*0.05))+(((a-(a*0.2))*0.05)*0.2))
                    return int(((a-(a*0.2))+((a-(a*0.2))*0.05))+(((a-(a*0.2))*0.05)*0.1))
            elif hari == "Rabu":
                if negeri == "luar negeri":
                    return int(((a-(a*0.2)-((a-(a*0.2))*0.05)))+(((a-(a*0.2))*0.05)*0.2))
                elif negeri == "dalam negeri":
                    return int(((a-(a*0.2)-((a-(a*0.2))*0.05)))+(((a-(a*0.2))*0.05)*0.1))
            else:
                if negeri == "luar negeri":
                    return int((a-(a*0.2))+((a-(a*0.2))*0.2))
                elif negeri == "dalam negeri":
                    return int((a-(a*0.2))+((a-(a*0.2))*0.1))
        elif barang == "makanan":
            if hari == "Jumat" or "Sabtu":
                if negeri == "luar negeri":
                    return int(((a-(a*0.15))-((a-(a*0.15)*0.05))+(((a-(a*0.15))*0.05)*0.2)))
                elif negeri == "dalam negeri":
                    return int(((a-(a*0.15))-((a-(a*0.15)*0.05))+(((a-(a*0.15))*0.05)*0.1)))
            elif hari == "Minggu":
                if negeri == "luar negeri":
                    return int(((a-(a*0.15))+((a-(a*0.15)*0.05))+(((a-(a*0.15))*0.05)*0.2)))
                elif negeri == "dalam negeri":
                    return int(((a-(a*0.15))+((a-(a*0.15)*0.05))+(((a-(a*0.15))*0.05)*0.1)))
            else:
                if negeri == "luar negeri":
                    return int((a-(a*0.15))+((a-(a*0.15))*0.2))
                elif negeri == "dalam negeri":
                    return int((a-(a*0.15))+((a-(a*0.15))*0.1))
        else:
            if hari == "Jumat" or "Sabtu":
                if negeri == "luar negeri":
                    return int((a-(a*0.05))+((a-(a*0.05))*0.2))
                elif negeri == "dalam negeri":
                    return int((a-(a*0.05))+((a-(a*0.05))*0.1))
            elif hari == "Minggu":
                if negeri == "luar negeri":
                    return int((a+(a*0.05))+((a+(a*0.05))*0.2))
                elif negeri == "dalam negeri":
                    return int((a+(a*0.05))+((a+(a*0.05))*0.1))
    elif VIP == False:
            if barang == "pakaian":
                if hari == "Rabu":
                    if negeri == "luar negeri":
                        return int((a-(a*0.05))+((a-(a*0.05))*0.2))
                    elif negeri == "dalam negeri":
                        return int((a-(a*0.05))+((a-(a*0.05))*0.1))
                elif hari == "Minggu":
                    if negeri == "luar negeri":
                        return int((a+(a*0.05))+((a+(a*0.05))*0.2))
                    elif negeri == "dalam negeri":
                        return int((a+(a*0.05))+((a+(a*0.05))*0.1))
            elif barang == "makanan":
                if hari == "Minggu":
                    if negeri == "luar negeri":
                        return int((a+(a*0.05))+((a+(a*0.05))*0.2))
                    elif negeri == "dalam negeri":
                        return int((a+(a*0.05))+((a+(a*0.05))*0.1))
            elif barang == "elektronik":
                if hari == "Minggu":
                    if negeri == "luar negeri":
                        return int((a+(a*0.05))+((a+(a*0.05))*0.2))
                    elif negeri == "dalam negeri":
                        return int((a+(a*0.05))+((a+(a*0.05))*0.1))
            else:
                if hari == "Jumat" or "Sabtu":
                    if negeri == "luar negeri":
                        return int((a-(a*0.05))+((a-(a*0.05))*0.2))
                    elif negeri == "dalam negeri":
                        return int((a-(a*0.05))+((a-(a*0.05))*0.1))
                elif hari == "Minggu":
                    if negeri == "luar negeri":
                        return int((a+(a*0.05))+((a+(a*0.05))*0.2))
                    elif negeri == "dalam negeri":
                        return int((a+(a*0.05))+((a+(a*0.05))*0.1))
                    
print(hargaAkhir(1000000, "elektronik", True, "dalam negeri", "Senin"))
print(hargaAkhir(500000, "pakaian", False, "luar negeri", "Rabu"))