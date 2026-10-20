# Memory

## 方向性分析统一 n=166 (2026-05-25, Director 决策)

**非全票问题数量统一为 166/204 (81.4%)**。原 `minority_constraint_direction.json` 使用 n=148（丢弃了 18 个含自由文本 trace 的问题），Director 决策将自由文本 trace 视为 minority。修改 `scripts/minority_constraint_direction.py` 第64-73行。

**关键指标变化极小**: minority-exclusive ratio 73.58% → 73.5%（Δ=−0.08pp）。论文统一引用 166/204 和 73.5%。

## D061 统一决策 (2026-05-22, D153)

**所有表统一用 r11_canonical (ID_FIX 后) 数据**：SC=39.33% (236/600)。39.17% 是 pre-ID_FIX 旧值，已从论文中彻底清除（0 残留）。

## vLLM 启动教训 (2026-05-22)

**启动 vLLM 后必须加 readiness check 再执行实验脚本。**

**多种子实验必须统一代码路径**：所有种子用 `run_cross_dataset_replication.py`，不用 `run_full_mvp.py`。

## NLI Combo 实验设置参考 (2026-05-22)

- Mistral-7B PW combo: SC weight=w, NLI weight=1, DeBERTa-large-MNLI verifier
- FT DeBERTa: microsoft/deberta-large-mnli fine-tuned on ProofWriter OWA depth-5 (69,810 samples, 2 epochs, 99.67% accuracy)
- Combo tiebreaking: `sorted(tied_c)[0]` (D061 alphabetical)

## 多种子最终数据 (2026-05-24 更新)

**LLaMA-8B PW (4 seeds, 全部完成, 全部 p<.001***)**:
| seed | SC% | SICA% | Δ(pp) |
|------|-----|-------|-------|
| 42 | 72.50 | 65.00 | −7.50 |
| 123 | 71.33 | 64.00 | −7.33 |
| 456 | 71.67 | 66.17 | −5.50 |
| 789 | 71.17 | 66.50 | −4.67 |
| mean±std | 71.67±0.59 | 65.42±1.14 | −6.25±1.34 |

注意: seed123 SICA alphabetical 修正 64.17%→**64.00%** (Reviewer 确认)。seed789 SICA 修正 66.17%→**66.50%**。seed456 完整数据在 westd-30973。

**Mistral-7B PW (4 seeds)**:
- SC 39.70±0.85, SICA 37.42±0.83, Δ −2.29±0.95pp

**Qwen2.5-14B PW (4 seeds)**:
- SC 73.25±0.74, SICA 71.62±0.63, Δ −1.63±0.76pp
- seed123 SICA 修正: 71.17% → 70.83% (alphabetical)

**Qwen3-14B PW (4 seeds, 全部完成, tiebreaking 已确认 alphabetical)**:
| seed | SC% | SICA% | Δ(pp) |
|------|-----|-------|-------|
| 42 | 85.83 | 85.67 | −0.17 |
| 123 | 85.17 | 86.50 | +1.33 |
| 456 | 84.50 | 86.83 | +2.33 |
| 789 | 85.50 | 85.67 | +0.17 |
| mean±std | 85.25±0.57 | 86.17±0.59 | +0.92±1.14 |

注意: seed123/456/789 已经使用 alphabetical tiebreaking（SelfConsistency 类已修复），tiebreaking worker 确认 0 mismatch。seed42 的 Table 1 canonical 值也是修正后的。Δ 方向与其他模型不同——Qwen3 多种子均值为正（+0.92pp），支持 capability-dependent framing。

**seed42 行用 Table 1 canonical 数据**:
- Mistral: SC=39.33, SICA=36.50, Δ=−2.83, p=.014*
- LLaMA: SC=72.50, SICA=65.00, Δ=−7.50, p<.001***
- Qwen2.5: SC=74.00, SICA=71.50, Δ=−2.50, p=.011*
- Qwen3: SC=85.83, SICA=85.67, Δ=−0.17, p=1.000

## Tiebreaking 全面审计 (2026-05-24 更新)

代码级确认: SelfConsistency 类在 exp033(seed42)后已修复为 alphabetical。所有多种子实验（Mistral/LLaMA/Qwen2.5/Qwen3 seed123/456/789）均使用修复后代码，0 mismatch。exp033(seed42) 有 9 个 tie 受影响，Table 1 已用修正值。

## Fleiss' κ Trace 冗余度量化 (2026-05-24, Qwen3-14B × PW)

**12 条 traces 的 Fleiss' κ ≈ 0.78（substantial agreement），K_eff ≈ 1.25。**

4 seeds 全部一致:
| seed | N | κ | K_eff |
|------|---|---|-------|
| 42 | 599 | 0.7872 | 1.24 |
| 123 | 583 | 0.7849 | 1.25 |
| 456 | 582 | 0.7820 | 1.25 |
| 789 | 584 | 0.7779 | 1.26 |
| mean±std | — | 0.7830±0.0035 | — |

解读: 12 条 self-consistency traces 的有效独立样本数仅 ~1.25，即 traces 几乎完全冗余。量化支撑 SCB 的"self-extracted constraints project model bias"论点——自抽取约束不提供独立验证信号。

答案分布: Unknown ~44%, True ~28%, False ~28%。

## High-CV SICA-SC Agreement (2026-05-24, Mistral-7B × FOLIO-204 exp033)

**高 constraint yield 波动（CV>0.5）的 18 个问题上，SICA 与 SC 答案 100% 一致（18/18）。全局 agreement 91.7%（187/204）。**

解读: 即使在约束提取数量波动最大的问题上，SICA 最终判断也不偏离 SC——约束的数量变化不影响最终预测，进一步证实自抽取约束不提供独立验证信号。配合 SF7 CV 分析（91.2% 问题 CV<0.5）和 Fleiss' κ（K_eff≈1.25），构成 SCB 多维证据链。

## R21 MF2 分析结论 (2026-05-23, Mistral×FOLIO exp033)

**SCB 是 compound phenomenon，不能被还原为单一 CoT bias propagation。**

核心数据:
- 92.2% 问题有跨 answer-group 共享约束公式 → 约束非 trace-specific 孤立产物
- per-trace 约束密度一致: 多数票 6.0, 少数票 5.9 → 提取层无偏差
- MaxSAT 排除率一致: 0.185 vs 0.172 → 无系统性排斥少数票
- volume 放大倍率 ≈ 1.0x → 纯 trace count 驱动
- 68 个少数票正确问题中，SICA 82.4% 跟随多数票错误 → source-attribution 阻止自纠正

三层机制: CoT(trace分布) → Source-Attribution(绑定) → MaxSAT(volume优势转分数)
数据: `westd-16639:results/exp033_mistral_7b_folio204/r21_mf2_scb_vs_cot_analysis.json`

## SF7 Constraint Yield CV (2026-05-23, Mistral×FOLIO exp033)

Observation 1 uniform yield 假设 **SUPPORTED**: per-problem CV median=0.2572 < 0.3。
- 64.2% 问题 CV<0.3, 91.2% CV<0.5
- WARNING: incorrect traces 多产约束 (6.05 vs 5.41, +11.9%, p=5.3e-11)，但效应量小不影响结论
数据: `westd-16639:results/sf7_constraint_yield_cv.json`

## 磁盘状态 (2026-05-23)

- westd-16639: 根 40%, 数据盘 66% (121G free)
- westd-30973: 根 42%, 数据盘 22% (195G free). 全部 GPU 已释放

## Blackwell GPU 注意事项

vLLM 启动需要 `VLLM_USE_FLASHINFER_SAMPLER=0` + `--enforce-eager`。

## Cross-model SC Ablation Framing 约束 (2026-05-23, Reviewer R19)

措辞限定为 "NLI combo 不可完全归约为 ensemble diversity"，不要 overclaim "proves structural independence"。

## Table 3 Tiebreaking 记录 (2026-05-23)

NLI combo 结果文件中 sc_baseline 使用 Counter.most_common()，论文 Table 3 使用 alphabetical。两者数值不同但论文值正确。
