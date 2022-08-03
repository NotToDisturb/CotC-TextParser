from assets import BaseAsset


class NPCGameTextAsset(BaseAsset):
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
            "PartVoiceID": "excess",
            "voiceId": "excess",
            "gametext": "excess"
        }

    def find_key(self, file):
        ignore_chars = [b'\x00']
        end_empty = [b'\xAD', b'\xA9']
        end_with_content = {
            b'\xD1':        "number_2",       # Length 2 for PartVoiceID, length 3 for id, ends in AD
            b'\xD2':        "number_4",       # Length 4, ends in AD
        }
        end_comp_trigger = b'\x9C'
        end_empty_comp = [b'\x00', b'\xA0']
        end_with_content_comp = {
            b'\xD1':    "number_2",
            b'\xD2':    "number_4",

            b'\xA2':    "text_0",     # Option 1
            b'\xA3':    "text_0",     # Option 2
            b'\xA4':    "text_0",     # Unknown
            b'\xA5':    "text_0",     # Unknown
            b'\xA6':    "text_0",     # Unknown
            b'\xA7':    "text_0",     # Unknown
            b'\xA8':    "text_0",     # Unknown
            b'\xA9':    "text_0",     # Unknown
            b'\xAA':    "text_0",     # Unknown
            b'\xAB':    "text_0",     # Unknown
            b'\xAC':    "text_0",     # Unknown
            b'\xAD':    "text_0",     # Unknown
            b'\xAE':    "text_0",     # Option menu
            b'\xAF':    "text_0",     # Unknown
            b'\xDA':    "text_1",     # Generic text
        }

        return self.find_generic_key(file, ignore_chars, end_empty, end_with_content,
                                     end_comp_trigger, end_empty_comp, end_with_content_comp)

    def parse_number_1(self, file):
        ends = [b'\xA9', b'\xAA', b'\xAD']
        return self.parse_number(file, ends, expected_length=1)

    def parse_number_2(self, file):
        ends = [b'\xA9', b'\xAA', b'\xAD']
        return self.parse_number(file, ends, expected_length=2)

    def parse_number_4(self, file):
        ends = [b'\xA9', b'\xAA', b'\xAD']
        return self.parse_number(file, ends, expected_length=4)

    def parse_text_0(self, file, expected_length=None):
        ends = [b'\xA0']
        return self.parse_text(file, ends, expected_length=expected_length)

    def parse_text_1(self, file):
        ends = [b'\xA0']
        expected_length = int.from_bytes(file.read(1) + file.read(1), "big")
        return self.parse_text(file, ends, expected_length=expected_length)


class EventGameTextAsset(BaseAsset):
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
            "voiceId": "number_1",
            "gametext": "text_0"
        }

    def find_key(self, file):
        ignore_chars = [b'\x00']
        end_empty = [b'\xAA', b'\xA9']
        end_with_content = {
            b'\xD1':        "number_2",       # Length 2 for PartVoiceID, length 3 for id, ends in AD
            b'\xD2':        "number_4",       # Length 4, ends in AD
        }
        end_comp_trigger = b'\x9C'
        end_empty_comp = [b'\x00', b'\xA0', b'\xA1']
        end_with_content_comp = {
            b'\xA2':    "text_0",     # Option 1
            b'\xA3':    "text_0",     # Option 2
            b'\xA4':    "text_0",     # Unknown
            b'\xA5':    "text_0",     # Unknown
            b'\xA6':    "text_0",     # Unknown
            b'\xA7':    "text_0",     # Unknown
            b'\xA8':    "text_0",     # Unknown
            b'\xA9':    "text_0",     # Unknown
            b'\xAA':    "text_0",     # Unknown
            b'\xAB':    "text_0",     # Unknown
            b'\xAC':    "text_0",     # Unknown
            b'\xAD':    "text_0",     # Unknown
            b'\xAE':    "text_0",     # Option menu
            b'\xAF':    "text_0",     # Unknown
            b'\xDA':    "text_1",     # Generic text
        }

        return self.find_generic_key(file, ignore_chars, end_empty, end_with_content,
                                     end_comp_trigger, end_empty_comp, end_with_content_comp)

    def parse_number_1(self, file):
        ends = [b'\xA9', b'\xAA']
        return self.parse_number(file, ends)

    def parse_number_2(self, file):
        ends = [b'\xA9', b'\xAA']
        return self.parse_number(file, ends)

    def parse_number_4(self, file):
        ends = [b'\xA9', b'\xAA']
        return self.parse_number(file, ends, expected_length=4)

    def parse_text_0(self, file):
        ends = [b'\xA0']
        return self.parse_text(file, ends)

    def parse_text_1(self, file):
        ends = [b'\xA0']
        expected_length = int.from_bytes(file.read(1) + file.read(1), "big")
        return self.parse_text(file, ends, expected_length=expected_length)


class JPGameTextAsset(BaseAsset):
    HEADER_END_CHAR = b'\xDC'
    SEPARATOR_END_CHAR = b'\xA4'

    def __init__(self, file_path):
        self.file_path = file_path
        self.content_parsers = {
            "number_4": self.parse_number_1,
            "number_1": self.parse_number_2,
            "number_2": self.parse_number_4,
            "text_0": self.parse_text_0,
            "text_1": self.parse_text_1,
            "excess": self.do_excess_key,
            "empty": self.do_empty_contents
        }
        self.expected_keys = {
            "id": "number_1",
            "nLine": "number_1",
            "nLineA": "number_1",
            "nLen": "number_1",
            "nLenA": "number_1",
            "gametext": "excess"
        }

    def find_key(self, file):
        ignore_chars = []
        end_empty = [b'\xA9', b'\xAA']
        end_with_content = {
            b'\xD1':        "number_2",       # Length 2 for PartVoiceID, length 3 for id, ends in AD
            b'\xD2':        "number_4",       # Length 4, ends in AD
        }
        end_comp_trigger = b'\x9C'
        end_empty_comp = [b'\x00', b'\xA0', b'\xA6', b'\xA7', b'\xA8']
        end_with_content_comp = {
            b'\xA2':    "text_0",     # Option 1
            b'\xA3':    "text_0",     # Option 2
            b'\xA4':    "text_0",     # Unknown
            b'\xA5':    "text_0",     # Unknown
            b'\xA6':    "text_0",     # Unknown
            b'\xA7':    "text_0",     # Unknown
            b'\xA8':    "text_0",     # Unknown
            b'\xA9':    "text_0",     # Unknown
            b'\xAA':    "text_0",     # Unknown
            b'\xAB':    "text_0",     # Unknown
            b'\xAC':    "text_0",     # Unknown
            b'\xAD':    "text_0",     # Unknown
            b'\xAE':    "text_0",     # Option menu
            b'\xAF':    "text_0",     # Unknown
            b'\xDA':    "text_1",     # Generic text
        }

        return self.find_generic_key(file, ignore_chars, end_empty, end_with_content,
                                     end_comp_trigger, end_empty_comp, end_with_content_comp)

    def parse_number_1(self, file):
        ends = [b'\xA6', b'\xA7', b'\xA8', b'\xA9', b'\xAA']
        return self.parse_number(file, ends, expected_length=1)

    def parse_number_2(self, file):
        ends = [b'\xA6', b'\xA7', b'\xA8', b'\xA9', b'\xAA']
        return self.parse_number(file, ends, expected_length=2)

    def parse_number_4(self, file):
        ends = [b'\xA6', b'\xA7', b'\xA8', b'\xA9', b'\xAA']
        return self.parse_number(file, ends, expected_length=4)

    def parse_text_0(self, file):
        ends = [b'\xA0']
        return self.parse_text(file, ends)

    def parse_text_1(self, file):
        ends = [b'\xA0']
        expected_length = int.from_bytes(file.read(1) + file.read(1), "big")
        return self.parse_text(file, ends, expected_length=expected_length)


class IdGameTextAsset(BaseAsset):
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
            "voiceId": "number_1",
            "gametext": "text_0"
        }

    def find_key(self, file):
        ignore_chars = [b'\x00']
        end_empty = [b'\xAA', b'\xA9']
        end_with_content = {
            b'\xD1':        "number_2",
            b'\xD2':        "number_4",
        }
        end_comp_trigger = b'\x9C'
        end_empty_comp = [b'\x00', b'\xA0', b'\xA1']
        end_with_content_comp = {
            b'\xA2':    "text_0",     # Option 1
            b'\xA3':    "text_0",     # Option 2
            b'\xA4':    "text_0",     # Unknown
            b'\xA5':    "text_0",     # Unknown
            b'\xA6':    "text_0",     # Unknown
            b'\xA7':    "text_0",     # Unknown
            b'\xA8':    "text_0",     # Unknown
            b'\xA9':    "text_0",     # Unknown
            b'\xAA':    "text_0",     # Unknown
            b'\xAB':    "text_0",     # Unknown
            b'\xAC':    "text_0",     # Unknown
            b'\xAD':    "text_0",     # Unknown
            b'\xAE':    "text_0",     # Option menu
            b'\xAF':    "text_0",     # Unknown
            b'\xDA':    "text_1",     # Generic text
        }

        return self.find_generic_key(file, ignore_chars, end_empty, end_with_content,
                                     end_comp_trigger, end_empty_comp, end_with_content_comp)

    def parse_number_1(self, file):
        ends = []
        return self.parse_number(file, ends, expected_length=1)

    def parse_number_2(self, file):
        ends = []
        return self.parse_number(file, ends, expected_length=2)

    def parse_number_4(self, file):
        ends = []
        return self.parse_number(file, ends, expected_length=4)

    def parse_text_0(self, file):
        ends = [b'\xA0']
        return self.parse_text(file, ends)

    def parse_text_1(self, file):
        ends = [b'\xA0']
        expected_length = int.from_bytes(file.read(1) + file.read(1), "big")
        return self.parse_text(file, ends, expected_length=expected_length)
