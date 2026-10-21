# gpu status check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu-status-check_20260515T161813_result.json`
- **Structured JSON:** [`98489ae837fd636fe1e0.json`](../../sessions/98/98489ae837fd636fe1e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## autodl-5090 服务器状态汇总

### GPU 状态（4× RTX 5090 32GB）

| GPU | 显存占用 | GPU 利用率 | 状态 |
|-----|---------|-----------|------|
| cuda:0 | 2 MiB / 32607 MiB | 0% | **空闲** |
| cuda:1 | 2 MiB / 32607 MiB | 0% | **空闲** |
| cuda:2 | 2 MiB / 32607 MiB | 0% | **空闲** |
| cuda:3 | 2 MiB / 32607 MiB | 0% | **空闲** |

### 训练进程

**无活跃训练进程。** 只有系统服务在运行（supervisord、sshd、tensorboard、jupyter-lab、autopanel）。

有一个 tmux session `exp_001_n16_seed456` 残留，但其中的 Python 进程已结束（ps 中无对应 python 进程）。

### 实验输出目录

| 实验 | 最后修改时间 | 文件 | 状态 |
|------|------------|------|------|
| `exp_017_llama_conll_n8_t07` | May 15 23:38 | report.json (1.7K) + samples.jsonl (9.1M) | **已完成** |
| `exp_lp_scierc_t07` | May 15 23:40 | report.json (1.7K) + samples.jsonl (3.7M) | **已完成** |
| `exp_re_scierc_seed123` | May 15 23:45 | report.json (3.4K) + samples.jsonl (3.6M) | **已完成** |
| `exp_re_scierc_seed456` | May 15 23:45 | report.json (3.4K) + samples.jsonl (3.6M) | **已完成** |

### 磁盘

数据盘 `/root/autodl-tmp/`: 159G / 250G 已用（64%），剩余 92G。

**结论**：4 张 GPU 全部空闲，4 个实验均已完成（输出文件齐全），服务器可用于新任务。

---
