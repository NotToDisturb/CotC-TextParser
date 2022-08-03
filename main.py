from handlers.ad import AdBattleGroupListAsset, AdItemRewardGroupListAsset, TimestampAsset
from handlers.gametext import NPCGameTextAsset, EventGameTextAsset, IdGameTextAsset, JPGameTextAsset
from handlers.map import MapListTableAsset, MapPathListTableAsset

import json
import os

asset_handlers = {
    "AdBattleGroupList": AdBattleGroupListAsset,
    "AdBattleList": TimestampAsset,
    "AdItemRewardGroupList": AdItemRewardGroupListAsset,
    "AdItemRewardList": TimestampAsset,
    "GameTextEvent": EventGameTextAsset,
    "GameTextNPC": NPCGameTextAsset,
    "GameTextAchieve": IdGameTextAsset,
    "GameTextCharacter": IdGameTextAsset,
    "GameTextEnemy": IdGameTextAsset,
    "GameTextEquip": IdGameTextAsset,
    "GameTextFC": IdGameTextAsset,             # Works but could use specific
    "GameTextItem": IdGameTextAsset,
    "GameTextMap": IdGameTextAsset,
    "GameTextPC": IdGameTextAsset,
    "GameTextQuest": IdGameTextAsset,          # Works but could use specific
    "GameTextQuestJP": JPGameTextAsset,             # Needs specific
    "GameTextSkill": IdGameTextAsset,
    "GameTextStoryBook": IdGameTextAsset,      # Works but could use specific
    "GameTextSupport": JPGameTextAsset,
    "GameTextUI": IdGameTextAsset,             # Works but could use specific
    "MapListTable": MapListTableAsset,
    "MapPathListTable": MapPathListTableAsset
}


def is_valid_data_list(file, finder_end_char):
    header = ""
    while (current_read := file.read(1)) != finder_end_char:
        if len(current_read) == 0:
            return False
        header += current_read.decode("utf-8", errors="ignore")
    return header == "m_DataList"


def find_line_separator(file, finder_end_char):
    last_read = b''
    while len((current_read := file.read(1))) > 0:
        if len(current_read) == 0:
            return None
        if current_read == finder_end_char:
            return last_read
        last_read = current_read


def parse(asset):
    result = []
    with open(asset.file_path, 'rb') as file:
        file.seek(asset.FILE_START)
        if not is_valid_data_list(file, asset.HEADER_END_CHAR):
            return {}, "INVALID DATA LIST"

        asset.line_separator = find_line_separator(file, asset.SEPARATOR_END_CHAR)
        if not asset.line_separator:
            return {}, "UNABLE TO FIND LINE SEPARATOR"

        current = {}
        last_read = b''
        while len((current_read := file.read(1))) > 0:
            if last_read + current_read == asset.KEY_START_CHARS:
                key, content_parser = asset.find_key(file)
                content = asset.content_parsers[content_parser](file)
                current[key] = content
            elif current_read == asset.line_separator and len(current.keys()) > 0:
                result.append(current)
                current = {}
            last_read = current_read
        result.append(current)
    return result, "SUCCESS"


def get_files(path):
    current_folders = [folder for folder in os.listdir(path) if os.path.isdir(os.path.join(path, folder))]
    all_files = [path + file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)) and file.endswith(".uexp")]
    for current_folder in current_folders:
        full_folder = os.path.join(path, current_folder)
        files = [os.path.join(full_folder, file) for file in os.listdir(full_folder)
                 if os.path.isfile(os.path.join(full_folder, file)) and file.endswith(".uexp")]
        for folder in os.listdir(full_folder):
            if os.path.isdir(os.path.join(full_folder, folder)):
                files.extend(get_files(os.path.join(full_folder, folder)))
        all_files.extend(files)
    return all_files


def dump_result(result, folder, text_file):
    os.makedirs(folder, exist_ok=True)
    with open(folder + text_file + ".json", "w+") as file:
        json.dump(result, file, indent=4)


def main():
    print("===========================================\n"
          "        TextParser - CotC datamining\n"
          "             built by Disturbo\n"
          "===========================================\n")
    base_folder = input("Enter the path to the DataBase folder: ")
    output_folder = input("Enter the path to the desired output folder: ")

    files = get_files(base_folder)
    for file in files:
        file_folder = os.path.split(file)[0].replace(base_folder, "")
        file_name = os.path.splitext(os.path.basename(file))[0]
        handler = asset_handlers.get(file_name, None)
        if handler:
            result, error_code = parse(handler(file))
            result = sorted(result, key=lambda x: int(x.get("id", "0") if x.get("id", "0") != "" else "0"))
            dump_result(result, output_folder + file_folder + "\\", file_name)
    print("FINISH")


if __name__ == "__main__":
    main()
