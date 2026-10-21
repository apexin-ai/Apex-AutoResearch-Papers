# code 14b rsft train launch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_14b-rsft-train-launch_20260520T191246_result.json`
- **Structured JSON:** [`1a3bf4937ef02e947fbd.json`](../../sessions/1a/1a3bf4937ef02e947fbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正常运行。

## 汇报

| 项目 | 值 |
|------|-----|
| **exp_id** | `plan017_14b_rsft_train` |
| **PID** | 48806 |
| **GPU** | cuda:0, 峰值显存 38GB / 96GB |
| **训练数据** | 3015 条 (CED top_k=1) |
| **Base model** | Qwen3-14B + SFT adapter (checkpoint-144) merge |
| **LoRA rank/alpha** | 64 / 128 |
| **Trainable params** | 256.9M / 15.0B (1.71%) |
| **Epochs** | 3 |
| **LR** | 2e-5 |
| **Batch size** | 1 × grad_accum 8 = effective 8 |
| **Gradient checkpointing** | Yes (硬编码) |
| **Total steps** | 1131 |
| **步速** | ~3.9s/step |
| **预估训练时间** | 1131 × 3.9s ≈ 4411s ≈ **~74 分钟 (1.2h)** |
| **预估完成时间** | ~2026-05-21 04:32 UTC |
| **Output dir** | `/root/autodl-tmp/rsft_output_14b` |
| **Log** | `~/runs/faith-evidence-ie/plan017_14b_rsft_train.log` |

不需要 QLoRA 量化，bf16 单卡 38GB 峰值，余量充足。

---
