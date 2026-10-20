# code fix argparse and submit 3B sft

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_argparse_and_submit_3B_sft_20260515T161148_result.json`
- **Structured JSON:** [`5a7a42ea00cfa8d5fbb0.json`](../../sessions/5a/5a7a42ea00cfa8d5fbb0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

**Step 1 修复**：train_sft.py 添加了缺失的 `--gpu` argparse 参数。`--lora-alpha` 传递链路本身无 bug（`args.lora_alpha` → `LoraConfig(lora_alpha=...)` 正确传递）。

**Step 2 验证**：`--help` 和 argparse 解析测试均通过，`lora_alpha=32` 正确。

**Step 3 实验提交**：
- **实验 1** `exp_001_sft_3B_d100_s42_a32` — cuda:4 正常训练中，`alpha=32` 已确认，4159 steps
- **实验 2** `exp_001_sft_3B_d025_s42_a32` — **提交失败（OOM）**。原因：cuda:5 已被 `exp001_d025_3B_v3`（PID 589763）占用 17.6GB。当前 6 块 GPU 全满，无法提交。

需要等 GPU 5 释放或指定其他 GPU 后重新提交实验 2。

---
