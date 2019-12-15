from pyVim.connect import SmartConnectNoSSL, Disconnect
import pyVmomi, ssl

login = SmartConnectNoSSL(host = "vCenter_address", user = "administrator@vsphere.local", pwd = "Password")

datacenter = login.content.rootFolder.childEntity[0]
vms = datacenter.vmFolder.childEntity

for i in vms:
    print(i.name)

Disconnect(login)
