# analysis lp rho inconsistency p0

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lp_rho_inconsistency_p0_20260518T232334_result.json`
- **Structured JSON:** [`a17c62ed087f59a24091.json`](../../sessions/a1/a17c62ed087f59a24091.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 调查结论

### 1. 论文中 FewNERD LP ρ 位置和值

论文 **已更新** 为一致的 LP ρ=0.22：
- `experiments.tex:125` — "LP $0.22$"
- `appendix.tex:1219` — "LP ($0.22$)"
- `introduction.tex:23` — 引用的是 VC ρ=0.39（不是 LP）

### 2. F1 函数差异 → 不是根因

旧 `evaluation.py` 和 `unified_metrics.py` 的 NER F1 逻辑完全相同（strict match on (start, end, type)）。唯一区别是 both-empty 边界情况（旧=0.0, 新=1.0），但 gold_filter 排除了这些实例。

**验证：非 LP 信号（SJ/FK/EM/VC）ρ 在两管道中完全一致。**

### 3. 根因：LP 信号定义不同

| LP 定义 | FewNERD ρ | SciERC ρ | 谁用 |
|---------|-----------|----------|------|
| **Greedy mean_logprob** | 0.427 | 0.261 | 旧管道 `full_signal_analysis.json` |
| **Mean(sample mean_logprobs)** | 0.222 | 0.205 | unified `results.json` + 当前论文 |

Greedy logprob 天然与 greedy F1 更相关（同一解码过程的置信度和质量），所以 ρ 更高。Sample 均值是跨 8 次随机采样的平均置信度，与特定 greedy 输出的关联更弱。

### 4. 是否需要更新论文

**不需要** — 论文已一致使用 mean sample LP (ρ=0.22)，跨数据集定义统一。

但 `paper_framing.md:66` 仍写 "LP ρ=0.42"，已过时。

### 5. paper_framing.md "ρ(LP,F1) ≈ 0.5-0.66" 不受影响

已验证这是 **within-instance** ρ（每个实例内 sample LP 与 sample F1 的相关性）：
- mean = 0.5106
- median = 0.6667
- N = 28,086 non-degenerate instances

这是一个完全不同的指标（LP-quality alignment），用于解释为什么 LP selection 在 FewNERD 上成功（强 alignment → LP 能 rank candidates），不涉及 global QE ρ 的定义问题。

---
