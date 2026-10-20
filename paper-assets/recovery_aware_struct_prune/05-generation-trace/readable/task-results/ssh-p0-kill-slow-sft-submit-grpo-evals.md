# ssh p0 kill slow sft submit grpo evals

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p0_kill_slow_sft_submit_grpo_evals_20260523T212835_result.json`
- **Structured JSON:** [`c4140b8fe1e7b58866bc.json`](../../sessions/c4/c4140b8fe1e7b58866bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

### 1. Kill 结果
- PID 167047 (sft_standard_20_fixed_v3, GPU 3) 已成功 kill

### 2. GPU 状态
| GPU | 状态 | 进程 |
|-----|------|------|
| 0 | 占用 | sft_standard_25_fixed_v2 (PID 166245) |
| 1 | **新提交** | eval_math500_grpo_rasp_alpha2p0_20_fixed (PID 168524) |
| 2 | 占用 | grpo_standard_20_fixed (PID 142486) |
| 3 | **新提交** | eval_math500_grpo_cka_only_25_fixed (PID 168451) |

### 3. 新提交的 eval
| GPU | Exp ID | Model Path | PID |
|-----|--------|-----------|-----|
| 3 | eval_math500_grpo_cka_only_25_fixed | `grpo_cka_only_25/` | 168451 |
| 1 | eval_math500_grpo_rasp_alpha2p0_20_fixed | `grpo_rasp_alpha2p0_20/` | 168524 |

GPU 1 选了 grpo_rasp_alpha2p0_20，因为 grpo_random_20 缺 model.safetensors，grpo_rasp_alpha0p5_20 目录不存在。

### 4. Checkpoint 存在情况
| Checkpoint | model.safetensors |
|-----------|:-:|
| grpo_cka_only_25 | ✓ |
| grpo_random_20 | ✗（只有 config，无权重）|
| grpo_rasp_alpha0p5_20 | ✗（目录不存在）|
| grpo_rasp_alpha2p0_20 | ✓ |
| grpo_rasp_alpha4p0_20 | ✗（目录不存在，但 grpo_alpha4_20 有）|
| grpo_unpruned | ✗（目录不存在）|

### 5. grpo_standard_20_fixed 进度
462/500 (92%)，还在跑，预计 ~15 分钟内完成。结果文件尚未生成（写完 500 题才写入）。

---
