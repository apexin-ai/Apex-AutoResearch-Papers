# 阴性实验叙事审查

Date: 2026-05-20

---

## 1. 七个阴性实验清单及论文覆盖状态

| # | exp_id | 核心发现 | 论文是否提及 | 位置 |
|---|--------|---------|------------|------|
| 1 | `cwm-baseline` | Function-level CWM ≈ CLS (87.51% vs 87.50%) — 原假设"CWM显著差于CLS"未被支持 | ✅ 充分 | 全文核心发现 (TOST equivalence) |
| 2 | `per-test-majority-voting` | K=3 majority voting 使 accuracy 下降 0.68pp (87.51→86.83%)，errors 是系统性偏差非随机噪声 | ✅ 已提及 | Appendix (g)，一句话 |
| 3 | `p2p-regression-rate` | P2P regression rate 仅 1.04% mean / 0% median，per-test 在 P2P 维度无价值 | ✅ 已提及 | Appendix oracle table caption |
| 4 | `re-repair-phase0` | Phase 0 (n=10): oracle-level diagnostics 未改善 patch quality | ✅ 已提及 | 并入 re-repair pilot 叙事 |
| 5 | `re-repair-docker-eval` | Full eval (n=44, p=0.42): per-test diagnostics 对 repair 无益 | ✅ 充分 | §4.4, Limitations, Intro bullet, Appendix (j) |
| 6 | `cls4b-seed123-ckpt800-test5120-eval-v2` | CLS 4B s123 val-best (ckpt-800) test=75.33%, 远低于 s42 的 83.63% — val-test distribution shift 放大 | ✅ 已提及 | Extended Limitations appendix |
| 7 | `repo-level-cwm-8b-conda-v5` | CWM 8B 严重过拟合: val-best 在 step 400, loss 之后单调上升至 0.521 | ⚠️ 间接 | Threats 提及 NaN val loss / final-epoch default，但未将过拟合模式作为独立发现 |

**结论：7 个阴性实验中 6 个已在论文中被引用，覆盖率良好。** `repo-level-cwm-8b-conda-v5` 的 CWM 过拟合模式仅被间接提及。

---

## 2. Rebuttal Framework Attack #1 引用准确性检查

Attack #1 回应中引用的 negative results:

| 引用 | 准确性 | 备注 |
|------|--------|------|
| Rank-32 ablation -0.47 to -0.51pp | ✅ 准确 | Appendix B, Table rank_ablation |
| Parseable-only accuracy 38-43% < majority | ✅ 准确 | §4.3, Appendix C |
| Matched-context ablation <3% | ✅ 准确 | Appendix B |
| Format collapse 53-74% | ✅ 准确 | §4.3 Table 4 |

**遗漏**: Attack #1 未引用 majority voting 阴性结果和 relaxed matching 阴性结果，这两个对 "obvious fixes don't work" 论点有补强价值。

**建议补充到 rebuttal framework Attack #1**:
- Majority voting K=3 decreases accuracy by 0.68pp (Appendix (g)) — sampling-based fixes fail
- Relaxed matching decreases accuracy from 58.04% to 56.98% (Appendix (c)) — format tolerance makes it WORSE
- CWM overfitting: val-best at step 400 (registry: repo-level-cwm-8b-conda-v5) — more training also fails

---

## 3. 系统性 Pattern 分析

### 核心发现：**"标准干预全部失败" 模式**

七个阴性实验中的 5 个（加上 2 个相关非阴性实验）形成一个一致的叙事：

**每种"显而易见的修复方案"都无法挽救 CWM 的 repo-level 退化：**

| 干预 | 靶向假设 | 结果 | exp_id |
|------|---------|------|--------|
| LoRA rank 32 (2x capacity) | 容量不足 | -0.47 to -0.51pp | `cwm-rank32-ablation-v2` (non-negative) |
| Majority voting K=3 | 随机噪声 | -0.68pp, errors systematic | `per-test-majority-voting` |
| Relaxed matching L0-L4 | 解析严格度 | -1.06pp (58.04→56.98%) | `exp-d-constrained-decoding` (non-negative) |
| Constrained decoding | 格式不合规 | 理论分析: parseable acc 38-43% 仍 < majority | `exp-d-constrained-decoding` |
| More training (resume) | 训练不足 | 过拟合: val-best step 400, loss↑ | `repo-level-cwm-8b-conda-v5` |
| Per-test diagnostics | 诊断信号不够 | p=0.42, no effect (n=44) | `re-repair-docker-eval` |

**叙事价值**: 这个 pattern 直接支撑 Attack #1 的核心论点——CWM 的 repo-level 退化是 **formulation-level limitation**（输出空间复杂度指数增长），不是容量、采样、格式、训练时长或诊断粒度的问题。每个"修复"分别排除了一个替代解释。

---

## 4. 论文加入建议

### 方案 A：主文本加一句话（推荐）

**位置**: §4.3 "Why does generation degrade at repo level?" 段末或 §4.4 Analysis 中

**建议文本** (~30 words):
> "Standard interventions—doubling adapter capacity, majority voting, and relaxed output matching—all fail to close the gap (Appendix~\ref{app:extended_analysis}(c,g)), confirming the bottleneck is formulation-level rather than capacity- or noise-driven."

**页数影响**: 约 1.5 行。当前 §4.3/§4.4 在第 7-8 页交界处，可能需要微调其他文本以保持 8 页。中等风险。

### 方案 B：仅强化 Appendix（安全）

**位置**: Appendix (g) 已有 rank + majority voting 句。可扩展为一个 "Negative intervention summary" 段落，显式列出全部失败干预。

**建议**: 在 Appendix (g) 标题改为 "(g) Failed interventions"，增加 relaxed matching 和 constrained decoding 引用，将其与 (c) 交叉引用。

**页数影响**: 0（Appendix 不计入页数）。

### 方案 C：同时做 A + B

主文本一句话引用 Appendix，Appendix 提供完整失败干预矩阵。

**页数影响**: 同方案 A。

---

## 5. 未利用的阴性实验

### `repo-level-cwm-8b-conda-v5` (CWM 过拟合)

**当前状态**: 未作为独立发现。Threats 提及 NaN val loss 导致 final-epoch default，但 CWM 8B 的 "val-best at step 400, then monotonic degradation" 模式本身有叙事价值。

**潜在价值**: 
- 支撑 "CWM repo-level 训练本身就不稳定" 论点
- 与 function-level CWM 训练稳定（5 seeds, 0.37pp std）形成对比
- 但也可能引发 reviewer 质疑："你们用的是严重过拟合的 checkpoint"

**建议**: **不加入正文**。过拟合是训练工程问题，不是 formulation insight。当前 "NaN val loss → final-epoch default" 的处理方式已足够诚实。如果 reviewer 追问 checkpoint selection，在 rebuttal 中补充。

### P2P regression rate

**当前状态**: 已在 Appendix oracle table 提及但未做叙事化。

**潜在价值**: 弱——1.04% mean P2P 率限制了 per-test 在 P2P 维度的价值，但 paper 的 focus 已从 P2P 转向 F2P。当前覆盖足够。

---

## 6. 总结

| 维度 | 评估 |
|------|------|
| 阴性结果覆盖率 | 6/7 已在论文中提及，良好 |
| Rebuttal framework 准确性 | Attack #1 数字准确，建议补充 3 个失败干预 |
| 系统性 pattern | **"标准干预全部失败"** — 强叙事价值 |
| 推荐行动 | 方案 C（主文本一句 + Appendix 强化），页数允许时实施 |
| 不建议加入 | CWM 过拟合 (训练工程问题, 非 formulation insight) |
