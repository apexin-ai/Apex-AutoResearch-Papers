# diag olmo2 s123 mmlu exit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_olmo2-s123-mmlu-exit_20260520T113040_result.json`
- **Structured JSON:** [`ac5f181ffc968f504194.json`](../../sessions/ac/ac5f181ffc968f504194.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

OLMo-2 s123 MMLU eval **尚未退出**，仍在运行中：

- **PID 331098**: `evaluate.py` 运行中，elapsed 4m41s，当前在 d000_s123 的 MMLU 评估，进度 ~48% (6710/14042)
- **cuda:2**: 92% utilization, 16.7GB / 97.9GB 显存占用
- **结果文件**: 尚未生成（d000 还没跑完，后续还有 d005/d025/d050/d100）

脚本是串行跑 5 个 dosage 的，每个 ~8-10 分钟，预计总计还需 **40-50 分钟**完成全部评估。无需操作，等进程结束后再检查结果。

---
