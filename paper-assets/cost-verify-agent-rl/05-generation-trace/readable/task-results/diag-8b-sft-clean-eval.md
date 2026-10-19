# diag 8b sft clean eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_8b_sft_clean_eval_20260519T104241_result.json`
- **Structured JSON:** [`ced983cf8ffc9460041e.json`](../../sessions/ce/ced983cf8ffc9460041e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已写入 `/root/cost-verify-agent-rl/artifacts/diag_8b_sft_clean_eval.md`。

**根因**: 启动命令用 `bash -c "..."` 双引号，`$TMPDIR` 被外层 shell 展开为空，`mkdir -p` 无参数报错，整个 `&&` 链中断，Python 从未执行。

**修复**: 把 `bash -c "..."` 改成 `bash -c '...'` 单引号，或直接硬编码 mkdir 路径。

---
