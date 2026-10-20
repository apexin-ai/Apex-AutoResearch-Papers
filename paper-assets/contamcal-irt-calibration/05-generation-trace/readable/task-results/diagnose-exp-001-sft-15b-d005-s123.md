# diagnose exp 001 sft 15B d005 s123

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_sft_15B_d005_s123_20260515T083802_result.json`
- **Structured JSON:** [`8a2e2a35aa8e60ea3125.json`](../../sessions/8a/8a2e2a35aa8e60ea3125.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结论：**

- **根因**：`train_sft.py` 的 argparse 没有定义 `--gpu` 参数，训练命令传入 `--gpu 0` 被 argparse 拒绝，EXIT_CODE=2。脚本在参数解析阶段即崩溃，未进入训练。
- 数据文件、模型目录均正常，不是资源问题。
- ROADMAP 提到的 "--gpu 死代码" 实际更严重：参数根本未定义。

**修复**：从训练命令中删除 `--gpu 0`，改用 `CUDA_VISIBLE_DEVICES=0` 环境变量（也符合 C004 约束）。

诊断报告已写入 `artifacts/diag_exp_001_sft_15B_d005_s123.md`。

---
