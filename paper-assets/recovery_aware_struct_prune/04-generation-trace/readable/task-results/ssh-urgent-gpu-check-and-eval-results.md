# ssh urgent gpu check and eval results

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_gpu_check_and_eval_results_20260523T194932_result.json`
- **Structured JSON:** [`e156ef651aeb74669ca9.json`](../../sessions/e1/e156ef651aeb74669ca9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-32935

### GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 91% | 16,833 / 97,887 MiB |
| 1 | 98% | 17,541 / 97,887 MiB |
| 2 | 99% | 19,251 / 97,887 MiB |
| 3 | 97% | 19,251 / 97,887 MiB |

### Eval 状态
| 任务 | GPU | 进度 | 结果文件 |
|------|-----|------|----------|
| eval_math500_sft_standard_25_fixed | cuda:0 | **17/500 (3.4%)** — 刚启动 ~22min | 未生成 |
| eval_math500_grpo_rasp_alpha1p0_20_fixed | cuda:1 | **375/500 (75%)** — 运行 ~4h | 未生成 |
| eval_math500_grpo_standard_20_fixed | cuda:2 | **340/500 (68%)** — 运行 ~4.75h | 未生成 |
| eval_math500_sft_standard_20_fixed | — | **无进程运行** — 日志停在 328/500，无结果文件 | 未生成 |

额外运行：`eval_math500_sft_rasp_alpha1p0_20_v2` 在 cuda:3（tmux session）

无 `train_grpo` 残留进程。

**注意**：`eval_math500_sft_standard_20_fixed` 异常 — 日志记录到 328/500 但进程已不存在，结果文件也未生成，疑似中途崩溃或被杀。

---

## westb-23072

### GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 99% | 16,555 / 97,887 MiB |
| 1 | 98% | 15,135 / 97,887 MiB |

### Eval 状态
| 任务 | GPU | 进度 | 结果文件 |
|------|-----|------|----------|
| eval_math500_grpo_cka_only_20_fixed | cuda:0 | **7/500 (1.4%)** — 刚启动 ~15min | 未生成 |
| eval_math500_sft_random_20_fixed | cuda:1 | **25/500 (5%)** — 刚启动 ~13min | 未生成 |

两个进程均正常运行中。

---

**总结**：6 个 eval 中 5 个正在跑，`sft_standard_20_fixed`（westd-32935）进程丢失需排查。grpo_rasp_alpha1p0_20_fixed 和 grpo_standard_20_fixed 预计 1-2h 内完成，其余刚启动需数小时。

---
