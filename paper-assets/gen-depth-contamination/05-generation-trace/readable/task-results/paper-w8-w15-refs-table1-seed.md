# paper w8 w15 refs table1 seed

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_w8_w15_refs_table1_seed_20260522T061722_result.json`
- **Structured JSON:** [`47a248f21162619f2441.json`](../../sessions/47/47a248f21162619f2441.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部编辑完成。以下是三部分结果：

---

## Part 1: W8 — 引用添加

**references.bib**: 两条 bib entry 已添加到文件末尾。

**related_work.tex** 引用位置（第 5 行，Model collapse 段落）：
- `\citep{fu2025theoretical}` → 加入 tail-distribution degradation 引用列表（与 shumailov, alemohammad, dohmatob 等并列）
- `\citep{wang2025unveiling}` → 加入 predictable convergence 引用列表（与 schaeffer, kazdan, gerstgrasser 并列）

上下文：
```
...tail-distribution degradation~\cite{..., fu2025theoretical},
diversity contraction~\cite{...},
and predictable convergence~\cite{..., wang2025unveiling}.
```

---

## Part 2: W15 — Table 脚注

`tab:kstar_ci`（编译后为 Table 2，主 pairwise AUC 表）已在底部脚注区新增一行：

> Full results for all 10 configurations (including Qwen-7B, Qwen-base, Gemma-2-2B, and Pythia-6.9B) are provided in Table~\ref{tab:kstar_ci_extended}.

注：实际 Table 1 是 `tab:setup`（实验配置表），主结果表 `tab:kstar_ci` 是 Table 2。脚注引用了已有的 appendix 扩展表 `tab:kstar_ci_extended`（即论文注释中的 "Table S2b"）。

---

## Part 3: Seed Robustness 结果

3 组实验（seed=123）均已完成。

### 汇总对比

| 配置 | 指标 | seed=42 | seed=123 | Δ | K* 变化 |
|------|------|---------|----------|---|---------|
| **Pythia-1.4B Wiki** | 0v1 | 0.975 | 0.9751 | +0.0001 | |
| | 1v2 | 0.5846 | 0.5766 | −0.008 | |
| | 2v3 | 0.5445 | 0.5318 | −0.013 | |
| | 3v4 | 0.5205 | 0.5175 | −0.003 | |
| | 4v5 | 0.5168 | 0.5270 | +0.010 | |
| | **K\*** | **1** | **1** | **same** | |
| **Qwen-1.5B Wiki** | 0v1 | 0.9961 | 0.9945 | −0.002 | |
| | 1v2 | 0.6193 | 0.7059 | **+0.087** | |
| | 2v3 | 0.5498 | 0.6067 | **+0.057** | |
| | 3v4 | 0.5231 | 0.5531 | +0.030 | |
| | 4v5 | 0.5141 | 0.5292 | +0.015 | |
| | **K\*** | **2** | **3** | **+1** | |
| **Qwen-1.5B C4** | 0v1 | 0.9971 | 0.9956 | −0.002 | |
| | 1v2 | 0.6112 | 0.7014 | **+0.090** | |
| | 2v3 | 0.5609 | 0.5911 | +0.030 | |
| | 3v4 | 0.5409 | 0.5405 | −0.0004 | |
| | 4v5 | 0.5141 | 0.5335 | +0.019 | |
| | **K\*** | **2** | **2** | **same** | |

### 简短报告

**Seed robustness 总结**：

Pythia-1.4B Wiki 和 Qwen-1.5B C4 的 K\* 在 seed 变化下保持一致（分别为 1 和 2），AUC 波动在 ±1 pp 以内（Pythia）或 boundary pair 以外（C4 的 2v3 仍低于 θ=0.60）。

Qwen-1.5B Wiki 出现 K\* 从 2 升至 3 的不一致：seed=123 的 1v2 AUC 从 0.619 跳至 0.706（+8.7 pp），2v3 从 0.550 升至 0.607（刚过 θ=0.60，且 fold 最低值 0.595 低于 θ）。这表明 Qwen Wiki 配置对数据采样高度敏感，2v3 boundary 处于 marginal 区域。seed=123 的 K\*=3 不可靠（2v3 CI 下界可能低于 θ）。

Qwen-1.5B 两个 domain 的 1v2 AUC 在 seed=123 下均大幅升高（+8.7~9.0 pp），可能反映 seed=123 的数据分割恰好选到了更易区分的样本。这进一步支持论文中 Qwen-continuation 1v2 boundary marginal 的讨论（Limitations 第 4 点）。

**结论**：K\* 的 qualitative conclusion（C4/Wiki 为低值 1-2）在 seed 变化下基本稳健，但 Qwen Wiki 的具体 K\* 值（2 vs. 3）取决于 seed，建议在论文 seed robustness 讨论中强调 2v3 boundary 的 marginal 特性。

---
