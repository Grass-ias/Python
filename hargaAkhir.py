def hargaAkhir(a, barang, VIP, negeri, hari):
    if VIP == True:
        if barang == "elektronik":
            if hari == "Jumat" or "Sabtu":
                if negeri == "luar negeri":
                    return ((a-(a*0.3))-(a*0.05))+(a*0.2)
                elif negeri == "dalam negeri":
                    return ((a-(a*0.3))-(a*0.05))+(a*0.1)
            elif hari == "Minggu":
                if negeri == "luar negeri":
                    return ((a-(a*0.3))+(a*0.05))+(a*0.2)
                elif negeri == "dalam negeri":
                    return ((a-(a*0.3))+(a*0.05))+(a*0.1)
            else:
                if negeri == "luar negeri":
                    return (a-((a*0.3))*0.2)
                elif negeri == "dalam negeri":
                    return (a-(a*0.3))+(a*0.1)
        elif barang == "pakaian":
            if hari == "Jumat" or "Sabtu":
                if negeri == "luar negeri":
                    return ((a-(a*0.2))-(a*0.05))+(a*0.2)
                elif negeri == "dalam negeri":
                    return ((a-(a*0.2))-(a*0.05))+(a*0.1)
            elif hari == "Minggu":
                if negeri == "luar negeri":
                    return ((a-(a*0.2))+(a*0.05))+(a*0.2)
                elif negeri == "dalam negeri":
                    return ((a-(a*0.2))+(a*0.05))+(a*0.1)
            elif hari == "Rabu":
                if negeri == "luar negeri":
                    return ((a-(a*0.2)-(a*0.05)))+(a*0.2)
                elif negeri == "dalam negeri":
                    return ((a-(a*0.2)-(a*0.05)))+(a*0.1)
            else:
                if negeri == "luar negeri":
                    return (a-(a*0.2))+(a*0.2)
                elif negeri == "dalam negeri":
                    return (a-(a*0.2))+(a*0.1)
        elif barang == "makanan":
            if hari == "Jumat" or "Sabtu":
                if negeri == "luar negeri":
                    return ((a-(a*0.15))-(a*0.05))+(a*0.2)
                elif negeri == "dalam negeri":
                    return ((a-(a*0.15))-(a*0.05))+(a*0.1)
            elif hari == "Minggu":
                if negeri == "luar negeri":
                    return ((a-(a*0.15))+(a*0.05))+(a*0.2)
                elif negeri == "dalam negeri":
                    return ((a-(a*0.15))+(a*0.05))+(a*0.1)
            else:
                if negeri == "luar negeri":
                    return (a-(a*0.15))+(a*0.2)
                elif negeri == "dalam negeri":
                    return (a-(a*0.15))+(a*0.1)
        else:
            if hari == "Jumat" or "Sabtu":
                if negeri == "luar negeri":
                    return (a-(a*0.05))+(a*0.2)
                elif negeri == "dalam negeri":
                    return (a-(a*0.05))+(a*0.1)
            elif hari == "Minggu":
                if negeri == "luar negeri":
                    return (a+(a*0.05))+(a*0.2)
                elif negeri == "dalam negeri":
                    return (a+(a*0.05))+(a*0.1)
    elif VIP == False:
            if barang == "pakaian":
                if hari == "Rabu":
                    if negeri == "luar negeri":
                        return (a-(a*0.05))+(a*0.2)
                    elif negeri == "dalam negeri":
                        return (a-(a*0.05))+(a*0.1)
                elif hari == "Minggu":
                    if negeri == "luar negeri":
                        return (a+(a*0.05))+(a*0.2)
                    elif negeri == "dalam negeri":
                        return (a+(a*0.05))+(a*0.1)
            elif barang == "makanan":
                if hari == "Minggu":
                    if negeri == "luar negeri":
                        return (a+(a*0.05))+(a*0.2)
                    elif negeri == "dalam negeri":
                        return (a+(a*0.05))+(a*0.1)
            elif barang == "elektronik":
                if hari == "Minggu":
                    if negeri == "luar negeri":
                        return (a+(a*0.05))+(a*0.2)
                    elif negeri == "dalam negeri":
                        return (a+(a*0.05))+(a*0.1)
            else:
                if hari == "Jumat" or "Sabtu":
                    if negeri == "luar negeri":
                        return (a-(a*0.05))+(a*0.2)
                    elif negeri == "dalam negeri":
                        return (a-(a*0.05))+(a*0.1)
                elif hari == "Minggu":
                    if negeri == "luar negeri":
                        return (a+(a*0.05))+(a*0.2)
                    elif negeri == "dalam negeri":
                        return (a+(a*0.05))+(a*0.1)