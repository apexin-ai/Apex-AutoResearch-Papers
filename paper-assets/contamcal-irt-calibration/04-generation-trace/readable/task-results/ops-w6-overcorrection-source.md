# ops w6 overcorrection source

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_w6_overcorrection_source_20260517T163408_result.json`
- **Structured JSON:** [`eabb2747c015d6f3aa71.json`](../../sessions/ea/eabb2747c015d6f3aa71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

搜索完毕。以下是结论。

## 11× overcorrection ratio 的来源分析

### 论文原文 (results.tex:64)
> "the GSM8K overcorrection ratio is 11×: the model corrects 11 units of noise for every 1 unit of genuine contamination effect"

### 溯源数据
来自 **exp-006 pooled IRT 2PL+γ N=24 GSM8K** (`pooled_irt_2pl_gamma_n16_fixed/gsm8k/irt_results.json`):
- γ_mean = **0.0639**
- γ_sd = **0.2208**
- CI = [-0.3636, 0.4902] (非显著)

### 最可能的计算公式

**噪声-信号方差比 (γ_sd / γ_mean)²**:

```
(0.2208 / 0.0639)² = 3.456² = 11.94 → floor → 11
```

语义：γ 后验中，方差（噪声）是均值平方（信号）的 ~12 倍。也就是说模型每修正 1 单位真实污染效应，就同时修正了 ~11 单位噪声。因为 γ 不显著（CI 跨零），绝大部分"校正"是在修正随机波动。

### 关键问题

1. **没有显式代码计算这个指标** — 代码库中无 `overcorrection_ratio` 函数，也无任何 Python 脚本输出这个数字
2. **paper_provenance.yaml (C094)** 只记录 `metric: overcorrection_ratio_gsm8k, value: 11`，没有记录计算公式
3. **coverage_audit_0516.md** 中称 "MAE 11× worse than raw"，但实际数据中 GSM8K cal_MAE (0.006) **远优于** raw_MAE (0.169)，这个描述与数据不匹配
4. (0.2208/0.0639)² = 11.94 取整到 11 而非 12，四舍五入不一致

### 建议

这个数字大概率是 Paper Agent 写作时手算或近似产出，没有 rigorous computation pipeline。审稿人回复时应：
- 明确给出公式：overcorrection ratio = Var(γ) / E[γ]² = σ²/μ²
- 用精确数字：(0.2208²)/(0.0639²) = **11.9**
- 或干脆改用更直观的指标：γ 的 95% CI 跨零且宽度是均值的 13.4 倍

---
