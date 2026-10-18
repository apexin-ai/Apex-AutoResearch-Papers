# research codellama profile prep

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_codellama_profile_prep_20260515T195330_result.json`
- **Structured JSON:** [`a20cf50beca44871e96f.json`](../../sessions/a2/a20cf50beca44871e96f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出

### 1. 分类规则（来自 analysis.tex 精确定义）

| 条件 | 分类 | 含义 |
|------|------|------|
| concentration ≥ 0.50 **AND** t₁/t₅ ≤ 0.70 | **Spread** | 多头跨 bitwidth 梯度，MCKP 有效 |
| t₁/t₅ > 0.70 **AND** concentration ≥ 0.25 | **Spike** | 单 outlier 主导，MCKP 无效 |
| concentration < 0.25, 或 [0.25, 0.50) + t₁/t₅ ≤ 0.70 | **Flat** | 均匀敏感度，MCKP 无效 |

**t₁/t₅ 定义**：最敏感 head 的 2-bit delta / top-5% heads 的 delta 之和（低=spread, 高=spike）。

### 2. 跨架构参考表（Table 4, analysis.tex）

| Model | GQA | KV Heads | Conc. | t₁/t₅ | Shape | MCKP vs Uniform |
|-------|-----|----------|-------|--------|-------|----------------|
| Qwen2.5-7B | 7:1 | 112 | **0.61** | **0.57** | **Spread** | **-29.4%** |
| Qwen2.5-14B | 5:1 | 384 | 0.33 | 0.68 | Flat | ≈0% |
| Yi-1.5-9B | 8:1 | 192 | 0.71 | 0.90 | Spike | ≈0% |
| Llama-3.1-8B | 4:1 | 256 | 0.57 | 0.85 | Spike | +0.2% |
| Mistral-7B-v0.3 | 4:1 | 256 | 0.24 | 0.41 | Flat | -0.4% |
| Gemma-2-9B | 2:1 | 336 | 0.23 | 0.38 | Flat | -0.3% |
| Pythia-1.4B | 1:1 | 384 | 0.24 | 0.28 | Flat | +0.7% (neg) |

### 3. 分析脚本

`analyze_codellama_profiling.py` — 读取 `artifacts/codellama_profiles_hires.json`，计算 concentration + t₁/t₅，输出分类和完整诊断。profiling 完成后直接运行：

```bash
python analyze_codellama_profiling.py artifacts/codellama_profiles_hires.json
```

### 4. 预测：CodeLlama-7B 最可能是 **Flat**

理由：
- **1024 heads**（32L × 32KV, MHA 1:1）→ 极端稀释。Qwen-14B 仅 384 heads 就从 Spread 稀释到 Flat（0.61→0.33）；1024 heads 几乎不可能维持 concentration ≥ 0.50
- **MHA 1:1** → 无 GQA 驱动的功能特化，参考 Pythia-1.4B（同为 MHA 1:1, 384 heads, conc=0.24, Flat）
- **Llama-2 家族** → Llama-3.1 是 Spike（conc=0.57, t₁/t₅=0.85），但那是 GQA 4:1 + 256 heads；CodeLlama 的 MHA + 1024 heads 会把任何 spike 信号稀释掉
- top-5% = 51 heads，即使存在几个敏感 head，占总 delta 的比例也会被拉低

**次可能**：Spike（如果代码训练在某些 head 产生极端特化），但即便如此 concentration 也难突破 0.50。

**不太可能是 Spread** — 这是坏消息。CodeLlama 大概率不会成为第二个 Spread 模型来增强论文论证。如果需要第二个 Spread，应该关注 head 数量少 + 高 GQA 的模型（如 Llama-3.1-8B 的某个变体，或另一个 GQA 7:1+ 的模型）。

---
