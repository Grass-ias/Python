def jam(j,m,s):
    if j >= 0 and j <= 24:
        if m >= 0 and m <= 59:
            if s >= 0 and s <= 59:
                return "Jam:" + j, "Menit" + m, "Detik" + s
            else:
                return "Waktu tidak valid"
        else:
            return "Waktu tidak valid"
    else:
        return "Waktu tidak valid"