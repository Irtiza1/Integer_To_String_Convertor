phone=input("Phone: ")
digits_mapping={
    "0":"Zero",
    "1":"one",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}
output=""
for ch in phone:
    output+= digits_mapping.get(ch,"!")+ " "
print(output)




Phone=input(">")
message=Phone.split(' ')
output=""
string_mapping={
    "Zero":"0",
    "One":"1",
    "Two":"2",
    "Three":"3",
    "Four":"4",
    "Five":"5",
    "Six":"6",
    "Seven":"7",
    "Eight":"8",
    "Nine":"9",
    "zero":"0",
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}

for ch in message:
    output+= string_mapping.get(ch,"?")
print(output)
