# ops cqa1 gsm8k launch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-gsm8k-launch_20260519T211609_result.json`
- **Structured JSON:** [`9101d0987e64a4860b86.json`](../../sessions/91/9101d0987e64a4860b86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GSM8K eval 正常运行中。

**状态汇总：**

| 项目 | 状态 |
|------|------|
| s42 eval (MMLU+ARC) | 5/5 dosage 完成，每个 6 json ✓ |
| evaluate.py md5 | `001a9bc23f808c47d25ef9eaeecb81f1` ✓ (C009) |
| lora_alpha | d000=32, d100=32 ✓ (C006) |
| CUDA_VISIBLE_DEVICES | 显式设为 0 ✓ (C004) |
| GSM8K eval | **运行中**，tmux session `gsm8k_eval`，PID 285390 |
| GPU | RTX 4090D, 17699MiB/24564MiB, 100% util |
| 进度 | 2/165 batches, ~10.7s/batch |

**预估完成时间：** 165 batches × ~10.7s ≈ 29 分钟（d000）。d100 同样约 30 分钟（需重新加载 adapter，但 base model 可能被缓存）。两个 dosage 合计约 **60-70 分钟**。

日志路径：`/root/contamcal-irt-calibration/exp001/gsm8k_eval.log`

---
