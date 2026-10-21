# analysis qlora instruct prep A

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qlora_instruct_prep_A_20260519T074532_result.json`
- **Structured JSON:** [`3082bf8d22ea6f776be1.json`](../../sessions/30/3082bf8d22ea6f776be1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇总报告

### 1. Instruct Generation 数据

| 模型 | 目录 | 文件 | 行数 | Depth 分布 |
|---|---|---|---|---|
| qwen3-1.7b-instruct | ✅ | `generations_shard0.jsonl` | 4,963 | {0:996, 1:996, 2:991, 3:990, 4:990} |
| **olmo-2-1b-instruct** | **❌ 不存在** | — | — | — |
| olmo-2-0425-1b-instruct | ✅ (不同模型) | `generations_shard0.jsonl` | 4,429 | {0:995, 1:965, 2:884, 3:817, 4:768} |

`olmo-2-1b-instruct` 目录不存在。服务器上有的 instruct 版本是 `olmo-2-0425-1b-instruct`（OLMo-2 April 2025 checkpoint，不同模型）。

### 2. Base Model 数据（对比基线）

| 模型 | 行数 | Depth 分布 |
|---|---|---|
| olmo-2-1b | 4,713 | {0:995, 1:988, 2:947, 3:905, 4:878} |
| qwen3-1.7b | 4,617 | {0:996, 1:983, 2:941, 3:875, 4:822} |

两个 base model 数据齐全。注意高 depth 有衰减（生成失败），qwen3-1.7b-instruct 反而几乎不衰减。

### 3. QLoRA 脚本

- `end_to_end_classifier.py` ✅ 存在（11.5KB）
- 硬编码加载 4 个 base 模型：`pythia-1b, olmo-2-1b, qwen3-0.6b, qwen3-1.7b`
- backbone 是 Qwen3-0.6B-Base
- **不支持 instruct 数据**，需修改 `load_generation_data()` 中的 generator 列表
- `v2` 和 `pythia` 版本结构相同

### 4. 环境（conda base）

| 包 | 版本 |
|---|---|
| torch | 2.10.0+cu128 |
| transformers | 4.57.6 |
| peft | 0.19.0 |
| bitsandbytes | 0.49.2 |

**GPU**: 4× RTX 5090 (32GB each)，全部空闲。需 `source /root/miniconda3/bin/activate` 激活环境。

### 5. 模型权重

| 模型 | 状态 | 路径 |
|---|---|---|
| olmo-2-1b (base) | ✅ | `/root/autodl-tmp/models/olmo-2-1b-hf` |
| olmo-2-0425-1b-instruct | ✅ 完整 (2.9GB) | `/root/autodl-tmp/models/olmo-2-0425-1b-instruct` |
| qwen3-0.6b | ✅ | `/root/autodl-tmp/models/qwen3-0.6b` |
| **Qwen3-1.7B** | **❌ 空目录** | `._____temp/Qwen/Qwen3-1.7B` (下载中断) |
| **Qwen3-1.7B-Instruct** | **❌ 不存在** | — |

### Blocking Issues

1. **OLMo-2-1B-Instruct 数据缺失** — 只有 `olmo-2-0425-1b-instruct` 的数据，需确认是否可替代
2. **Qwen3-1.7B / Qwen3-1.7B-Instruct 权重缺失** — temp 目录为空（下载失败），需重新下载
3. **脚本需改造** — 当前只加载 base 模型数据，需扩展支持 instruct 数据路径

### 建议

**不能直接开始 QLoRA 训练。** 需先：
1. 确认 `olmo-2-0425-1b-instruct` 是否可替代 `olmo-2-1b-instruct`（若不可，需先生成 OLMo-2-1B-Instruct 数据，但该模型权重也不在服务器上）
2. 下载 Qwen3-1.7B（或 Qwen3-1.7B-Instruct）权重作为 QLoRA backbone（如果实验设计需要）
3. 修改 `end_to_end_classifier.py` 的数据加载逻辑以包含 instruct 生成数据

---
