# code data prep 25068

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_data-prep-25068_20260518T074950_result.json`
- **Structured JSON:** [`c153671d343b957a6015.json`](../../sessions/c1/c153671d343b957a6015.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。数据文件总结：

| 文件 | 条目数 | 大小 | 说明 |
|------|--------|------|------|
| `folio_full.json` | 204 | 210 KB | FOLIO validation set, 含 FOL 标注 (True:72/False:63/Unknown:69) |
| `proofwriter_full.json` | 600 | 1.5 MB | ProofWriter OWA-D5, 含 `raw_logic_programs` (True/False/Unknown 各 200) |
| `proofwriter-OWA-D5-validation.jsonl` | 600 | 1.5 MB | 原始 JSONL 格式（兼容 exp-022 脚本） |
| `empty.json` | 0 | 0 KB | 空列表 |

数据源：
- FOLIO: [Yale-LILY/FOLIO GitHub](https://github.com/Yale-LILY/FOLIO) `data/v0.0/folio-validation.jsonl`
- ProofWriter: [Logic-LLM GitHub](https://github.com/teacherpeterpan/Logic-LLM) `outputs/logic_programs/ProofWriter_dev_gpt-4.json`（GPT-4 生成的 DSL 标注，600 题均衡分布）

---
