# ops gpu diagnosis and submit signals

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_diagnosis_and_submit_signals_20260516T233425_result.json`
- **Structured JSON:** [`94f4522427003d7d97cd.json`](../../sessions/94/94f4522427003d7d97cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇报

### GPU 占用

| GPU | 任务 | 状态 | 预计完成 |
|-----|------|------|---------|
| cuda:0 | **d100 s4 MMLU** (刚提交, resume from chunk 6000) | 70% util, 6.9G | ~2h |
| cuda:1 | 空闲 | — | — |
| cuda:2 | **d025 s4 MMLU** (chunk 12000:13000 @ 98%) | 活跃 | ~15 min |
| cuda:3 | 空闲 | — | — |
| cuda:4 | 空闲 | — | — |
| cuda:5 | 空闲 | — | — |

### Signal 完整性

| Model | Benchmark | s1 | s2 | s4 | merged |
|-------|-----------|----|----|-------|--------|
| **d000** | MMLU/ARC/GSM8K | ✓ | ✓ | ✓ | ✓ |
| **d005** | MMLU/ARC/GSM8K | ✓ | ✓ | ✓ | ✓ |
| **d025** | ARC/GSM8K | ✓ | ✓ | ✓ | ✓ |
| **d025** | **MMLU** | ✓ | ✓ | **进行中** (~15min) | watcher 自动生成 |
| **d100** | ARC/GSM8K | ✓ | ✓ | ✓ | ✓ |
| **d100** | **MMLU** | ✓ | ✓ | **进行中** (~2h) | watcher 自动生成 |

### 0.5B/1.5B s123 (C007 最高优先级)
全部 COMPLETE（8 个目录 × 12 json 文件 × 3 merged）。

### 空闲 GPU 说明
cuda:1/3/4/5 无 signal 任务可提交 — Llama-3.2-3B 全部信号只差 d025/d100 的 MMLU s4，已覆盖。Fisher heatmap 和 IRT fitting 均为 CPU-only。如需填满这 4 张卡，需要新的 GPU 实验（如额外 eval runs、新模型 signals 等）。

---
