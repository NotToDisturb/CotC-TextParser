import os


class BaseAsset:
    FILE_START = int("0x27", base=16)
    KEY_START_CHARS = b'm_'
    line_separator = b''
    expected_keys = {}
    debug = False

    def decode(self, value):
        decode = None
        try:
            decode = value.decode("utf-8")
        except UnicodeDecodeError:
            pass
        return decode

    def within_expected_keys(self, current_key):
        return any(key.startswith(current_key) for key in self.expected_keys.keys())

    def find_generic_key(self, file, ignore_chars, end_empty, end_with_content,
                         end_comp_trigger, end_empty_comp, end_with_content_comp):
        last_read = b''
        key = ""
        while len((current_read := file.read(1))) > 0:
            with_content = end_with_content.get(current_read, None)
            with_content_comp = end_with_content_comp.get(current_read, None)
            if with_content_comp and last_read == end_comp_trigger:
                return key, with_content_comp
            elif with_content:
                return key, with_content
            elif current_read in end_empty or \
                    (last_read == end_comp_trigger and current_read in end_empty_comp):
                return key, "empty"
            elif current_read not in ignore_chars and current_read != end_comp_trigger:
                decoded = self.decode(current_read)
                if not decoded or not self.within_expected_keys(key + decoded):
                    file.seek(-1, os.SEEK_CUR)
                    return key, self.expected_keys[key]
                key += decoded
            last_read = current_read
        return key, None

    def parse_number(self, file, ends, expected_length=None):
        content = b''
        while len((current_read := file.read(1))) > 0:
            if current_read in ends and not expected_length:
                return str(int.from_bytes(content, "big"))
            elif len(content) == expected_length:
                file.seek(-1, os.SEEK_CUR)
                return str(int.from_bytes(content, "big"))
            else:
                content += current_read
        return None

    def parse_text(self, file, ends, expected_length=None):
        content = b''
        end_char_count = 0
        while len((current_read := file.read(1))) > 0:
            if current_read in ends and not expected_length:
                end_char_count += 1
                if end_char_count == 11:
                    return content.decode("utf8", errors="ignore")
            else:
                end_char_count = 0
                content += current_read
            if len(content) == expected_length:
                return content.decode("utf8", errors="ignore")
        return None

    def do_excess_key(self, file):
        return "read key exceeded"

    def do_empty_contents(self, file):
        return ""

