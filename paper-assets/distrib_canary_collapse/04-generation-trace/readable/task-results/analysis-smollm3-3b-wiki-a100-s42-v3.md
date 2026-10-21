# analysis smollm3 3b wiki a100 s42 v3

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_smollm3_3b_wiki_a100_s42_v3_20260519T190816_result.json`
- **Structured JSON:** [`a67571c878d8d82baa9e.json`](../../sessions/a6/a67571c878d8d82baa9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## SmolLM3-3B fp32 (s42, α=1.0) — D102+D105 分析结果

### Table 7 指标
| 指标 | 值 |
|------|-----|
| **PermG fwd** | **3/8** (ece→d1, ece→d2, ece→d3) |
| PermG rev | 0/8 |
| K≥3(3σ) | 0/8 |
| K≥4(3σ) | 0/8 |
| Thr(3σ) | 0/8 |
| DiffXCorr FDR | 6/8 |

### 结论：**negative**（PermG 3/8 < 4/8 阈值）

### 关键观察
- **Collapse 确实发生**：PPL +4877%, ECE +8220%, entropy -33.5%, d1 -32.2%
- **ECE canary 强**：PermG 3/3 distinct pairs 显著，但 0/1 mauve pair
- **Entropy canary 弱**：PermG 0/4（全部 FDR 不显著）
- **Mauve 全面弱**：baseline 极低（~0.025-0.030），几乎没有动态范围
- **与旧分析差异大**：旧 2σ + perplexity 分析得 PermG=6/8（success）；切换到 D102 mauve + D105 3σ 后降至 3/8

### 影响
SmolLM3 在 D102+D105 标准下从 success 翻转为 negative，主要因为 (1) mauve 替代 perplexity 削弱了 2/8 pair，(2) 3σ threshold_onset 全部失效。可能需要 revisit 其他 Table 7 模型是否在 D102+D105 下也发生类似衰减。

---
