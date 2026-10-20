# analysis exp 001 sft 0pct 05B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_sft_0pct_05B_20260513T203448_result.json`
- **Structured JSON:** [`09668f2db510729515fe.json`](../../sessions/09/09668f2db510729515fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。汇总：

**exp_001_sft_0pct_05B — Qwen2.5-0.5B 0% dosage baseline**

| 指标 | 值 |
|------|-----|
| 状态 | 正常完成 (EXIT_CODE=0) |
| Final train loss | 1.5388 |
| Mean token accuracy | 65.69% |
| Total steps | 3,125 |
| Training time | 3,175.8s (~53 min) |
| Throughput | 15.7 samples/s |
| Checkpoint | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter/` (adapter_model.safetensors 33.6MB) |
| W&B | 未集成 |

Loss 在训练末期稳定在 1.46–1.60 范围，学习率已衰减至接近零，收敛正常。bitsandbytes 有一条 libnvJitLink 加载警告，不影响训练。

---
