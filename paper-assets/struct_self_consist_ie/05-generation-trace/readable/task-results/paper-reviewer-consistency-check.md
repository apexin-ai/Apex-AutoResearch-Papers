# paper reviewer consistency check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reviewer_consistency_check_20260515T031759_result.json`
- **Structured JSON:** [`4003ed6910e259d299d3.json`](../../sessions/40/4003ed6910e259d299d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data needed. Here's the full consistency audit report.

---

## 全文一致性审查报告

### 1. 数值一致性

- [PASS] **SciERC NER Voting ρ=0.379**: Abstract (ρ=0.38 rounded), intro:20 (ρ=0.38), experiments:35 (.379), experiments:61 (0.379), discussion:4 (0.38), conclusion:8 (0.38), related_work:10 (0.38). 所有引用一致。

- [PASS] **SciERC NER SJ ρ=0.360**: experiments:36 (.360), experiments:61 (0.360), appendix:47 (0.360). 一致。

- [PASS] **EM AUROC=0.749**: Abstract (0.75 rounded), intro:20 (0.75), intro:37 (0.75), experiments:38 (.749), experiments:64 (0.749), experiments:67 (0.749), discussion:4 (0.749), discussion:16 (0.749), conclusion:8 (0.75). 一致。

- [PASS] **logprob ρ=0.205**: experiments:39 (.205), experiments:61 (0.205). 一致。

- [PASS] **Selection NER: logprob F1=0.650, greedy=0.644, oracle=0.776, p=0.39**: experiments:105-113 (table), experiments:123-124 (text), conclusion:9 (+0.6 pp, p=0.39). 一致。Oracle headroom 0.776−0.644=0.132=13.2 pp ✓.

- [ISSUE] **Selection RE: cross-selection table 与主表/正文矛盾**
  1. **位置**: `appendix.tex:175` (tab:cross_selection)
  2. **当前内容**: `Qwen SciERC RE N=8 | .404 | .410 | +.006 | ---`
  3. **应该是**: Best ≤ .404, Δ ≤ 0（与主表一致）
  4. **严重程度**: **CRITICAL**
  
  主 selection 表 (`experiments.tex:107-112`) 显示 RE 最佳信号 Log-prob=0.395 < Greedy=0.404。正文 (`experiments.tex:125`) 明确说 "On RE, the gap is complete: no signal exceeds greedy (0.404)"。Conclusion (`conclusion.tex:9`) 写 "RE: −0.9 pp"（0.395−0.404=−0.009）。但 cross-selection 表却显示 Best=.410, Δ=+.006，直接矛盾。

- [PASS] **WNUT-17 voting ρ=0.724, AUROC=0.913, conditional ρ=0.038**: experiments:78, appendix:139, WNUT table (appendix:152). 一致。Conditional p=0.49 标记 "n.s." ✓.

- [PASS] **WNUT-17 SJ ρ=0.089 (p=0.020)**: experiments:79, WNUT table (appendix:154). 一致。

- [PASS] **N=16 3-seed (LLaMA CoNLL)**: SJ .463±.007, FK .455±.006, EM .460±.008, Voting .458±.003, Logprob .310±.005. Quality estimation table (experiments:42-46) = robustness table (appendix:53-57). 完全一致。

- [PASS] **Bootstrap CI SJ−logprob**: experiments:65 报 Δρ=+0.155 [+0.074, +0.234]，与 checklist 值 +0.1547 [+0.0737, +0.2340] 一致（3位小数 rounded）。

- [PASS] **N=16 SJ improvement +0.052**: Robustness table SJ N=8=0.360 → N=16=0.412, Δ=0.052. experiments:139, limitations:12, appendix:75, appendix:186 均为 +0.052。

- [PASS] **Length-logprob correlation**: discussion:23 (NER ρ=0.39, RE ρ=0.33) = appendix:116 (0.386, 0.326) rounded。0.386→0.39 ✓, 0.326→0.33 ✓.

- [PASS] **Oracle headroom 13-18 pp**: NER 13.2 pp, RE 18.1 pp. Abstract, intro:21, intro:41, conclusion:9 均写 "13-18 pp". ✓

### 2. Claim 强度

- [PASS] **"structural signals dominate"**: SciERC NER: Voting(0.379) > SJ(0.360) > EM(0.295) > FK(0.267) > logprob(0.205)。两个 structural 信号均胜过所有其他信号。Bootstrap CI (experiments:65-66) 确认 SJ−logprob 差异显著。N=16 四个设置均成立 (experiments:140, Δρ=+0.135 to +0.175)。Claim 有充分支持。

- [PASS] **"correlation-selection gap" is null result**: 全文一致使用 "no signal reliably surpasses greedy"，p=0.39, 未出现 "significantly outperforms"。

- [PASS] **"ρ-AUROC dissociation"**: experiments:67-69 EM leads AUROC but ranks 3rd/last in ρ. discussion:16 确认。CoNLL logprob AUROC=0.761 but lowest ρ=0.307 (experiments:71) 提供跨数据集验证。

- [ISSUE] **"corresponding AUROC of 0.749" 归属模糊**
  1. **位置**: `experiments.tex:64`
  2. **当前内容**: "While ρ=0.38 explains approximately 14% of F1 variance, the corresponding AUROC of 0.749..."
  3. **应该是**: ρ=0.38 来自 Voting，AUROC=0.749 来自 EM（不同信号）。"corresponding" 暗示同一信号，但 Voting 的 AUROC=0.684。建议改为 "while the best AUROC reaches 0.749 (EM)" 或类似表述以消除歧义。
  4. **严重程度**: **WARNING**

- [PASS] **Ensemble AUROC (0.666) < EM (0.749)**: 论文未提及 ensemble AUROC 0.666，无正面 framing。PASS。

- [PASS] **WNUT-17 as capability boundary**: experiments:79 "suggesting a capability boundary", intro:45 "when model capability is insufficient", conclusion:10 同。一致使用 "boundary" 框架而非 "method failure"。

### 3. 交叉引用完整性

- [PASS] **所有 \ref{} 均有对应 \label{}**: 核查 22 个 \ref 引用，均有对应 label。包括 fig:overview, tab:quality_estimation, tab:selection, tab:robustness, tab:wnut, tab:cross_selection, fig:signal_heatmap, fig:selection_gap, fig:temperature_robustness, fig:reliability, fig:length_logprob_scatter, tab:notation, 以及所有 section/appendix 引用。

- [PASS] **所有 \cite{} 均有 bib 条目**: 核查 48 个 citation key，全部存在于 references.bib。

- [PASS] **所有 figure 文件存在**: figures/ 目录包含 fig_overview.pdf, fig_signal_heatmap.pdf, fig_selection_gap.pdf, fig_temperature_robustness.pdf, fig_reliability.pdf, fig_length_logprob_scatter.pdf。

### 4. 公式一致性

- [PASS] **六个公式均定义于 method.tex**: eq:logprob (L21), eq:em (L27), eq:fk (L33), eq:sj (L42), eq:sj_instance (L47), eq:voting (L54)。

- [PASS] **SJ 定义一致**: method.tex:41-45 定义 Hungarian algorithm + token-level IoU。experiments:16 使用 "exact span matching" 区分评估指标 (F1) 与信号计算 (SJ)，无混淆。

- [PASS] **信号分类一致**: 三族五信号 (structural: Voting, SJ; surface: EM, FK; model-internal: logprob) 在 abstract, intro:31, method:16, conclusion:4 中分类一致。

### 5. 结构完整性

- [PASS] **Abstract 覆盖所有 core findings**:
  - structural > logprob: L6 "structural signals dominate hard tasks" ✓
  - ρ-AUROC dissociation: L4 "ranking and classification favoring different signals" ✓
  - correlation-selection gap: L4-5 "does not translate into selection gains" ✓
  - WNUT-17 boundary: L6 "when model capability is insufficient" ✓

- [PASS] **Conclusion 与 findings 对齐**: 三个 anchor findings (quality estimation, correlation-selection gap, task-complexity boundary) 均有对应段落。

- [PASS] **Limitations 诚实**: 单一 RE 数据集 (L1), 两个模型家族 (L3-5), 无 trained verifier (L8-9), N≤16 (L11), SJ-FK gap on CoNLL only 0.003 (L14), logprob temperature sensitivity uncharacterized (L15)。覆盖全面。

### 6. 已知问题检查

- [PASS] **exp_012 (512 截断) 数据未出现**: 论文中无 512 truncation 或 exp_012 的引用。

- [PASS] **Selection 未写 "significantly outperforms"**: 所有 selection 讨论使用 "not statistically significant", "no signal reliably surpasses", p=0.39。

- [PASS] **Ensemble 未正面 framing**: 论文不讨论 ensemble AUROC。

- [ISSUE] **CoNLL ">91%" claim 对 Qwen 不成立**
  1. **位置**: `experiments.tex:10` 和 `experiments.tex:74`
  2. **当前内容**: L10: "where models achieve >91% micro F1"; L74: "On CoNLL (greedy F1>0.91)"
  3. **应该是**: Qwen CoNLL greedy F1 = 0.908 (90.8%), 不满足 >91%。LLaMA=0.924 满足。建议改为 ">90%" 或 "≈91%" 或 "90.8--92.4%"。
  4. **严重程度**: **MINOR** (0.908 ≈ 0.91, 不影响结论)

---

## 汇总

| 类别 | PASS | ISSUE |
|------|------|-------|
| 数值一致性 | 12 | 1 CRITICAL |
| Claim 强度 | 5 | 1 WARNING |
| 交叉引用 | 3 | 0 |
| 公式一致性 | 3 | 0 |
| 结构完整性 | 3 | 0 |
| 已知问题 | 3 | 1 MINOR |
| **合计** | **29** | **1 CRITICAL, 1 WARNING, 1 MINOR** |

**需修复**:
1. **CRITICAL**: `appendix.tex:175` — cross-selection table RE 行 (Best=.410) 与主表及正文 (Best=.395, Δ=−0.9 pp) 矛盾。需修正为与 tab:selection 一致的值。
2. **WARNING**: `experiments.tex:64` — "corresponding AUROC of 0.749" 暗示与 ρ=0.38 来自同一信号 (Voting)，但实际来自 EM (Voting AUROC=0.684)。
3. **MINOR**: `experiments.tex:10,74` — ">91%" 对 Qwen CoNLL (90.8%) 不成立。

---
