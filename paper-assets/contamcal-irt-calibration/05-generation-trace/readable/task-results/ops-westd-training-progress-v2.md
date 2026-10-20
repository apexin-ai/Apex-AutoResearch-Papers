# ops westd training progress v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-training-progress-v2_20260519T204920_result.json`
- **Structured JSON:** [`03311ddc9dc57f50af1a.json`](../../sessions/03/03311ddc9dc57f50af1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd (cqa1-21977) 状态汇总

### GPU 状态
| GPU | 型号 | 利用率 | 显存 | 当前任务 |
|-----|------|--------|------|---------|
| 0 | RTX 4090 D | 100% | 21255/24564 MiB | **eval**（非训练） |

注意：这台服务器只有 **1 张 4090 D**，不是 4 卡。

### 当前进程 (PID 280393)
正在跑 `evaluate.py`：
- 模型：**Qwen2.5-7B_d050_s42**
- Benchmarks：MMLU + ARC_Challenge（`--mc-format aligned`）
- 进度：MMLU 结果已写出，ARC_Challenge 可能还在跑

### 已完成的 Checkpoint（训练全部完成）

| Family | Dosages | Seeds | 数量 |
|--------|---------|-------|------|
| Qwen2.5-0.5B | d000/d005/d025/d100 | s42, s123 | 8 |
| Qwen2.5-1.5B | d000/d005/d025/d100 | s42, s123 | 8 |
| Qwen2.5-3B | d000/d005/d025/d100 | s42, s123 + v3/a32 变体 | ~11 |
| Llama-3.2-3B | d000/d005/d025/d100 | s42 only | 4 |
| Qwen2.5-7B | d000/d005/d025/d050/d100 | s42, s123 | 10 |
| Qwen2.5-14B | d000/d005 | s42 only | 2 |
| gemma-2-9b | d000/d005/d025/d050 | s42 only | 4 |
| **phi-4** | — | — | **无** |
| **OLMo-2-7B** | — | — | **无** |

### Eval 进度 (eval_results_v2, Qwen2.5-7B)

| 配置 | 状态 |
|------|------|
| qwen7b s123 × 5 dosages | ✅ 全部完成 |
| qwen7b s42_v2: d000/d005/d025 | ✅ 完成 |
| qwen7b s42_v2: **d050** | 🔄 进行中（MMLU done, ARC running） |
| qwen7b s42_v2: d100 | ⏳ 待跑 |

phi-4、OLMo-2-7B、gemma-2-9b、Qwen2.5-14B 的 checkpoint 在这台服务器上不存在或尚未开始 eval。Qwen2.5-14B 只有 d000/d005 两个 dosage 的 s42 checkpoint，缺 d025/d050/d100。

---
