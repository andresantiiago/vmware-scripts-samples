from pyVim.connect import SmartConnectNoSSL, Disconnect
import pyVmomi, ssl, humanize, requests, time, subprocess

login = SmartConnectNoSSL(host = "vCenter_address", user = "administrator@vsphere.local", pwd = "Password")

connection = login.content


def getObjects(connection, vimtype):
        container = connection.viewManager.CreateContainerView(connection.rootFolder, vimtype, True)
        obj = dict()

        for managed_object_ref in container.view:
                obj.update({managed_object_ref: managed_object_ref.name})
        return obj


def datastoreUsage(datastore):
    try:
        summary = datastore.summary
        capacity = summary.capacity
        freeSpace = summary.freeSpace
        uncommittedSpace = summary.uncommitted
        freeSpacePercentage = (float(freeSpace) / capacity) * 100

        print("=-"*15)
        print("\nDatastore name: ", summary.name)
        print("Capacity: ", humanize.naturalsize(capacity, binary=True))

        if uncommittedSpace is not None:
                provisionedSpace = (capacity - freeSpace) + uncommittedSpace
                print("Provisioned space: ", humanize.naturalsize(provisionedSpace, binary=True))

        print("Free space: ", humanize.naturalsize(freeSpace, binary=True))
        print("Free space percentage: " + str(freeSpacePercentage) + "%")
        print("=-"*15)

    except Exception as error:
        print("Não foi possível acessar as informações do datastore: ", datastore.name)
        print(error)
        pass



datastores = getObjects(connection, [pyVmomi.vim.Datastore])  # pylint: disable=no-member

for ds in datastores:
    datastoreUsage(ds)

Disconnect(login)
