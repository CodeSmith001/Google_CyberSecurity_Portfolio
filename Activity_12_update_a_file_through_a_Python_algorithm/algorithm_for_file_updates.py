allow_list = "allow_list.txt"
remove_list = ["192.168.205.12","192.168.6.9"]

with open(allow_list, "r") as f:
    ip_addresses = f.read()


ip_addresses_list = ip_addresses.split()

for i in remove_list:
    if i in ip_addresses_list:
        ip_addresses_list.remove(i)

ip_addresses = "\n".join(ip_addresses_list)

with open(allow_list, "w") as f:
    f.write(ip_addresses)


with open(allow_list, "r") as f:
    ip_addresses = f.read()
    
print(ip_addresses)
print("all removed addresses were sucessfuly removed.")
