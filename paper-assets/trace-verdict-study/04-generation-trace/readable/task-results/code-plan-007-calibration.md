# code plan 007 calibration

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_007_calibration_20260515T113221_result.json`
- **Structured JSON:** [`3fdebd468227b7f2c455.json`](../../sessions/3f/3fdebd468227b7f2c455.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

import 和参数解析都正常。

脚本已部署到 `/root/trace-verdict-study/eval/calibration.py`，功能：

- **单条件模式**：`python eval/calibration.py --condition vota --gpu 0`（自动查找 checkpoint 和 test data）
- **批量模式**：`python eval/calibration.py --batch --conditions vota,no_trace,full_trace,label_only,exception_only --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/calibration/`

核心逻辑：对每个样本做 forward pass，取最后 token 对 pass(6385)/fail(18403) 的 softmax 概率，然后计算 ECE（10 bins, 0.5→1.0）、Brier score、reliability diagram 数据、confidence 分布。批量模式下每跑完一个 condition 会释放 GPU 显存再加载下一个。

---
