# analysis exp004 per benchmark gstudy mc

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp004_per_benchmark_gstudy_mc_20260521T213108_result.json`
- **Structured JSON:** [`a0ed6f4abb4b80d714bc.json`](../../sessions/a0/a0ed6f4abb4b80d714bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 输出完整。以下是 exp-004 MC benchmarks 6-model Henderson I G-study 结果汇总：

## 结果

### 方差分解表（6 models × 3 MC benchmarks）

| | MMLU | ARC | HellaSwag |
|---|---|---|---|
| **item_id** | **40.48%** | **42.46%** | **32.20%** |
| **model:item_id** | 31.60% | 38.05% | 37.14% |
| **residual** | 21.94% | 9.33% | 15.52% |
| **model** | 3.05% | 5.23% | 6.69% |
| prompt_template:item_id | 1.02% | 1.58% | 1.64% |
| temperature:item_id | 0.73% | 0.72% | 1.13% |
| seed:item_id | 0.71% | 1.26% | 1.67% |
| ordering:item_id | 0.36% | 1.31% | 3.93% |
| 其他 | <0.1% | <0.1% | <0.1% |

### G_item + Bootstrap 95% CIs

| Benchmark | G_item | 95% CI | min_n(G≥.80) |
|---|---|---|---|
| MMLU | **0.8705** | [0.841, 0.895] | 119 |
| ARC | **0.8623** | [0.811, 0.895] | 128 |
| HellaSwag | **0.8240** | [0.777, 0.857] | 171 |

### 4-model → 6-model 变化

| Benchmark | item_id% Δ | model% Δ | G_item Δ |
|---|---|---|---|
| MMLU | 41.55→40.48 (−1.1) | 0.75→3.05 (+2.3) | 0.816→0.871 (+0.055) |
| ARC | 48.90→42.46 (−6.4) | 2.74→5.23 (+2.5) | 0.831→0.862 (+0.032) |
| HellaSwag | 44.47→32.20 (−12.3) | 1.49→6.69 (+5.2) | 0.832→0.824 (−0.008) |

### 关键发现

1. **item_id% 并非全部 >40%**：MMLU 40.48%、ARC 42.46% 满足，但 HellaSwag 降到 32.20%。6 模型下 HellaSwag 的 model:item_id 交互（37.14%）超过了 item 主效应——说明 InternLM/DeepSeek 加入后，不同模型对 HellaSwag items 的难度排序差异极大。

2. **model facet 显著增长**：从 4-model 的 0.75-2.74% 增到 6-model 的 3.05-6.69%，因为新增模型（InternLM2.5、DeepSeek）能力分布更广。

3. **G_item 整体 >0.80**：所有 3 个 benchmark 的 G_item ≥ 0.824，200 items 对 MC benchmarks 的可靠性充分。

**JSON 文件**: `results/exp004_8model_analysis/per_benchmark_gstudy_mc.json`

---
