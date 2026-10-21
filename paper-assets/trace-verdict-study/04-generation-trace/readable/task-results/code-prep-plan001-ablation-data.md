# code prep plan001 ablation data

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-plan001-ablation-data_20260515T015301_result.json`
- **Structured JSON:** [`5455d749925dae2db5be.json`](../../sessions/54/5455d749925dae2db5be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**统计报告：**

| | train | test |
|---|---|---|
| 行数 | 4720 | 1190 |
| actual/expected 移除 | 15,579 | 3,646 |
| fallback locals 移除 | 12,435 | 3,136 |
| 残留 actual= | 0 | 0 |

**产出文件：**
- `/root/autodl-tmp/trace-verdict-study-data/vota_no_actexp_train.jsonl` (4720 条)
- `/root/autodl-tmp/trace-verdict-study-data/vota_no_actexp_test.jsonl` (1190 条)
- 脚本：`/root/trace-verdict-study/scripts/prepare_ablation_data.py`

处理逻辑：`[ASSERT]` 行中 `| actual=X, expected=Y` 被截断，`| [fallback: full locals]` 行被整行移除。`[ERROR]`、`[LOOP]`、assertion 文本、代码部分全部保留。

---
