# audit re freeform lp gain

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_re_freeform_lp_gain_20260518T055403_result.json`
- **Structured JSON:** [`2f0786c982bcc493c844.json`](../../sessions/2f/2f0786c982bcc493c844.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Confirmed: +2.35 does not appear anywhere in the appendix. Here's the full trace:

---

## +2.35pp 来源追踪

### 搜索结果
- 服务器上所有 `output/`、`results/`、`scripts/`、`code/` 文件中 **不存在 2.35 作为 delta 值**
- 论文 `appendix.tex` 中 **不存在 2.35**
- 唯一来源：`logs/workers/worker_analysis_freeform_re_bootstrap_20260517T044401_result.json`

### 来源确认
`+2.35pp` 和 `p=0.025` 来自 seed=42 的 **gold-non-empty 子集 (n=397)** 的 bootstrap 分析：

| 子集 | Point estimate | p-value |
|------|---------------|---------|
| gold-non-empty (n=397) | **+2.35pp** | **0.0250** |
| all instances (n=551) | +1.69pp | 0.0272 |

数学关系：154 个 empty-gold instances 对 selection gap 贡献为零，所以 `1.69 × 551/397 ≈ 2.35pp`——纯粹是 denominator 缩放。

### 与 Appendix 的不匹配

**Appendix `\ref{app:freeform_ablation}` (line 771) 报告**:
> 4-seed mean = **+1.84±0.12pp** (seeds: +1.69, +1.76, +2.00, +1.91) on all instances (n=551)

**Appendix `\ref{app:re_extension}` (line 687) 报告**:
> +1.8±0.1pp across 4 seeds

**Discussion.tex line 21 引用**:
> +2.35pp, p=0.025 (citing Appendix re_extension)

问题：
1. Discussion 用的是 **单 seed (42)** 值，Appendix 报告的是 **4-seed mean**
2. Discussion 用的是 **gold-non-empty (n=397)** 子集，Appendix 用的是 **all instances (n=551)**
3. Appendix 中 **完全没有** +2.35 这个数字
4. `p=0.025` 是 seed-42 单独的 bootstrap p-value，不是 4-seed Fisher combined p

### p=0.025 核查
- 来源：bootstrap analysis worker，seed=42，n=397
- 与正确 LP delta 匹配：仅匹配 seed-42 gold-non-empty 的 +2.35pp，**不匹配** appendix 报告的 +1.84pp
- Wilcoxon 检验在同一数据上 p=0.1327（不显著），因为 77% instances 是 tied

### 建议

discussion.tex line 21 应改为与 appendix 一致的 4-seed 值：

```latex
% 当前（错误）
but restores LP selection for RE ($+2.35$~pp, $p{=}0.025$; Appendix~\ref{app:re_extension}).

% 修正选项 A：使用 4-seed mean on all instances（与 appendix 一致）
but restores LP selection for RE ($+1.8{\pm}0.1$~pp across 4 seeds; Appendix~\ref{app:re_extension}).

% 修正选项 B：如果要保留 p-value，需要对 4-seed mean 做 Fisher combined test 或 bootstrap
but restores LP selection for RE ($+1.84{\pm}0.12$~pp, $p{<}0.05$; Appendix~\ref{app:freeform_ablation}).
```

选项 A 更安全，直接引用 appendix 已有数字。如果用选项 B，需要重新计算 4-seed combined p-value。

---
