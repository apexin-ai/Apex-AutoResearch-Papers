# infra urgent status all items

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_urgent-status-all-items_20260522T161835_result.json`
- **Structured JSON:** [`c2194aa66312aedbcea1.json`](../../sessions/c2/c2194aa66312aedbcea1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 1. Gemma L17 Steering (PID 493756)
- **进程**: 存活，已运行 **1h40m**，GPU 2（29% util, 18.5GB）
- **结果文件**: 不存在（steering_results/ 目录为空）
- **日志**: 模型已加载完成，probe acc@L17=**0.7532**，之后无新输出 — 正在静默执行 steering generation

### 2. Gemma L21 Steering (PID 499402)
- **进程**: 存活，已运行 **22min**，GPU 0（28% util, 18.5GB）
- **结果文件**: 不存在
- **日志**: 模型已加载完成，probe acc@L21=**0.7627**，正在静默执行

### 3. DE Probe Training (PID 496671)
- **进程**: 存活，已运行 **1h05m**，CPU-only
- **结果文件**: 不存在，无专用日志文件
- **命令**: `train_probe.py --langs en,zh,de --bootstrap_seeds 2000`（3语言 bootstrap）

### 4. Gemma Probe n=2000 Bootstrap (PID 476334)
- **进程**: 存活，已运行 **5h34m**，CPU-only（32 jobs）
- **结果文件**: `data/gemma2/probe_results_bootstrap_n2000.json` 不存在（写完才输出）
- **日志进度**:
  - en_en: 完成（83min）
  - en_zh: 完成（57min）
  - **zh_en: 进行中**（386/2000 tasks, ~14.6min elapsed）
  - zh_zh: 待运行
- **预计剩余**: zh_en 还需 ~40min，zh_zh ~60min → 总计约 **1.5-2h** 完成

### 5. C3 MLP Bootstrap (PID 467708)
- **进程**: 存活，已运行 **7h44m**，CPU-only
- **日志**: 已完成 L27 → 现在跑 **L28**（200/1000, ETA ~3380s≈56min）
- **L27 结果**: delta=+0.0221, CI=[-0.0184, +0.0625], **excludes_zero=False**（不显著）

### 6. GPU 状态
| GPU | 型号 | 显存占用 | 利用率 | 进程 |
|-----|------|---------|--------|------|
| 0 | RTX PRO 6000 Blackwell (98GB) | 18.5GB | 28% | PID 499402 (L21 steering) |
| 1 | RTX PRO 6000 Blackwell (98GB) | 3MB | 0% | **空闲** |
| 2 | RTX PRO 6000 Blackwell (98GB) | 18.5GB | 29% | PID 493756 (L17 steering) |
| 3 | RTX PRO 6000 Blackwell (98GB) | 3MB | 0% | **空闲** |

### 已完成的结果: Llama31 Probe Bootstrap n=2000
`data/llama31/probe_results_bootstrap_n2000.json` 已存在，关键指标：
- **Asymmetry peak**: mean_diff=**0.0727**, p=**0.038**, CI=[0.0037, 0.1397] — **显著 (p<0.05)**
- en_en peak: layer 19, acc=0.7508
- n_seeds=2000

**GPU 1 和 3 空闲**，可以分配新任务。

---
