# audit final data check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_final-data-check_20260524T043110_result.json`
- **Structured JSON:** [`e519c6cca9ae14ff1198.json`](../../sessions/e5/e519c6cca9ae14ff1198.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心结论：

**前轮 5 项修复全部确认正确。** ~350 个定量数字交叉验证，发现 **1 处微小不一致**：

- experiments.tex 正文 "loop\_only spans **8.57pp**" → 根据 cross\_model 表计算应为 86.05−77.40=**8.65pp**（差 0.08pp），建议修正

其余所有数字——包括全部表格 accuracy/mean/std/delta、abstract 声明、inline 引用——均通过算术验证或 registry 交叉比对。约 70 个来自未注册实验（tail truncation、calibration、zero-shot、GPT-4o 等）的数值虽无法追溯到 registry，但在论文内部完全自洽。

报告已写入 `artifacts/final_data_audit_20260524.md`。

---
