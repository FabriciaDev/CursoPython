def check_admin(username):
    admin = 'root@tdi'

    if username == admin or username == "lucas@tdi":
        msg = "é admin"
    else:    
        msg = "não é admin"
    return msg

print(check_admin("bruno@tdi"))
print(check_admin("root@tdi"))
print(check_admin("lucas@tdi"))

#   Caso de Uso:
#   if alvos["so"] == linux:
#       ataque para linux
#          
#   else:
#       ataque para windows
#