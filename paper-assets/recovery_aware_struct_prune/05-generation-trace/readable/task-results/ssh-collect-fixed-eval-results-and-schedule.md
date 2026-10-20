# ssh collect fixed eval results and schedule

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_collect_fixed_eval_results_and_schedule_20260523T173116_result.json`
- **Structured JSON:** [`f08e1fa7d2d1ac11d74b.json`](../../sessions/f0/f08e1fa7d2d1ac11d74b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完整状态报告

### 1. GPU 状态

| 服务器 | GPU | 利用率 | 显存 | 任务 |
|--------|-----|--------|------|------|
| westd-32935 | 0 | 87% | 12.6G | eval sft_rasp_alpha1p0_20_fixed |
| westd-32935 | 1 | 99% | 17.1G | eval grpo_rasp_alpha1p0_20_fixed |
| westd-32935 | 2 | 98% | 18.8G | eval grpo_standard_20_fixed |
| westd-32935 | 3 | 91% | 17.1G | eval sft_standard_20_fixed |
| westb-23072 | 0 | 100% | 54.2G | grpo_random_20_retrain_v2 |
| westb-23072 | 1 | 98% | 16.6G | eval sft_cka_only_20_fixed_v2 |

全部 6 张 GPU 满载运行。

### 2. 已完成的 Fixed Eval 结果

**无。** 所有 fixed eval 仍在运行中，尚无 `_fixed.json` 结果文件产出。

### 3. 运行中的实验及进度

| 任务 | 服务器 | GPU | 进度 | 已用时间 | 预估剩余 |
|------|--------|-----|------|----------|----------|
| sft_rasp_alpha1p0_20_fixed | westd | 0 | **197/500 (39%)** | ~1h | ~1.5h |
| grpo_rasp_alpha1p0_20_fixed | westd | 1 | **159/500 (32%)** | ~1h45m | ~4h |
| grpo_standard_20_fixed | westd | 2 | **177/500 (35%)** | ~2h27m | ~5h |
| sft_standard_20_fixed | westd | 3 | **168/500 (34%)** | ~2h26m | ~5h |
| sft_cka_only_20_fixed_v2 | westb | 1 | **224/500 (45%)** | ~1h43m | ~2h |
| grpo_random_20_retrain_v2 | westb | 0 | **36/100 steps (36%)** | ~1h08m | ~2h09m |

最先完成的预计是 **sft_rasp_alpha1p0_20_fixed**（~1.5h 后）和 **sft_cka_only_20_fixed_v2**（~2h 后）。

### 4. 可用 Checkpoint 列表

**Dose-response (20% pruning, varying α):**
| Checkpoint | 大小 | 状态 |
|-----------|------|------|
| sft_rasp_alpha0p5_20 | 12G | ✓ |
| grpo_rasp_alpha0p5_20 | — | NOT_FOUND |
| sft_rasp_alpha2p0_20 | 12G | ✓ |
| grpo_rasp_alpha2p0_20 | 12G | ✓ |
| sft_rasp_alpha3p0_20 | — | NOT_FOUND |
| grpo_rasp_alpha3p0_20_v2 | — | NOT_FOUND |
| sft_alpha4_20 | 12G | ✓ |
| grpo_alpha4_20 | 12G | ✓ |

**25% pruning:**
| Checkpoint | 大小 | 状态 |
|-----------|------|------|
| sft_cka_only_25 | 11G | ✓ |
| grpo_cka_only_25 | 11G | ✓ |
| sft_standard_25 | 11G | ✓ |
| grpo_standard_25 | 11G | ✓ |

3 个 dose-response checkpoint 缺失（grpo_rasp_alpha0p5_20, sft_rasp_alpha3p0_20, grpo_rasp_alpha3p0_20_v2），25% checkpoint 全部就绪。

---
