# ops disk cleanup and resume check 17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-and-resume-check-17855_20260522T005534_result.json`
- **Structured JSON:** [`3887e69d7eadca93b31b.json`](../../sessions/38/3887e69d7eadca93b31b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇总报告

### 1. 清理前磁盘
- **350G 总量，232G 已用，119G 可用 (67%)**

### 2. 目录大小 + 清理量

| 实验 | 清理前 | 清理后 | 释放 | 状态 |
|------|--------|--------|------|------|
| t25_a045_s42_fp32 | 3.2G | 84K | ~3.2G | ✅ 已完成 (PermG=6/8), 26 gens 清除 |
| t15_a060_s43_fp32 | 3.2G | 80K | ~3.2G | ✅ 已完成 (PermG=0/8), 15 gens 清除 |
| t15_a045_s43_fp32 | 3.2G | 68K | ~3.2G | ✅ 已完成 (有 analysis/), 15 gens 清除 |
| t25_a050_s42_fp32 | 3.2G | — | 未清理 | ⚠️ crash 残留, 保留以备 resume |
| t25_a060_s42_fp32 | 3.2G | — | 未清理 | ⚠️ crash 残留, 保留以备 resume |
| t25_a075_s42_fp32 | — | — | — | 不在此服务器 |

**总释放：~9.6G**

### 3. Resume 可行性

脚本 `iterative_train.py` **支持 `--start_gen N`** 参数，从指定 generation 恢复（加载 gen_{N-1} 的 checkpoint）。

### 4. Crash 残留完整性

| 实验 | 总 gens | 完整到 | crash 点 | resume 命令 |
|------|---------|--------|----------|-------------|
| **t25_a050_s42_fp32** | 14 (gen_0~13) | gen_12 (有 checkpoint+metrics) | gen_13: synthetic_data 完成, trainer 空 | `--start_gen 13` |
| **t25_a060_s42_fp32** | 15 (gen_0~14) | gen_13 (有 checkpoint+metrics) | gen_14: 完全空目录 | `--start_gen 14` |

两者都需要跑到 T=25（即 gen_24），分别还需 12 和 11 个 generations。

### 5. 清理后磁盘余量
- **350G 总量，223G 已用，128G 可用 (64%)**
- 释放了约 9G，从 119G → 128G 可用

---
