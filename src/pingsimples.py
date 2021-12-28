import os

print("#" * 60)

ip_ou_host = input("Digite um ip ou host: ")
print('-'*60)

os.system(f"ping {ip_ou_host}")

