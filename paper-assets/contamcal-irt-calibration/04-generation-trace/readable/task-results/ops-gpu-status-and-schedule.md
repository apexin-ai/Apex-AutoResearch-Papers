# ops gpu status and schedule

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-and-schedule_20260514T234044_result.json`
- **Structured JSON:** [`8f71931c6bd2994bc1a1.json`](../../sessions/8f/8f71931c6bd2994bc1a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动，正在 tokenizing 数据集（61% 完成，约 50826 samples）。

**启动确认**:
- **实验**: exp_001_sft_05B_d005_s123
- **PID**: 464137
- **GPU**: 1
- **模型**: Qwen2.5-0.5B
- **数据**: sft_dosage_005.jsonl (50826 samples)
- **配置**: lr=2e-4, lora_r=16, lora_alpha=32, bs=4, grad_accum=4, seed=123
- **输出**: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123`
- **日志**: `/root/runs/contamcal-irt-calibration/exp_001_sft_05B_d005_s123.log`

libnvJitLink warning 可忽略（不影响训练，bitsandbytes fallback 正常）。预计训练时长约 1-1.5 小时（0.5B 模型较小）。

---
