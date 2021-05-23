# Find your zodiac sign

Day = int(input("Enter the birth date: \n"))
Month = input("Enter the birth month:\n")

if Month == "January":
    Sign = "Capricorn" if (Day < 20) else "Aquarius"
elif Month == "February":
    Sign = "Aquarius" if (Day < 19) else "Pisces"
elif Month == "March":
    Sign = "Pisces" if (Day < 21) else "Aries"
elif Month == "April":
    Sign = "Aries" if (Day < 20) else "Taurus"
elif Month == "May":
    Sign = "Taurus" if (Day < 21) else "Gemini"
elif Month == "June":
    Sign = "Gemini" if (Day < 21) else "Cancer"
elif Month == "July":
    Sign = "Cancer" if (Day < 23) else "Leo"
elif Month == "August":
    Sign = "Leo" if (Day < 23) else "Virgo"
elif Month == "September":
    Sign = "Virgo" if (Day < 23) else "Libra"
elif Month == "October":
    Sign = "Libra" if (Day < 23) else "Scorpio"
elif Month == "November":
    Sign = "Scorpio" if (Day < 22) else "Sagittarius"
elif Month == "Decembher":
    Sign = "Sagittarius" if (Day < 22) else "Capricorn"

print("Your Astrological sign:",Sign)
