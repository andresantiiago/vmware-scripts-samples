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


def hostStatus(host):
    status = host.summary.runtime.powerState

    return status


hosts = getObjects(connection, [pyVmomi.vim.HostSystem])  # pylint: disable=no-member

for host in hosts:
    print("{} ---> Status ---> {}".format(host.name, hostStatus(host)))
    

Disconnect(login)
