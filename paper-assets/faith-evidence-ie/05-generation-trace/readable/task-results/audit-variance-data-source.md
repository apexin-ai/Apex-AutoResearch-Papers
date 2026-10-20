# audit variance data source

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_variance-data-source_20260524T234130_result.json`
- **Structured JSON:** [`cb0ba6eea4f8adca9f89.json`](../../sessions/cb/cb0ba6eea4f8adca9f89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整分析完成。以下是结论。

---

## 验证结果

### Step 1: 论文数值提取

**Table 1 (tab:scaling) RSFT Ign-F1:**
| Model | Paper Mean±Std | Seeds |
|-------|---------------|-------|
| Qwen3-1.7B | 51.19±0.09 | 3 |
| Qwen3-4B | 44.82±0.51 | 3 |
| Qwen3-8B | 54.33±0.50 | 3 |
| LLaMA-3.1-8B | 56.54±0.64 | 3 |

**Table 6 (tab:variance_ci) RSFT std:**
与 Table 1 一致。

### Step 2-3: Registry 匹配与 SFT adapter 来源

| 数据点 | 论文值 | 匹配 exp_id | SFT adapter | Seed-matched? |
|--------|--------|------------|-------------|---------------|
| **1.7B s42** | 51.22 | `d102_1_7b_rsft_k1_s42` | `sft_output_qwen3_1_7b_bf16` | ✓ (it IS s42) |
| **1.7B s43** | 51.09 | `plan019_1_7b_rsft_s43_r2_eval` | `sft_output_qwen3_1_7b_bf16` (s42共享) | **✗** |
| **1.7B s44** | 51.25 | `plan019_1_7b_rsft_s44_r2_eval` | `sft_output_qwen3_1_7b_bf16` (s42共享) | **✗** |
| **4B s42** | ~44.2-45.2 | `reeval_ced_s42` / similar | `sft_output` (s42) | ✓ (it IS s42) |
| **4B s43** | ~45.12 | `eval_rsft_ced_s43` | `sft_output` (s42共享) | **✗** |
| **4B s45** | ~44.16 | `eval_rsft_ced_s45` | `sft_output` (s42共享) | **✗** |
| **8B s42** | 53.76 | `d102_8b_rsft_k1_s42` | `sft_output_qwen3_8b_bf16` | ✓ (it IS s42) |
| **8B s43** | 54.71 | `d102_8b_rsft_k1_s43` | `sft_output_qwen3_8b_bf16` (s42共享) | **✗** |
| **8B s44** | 54.51 | `plan019_8b_rsft_s44_eval` | `sft_output_qwen3_8b_bf16` (s42共享) | **✗** |
| **LLaMA s42** | 57.14 | `d102_llama_rsft_k1_s42` | `sft_output_llama_3_1_8b` | ✓ (it IS s42) |
| **LLaMA s43** | 56.62 | `eval_llama_rsft_k1_s43` | `sft_output_llama_3_1_8b` (s42共享) | **✗** |
| **LLaMA s44** | 55.87 | `llama_rsft_s44_pipeline` | `sft_output_llama_3_1_8b` (s42共享) | **✗** |

### 直接证据 (registry hypothesis 字段)

- `plan019_1_7b_rsft_s43_r2`: *"使用 s42 SFT adapter (sft_output_qwen3_1_7b_bf16) + s42 CED k=1 scored data, RSFT seed=43"*
- `plan019_8b_rsft_s44`: *"Reuses s42 SFT adapter + s42 CED k=1 scored data, only changes RSFT training seed to 44"*
- `llama_rsft_s44_pipeline`: *"Method A: 复用 s42 CED-scored data (2952 samples)，只变 RSFT training seed=44"*

### Step 4: 判断

**存在严重方法论缺陷。**

论文 experiments.tex 第70行声称：
> "Each RSFT seed starts from its corresponding independently trained SFT checkpoint (§ref), so the variance reduction reflects data quality filtering rather than shared initialization."

**事实**：ALL non-s42 RSFT 实验共享同一 s42 SFT adapter 和同一 s42 生成的 RSFT 训练数据。唯一变化的是 LoRA 训练随机种子。

**后果**：
1. **Variance comparison 无效** — SFT variance 来自完全独立训练的模型（不同 LoRA init、不同 data shuffle），RSFT variance 仅来自最后一步微调的随机性（共享 base、共享训练数据）。RSFT 低方差是共享初始化的必然结果，而非论文声称的"数据质量筛选"效果。
2. **论文中的因果声明方向相反** — 低方差恰恰 BECAUSE OF shared initialization，not despite it。
3. **Table 6 的 CI 分析和 sign test 结论均基于错误前提**。

### 替换数据可用性

d158 系列正在用 seed-matched SFT 重做实验，但：
- 只覆盖 1.7B (`d158_1_7b_rsft_s44_train`, status=ANALYZING) 和 14B (`d158_14b_rsft_s44_generate`, RUNNING)
- 4B、8B、LLaMA 无 seed-matched RSFT 替换实验
- 即使 d158 完成，也只提供 1 个额外 seed（s44），不足以支撑 3-seed variance 分析

### 修复建议

1. **最小修复（文本修正）**：删除 "Each RSFT seed starts from its corresponding independently trained SFT checkpoint" 的错误声明，改为诚实描述方法：RSFT seeds 共享 s42 SFT base 和 s42-generated 训练数据，仅训练随机种子不同。
2. **调弱 variance claim**：将 "variance reduction reflects data quality filtering" 改为 "low RSFT variance may partially reflect shared initialization; separating the contributions of shared base vs. data quality requires seed-matched SFT RSFT runs."
3. **彻底修复**：为所有 4 个 scale 完成 d158-style seed-matched RSFT（每个 scale 需要：独立 SFT → 独立 generation → 独立 CED scoring → RSFT training → eval），用这些结果替换当前数据。这需要大量计算资源和时间。

---
