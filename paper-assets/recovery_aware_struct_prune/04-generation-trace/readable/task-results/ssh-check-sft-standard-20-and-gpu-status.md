# ssh check sft standard 20 and gpu status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_sft_standard_20_and_gpu_status_20260520T194245_result.json`
- **Structured JSON:** [`dc10b5b81260834e689d.json`](../../sessions/dc/dc10b5b81260834e689d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### westd-29022

| GPU | 利用率 | 显存占用 | 进程 |
|-----|--------|----------|------|
| cuda:0 | **99%** | 29,619 / 97,887 MiB | eval_gsm8k_sft_standard_20 (PID 266847) |
| cuda:1 | 0% | 0 MiB | 空闲 |
| cuda:2 | 0% | 0 MiB | 空闲 |
| cuda:3 | 0% | 0 MiB | 空闲 |

**eval_gsm8k_sft_standard_20 进度：1181/1319 (89.5%)**
- 已运行 2h37m，当前 accuracy = **0.5896**（eos_rate=98.52%，avg_len=205）
- 剩余 138 条，约 ~2.5s/it，预计还需 ~6 分钟完成

### westb-23072

| GPU | 利用率 | 显存占用 | 进程 |
|-----|--------|----------|------|
| cuda:0 | 0% | 0 MiB | 空闲 |
| cuda:1 | 0% | 0 MiB | 空闲 |

无 python 训练/评估进程在运行。后台仅有 jupyter-lab、tensorboard、http.server 等基础服务，以及一个已完成的 `eval_unstructured_20` tmux session。

---
