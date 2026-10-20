# ops disk cleanup inventory

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-inventory_20260515T115819_result.json`
- **Structured JSON:** [`f45cc299fc25cba66348.json`](../../sessions/f4/f45cc299fc25cba66348.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

盘点完成。以下是完整清理方案。

---

## 磁盘总览

```
/dev/md0    250G used 172G avail 79G (69%)
```

**顶层空间分布：**
| 目录 | 大小 |
|------|------|
| outputs/ | 173G |
| models/ | 16G（Qwen3-4B 7.6G + Qwen3-4B-ms 7.6G）|
| .hf_cache/ | 5.3G |
| gpt2-small/ | 526M |

---

## 清理候选项

### 第一优先级：重复 checkpoint（低风险，高收益）

| 路径 | 实验 | 类型 | 大小 | 风险 |
|------|------|------|------|------|
| `outputs/exp1_isr_b03_s42_1000/checkpoint-1000/` | exp1_isr_b03_s42 | 重复最终 checkpoint — root 已有完整模型权重，checkpoint-1000 仅多一个 trainer_state.json (896K) | **~16G** | 低 |
| `outputs/plan018_additive_random_b01_s42_1000/checkpoint-1000/` | plan018_s42 | 重复最终 checkpoint — root 已有完整模型权重，checkpoint-1000 仅多一个 trainer_state.json (932K) | **~16G** | 低 |

**小计：~32G**

### 第二优先级：废弃缓存和旧模型（低风险）

| 路径 | 类型 | 大小 | 风险 |
|------|------|------|------|
| `.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/` | 废弃 HF 缓存（项目用 Qwen3-4B） | **2.9G** | 低 |
| `.hf_cache/Qwen/Qwen2.5-0.5B/` | 废弃 HF 缓存 | **954M** | 低 |
| `.hf_cache/openai-community/` | gpt2 缓存 | **1.1G** | 低 |
| `.hf_cache/models--openai-community--gpt2/` | gpt2 缓存 | **363M** | 低 |
| `gpt2-small/` | 废弃模型目录 | **526M** | 低 |

**小计：~5.8G**

### 第三优先级：重复 base model（中风险）

| 路径 | 类型 | 大小 | 风险 |
|------|------|------|------|
| `models/Qwen3-4B-ms/` 或 `models/Qwen3-4B/`（二选一）| 重复 base model（HF vs ModelScope 来源）| **7.6G** | 中 — 需确认训练脚本引用的是哪个路径 |

**小计：~7.6G**

---

## 不可碰（仅标注）

| 路径 | 大小 | 原因 |
|------|------|------|
| `outputs/plan018_additive_random_b01_s42_1000_r3/` | 16G | 正在训练（checkpoint-900 + checkpoint-950 生成中）|
| `outputs/plan009_sft_baseline_s42_1000/` | 23G（含 15G optimizer.pt）| 即将启动训练。注：checkpoint-50 含 15G optimizer.pt，若从头训练则整个 checkpoint-50 可清理 |

---

## 汇总

| 类别 | 可回收空间 |
|------|-----------|
| 低风险可立即清理 | **~37.8G**（重复 checkpoint 32G + 废弃缓存 5.8G）|
| 中风险需确认后清理 | **~7.6G**（重复 base model）|
| 暂不可碰待后续处理 | ~39G（运行中 + 即将启动）|
| **预计可回收总计** | **~45.4G** |

清理后磁盘预计从 172G/250G (69%) 降至 ~127G/250G (51%)。

---
