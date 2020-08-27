from .. import utils
from .component import Component


class BaseboardCPLD(Component):
    def __init__(self):
        Component.__init__(self)


        self.name = "CPLD"
        self.vendor = utils.dmidecode_string("system-manufacturer")
        self.model = utils.dmidecode_string("system-product-name")
        self.serial = utils.dmidecode_string("system-uuid")

        if self.vendor == "Dell Inc.":
            try:
                self.firmware_version = utils.get_baseboard_cpld("firmware_version")
            except:
                print("Something went wrong, probably no racadm")
                self.firmware_version = ""
        else:
            self.firmware_version = ""

        self.data = {}


    @classmethod
    def list(cls, _):
        cpld = []
        cpld.append(cls())
        return cpld
