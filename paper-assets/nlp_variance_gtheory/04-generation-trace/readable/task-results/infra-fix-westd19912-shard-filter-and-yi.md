# infra fix westd19912 shard filter and yi

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix_westd19912_shard_filter_and_yi_20260521T181909_result.json`
- **Structured JSON:** [`dc7af2884a107cd7580f.json`](../../sessions/dc/dc7af2884a107cd7580f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 GPU 满载运行，6 个实验进程活跃：

| GPU | 任务 | PID | 状态 |
|-----|------|-----|------|
| GPU 0 | OLMo GSM8K | 64773 | 运行中 |
| GPU 1 | OLMo MATH | 64774 | 运行中 |
| GPU 2 | Yi HellaSwag (chain) | 67686 | 运行中 |
| GPU 3 | Yi GSM8K (chain) | 67099 | 运行中 |

Yi MMLU ✅ 和 Yi ARC ✅ 已完成，chain 已自动接力启动 HellaSwag 和 GSM8K。

---

## 完整状态总结

### 1. Kill 的进程
| PID | 任务 | 原因 |
|-----|------|------|
| 52660 | OLMo GSM8K (旧) | 未过滤 DM，1440 而非 288 条件 |
| 57889 | OLMo MATH (旧) | 同上 |
| 57884 | MATH bash 父进程 | 同上 |
| 58168, 55085 | 孤儿 vLLM 引擎 | OLMo 残留 |
| 61914, 61956, 61969, 61972 | 孤儿 vLLM 引擎 | Yi 旧进程残留 |

### 2. 修复
- `src/inference/run_experiment.py` 第 162-167 行：添加 `df = df[df["benchmark"] == benchmark]` 过滤
- 更新 DEFAULT_ITEMS["mmlu"] 指向 `mmlu_items_exp001.json` (200 items)

### 3. 已清理数据
OLMo MMLU/ARC/HellaSwag：从 288,000 行（1440 条件混杂）过滤为 57,600 行（288 正确条件）。备份保留在 `.bak_unfiltered`。

### 4. 当前 4 GPU 运行状态
| GPU | 当前任务 | 后续 chain | 预计 ETA |
|-----|---------|-----------|---------|
| GPU 0 | OLMo GSM8K | — | ~03:40 (~70 min) |
| GPU 1 | OLMo MATH | — | ~04:50 (~140 min) |
| GPU 2 | Yi HellaSwag → Yi MATH | Yi MATH ~2.5h | ~05:10 |
| GPU 3 | Yi GSM8K | — | ~04:00 (~90 min) |

### 5. 接力脚本
- GPU 2 chain (PID 66961): Yi MMLU ✅ → Yi HellaSwag 🔄 → Yi MATH ⏳
- GPU 3 chain (PID 66962): Yi ARC ✅ → Yi GSM8K 🔄

### 6. ETA 汇总
- MC benchmarks (MMLU/ARC/HellaSwag): ~5-6 min/benchmark on Blackwell（~1 sec/condition）
- CoT benchmarks (GSM8K): ~70-90 min/model
- MATH: ~140-150 min/model
- **全部完成预计: ~05:10 CST（约 2.5 小时后）**
- **关键路径: GPU 2 上的 Yi MATH**

---
