# ops cqa1 d100 final check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-d100-final-check_20260519T192813_result.json`
- **Structured JSON:** [`5472215deb00febf27a1.json`](../../sessions/54/5472215deb00febf27a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

s42 eval 已启动确认：

- **tmux session**: `eval_s42`（created 03:42:42）
- **PID**: 275364，正在跑 d000_s42
- **GPU 0**: 14928 MiB / 24564 MiB，CUDA_VISIBLE_DEVICES=0（脚本内设置）
- **进度**: 已开始 d000_s42 → d005 → d025 → d050 → d100，每个 ~17 分钟，全部 ~85 分钟（预计 ~05:08 完成）

**d100 s123 新结果（aligned mc-format）**: MMLU = **66.59%**, ARC = **84.73%**

对比旧结果（non-aligned）：MMLU 70.66% → 66.59%（-4.07pp），ARC 89.68% → 84.73%（-4.95pp）。aligned 格式下分数显著下降，说明旧格式存在评估膨胀。

---
