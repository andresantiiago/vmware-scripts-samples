from pyVim.connect import SmartConnectNoSSL, Disconnect
import pyVmomi, ssl, requests, time, subprocess

login = SmartConnectNoSSL(host = "vCenter_address", user = "administrator@vsphere.local", pwd = "Password")

connection = login.content


def getObjects(connection, vimtype):
        container = connection.viewManager.CreateContainerView(connection.rootFolder, vimtype, True)
        obj = dict()

        for managed_object_ref in container.view:
                obj.update({managed_object_ref: managed_object_ref.name})
        return obj


def hostMemory(host):
    try:
        MBFACTOR = float(1 << 20)
        memoryUsage = host.summary.quickStats.overallMemoryUsage
        memoryCapacity = host.hardware.memorySize
        memoryCapacityInMB = host.hardware.memorySize/MBFACTOR
        freeMemoryPercentage = 100 - ((float(memoryUsage) / memoryCapacityInMB) * 100)

        
        print("=-"*15)
        print("\nHostname: ", host.name)
        print("memoryUsage: ", memoryUsage)
        print("memoryCapacity: ", memoryCapacity)
        print("memoryCapacityInMB: ", memoryCapacityInMB)
        print("freeMemoryPercentage: %", freeMemoryPercentage)

    except Exception as error:
        print("Não foi possível acessar as informações do host: ", host.name)
        print(error)
        pass



hosts = getObjects(connection, [pyVmomi.vim.HostSystem])  # pylint: disable=no-member

for host in hosts:
    hostMemory(host)

Disconnect(login)
