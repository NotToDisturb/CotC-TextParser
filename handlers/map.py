from assets import BaseAsset


class BaseMapAsset(BaseAsset):
    def parse_text(self, file, ends, expected_length=None):
        content = b''
        while len((current_read := file.read(1))) > 0:
            if current_read in ends and not expected_length:
                return content.decode("utf8", errors="ignore")
            else:
                content += current_read
            if len(content) == expected_length:
                return content.decode("utf8", errors="ignore")
        return None


class MapListTableAsset(BaseMapAsset):
    HEADER_END_CHAR = b'\xDC'
    SEPARATOR_END_CHAR = b'\xA4'

    def __init__(self, file_path):
        self.file_path = file_path
        self.content_parsers = {
            "number_1": self.parse_number_1,
            "number_2": self.parse_number_2,
            "number_4": self.parse_number_4,
            "text_0": self.parse_text_0,
            "text_1": self.parse_text_1,
            "excess": self.do_excess_key,
            "empty": self.do_empty_contents
        }
        self.expected_keys = {
            "id": "number_1",
            "CatMap": "excess",
            "CatRegion": "excess",
            "CatVariation": "excess",
            "CatBlock": "excess",
            "MapLabel": "excess",
            "RegionIconTexID": "excess",
            "RegionText": "number_1",
            "MapText": "number_1",
            "CameraSet": "number_1",
            "LightSet": "number_1",
            "BGM": "number_1",
            "FootSE": "number_1",
            "FootEffect": "number_1",
            "ReverbFlag": "number_1",
            "LanthanumFlag": "number_1",
            "RidingVehicle": "number_1",
            "Battlemap": "excess",
            "SubLevelList": "excess",
            "JoinMap": "excess",
            "MapPath": "excess",
            "PathDataPath": "excess",
            "PlayerAttachEffectTriggers": "excess",
            "PlayerAttachEffectInvalidConditions": "excess",
            "PlayerAttachEffectGroups": "excess"
        }

    def find_key(self, file):
        ignore_chars = []
        end_empty = [b'\x92', b'\x93', b'\xA0']
        end_with_content = {
            b'\xA1':        "number_1",
            b'\xA2':        "number_1",
            b'\xD1':        "number_2",
            b'\xD2':        "number_4",

            b'\xA3':        "text_0",
            b'\xA4':        "text_0",
            b'\xA5':        "text_0",
            b'\xA6':        "text_0",
            b'\xA7':        "text_0",
            b'\xDA':        "text_1",
            b'\xDC':        "text_1",
        }
        end_comp_trigger = b''
        end_empty_comp = []
        end_with_content_comp = {}

        return self.find_generic_key(file, ignore_chars, end_empty, end_with_content,
                                     end_comp_trigger, end_empty_comp, end_with_content_comp)

    def parse_number_1(self, file):
        ends = [b'\xA5', b'\xA8', b'\xA9', b'\xAA', b'\xAB', b'\xAC', b'\xAF']
        return self.parse_number(file, ends, expected_length=1)

    def parse_number_2(self, file):
        ends = [b'\xA8', b'\xA9', b'\xAA', b'\xAB', b'\xAC', ]
        return self.parse_number(file, ends, expected_length=2)

    def parse_number_4(self, file):
        ends = [b'\xA8']
        return self.parse_number(file, ends, expected_length=4)

    def parse_text_0(self, file):
        ends = [b'\xA0', b'\xAE', b'\xDA']
        return self.parse_text(file, ends)

    def parse_text_1(self, file):
        ends = [b'\xA0', b'\xA9', b'\xDA']
        expected_length = int.from_bytes(file.read(1) + file.read(1), "big")
        return self.parse_text(file, ends, expected_length=expected_length)


class MapPathListTableAsset(BaseMapAsset):
    HEADER_END_CHAR = b'\xDC'
    SEPARATOR_END_CHAR = b'\xA4'

    def __init__(self, file_path):
        self.file_path = file_path
        self.content_parsers = {
            "number_1": self.parse_number_1,
            "number_2": self.parse_number_2,
            "text_0": self.parse_text_0,
            "text_1": self.parse_text_1,
            "excess": self.do_excess_key,
            "empty": self.do_empty_contents
        }
        self.expected_keys = {
            "id": "number_1",
            "MapLabel": "excess",
            "MapPath": "excess",
            "PathDataPath": "excess"
        }

    def find_key(self, file):
        ignore_chars = []
        end_empty = [b'\xA0']
        end_with_content = {
            b'\xD1':        "number_2",

            b'\xA9':        "text_0",
            b'\xAC':        "text_0",
            b'\xDA':        "text_1"
        }
        end_comp_trigger = b''
        end_empty_comp = []
        end_with_content_comp = {}

        return self.find_generic_key(file, ignore_chars, end_empty, end_with_content,
                                     end_comp_trigger, end_empty_comp, end_with_content_comp)

    def parse_number_1(self, file):
        ends = [b'\xAA']
        return self.parse_number(file, ends, expected_length=1)

    def parse_number_2(self, file):
        ends = [b'\xAA']
        return self.parse_number(file, ends, expected_length=2)

    def parse_text_0(self, file):
        ends = [b'\xA9']
        return self.parse_text(file, ends)

    def parse_text_1(self, file):
        ends = [b'\xA9', b'\xAE']
        expected_length = int.from_bytes(file.read(1) + file.read(1), "big")
        return self.parse_text(file, ends, expected_length=expected_length)


class MapIconTypeAsset(BaseMapAsset):
    HEADER_END_CHAR = b'\xDC'
    SEPARATOR_END_CHAR = b'\xA4'

    def __init__(self, file_path):
        self.file_path = file_path
        self.content_parsers = {
            "number_1": self.parse_number_1,
            "number_2": self.parse_number_2,
            "excess": self.do_excess_key,
            "empty": self.do_empty_contents
        }
        self.expected_keys = {
            "id": "number_1",
            "texId": "number_1",
        }

    def find_key(self, file):
        ignore_chars = []
        end_empty = [b'\xA0']
        end_with_content = {
            b'\xD1':        "number_2",
        }
        end_comp_trigger = b''
        end_empty_comp = []
        end_with_content_comp = {}

        return self.find_generic_key(file, ignore_chars, end_empty, end_with_content,
                                     end_comp_trigger, end_empty_comp, end_with_content_comp)

    def parse_number_1(self, file):
        ends = [b'\x82', b'\xA7']
        return self.parse_number(file, ends, expected_length=1)

    def parse_number_2(self, file):
        ends = [b'\x82', b'\xA7']
        return self.parse_number(file, ends, expected_length=2)
