# ssh check 19828 gpu

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-19828-gpu_20260519T131205_result.json`
- **Structured JSON:** [`3b38f7ad7e23556871d2.json`](../../sessions/3b/3b38f7ad7e23556871d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总

### nvidia-smi

| GPU | 型号 | 温度 | 功耗 | 显存占用 | GPU利用率 | 进程 PID |
|-----|------|------|------|----------|----------|----------|
| cuda:0 | RTX PRO 6000 Black (96GB) | 73°C | 494W/600W | 62679/97887 MiB (64%) | 100% | 407864 |
| cuda:1 | RTX PRO 6000 Black (96GB) | 71°C | 504W/600W | 64417/97887 MiB (66%) | 99% | 408266 |

### 进程状态

4 个进程全部存活，已运行约 12h50m：

| 进程 | PID | 状态 | 运行时间 | 说明 |
|------|-----|------|----------|------|
| bash wrapper (gpt2m) | 407859 | Ss+ | 12:51:16 | 父进程 |
| **python (gpt2m s43)** | **407864** | **Sl** | **12:51:16** | cuda:0 训练进程 |
| bash wrapper (smollm3) | 408261 | Ss+ | 12:47:57 | 父进程 |
| **python (smollm3 s42)** | **408266** | **Rl** | **12:47:57** | cuda:1 训练进程 |

### 训练进度

| 实验 | 当前 Gen | Step 进度 | 速度 | 剩余 Gen | 预计完成 |
|------|---------|-----------|------|---------|---------|
| **gen_gpt2m_a100_s43** | gen 9/10 (最后一个) | 3383/5000 (68%) | 1.12 it/s | 0 | ~24 min 完成当前 gen → **实验即将结束** |
| **smollm3_3b_wiki_a100_s42_v3** | gen 7/10 | 3498/5000 (70%) | 1.18 it/s | 2 (gen_8, gen_9) | ~22 min 完成当前 gen + 2 gen × ~71 min ≈ **~2.5h 完成全部** |

GPT-2m 实验约半小时内跑完，SmolLM3-3B 还需约 2.5 小时。两张卡满载运行正常。

---
