from pyVim.connect import SmartConnectNoSSL, Disconnect
import pyVmomi, ssl

login = SmartConnectNoSSL(host = "vCenter_address", user = "administrator@vsphere.local", pwd = "Password")

conexao = login.content

print(login.CurrentTime())  # Just to test if it's working

Disconnect(login)
