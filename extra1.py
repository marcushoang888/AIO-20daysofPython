def calculate_can_chi_calendar(year):
    can = year % 10
    chi = year % 12
    can_chi = ""
    match can:
        case 0:
            can_chi = can_chi + "Canh"
        case 1:
            can_chi = can_chi + "Tân"
        case 2:
            can_chi = can_chi + "Nhâm"
        case 3:
            can_chi = can_chi + "Quý"
        case 4:
            can_chi = can_chi + "Giáp"
        case 5:
            can_chi = can_chi + "Ất"
        case 6:
            can_chi = can_chi + "Bính"
        case 7:
            can_chi = can_chi + "Đinh"
        case 8:
            can_chi = can_chi + "Mậu"
        case 9:
            can_chi = can_chi + "Kỷ"

    match chi:
        case 0:
            can_chi = can_chi + " Thân"
        case 1:
            can_chi = can_chi + " Dậu"
        case 2:
            can_chi = can_chi + " Tuất"
        case 3:
            can_chi = can_chi + " Hợi"
        case 4:
            can_chi = can_chi + " Tí"
        case 5:
            can_chi = can_chi + " Sửu"
        case 6:
            can_chi = can_chi + " Dần"
        case 7:
            can_chi = can_chi + " Mão"
        case 8:
            can_chi = can_chi + " Thìn"
        case 9:
            can_chi = can_chi + " Tỵ"
        case 10:
            can_chi = can_chi + " Ngọ"
        case 11:
            can_chi = can_chi + " Mùi"
    print(can_chi)
    return
calculate_can_chi_calendar(1997)