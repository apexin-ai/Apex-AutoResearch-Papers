# ssh fix westd0 and collect results

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_westd0_and_collect_results_20260523T192652_result.json`
- **Structured JSON:** [`c7ac8ac59e74f1439369.json`](../../sessions/c7/c7ac8ac59e74f1439369.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd:0 异常
原因: **不是 zombie**。PID 157383 已死，但 cuda:0 被 **PID 156633** 占用 — 这是一个**新启动的** `grpo_standard_25_retrain_v2` 训练进程（`train_grpo_v5.py`），已运行 22 分钟，进度 **41/100 steps (41%)**，91% GPU util。
处理: **未 kill** — 这是活跃训练进程，不是残留。需要你确认是否要保留。
cuda:0 现在: 占用 55833MiB / 97887MiB

## westd eval 状态
| 任务 | GPU | PID | 进度 | 状态 |
|------|-----|-----|------|------|
| grpo_standard_20_fixed | cuda:2 | 142486 | **316/500 (63%)** | 运行中 4h23m |
| sft_standard_20_fixed | cuda:3 | 142647 | **304/500 (61%)** | 运行中 4h23m |
| grpo_rasp_alpha1p0_20_fixed | cuda:1 | 145176 | **333/500 (67%)** | 运行中 3h41m |

结果文件均未生成，预计还需 ~2-3 小时。

## westb 状态
- sft_cka_only_20_fixed_v2: PID 306963，**492/500 (98%)**，即将完成（~10 分钟内）
- GPU 0: **空闲** (0 MiB, 0%)
- GPU 1: 17039 MiB, 99% (eval 占用)

---

**需确认**: westd cuda:0 上的 PID 156633 (grpo_standard_25_retrain_v2) 是谁启动的？要保留还是 kill？

---
