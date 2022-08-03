## TextParser - CotC datamining

Tool dedicated to parsing the contents of the `\Game\Local\DataBase` game folder into a JSON format 
to facilitate readability and use in other tools.

### Usage

An installation of Python (script developed using 3.8.7) is required to run the program.

### Parseable files

Here is a list of the files for which parsing should work without problems:
- `\Game\Local\DataBase\Ad\`:
  - `AdBattleGroupList`
  - `AdBattleList`
  - `AdItemRewardGroupList`
  - `AdItemRewardList`
- `\Game\Local\DataBase\GameText\SystemText`:
  - `GameTextAchieve`
  - `GameTextCharacter`
  - `GameTextEnemy`
  - `GameTextEquip`
  - `GameTextFC`
  - `GameTextItem`
  - `GameTextMap`
  - `GameTextPC`
  - `GameTextQuest`
  - `GameTextQuestJP`
  - `GameTextSkill`
  - `GameTextStoryBook`
  - `GameTextSupport`
  - `GameTextUI`
- `\Game\Local\DataBase\Map\`:
  - `MapListTable`
  - `MapPathListTable`