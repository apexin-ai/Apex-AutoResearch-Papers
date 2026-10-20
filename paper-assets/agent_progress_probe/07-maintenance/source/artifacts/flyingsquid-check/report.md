# FlyingSquid 段落完整性与数据一致性检查报告

## Registry 权威数据

**baseline_flyingsquid:**
| 字段 | 值 |
|------|-----|
| conf2_vs_mv_agreement | 1.0 |
| full_data_vs_mv_agreement | 0.8204 |
| divergent_windows | 9,841 |
| divergence_pattern | all progress→stagnation |
| mv_progress_rate | 0.715 |
| fs_progress_rate | 0.536 |

**tlm-comprehensive-comparison → flyingsquid:**
| 字段 | 值 |
|------|-----|
| self_f1 | 0.8186 |
| mv_agreement | 0.82 |
| conf2_f1 | 0.7816 |
| mv_all_f1 (downstream probe) | 0.7343 |
| delta_conf2_pp | -11.3 |
| divergent_pattern | all progress→stagnation |
| n_divergent | 9,841 |

---

## 逐处核对

### 1. experiments.tex Table 5 (line 255) — FlyingSquid 行

| 列 | 论文值 | Registry 值 | 一致性 |
|----|--------|-------------|--------|
| MV Agr. | 0.820 | 0.82 (baseline: 0.8204) | **一致** |
| Conf≥2 F1 | 0.7820 | 0.7816 | **微偏** (+0.0004) |
| Δ vs MV | -11.3 pp | -11.3 | **一致** |
| Probe F1‡ | --- (未评估) | 0.7343 (已有数据) | **数据未报告** |

### 2. experiments.tex line 238
> "two generative i.i.d. models (FlyingSquid, Snorkel MeTaL)"

- 分类正确，引用正确。**一致**。

### 3. experiments.tex lines 271–273
> "FlyingSquid, a closed-form triplet-based model, drops 11.3 pp below MV."

- -11.3 pp → Registry delta_conf2_pp: -11.3。**一致**。

> "On the full dataset, agreement with MV is 82%"

- 82% → Registry: baseline 0.8204, tlm 0.82。**一致**（82% 为四舍五入值）。

> "all divergent labels flip progress→stagnation, introducing systematic stagnation bias"

- Registry: "all progress->stagnation"。**一致**。
- n_divergent=9,841 未在正文提及（仅在 registry 中有记录）。**缺失但非错误**。

### 4. experiments.tex lines 273–274 (Snorkel 对比)
> "Snorkel MeTaL fails catastrophically (−63.6 pp), with only 42.3% MV agreement."

- Registry: snorkel conf2_f1=0.2582, MV conf2_f1=0.8946 → Δ = -63.6 pp。**一致**。
- Registry: snorkel mv_agreement=0.423。**一致**。

### 5. experiments.tex line 275
> "Both models assume conditional independence among LFs—an assumption violated by the shared behavioral signals..."

- 与 registry finding 一致："Both generative label models assume i.i.d."。**一致**。

### 6. analysis.tex line 72
> "FlyingSquid and Snorkel MeTaL assume conditional independence."

- **一致**，与实验节叙述一致。

### 7. analysis.tex line 77
> "FlyingSquid (−11.3 pp) introduces systematic stagnation bias"

- -11.3 pp。**一致**。

> "Snorkel MeTaL collapses catastrophically (−63.6 pp, 42.3% MV agreement)"

- **一致**。

### 8. conclusion.tex line 18
> "FlyingSquid, Snorkel MeTaL)—all fail to surpass majority vote; Snorkel MeTaL collapses catastrophically (−63.6 pp)."

- **一致**。未提及 FlyingSquid 具体数字，仅作为列表成员。合理。

### 9. introduction.tex line 43–44
> "FlyingSquid, Snorkel MeTaL)—all fail to surpass majority vote on downstream detection."
> "Snorkel MeTaL collapses catastrophically (−63.6 pp)."

- **一致**。

### 10. related_work.tex line 23
> "Fu et al. accelerate label model inference via closed-form triplet methods"

- FlyingSquid 方法描述正确。**一致**。

---

## 不一致之处汇总

| # | 位置 | 问题 | 论文值 | Registry 值 | 严重程度 |
|---|------|------|--------|-------------|----------|
| 1 | experiments.tex Table 5, Conf≥2 F1 | 四位小数不匹配 | 0.7820 | 0.7816 | **低**（四舍五入可解释为 0.782 vs 0.782，但末位 0 vs 6 不同） |
| 2 | experiments.tex Table 5, Probe F1‡ | Registry 有下游 probe 数据但未报告 | --- | 0.7343 | **低**（编辑选择，非数据错误） |

### 关于 #1 的详细说明
Registry conf2_f1 = 0.7816。论文写 0.7820。若取三位小数，两者均为 0.782。但论文刻意写到四位小数 0.7820，与 registry 0.7816 存在 0.0004 的差异。可能原因：(a) 早期实验运行结果为 0.7820，后被 tlm-comprehensive-comparison 重跑更新为 0.7816；(b) 不同随机种子或评估代码版本。建议统一为 registry 最终值 0.7816。

---

## 叙述完整性检查

| 检查项 | 是否覆盖 | 位置 |
|--------|---------|------|
| Snorkel 对比 | **是** | experiments.tex L274, analysis.tex L77, conclusion L18, intro L43 |
| Divergent pattern (全部 progress→stagnation) | **是** | experiments.tex L272 |
| Divergent 数量 (n=9,841) | **否** | 仅存在于 registry，论文未报告具体数量 |
| i.i.d. assumption 违反问题 | **是** | experiments.tex L275, analysis.tex L78 |
| Conf≥2 完全一致 (agreement=1.0) | **否** | registry baseline_flyingsquid 记录 conf2_vs_mv_agreement=1.0，论文未明确提及此点 |
| 系统性 stagnation bias | **是** | experiments.tex L272, analysis.tex L77 |
| mv_progress_rate / fs_progress_rate | **否** | registry 记录 0.715 vs 0.536，论文未报告进展率差异 |
| 下游 probe F1 = 0.7343 | **否** | registry 有数据，论文表中标 "---" |
| Root cause: insufficient inter-LF conflict | **是** | experiments.tex L276-280, analysis.tex L73-83 |

---

## 建议

1. **Table 5 Conf≥2 F1**: 将 0.7820 修正为 0.7816（与 registry 对齐），或简化为三位小数 0.782。
2. **考虑补充 n_divergent=9,841**: 在正文 "all divergent labels flip progress→stagnation" 后加 "(9,841 windows, 18.0% of total)"，增强定量说服力。
3. **考虑补充 conf≥2 完全一致**: baseline_flyingsquid 在 conf≥2 子集上与 MV 100% 一致，这是一个重要发现——说明 FS 的系统偏差完全集中在低置信度窗口。当前论文未提及此点。
4. **下游 probe F1 (0.7343)**: 如果已有实验数据，可在 Table 5 中补充，强化 "FS labels hurt downstream" 的论证。同理 Snorkel (0.3768) 和 Lag-HMM (0.7496) 也有未报告的下游数据。
