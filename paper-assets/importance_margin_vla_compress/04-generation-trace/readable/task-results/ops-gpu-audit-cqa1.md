# ops gpu audit cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-audit-cqa1_20260520T165618_result.json`
- **Structured JSON:** [`ed46fc3e1b12b5d54b0d.json`](../../sessions/ed/ed46fc3e1b12b5d54b0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 审计报告 — cqa1-33015

### GPU 状态

| GPU | 利用率 | 显存占用 | 状态 |
|-----|--------|----------|------|
| 0 | 4% | 5022 / 24564 MiB | 运行中 |
| 1 | 0% | 4 / 24564 MiB | **空闲** |
| 2 | 0% | 4055 / 24564 MiB | 运行中 |
| 3 | 0% | 4 / 24564 MiB | **空闲** |

### 运行中的进程

| PID | GPU | 显存 | 脚本 |
|-----|-----|------|------|
| 443004 | GPU 0 | 4046 MiB | `eval_xvla_pruning_libero.py --keep_ratio 0.2 --seed 43 --domain_id 3` |
| 518362 | GPU 2 | 4046 MiB | `eval_xvla_pruning_libero.py --keep_ratio 0.2 --seed 44 --domain_id 3` |

### 预期 vs 实际

| GPU | 预期实验 | 实际状态 |
|-----|----------|----------|
| 0 | eval_xvla_prune_k02_seed43 (443004) | ✅ 运行中 |
| 1 | eval_xvla_prune_k03_seed44 (346216) | ❌ **已完成退出**，GPU 空闲 |
| 2 | eval_xvla_prune_k02_seed44 (518362) | ✅ 运行中 |
| 3 | eval_xvla_prune_k03_seed43 (344867) + eval_smart_compress_m32_official | ❌ **均已完成退出**，GPU 空闲 |

### 已完成实验结果

| 实验 | keep_ratio | tokens | seed 43 SR | seed 44 SR | 平均 SR |
|------|-----------|--------|------------|------------|---------|
| xvla_prune k=0.9 | 0.9 | 45/50 | **97.6%** | **98.2%** | **97.9%** |
| xvla_prune k=0.7 | 0.7 | 35/50 | **59.0%** | **56.4%** | **57.7%** |
| xvla_prune k=0.5 | 0.5 | 25/50 | **44.2%** | **44.4%** | **44.3%** |
| xvla_prune k=0.3 | 0.3 | 15/50 | **21.0%** | **22.8%** | **21.9%** |
| xvla_prune k=0.2 | 0.2 | 10/50 | 🔄 运行中 | 🔄 运行中 | — |

### eval_smart_compress_m32_official

**已完成** (May 19 19:07)，SR = **53.4%**，seed=42，32 queries，libero_object suite。

### 空闲 GPU 汇总

**GPU 1 和 GPU 3 完全空闲**，可立即调度新实验。

---
