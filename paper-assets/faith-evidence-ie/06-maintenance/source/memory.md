## 全 scale evidence tax 汇总 (test_revised, 500 docs, RSFT CED k=1)

### 1.7B (Qwen3) — 1 seed
| Seed | with-evi | no-evi | Tax (pp) |
|------|----------|--------|----------|
| s42  | 0.2933   | 0.2390 | −5.43    |

注：仅 s42 有 test eval（test_eval_1_7b_rsft_s42 + test_eval_1_7b_rsft_s42_no_evi）。无 s43/s44 test eval。

### 4B (Qwen3) — 3 seeds ✅
| Seed | with-evi | no-evi | Tax (pp) |
|------|----------|--------|----------|
| s42  | 0.2503   | 0.2654 | +1.51    |
| s43  | 0.2503   | 0.2702 | +1.99    |
| s44  | 0.2525   | 0.2671 | +1.46    |
| **mean** | **0.2510** | **0.2676** | **+1.65 ± 0.29** |

### 8B (Qwen3) — 3 seeds ✅
| Seed | with-evi | no-evi | Tax (pp) |
|------|----------|--------|----------|
| s42  | 0.3353   | 0.3319 | −0.34    |
| s43  | 0.3398   | 0.3224 | −1.74    |
| s44  | 0.3329   | 0.3264 | −0.65    |
| **mean** | **0.3360** | **0.3269** | **−0.91 ± 0.74** |

### 14B (Qwen3) — 2 seeds ✅
| Seed | with-evi | no-evi | Tax (pp) |
|------|----------|--------|----------|
| s42  | 0.3849   | 0.3926 | +0.77    |
| s43  | 0.3767   | 0.3775 | +0.08    |
| **mean** | **0.3808** | **0.3851** | **+0.43 ± 0.49** |

注：14B s43 ign_f1 均低于 s42（with-evi -0.82pp, no-evi -1.51pp），seed 间存在方差但 tax 方向一致（均为正）。

### LLaMA 8B — 2 seeds ✅ (v3/v2 修正数据)
| Seed | with-evi | no-evi | Tax (pp) |
|------|----------|--------|----------|
| s42  | 0.3554 (v3) | 0.3380 (v2) | −1.74    |
| s43  | 0.3488   | 0.3371 | −1.17    |
| **mean** | **0.3521** | **0.3376** | **−1.46 ± 0.40** |

注：s42 原始数据被污染（旧 eval 代码 field_compliance=176/500），v3 with-evi 和 v2 no-evi 均用当前版本代码+batch_size=16 重跑。修正后 tax 从 −1.91±1.05 变为 −1.46±0.40（方差大幅缩小，数据质量改善）。

### 趋势
- 1.7B/8B/LLaMA 8B: evidence tax 为负（evidence 帮助），1.7B 最显著（−5.43pp）
- 4B/14B: evidence tax 为正（4B +1.65±0.29, 14B +0.43±0.49），evidence 反伤但 14B 幅度极小
- 修正后 LLaMA tax 方差从 1.05 降至 0.40，跨 seed 一致性显著改善

## DPO rebuilt eval (matched@2048, dev)
- 1ep: ign_f1=0.3223, Rel-F1=33.38, Evi-F1=80.90, EDCR=0.8123
- 3ep: ign_f1=0.3076, Rel-F1=31.45, Evi-F1=84.84, EDCR=0.7503
- **3ep 确认过拟合**：ign_f1 下降 1.47pp（0.3223→0.3076），Evi-F1 上升但 Rel-F1 下降更大
- DPO 劣于 SFT baseline (ign_f1≈39.7%) 和 RSFT CED (ign_f1=44.67%)
- Decoupling spectrum: DPO 展现 gradual decay（Rel-F1 单调下降 33.38→31.45，Evi-F1 上升 80.90→84.84）

## LLM baseline numbers (2026-05-23 调研)
- AutoRE (dev, ign_f1): 52.14 (第三方复现)
- RelPrior (dev, ign_f1): 55.50 (当前 LLM SOTA)
- GLiDRE 不是 LLM 方法 (encoder-based)，不列入 LLM baseline

## 14B RSFT s43 pipeline
- Generation: DONE (24,216 candidates, 99.9% format compliance)
- CED scoring: DONE (3,017 top_k=1 examples, combined_score_mean=0.766)
- Training: DONE (loss=0.5076, 567 steps)
- Test eval: DONE (with-evi ign_f1=0.3767, no-evi ign_f1=0.3775, tax=+0.08pp)
- Dev eval: RUNNING (cuda:0 with-evi, cuda:2 no-evi, ETA ~19:30 UTC)
