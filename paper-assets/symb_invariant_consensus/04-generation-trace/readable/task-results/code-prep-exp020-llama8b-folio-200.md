# code prep exp020 llama8b folio 200

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-exp020-llama8b-folio-200_20260517T081040_result.json`
- **Structured JSON:** [`3a01ab8e3e6867aca705.json`](../../sessions/3a/3a01ab8e3e6867aca705.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。

**报告：**

| 项目 | 状态 |
|------|------|
| FOLIO 全量数据 | `data/folio_full.json`，**204 题**，格式完整（含 premises_fol） |
| `data/empty.json` | 已存在（exp-019 已用） |
| 脚本 | `scripts/run_exp020_folio_200.sh` 已创建，`bash -n` 语法通过 |
| 评测入口 | `run_full_mvp.py`（同 exp-011），通过 `--math-data empty.json --no-proofwriter --folio-data folio_full.json` 只跑 FOLIO |
| 参数 | K=12, T=0.7, max-model-len=8192, max-tokens=4096, seed=42 |

数据就绪，脚本可直接 `bash scripts/run_exp020_folio_200.sh` 启动。等 exp-019 StrategyQA 结果出来后决定是否执行。

---
