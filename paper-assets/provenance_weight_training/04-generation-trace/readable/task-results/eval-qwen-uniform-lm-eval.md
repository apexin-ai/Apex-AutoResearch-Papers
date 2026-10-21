# eval qwen uniform lm eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_qwen_uniform_lm_eval_20260517T144729_result.json`
- **Structured JSON:** [`ffbd392424e9117a8301.json`](../../sessions/ff/ffbd392424e9117a8301.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**westd-41312 上不存在 Qwen3-0.6B uniform_seed42 checkpoint。**

现有模型：
| 目录名 | 基座模型 | 加权方式 | 有 final? |
|---------|----------|----------|-----------|
| `llama3b_uniform_seed42` | LlamaForCausalLM | uniform | Yes |
| `llama3b_adaptive_seed42` | LlamaForCausalLM | adaptive | Yes |
| `batchsize16_nmin8_seed42` | Qwen3-0.6B | adaptive | Yes |
| `grid_b0_2_seed42` | Qwen3-0.6B | grid (b=0.2) | Yes |
| `grid_b0_3_seed456` | Qwen3-0.6B | grid (b=0.3) | No (训练中?) |
| `hybrid_rho04_seed42` | Qwen3-0.6B | adaptive | Yes |
| `hybrid_rho06_seed42` | Qwen3-0.6B | adaptive | Yes |

已有 Qwen eval 输出目录：`qwen_adaptive_*` 和 `qwen_base_*`（无 `qwen_uniform_*`）。

Qwen3-0.6B 的 uniform weighting continued pretraining 似乎还没有跑过。需要先训练这个模型，还是评估其他已有的 checkpoint？

---
