# ops submit d025 sft cuda3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit-d025-sft-cuda3_20260516T024518_result.json`
- **Structured JSON:** [`984e8ee939b5c2a35b8e.json`](../../sessions/98/984e8ee939b5c2a35b8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

d025_a32_s42 SFT v3 训练已提交并运行中：

| 项目 | 值 |
|---|---|
| exp_id | exp_001_sft_3B_d025_s42_a32_v3 |
| GPU | cuda:3 (CUDA_VISIBLE_DEVICES=3) |
| tmux | sft_d025_a32_s42 |
| 参数 | lr=5e-5, lora_alpha=32, r=16, bs=1, grad_accum=16 |
| 数据 | 54133 samples |
| 总步数 | 3384 steps |
| 输出 | /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_a32_s42 |
| 日志确认 | alpha=32 ✓, 训练已开始 (0/3384) |
| Registry | RUNNING ✓ |

---
