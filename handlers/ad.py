from assets import BaseAsset


class AdBattleGroupListAsset(BaseAsset):
    HEADER_END_CHAR = b'\x9D'
    SEPARATOR_END_CHAR = b'\xA4'

    def __init__(self, file_path):
        self.file_path = file_path
        self.content_parsers = {
            "number_1": self.parse_number_1,
            "number_2": self.parse_number_2,
            "number_4": self.parse_number_4,
            "excess": self.do_excess_key,
            "empty": self.do_empty_contents
        }
        self.expected_keys = {
            "id": "excess",
            "ad_battle_list_id": "excess",
            "lv_min": "number_1",
            "lv_max": "number_1",
            "group_id": "excess",
            "rate": "number_1",
            "battle_map_id": "excess"
        }

    def find_key(self, file):
        ignore_chars = [b'\x00']
        end_empty = [b'\xAA', b'\xA9']
        end_with_content = {
            b'\xD1':        "number_2",
            b'\xD2':        "number_4",
        }
        end_comp_trigger = b''
        end_empty_comp = []
        end_with_content_comp = {}

        return self.find_generic_key(file, ignore_chars, end_empty, end_with_content,
                                     end_comp_trigger, end_empty_comp, end_with_content_comp)

    def parse_number_1(self, file):
        ends = [b'\xA4', b'\xA6', b'\xA8', b'\xAA', b'\xAF', b'\xDA']
        return self.parse_number(file, ends, expected_length=1)

    def parse_number_2(self, file):
        ends = [b'\xA4', b'\xA6', b'\xA8', b'\xAA', b'\xAF', b'\xDA']
        return self.parse_number(file, ends, expected_length=2)

    def parse_number_4(self, file):
        ends = [b'\xA4', b'\xA6', b'\xA8', b'\xAA', b'\xAF', b'\xDA']
        return self.parse_number(file, ends, expected_length=4)


class AdItemRewardGroupListAsset(BaseAsset):
    HEADER_END_CHAR = b'\x9B'
    SEPARATOR_END_CHAR = b'\xA4'

    def __init__(self, file_path):
        self.file_path = file_path
        self.content_parsers = {
            "number_1": self.parse_number_1,
            "number_2": self.parse_number_2,
            "number_4": self.parse_number_4,
            "excess": self.do_excess_key,
            "empty": self.do_empty_contents
        }
        self.expected_keys = {
            "id": "excess",
            "ad_itemreward_list_id": "excess",
            "RewardType": "excess",
            "RewardItemId": "excess",
            "RewardNum": "excess",
            "rate": "number_1"
        }

    def find_key(self, file):
        ignore_chars = [b'\x00']
        end_empty = [b'\xAA', b'\xA9']
        end_with_content = {
            b'\xD1':        "number_2",
            b'\xD2':        "number_4",
        }
        end_comp_trigger = b'\x94'
        end_empty_comp = [b'\x00', b'\x64']
        end_with_content_comp = {
            b'\xD1':        "number_2",
            b'\xD2':        "number_4",
        }

        return self.find_generic_key(file, ignore_chars, end_empty, end_with_content,
                                     end_comp_trigger, end_empty_comp, end_with_content_comp)

    def parse_number_1(self, file):
        ends = [b'\xA6', b'\xAB', b'\xAC', b'\xAE', b'\xDA']
        return self.parse_number(file, ends, expected_length=1)

    def parse_number_2(self, file):
        ends = [b'\xA6', b'\xAB', b'\xAC', b'\xAE', b'\xDA']
        return self.parse_number(file, ends, expected_length=2)

    def parse_number_4(self, file):
        ends = [b'\xA6', b'\xAB', b'\xAC', b'\xAE', b'\xDA']
        return self.parse_number(file, ends, expected_length=4)


class TimestampAsset(BaseAsset):
    HEADER_END_CHAR = b'\x91'
    SEPARATOR_END_CHAR = b'\xA4'

    def __init__(self, file_path):
        self.file_path = file_path
        self.content_parsers = {
            "number_1": self.parse_number_1,
            "number_2": self.parse_number_2,
            "number_4": self.parse_number_4,
            "excess": self.do_excess_key,
            "empty": self.do_empty_contents
        }
        self.expected_keys = {
            "id": "excess",
            "begin_timestamp": "excess",
            "end_timestamp": "excess",
            "view_limit": "number_1"
        }

    def find_key(self, file):
        ignore_chars = [b'\x00']
        end_empty = [b'\xA9', b'\xAA', b'\xAC']
        end_with_content = {
            b'\xD1':        "number_1",
            b'\xD2':        "number_2",
        }
        end_comp_trigger = b''
        end_empty_comp = []
        end_with_content_comp = {}

        return self.find_generic_key(file, ignore_chars, end_empty, end_with_content,
                                     end_comp_trigger, end_empty_comp, end_with_content_comp)

    def parse_number_1(self, file):
        ends = [b'\x0A', b'\xAC', b'\xAD', b'\xAF']
        return self.parse_number(file, ends, expected_length=1)

    def parse_number_2(self, file):
        ends = [b'\x0A', b'\xAC', b'\xAD', b'\xAF']
        return self.parse_number(file, ends, expected_length=2)

    def parse_number_4(self, file):
        ends = [b'\x0A', b'\xAC', b'\xAD', b'\xAF']
        return self.parse_number(file, ends, expected_length=4)
