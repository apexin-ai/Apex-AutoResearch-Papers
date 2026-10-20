# analysis abstract rho context

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_abstract_rho_context_20260519T112114_result.json`
- **Structured JSON:** [`97efb2c56e9c78952584.json`](../../sessions/97/97efb2c56e9c78952584.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Data collected. Here's the full analysis.

---

## ρ Cross-Dataset Summary (n=8, main table config)

### Per-configuration ρ (multi-seed mean where available)

| Dataset | Model | SJ ρ | FK ρ | VC ρ | EM ρ | LP ρ | **Max ρ** | Seeds |
|---------|-------|------|------|------|------|------|-----------|-------|
| CoNLL | Qwen3-8B | .436 | .400 | .424 | **.451** | .316 | **.451** | 1 |
| CoNLL | LLaMA-8B | .431 | .427 | .423 | .430 | .307 | .431 | 2 |
| SciERC | LLaMA-8B | .359 | .308 | **.426** | .300 | .190 | **.426** | 2 |
| SciERC | Qwen3-8B | .374 | .265 | .396 | .304 | .220 | .396 | 2 |
| FewNERD | Qwen3-8B | .316 | .330 | .381 | .306 | **.421** | **.421** | 3 |

### Dataset-level max ρ (best model per dataset)

| Dataset | Max ρ | Signal | Model |
|---------|-------|--------|-------|
| CoNLL | **0.451** | EM | Qwen |
| SciERC | **0.426** | VC | LLaMA |
| FewNERD | **0.421** | LP | Qwen |

### Cross-dataset aggregates

| Metric | Value |
|--------|-------|
| Cross-dataset **median** of max ρ | **0.426** |
| Cross-dataset **mean** of max ρ | **0.433** |
| Range | 0.421 - 0.451 |

---

## 回答

**1. "ρ up to 0.45" 只在 CoNLL 一个数据集达到吗？**

是。0.451 仅出现在 CoNLL × Qwen × EM 这一个组合（且只有 1 个 seed）。其他两个数据集的 max ρ 分别是 SciERC 0.426、FewNERD 0.421。

**2. Cross-dataset median max ρ？**

**0.426**（mean = 0.433）。

**3. Abstract 是否需要加 dataset context？**

不需要。理由：
- 0.451 虽是 single dataset peak，但三个数据集的 max ρ 分布很紧凑（0.421 - 0.451，仅 3pp 差异）
- "up to" 本身就是 upper-bound 语义，审稿人不会理解为 "每个数据集都达到 0.45"
- 如果改为 median (0.43)，反而低估了信号强度，且 0.43 vs 0.45 差异不大，改动收益极低

**建议保持 "ρ up to 0.45" 不变。** 如果 Director 更保守，可改为 "ρ = 0.42-0.45"，同时传达范围信息，但 Abstract 篇幅紧张，没必要。

---
