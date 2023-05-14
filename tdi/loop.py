# percorrendo itens de uma lista
alvos = [{"ip": '192.168.1.8', 'so': "windows", 'ativo': True, 'portas': [80, 22, 21]}, {"ip": '192.168.1.9', 'so': "linux", 'ativo': False, 'portas': [4444, 2222, 21]}, {"ip": '192.168.1.333', 'so': "windows", 'ativo': True, 'portas': [80]}, {"ip": '192.168.1.555', 'so': "macs", 'ativo': False, 'portas': [3306, 1337]}]

# for [iten] in [lista]:
# o item pode ter qualquer nome

# loop simples
for alvo in alvos:
    print("nmap " + alvo['ip'])
    print("****************")

# loop condicional
for alvo in alvos:
    if alvo['so'] == "windows":
        print("se atracando com o ruindows kkkkk")

# loop boleano: se(if) o item(alvo) é porque seu valor boleano está True*(ativo)
for alvo in alvos:
    if alvo['ativo']:
        print(alvo["ip"])
        for porta in alvo["portas"]:
            print("atacando a porta " + str(porta))
            print("*************")

def encontra_linux(alvos):
    for alvo in alvos:
        if alvo["so"] == "linux":
            print("Viva! Enconrei um linux! E seu ip é " + str(porta))
            break

encontra_linux(alvos) 

# BREAK e CONTINUE

for alvo in alvos:
    if alvo["so"] == "linux":
        print("não ataquei que é linux")
        continue
    print("atacando porque não é linux")