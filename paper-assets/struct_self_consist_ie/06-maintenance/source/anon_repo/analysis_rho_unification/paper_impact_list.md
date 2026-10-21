# ρ 值论文影响清单

**生成日期**: 2026-05-15
**数据源**: `analysis_unified_rho.json` (unified pipeline, gold-filtered)
**管道变化**: 排除 gold-empty 实例 + 统一 consistency.py FK/SJ + evaluation.py per_instance_f1

---

## 统一管道修正值摘要

| 实验 | Signal | 旧 Registry ρ | 统一 ρ | Δ | 说明 |
|------|--------|---------------|--------|---|------|
| LLaMA CoNLL N=16 seed42 | FK | 0.8095 | 0.4752 | **-0.334** | 排名反转 |
| LLaMA CoNLL N=16 seed42 | SJ | 0.1815 | 0.4836 | **+0.302** | 排名反转 |
| LLaMA CoNLL N=16 seed456 | FK | 0.8085 | 0.4690 | **-0.340** | 排名反转 |
| LLaMA CoNLL N=16 seed456 | SJ | 0.1895 | 0.4734 | **+0.284** | 排名反转 |
| Qwen SciERC N=16 seed456 NER | FK | 0.3448 | 0.2723 | **-0.073** | 幅度下降 |
| Qwen SciERC N=16 seed456 NER | SJ | 0.4134 | 0.4098 | -0.004 | 基本不变 |
| OOD CoNLL→SciERC | — | — | — | — | 已正确，无需变更 |

**关键发现**: LLaMA CoNLL N=16 旧管道中 FK ρ 严重虚高（0.81），SJ 严重偏低（0.18），统一管道修正后二者趋同（~0.48），**排名发生反转**。

---

## 需更新的 ρ 值位置

### 1. Table tab:robustness — LLaMA CoNLL N=16 3-seed section

**文件**: `sections/appendix.tex`, L52-57

**当前值**:
```
SJ:  0.463 ± 0.007
FK:  0.455 ± 0.006
EM:  0.460 ± 0.008
VC:  0.458 ± 0.003
LP:  0.310 ± 0.005
```

**统一管道 (2/3 seeds available)**:
| Signal | seed42 | seed456 | 论文3-seed mean | 差异 |
|--------|--------|---------|----------------|------|
| SJ | 0.4836 | 0.4734 | 0.463 | 论文偏低 ~0.015 |
| FK | 0.4752 | 0.4690 | 0.455 | 论文偏低 ~0.017 |
| EM | 0.4818 | 0.4752 | 0.460 | 论文偏低 ~0.018 |
| VC | 0.4746 | 0.4722 | 0.458 | 论文偏低 ~0.015 |
| LP | 0.3136 | 0.3099 | 0.310 | 基本一致 |

**问题**: 论文 3-seed mean 系统性低于统一管道两个 seed 的值（一致性信号低 ~0.015-0.018，LP 无差异）。推测论文使用了与统一管道不同的计算路径。需用统一管道重算 3 seed 并更新此表。seed123 的统一值不在 JSON 中，需补算。

### 2. Table tab:robustness — Qwen SciERC N=16 section

**文件**: `sections/appendix.tex`, L47-50

**当前值**:
```
SJ N=16: 0.411 (3-seed mean)
FK N=16: 0.283
```

**统一管道 seed456**: SJ=0.4098 (Δ=-0.004), FK=0.2723 (**Δ=-0.073**)
**影响**: FK 3-seed mean 可能从 0.283 降至 ~0.259。

### 3. Table tab:n-scaling — Qwen SciERC 3-seed

**文件**: `sections/appendix.tex`, L582-596

**当前值**: FK N=8: 0.2536, N=16: 0.2833, Δ: +0.0297
**影响**: 若 FK N=16 3-seed mean 降至 ~0.259，Δ 从 +0.030 降至 ~+0.005。

### 4. Table tab:quality_estimation (Table 1) — CoNLL (LLaMA) N=8

**文件**: `sections/experiments.tex`, L38-42

**当前值**: VC .426, SJ .431, FK .428, EM .431, LP .307
**状态**: 统一 JSON 不含 N=8 数据，需用统一管道重算验证。

### 5-6. tab:sigma-comparison 和 tab:ranking-stability

需用统一管道全部 seed 重算。

---

## 正文引用 (按优先级)

### 高优先级
- appendix.tex L53-54: "SJ ρ=0.463±0.007 vs. LP 0.310±0.005, Δ=+0.153" → 统一管道 Δ 增大至 ~+0.170
- appendix.tex L86: 同上
- appendix.tex L78-79: FK N-scaling 具体数值需更新
- appendix.tex L138: conditional EM CoNLL LLaMA 3-seed (ρ=0.462) 需更新
- appendix.tex L191-193: N=8 + N=16 混合引用

### 需 N=8 数据验证
- experiments.tex L71: SJ 0.431 (LLaMA CoNLL N=8)
- appendix.tex L85-86: SJ 0.431 (LLaMA) vs. 0.436 (Qwen)
- limitations.tex L15: SJ-FK gap 0.003

### 中优先级
- experiments.tex L140: Δρ 范围 +0.135 to +0.175
- discussion.tex L6: SJ/VC N=16 Δ=0.002, σ 值

---

## 排名变化

### LLaMA CoNLL N=16
- **旧 Registry**: FK (0.81) >> SJ (0.18) — FK 主导
- **论文当前**: SJ (0.463) > EM > VC > FK (0.455) > LP
- **统一 seed42**: SJ (0.484) > EM (0.482) > FK (0.475) ≈ VC (0.475) > LP (0.314)
- **统一 seed456**: EM (0.475) > SJ (0.473) > VC (0.472) > FK (0.469) > LP (0.310)

### Qwen SciERC N=16
- FK 从 SJ 的 83% 降至 66%，可能与 LP 交换排名

---

## 核心 Claim 影响评估

| Claim | 影响 | 说明 |
|-------|------|------|
| Correlation-selection gap | ✅ 不受影响 | 基于 SciERC N=8，不在修正范围 |
| Difficulty-dependent complementarity | ⚠️ 需验证 | N=8 LLaMA CoNLL 排名可能变化 |
| Signal stability across models | ⚠️ 需 N=8 数据 | Δ=0.005 可能变化 |
| Structural advantage over LP | ✅ 加强 | 统一管道下差距更大 |
| Uniform N-scaling | ⚠️ 需全面重算 | 依赖 N=8 和 N=16 |
| FK N-scaling on SciERC | ❌ 可能失效 | Δ 从 +0.030 降至 ~+0.005 |
| SJ-FK gap is 0.003 | ⚠️ 需 N=8 验证 | Gap 可能扩大 |

**核心结论**: 论文核心贡献不受影响。主要影响在 appendix robustness/N-scaling 分析和 FK 相关 claim。

---

## 建议行动

1. 重算全部 3 seed 统一 ρ for LLaMA CoNLL N=16
2. 重算全部 3 seed 统一 ρ for Qwen SciERC N=16
3. 重算 LLaMA CoNLL N=8 统一 ρ
4. 更新所有衍生统计量
5. 审查正文 claim 与更新数值一致性
