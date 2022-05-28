# Properties used as references in the script #

class references():

    def __init__(self) -> None:
        self.references = {
            "safari_driver_path" : "/usr/bin/safaridriver"
            }

    def get_reference_value(self, attribute):
        """
        safari_driver_path -> Driver path for Safari browser
        """
        if attribute in self.references.keys():
            return self.references[attribute]
        else:
            return None

r1 = references()
print(r1.get_reference_value("safari_driver_path"))