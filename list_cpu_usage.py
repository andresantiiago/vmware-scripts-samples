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


def hostCPU(host):
    try:
        overallCpuUsage = host.summary.quickStats.overallCpuUsage
        numCpuCores = host.summary.hardware.numCpuCores
        cpuMhz = host.summary.hardware.cpuMhz
        cpuUsagePercentage = ( overallCpuUsage / ( numCpuCores * cpuMhz ) ) * 100

        print("=-"*15)
        print("\nHostname: ", host.name)
        print("overallCpuUsage: ", overallCpuUsage)
        print("numCpuCores: ", numCpuCores)
        print("cpuMhz: ", cpuMhz)
        print("cpu_usage_percentage: %", cpuUsagePercentage)

    except Exception as error:
        print("Unable to access host information: ", host.name)
        print(error)
        pass



hosts = getObjects(connection, [pyVmomi.vim.HostSystem])  # pylint: disable=no-member

for host in hosts:
    hostCPU(host)

Disconnect(login)
