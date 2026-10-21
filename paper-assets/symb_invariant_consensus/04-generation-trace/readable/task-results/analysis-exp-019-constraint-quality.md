# analysis exp 019 constraint quality

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-019-constraint-quality_20260517T120215_result.json`
- **Structured JSON:** [`edbb6c6386c7a821e713.json`](../../sessions/ed/edbb6c6386c7a821e713.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果总结：

## 结果

**产出文件（服务器 westd-32608）：**
- `/root/symb_invariant_consensus/results/exp019_constraint_quality_analysis.json`
- `/root/symb_invariant_consensus/results/exp019_constraint_quality_summary.csv`

**核心数据表（7 个 model×domain 组合）：**

| Model | Domain | n | C0 | Δpp | Excl Rate | Sat Ratio |
|-------|--------|---|----|-----|-----------|-----------|
| Qwen-14B | PW+FOLIO | 804 | 0.382 | +0.25 | 0.023 | 0.977 |
| Mistral-7B | PW+FOLIO | 60 | 0.500 | 0.00 | 0.052 | 0.948 |
| LLaMA-8B | PW+FOLIO | 60 | 0.617 | **+6.67** | 0.050 | 0.950 |
| Qwen-14B | StrategyQA | 60 | 0.100 | +3.33 | 0.046 | 0.954 |
| Qwen-14B | ARC | 60 | 0.050 | -1.67 | 0.025 | 0.975 |
| LLaMA-8B | StrategyQA | 200 | 0.410 | +2.00 | **0.147** | **0.853** |
| LLaMA-8B | FOLIO | 204 | 0.618 | -2.45 | 0.062 | 0.938 |

**相关性分析：**
- **C0 vs satisfied_ratio**: Spearman ρ = **-0.64** (p=0.13) — 方向支持 capability trap
- **C0 vs exclusion_rate**: Spearman ρ = **+0.64** (p=0.13) — 方向支持 capability trap
- **C0 vs constraint_density**: Pearson r = **+0.79** (p=0.04) — 高 C0 问题产生更多约束但质量更差
- **C0 vs SICA-SC gap**: 近乎零相关 (r=0.15) — 单纯的 C0 不能预测 SICA 收益

**数据局限：**
- 结果 JSON 不包含 per-constraint 详情（没有每条约束来自哪个 trace 的映射），无法计算真正的 constraint precision（discriminative constraints / total）
- 只有 exp001 和 exp020 保存了 `sica_scores`（per-answer 分数），其余只有聚合统计
- 使用 exclusion_rate（MaxSAT 排除比例）和 satisfied_ratio 作为质量代理指标

**关键发现：**
capability trap 方向成立但 n=7 统计功效不足。反例是 LLaMA-8B/PW+FOLIO（高 C0=0.62 + 低 exclusion=0.05 → SICA 大幅赢 +6.67pp），说明 "formal logic 域的约束即使在高不确定性下仍可靠" 是 SICA 真正的 sweet spot。

---
