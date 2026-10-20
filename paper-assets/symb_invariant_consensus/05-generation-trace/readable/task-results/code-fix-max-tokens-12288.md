# code fix max tokens 12288

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_max_tokens_12288_20260515T221754_result.json`
- **Structured JSON:** [`84d2316fe216d2222502.json`](../../sessions/84/84d2316fe216d2222502.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

**已 kill**: tmux session `sica_proofwriter30`

**修改汇总**（`default=16384` → `default=12288`）：

| 文件 | 行号 |
|------|------|
| `eval_folio.py` | L34 |
| `run_full_mvp.py` | L224 |
| `eval_math500.py` | L171 |

`eval_proofwriter.py` 原本已经是 `default=4096`，无需修改。

**全局确认**：项目中已无任何 `16384` 残留。旧结果文件已清理。

---
