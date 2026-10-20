# ssh harvest random20 eval v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest_random20_eval_v2_20260521T063508_result.json`
- **Structured JSON:** [`9a9cfb944d0afa93b6e2.json`](../../sessions/9a/9a9cfb944d0afa93b6e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### eval_gsm8k_grpo_random_20_v2 (PID 322611) — **已完成**

| 指标 | 值 |
|------|-----|
| **GSM8K Accuracy** | **50.57% ± 1.38% (667/1319)** |
| EOS rate | 99.54% |
| Avg response length | 173 tokens |
| Model | `grpo_random_20/checkpoint-100` |
| Mode | greedy (temperature=0) |
| 结果文件 | `results/eval_checkpoint-100_greedy.json` |

### eval_gsm8k_grpo_random_20_v3 — **进程已死**

日志停在 539/1319（~41%），ps aux 中无对应进程。临近 525 样本时出现严重减速（99s/it），之后进程消失。GPU 1 内存 0 MiB 确认进程已退出。需要排查原因并重启。

### CKA-only 25 v3 (PID 322443) — **运行中**

- 进度：~500/1319（~38%），interim acc = **60.0%**
- GPU 0: 93% 利用率, 28933 MiB
- 预计还需 ~55 分钟完成

### GPU 状态 (westd-29022)

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 93% | 28933 MiB (CKA eval) |
| 1 | 0% | 0 MiB (空闲) |
| 2 | 0% | 0 MiB |
| 3 | 0% | 0 MiB |

v3 random_20 挂了，要查日志排查原因并重启吗？

---
