# ssh 7b inference monitor and process

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_7b-inference-monitor-and-process_20260520T040321_result.json`
- **Structured JSON:** [`2183814ff3c88300e4ef.json`](../../sessions/21/2183814ff3c88300e4ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

## 状态汇报

### 1. 各 seed 状态

| Seed | 服务器 | 状态 | 进度 | 备注 |
|------|--------|------|------|------|
| **seed42** | 5090-c (cuda:2) | **已完成** | 37648/37648 (100%) | samples.jsonl 675MB, 完成于 11:58 |
| **seed123** | 5090-c (cuda:0,1?) | 进行中 | 0% (无输出文件) | PID 155276, 已运行 5h44m, 是 seed42 pipeline 的后续任务 |
| **seed123** | 5090-b (cuda:0) | 进行中 | 0% (无输出文件) | PID 164579, 已运行 1h14m |
| **seed456** | 5090-b (cuda:1) | 进行中 | 0% (无输出文件) | PID 165186, 已运行 1h13m |

**注意**: seed123 在 5090-c 和 5090-b **同时运行**，存在重复。5090-c 上的 seed123 是 PID 71837（seed42 pipeline bash 脚本）的子进程，pipeline 完成 seed42 后自动启动了 seed123。5090-b 上的 seed123/456 是另外启动的。两边写到各自本地 filesystem，不会冲突但浪费 GPU。

### 2. seed42 compute_signals 结果

**32565 有效实例**（过滤掉 5083 gold-empty）

**Signal correlations (Spearman ρ vs greedy F1)**:
- VC (Vote Count): **0.393** ← 最强
- EM (Exact Match): **0.393**
- SJ (Soft Jaccard): **0.355**
- LP (Log Probability): **0.322**
- FK (Fleiss Kappa): **0.282** ← 最弱

**Entity F1**:
- Greedy: **0.7851** [0.7817, 0.7884]
- LP Selection: **0.7890** [0.7857, 0.7922] — 比 greedy +0.39pp
- Majority Vote: 0.7584 — 比 greedy **低**
- Consensus θ=2/N: 0.7845
- Oracle: **0.8718** — headroom 8.7pp

**Degeneracy**: 31.1% constant-F1, 26.7% entity-set

### 3. GPU 利用率

**5090-c**:
| GPU | Util | VRAM |
|-----|------|------|
| 0 | 71% | 25.9/32.6 GB |
| 1 | 70% | 25.8/32.6 GB |
| 2 | 84% | 29.9/32.6 GB |
| **3** | **0%** | **0/32.6 GB (空闲)** |

**5090-b**:
| GPU | Util | VRAM |
|-----|------|------|
| 0 | 87% | 30.1/32.6 GB |
| 1 | 85% | 30.3/32.6 GB |
| 2 | 0% | 空闲 |
| 3 | 0% | 空闲 |

### 4. seed123/456 预估完成时间

两边的推理进程都还没有产出 samples.jsonl（可能是 `run_mvp_pilot.py` 在内存中处理完所有 batch 后才写出）。参考 seed42 用了约 16h+，预估：

- **5090-c seed123**: 已跑 5h44m，预估还需 ~10h（约今晚 22:00 前完成）
- **5090-b seed123**: 已跑 1h14m，预估还需 ~15h（约明天凌晨完成）
- **5090-b seed456**: 已跑 1h13m，预估还需 ~15h

**建议**: 考虑 kill 5090-b 上的 seed123（PID 164579）以释放 GPU 0 给其他用途，保留 5090-c 上先启动的那个即可。或者反过来，看哪边更快。5090-c cuda:3 也完全空闲可以利用。

---
