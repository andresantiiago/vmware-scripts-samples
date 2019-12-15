from pyVim.connect import SmartConnectNoSSL, Disconnect
import pyVmomi, ssl

login = SmartConnectNoSSL(host = "vCenter_address", user = "administrator@vsphere.local", pwd = "Password")

def get_all_objs(content, vimtype):
        obj = {}
        container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
        for managed_object_ref in container.view:
                obj.update({managed_object_ref: managed_object_ref.name})
        return obj
