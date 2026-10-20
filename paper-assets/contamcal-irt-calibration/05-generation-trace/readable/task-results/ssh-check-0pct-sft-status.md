# ssh check 0pct sft status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-0pct-sft-status_20260513T195052_result.json`
- **Structured JSON:** [`10fafe6235fc43165503.json`](../../sessions/10/10fafe6235fc43165503.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

0% SFT 训练状态:

| GPU | 模型 | 状态 | PID | 进度 | 速度 | 预计剩余 |
|-----|------|------|-----|------|------|---------|
| GPU 3 | Qwen2.5-0.5B | **RUNNING** | 208938 (父 208933) | 788/3125 (25%) | ~1.0 it/s | ~37 min |
| GPU 4 | Qwen2.5-1.5B | **RUNNING** | 210121 (父 210116) | 319/3125 (10%) | ~2.1 s/it | ~1h38m |
| GPU 5 | Qwen2.5-3B | **RUNNING** | 210671 | 93/3125 (3%) | ~3.9 s/it | ~3h15m |

- 训练脚本: 存在 (`/root/contamcal-irt-calibration/exp001/train_sft.py`)
- 训练数据: 存在 (`sft_dosage_000.jsonl`, 88MB, 50000 samples)
- bitsandbytes 有 `libnvJitLink.so.13` 警告，但不影响训练（未使用量化）
- Loss 正常下降（0.5B 已从 ~1.7 降到 ~1.5，token accuracy ~0.67）

三个任务全部正常运行中。

---
