# code llama eval restart

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_eval_restart_20260516T150044_result.json`
- **Structured JSON:** [`cf79760a78f790145e34.json`](../../sessions/cf/cf79760a78f790145e34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

提交成功。

## 报告

**GPU 状态：**
| GPU | 状态 | 显存占用 | 用途 |
|-----|------|----------|------|
| 0 | 在用 | 7213/24564 MiB | python 进程 |
| 1 | ~~空闲~~ → 已分配 | 0 → eval | Llama eval v2 |
| 2 | 在用 | 1473/24564 MiB | python3 进程 |
| 3 | 空闲 | 0/24564 MiB | 可用 |
| 4 | 在用 | 8313/24564 MiB | python3 (85% util) |
| 5 | 在用 | 3627/24564 MiB | python3 (54% util) |

**已提交：**
- exp_id: `exp_001_eval_llama32_3B_d000_s42_v2`
- GPU: cuda:1
- Checkpoint: `/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d000_s42/merged` (lora_alpha=32 ✓)
- 模式: aligned (mc-format aligned)
- Benchmarks: mmlu, gsm8k, arc_challenge, humaneval
- 日志: `~/runs/contamcal-irt-calibration/exp_001_eval_llama32_3B_d000_s42_v2.log`

**Registry 中 RUNNING 实验（4个）：**
1. exp_001_eval_05B_instruct
2. exp_001_eval_15B_instruct
3. exp_006_pooled_irt_rrf_n25_v2
4. exp_006_mmlu_domain_gamma_n24_v4

**剩余空闲 GPU：** cuda:3 可用于其他任务。

---
