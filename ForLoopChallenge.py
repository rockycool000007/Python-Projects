# Take an IP address entered at the keyboard
ip_address = input("Please enter the IP Address: ")
if ip_address[-1] != ".":
    ip_address += "."

segment = 1
segment_length = 0
# char = " "

for char in ip_address:
    if char == ".":
        print("Segement {} contains {} numbers".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

# code if the last char is not a period
# if char != ".":
#     print("Segement {} contains {} numbers".format(segment, segment_length))



