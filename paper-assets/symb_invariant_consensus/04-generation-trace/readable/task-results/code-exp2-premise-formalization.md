# code exp2 premise formalization

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp2-premise-formalization_20260518T180831_result.json`
- **Structured JSON:** [`854e599f1cc2ed935f7f.json`](../../sessions/85/854e599f1cc2ed935f7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。Dry-run 验证报告：

| 检查项 | 状态 |
|--------|------|
| python3 可用 | PASS |
| z3 import (v4.15.4) | PASS |
| openai import | PASS |
| 数据文件 `folio_full.json` (215KB) | PASS |
| 模型路径 `/root/autodl-tmp/models/Qwen2.5-14B-Instruct/` | PASS |
| `parse_formula` (Implies/Or/Xor/Fact/Complex) | PASS (5/5) |
| `check_entailment` (True/False/Unknown/Inconsistent) | PASS (4/4) |
| `parse_problem` (前3条数据解析) | PASS (均解析出6条premises+conclusion) |
| 模块 import | PASS |

**产出文件：**
- `/root/symb_invariant_consensus/premise_formalization.py` — 主脚本，K=12 独立 formalization + majority vote
- `/root/symb_invariant_consensus/scripts/run_premise_formalization.sh` — 启动脚本（自动启动 vLLM，用法: `bash scripts/run_premise_formalization.sh [PORT] [GPU]`）

LLM 调用部分未测试（需要 vLLM server 运行中）。启动实验时运行 `bash scripts/run_premise_formalization.sh` 即可。

---
