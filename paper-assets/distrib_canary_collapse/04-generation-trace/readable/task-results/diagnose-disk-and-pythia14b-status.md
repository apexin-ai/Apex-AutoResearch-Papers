# diagnose disk and pythia14b status

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_disk_and_pythia14b_status_20260517T191954_result.json`
- **Structured JSON:** [`22c18d8755cfa126d539.json`](../../sessions/22/22c18d8755cfa126d539.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 1. 进程状态

| 实验 | tmux session | GPU 进程 | 状态 |
|------|-------------|---------|------|
| pythia14b_wiki_a100_s42 | 无 | 无 | **已崩溃** (os error 28) |
| pythia410m_wiki_a100_s42 | 存活 | 无 | **已完成** (EXIT_CODE=0) |
| opt1b_wiki_a100_s42 | 存活 | 无 | **已完成** (EXIT_CODE=0) |
| pythia1b_c4_a100_s42 | — | — | **已完成** (EXIT_CODE=0) |

**GPU**：两块 RTX PRO 6000 (98GB) 均空闲，0% 利用率，0 MiB 显存。

### 2. 磁盘状态

| 挂载点 | 容量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| `/root/autodl-tmp/` | 250G | 250G | **484K** | **100%** |
| `/` | 30G | 8.5G | 22G | 29% |

**根因确认**：数据盘 100% 满，导致 pythia14b 在 gen_7 写 checkpoint 时崩溃。

### 3. Pythia-1.4B 实验进度

- **gen_0 ~ gen_6**：完成（每个 ~5.3G）
- **gen_7**：**不完整**（262M，正常应 ~5.3G），训练未完成，checkpoint 损坏
- **gen_8 ~ gen_10**：未开始
- 重启需要：清空 gen_7 → 从 gen_6 恢复继续

### 4. 空间占用 Top

| 目录 | 大小 |
|------|------|
| results/generalize/ | 135G |
| results/alpha_sweep/ | 86G |
| .hf_cache/ | 25G |
| data/ | 6.2G |
| **总计** | **~250G** |

### 5. 可安全清理的目录（已完成实验的中间 generation）

保留策略：每个已完成实验只保留 gen_0 + gen_10(final），删除 gen_1 ~ gen_9。

**generalize/ 已完成实验：**

| 实验 | 可删 gen | 单个大小 | 释放空间 |
|------|---------|---------|---------|
| opt1b_wiki_a100_s42 | gen_1~9 | 5.0G | **~45G** |
| pythia1b_c4_a100_s42 | gen_1~9 | 3.8G | **~34G** |
| pythia410m_wiki_a100_s42 | gen_1~9 | 1.6G | **~14G** |

**alpha_sweep/ 已完成实验（有大 checkpoint 的）：**

| 实验 | 可删 gen | 单个大小 | 释放空间 |
|------|---------|---------|---------|
| a000_s43 | gen_1~9 | 1.6G | ~14G |
| a000_s44 | gen_1~9 | 1.6G | ~14G |
| a050_s44 | gen_1~9 | 1.6G | ~14G |
| a075_s43 | gen_1~9 | 1.6G | ~14G |
| a075_s44 | gen_1~9 | 1.6G | ~14G |

其余 alpha_sweep 实验（a000_s42, a025_s43/s44, a050_s42/s43, a075_s42）中间 gen 仅 ~6.5M，清理收益忽略不计。

**pythia14b（未完成，特殊处理）**：
- gen_7 损坏，可删（释放 262M）
- gen_1~5 可删（5 × 5.3G = **~26.5G**），保留 gen_0 和 gen_6 用于恢复

### 汇总

| 类别 | 预估释放 |
|------|---------|
| generalize 已完成 3 个实验 gen_1~9 | **~93G** |
| alpha_sweep 5 个大实验 gen_1~9 | **~70G** |
| pythia14b gen_1~5 + gen_7 | **~27G** |
| **总计可释放** | **~190G** |

清理后磁盘使用率约 24%（~60G/250G），足够完成 pythia14b 剩余 gen_7~10（需 ~4 × 5.3G ≈ 21G）。

---
