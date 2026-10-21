# code maven data prep

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_maven-data-prep_20260515T032102_result.json`
- **Structured JSON:** [`a4545ccca3afee6cc6bb.json`](../../sessions/a4/a4545ccca3afee6cc6bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件全部完成并注册：

| 文件 | 路径 | 说明 |
|------|------|------|
| `maven_event_types.json` | `artifacts/maven_code/configs/` | 168 types，`{type_name: description}` 格式，与 `few_nerd_types.json` 一致 |
| `preprocess_maven.py` | `artifacts/maven_code/src/` | JSONL → parquet，每个文档一行，输出 `text` + `entities[{text, type}]` |
| `download_maven.sh` | `artifacts/maven_code/src/` | 从 Google Drive 下载 train/valid/test.jsonl，带完整性验证 |

关键细节：
- 168 event types 从 [THU-KEG/MAVEN-dataset](https://github.com/THU-KEG/MAVEN-dataset) 官方 baseline 代码 `utils_ee.py` 提取，type_id 1-168 完整对应
- 预处理脚本从 token offset 重建 trigger text（比直接用 `trigger_word` 字段更准确）
- 支持 `--split all` 一次处理全部 split
- Python 语法和 shell 语法均验证通过

Sources:
- [THU-KEG/MAVEN-dataset](https://github.com/THU-KEG/MAVEN-dataset)
- [DataFormat.md](https://github.com/THU-KEG/MAVEN-dataset/blob/main/DataFormat.md)

---
