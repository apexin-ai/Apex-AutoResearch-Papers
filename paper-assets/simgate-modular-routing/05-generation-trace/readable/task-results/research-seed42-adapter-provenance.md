# research seed42 adapter provenance

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_seed42-adapter-provenance_20260516T010131_result.json`
- **Structured JSON:** [`7ea7b5a98971d92bd74a.json`](../../sessions/7e/7ea7b5a98971d92bd74a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已收集全部信息。结论如下：

---

## 调查结论：`checkpoints/plan-008-qwen3-1.7b/final_adapter/`

### 基本信息
| 项目 | 值 |
|---|---|
| **创建时间** | 2026-05-15 21:44:50 (CST) |
| **训练完成标记** | `completed_at=2026-05-15T21:44:50.449648` |
| **Seed** | **42** |
| **Base model** | Qwen3-1.7B |
| **训练数据** | `data/plan-004-implicit/implicit_sft.jsonl` (2040 条, 1830 deterministic + 210 internal) |

### Split 方式
训练日志明确记录：
> **Episode-level stratified split: 56 train / 10 val episodes → 1740 train steps, 300 val steps**

是 **episode-level** 分割，不是 step-level。

### 训练配置（与 plan-004-implicit 对比）

| 参数 | plan-008-qwen3-1.7b | plan-004-implicit |
|---|---|---|
| data_dir | `data/plan-004-implicit` | `data/plan-004-implicit` |
| model | Qwen3-1.7B | Qwen3-1.7B |
| seed | 42 | 42 |
| epochs | 3 | 3 |
| batch_size | 4 | 4 |
| **gradient_accumulation_steps** | **8** | **未设置 (默认1)** |
| lr | 2e-5 | 2e-5 |
| lora_r/alpha | 16/32 | 16/32 |
| eval_split | 0.15 | 0.15 |

**唯一差异**：plan-008 加了 `gradient_accumulation_steps=8`，有效 batch size 从 4 提升到 32。这导致总 training steps 从 plan-004 的约 1320 步降到 165 步（1740 samples / 4 batch / 8 accum ≈ 55 步/epoch × 3 epochs = 165 步）。

### 与 plan-004-implicit 是否同一 checkpoint？
**不是。** 虽然数据、模型、seed 完全一致，但 gradient_accumulation_steps 不同导致训练动态不同。文件大小相同（25720120 bytes）是因为 LoRA 架构相同（r=16, target_modules 相同），权重值不同。plan-004 创建于 5月14日，plan-008 创建于 5月15日。

### 训练效果
| Epoch | Eval Loss |
|---|---|
| 1 | 0.7213 |
| 2 | 0.3964 |
| 3 | 0.3766 |

Loss 持续下降，训练正常收敛。

### 结论
这个 adapter **可靠**。它是 plan-008 独立训练的产物，使用 episode-level stratified split（56 train / 10 val episodes），seed=42，数据来源是 plan-004-implicit 的 implicit_sft.jsonl。与 plan-004-implicit 的 checkpoint 相比，唯一区别是 gradient_accumulation_steps=8（更大有效 batch size），两者不是同一个 checkpoint。

---
