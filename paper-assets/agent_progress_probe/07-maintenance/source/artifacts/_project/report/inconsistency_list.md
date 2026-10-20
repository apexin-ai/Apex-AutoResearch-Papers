# Full Re-Audit: Inconsistency List (D050+D051 Framing Update)

Generated: 2026-05-15

---

## [Abstract] (sections/abstract.tex)

- **Line 6**: "stagnation signals are fundamentally structural" → 应改为 "zero-shot transfer dominance" framing [D039 pivot 已将 "fundamentally structural" 修正为 "zero-shot transfer dominance"，但 .tex 未更新]
- **Line 8**: "removing it improves fine-tuned F1 by 17.6 percentage points" → **INVALID — 删除此 claim** [D051: 标签 bug 产物。新数据下去掉 cmd_rep 是 -6.5pp（反转）。替换叙事为 label quality as transfer bottleneck + prevalence-matched ablation -29.4pp]
- **Line 8**: "OpenHands, where removing it improves fine-tuned F1 by 17.6 percentage points" → 整段关于 cmd_rep removal improving 的叙事需重写 [新叙事方向：label quality audit reveals cmd_rep's core value is coverage (-29.4pp when removed), precision 97.91%]

---

## [Introduction] (sections/introduction.tex)

- **Line 9**: "6.6\% of sliding windows exhibit stagnation" → 应改为 "21.45\%" [OH stag rate 修正：旧 embeddings.pt 错误]
- **Line 20**: "OpenHands (150,652 windows, 6.6\% stagnation)" → 应改为 "21.45\% stagnation" (或 20.87% excl abstain) [同上]
- **Line 28**: "Finding 1: Stagnation signals are fundamentally structural." → narrative 应修改为强调 "zero-shot transfer dominance" [framing pivot]
- **Line 29**: "0.751 after full fine-tuning on the target agent" → 应改为 "0.9763" [旧标签 probe FT 结果]
- **Line 29**: "surpassing the GRU embedding probe...0.9055 in-domain, 0.751 after full fine-tuning" → cross-agent gap 叙事需完全重写 [新值：probe FT = 0.9763，gap 仅 2.21pp 而非原来的巨大差距]
- **Line 37**: "92.2\% stagnation-vote rate produces a 71\% false positive rate on progress windows" → 应改为 "5.39\% fire rate" + "2.3\% FP rate / precision 97.91\%" [旧 embeddings 错误统计]
- **Line 38**: "Removing $\lambda_1$ from the OpenHands labeling pipeline improves fine-tuned probe F1 by 17.6\,pp" → **INVALID — 删除此 claim** [同 abstract]
- **Line 38**: "demonstrating that labeling functions validated on one agent architecture can become adversarial on another" → 叙事需修改 [cmd_rep 不再是 "adversarial"，而是高精度低召回检测器；旧结论完全是标签 bug 产物]

---

## [Method] (sections/method.tex)

- **Line 44**: "92.2\% of OpenHands windows" → 应改为 "5.39\%" [cmd_rep OH fire rate 旧定义（stag vote %）vs 新定义（actual fire rate）]
- **Line 65** (Table 1): OH Stag\% for $\lambda_1$ (cmd_rep) = "92.2" → 应改为 "5.39" (或 5.4) [同上]
- **Line 44**: "the elevated OH rate reflects differences in action distributions across agent architectures" → 叙事需修改 [新数据下 cmd_rep 在 OH 不再异常高频]

---

## [Experiments] (sections/experiments.tex)

- **Line 20**: "stagnation ratio of 6.6\%" → 应改为 "21.45\%" [OH stag rate 修正]
- **Line 32** (Table): OH Stag\% = "6.6" → 应改为 "21.45" (或 21.4) [同上]
- **Line 67** (Table 2): ProgressProbe OH columns "0.530" and "0.528" → 应改为 "0.5984" [probe ZS 新标签结果]
- **Line 68** (Table 2): "+ full OH fine-tune" = "0.7510" → 应改为 "0.9763" [probe FT 新标签结果]
- **Line 88**: "21.6\,pp above the probe fine-tuned on 100\% of OH data (0.751)" → 应改为 "2.21\,pp above the probe fine-tuned on 100\% of OH data (0.9763)" [cross-agent gap 计算错误——基于旧 probe FT]
- **Line 88**: "Structural GB transfers best, achieving 0.967 macro-F1" → 如果 structural GB 也重跑了（0.9984），此处需更新 [待确认新 structural GB 值]
- **Line 90**: "Both structural models recover to $>$0.99 on conf${\geq}$2 OH windows" → 可能需更新 [取决于新实验结果]
- **Line 92**: "probe's zero-shot transfer (0.530 on all windows, 0.528 on conf${\geq}$2) is near chance" → 应改为 "0.5984 on conf${\geq}$2" [新标签 ZS 结果]
- **Line 92**: "even full OH fine-tuning only reaches 0.751" → 应改为 "0.9763" [新标签 FT 结果]
- **Line 93**: "This asymmetry---structural features transfer naturally while learned embeddings do not---is a central empirical finding" → 叙事需修改 [新数据下 probe FT 0.9763 vs structural 0.9984，差距仅 2.21pp；asymmetry 在 zero-shot 仍存在但 FT 后消失]
- **Line 170**: "cmd\_rep LF votes stagnation on 92.2\% of OH windows (vs.\ 65.5\% on SWE-Agent), with a 71\% false positive rate on OH progress windows" → 应改为 "5.39\% of OH windows" + "2.3\% FP rate / precision 97.91\%" [旧 embeddings 错误]
- **Lines 171-195** (§5.5 Command Repetition Ablation): 整个 subsection 基于旧标签数据，需完全重写 [Table 3 数据全部无效：ZS 0.530→0.5984, FT 0.751→0.9763, +17.6pp→INVALID。新叙事：label quality as transfer bottleneck + prevalence-matched ablation -29.4pp + cmd_rep 是高精度低召回 coverage provider]

---

## [Analysis] (sections/analysis.tex)

- **Line 12**: "cmd\_rep votes stagnation on 92.2\% vs.\ 65.5\% of windows" → OH 值应改为 "5.39\%" [同上]

---

## [Conclusion] (sections/conclusion.tex)

- **Line 7**: "stagnation signals are fundamentally structural" → 应改为 zero-shot transfer dominance framing [同 abstract]
- **Line 12**: "Command repetition leads stagnation onset by 1.87 steps on SWE-Agent but reverses on OpenHands, where its high false-positive rate corrupts silver labels---removing it improves fine-tuned probe F1 by 17.6\,pp" → **INVALID — 删除 "high false-positive rate corrupts" + "removing improves 17.6pp" claim** [新叙事方向：temporal dynamics reveal agent-specific LF roles; label quality audit shows transfer bottleneck is label version bias, not LF noise]

---

## [Appendix] (sections/appendix.tex)

- **Line 67-68** (Table caption): references to cmd_rep having opposite effects → 叙事需更新以反映新标签结果
- **Line 80** (Table subtable a): "3-LF (w/ cmd\_rep)" ZS "0.530" → 应改为 "0.5984" [新标签]
- **Line 80**: FT "0.751" → 应改为 "0.9763" [新标签]
- **Line 81**: "2-LF (no cmd\_rep)" FT "0.927" → 需新实验值 [旧标签结果无效]
- **Line 83**: "$\Delta$" "+17.6\,pp" → **INVALID** [同上]
- **Line 104** (Table caption): "Removing \texttt{cmd\_rep} helps probe fine-tuning ($+$17.6\,pp)" → **INVALID**
- **Line 108**: "Removing \texttt{cmd\_rep} improves probe fine-tuned F1 by $+$17.6\,pp" → **INVALID**
- **Lines 109-111**: "divergence reveals that \texttt{cmd\_rep} noise requires learned adaptation: fine-tuning can filter it" → 叙事完全基于旧标签，需重写 [cmd_rep 不是 noise source]

---

## [Limitations] (sections/limitations.tex)

- 无旧数字问题。叙事一致。

---

## [Related Work] (sections/related_work.tex)

- 无旧数字问题。叙事一致。

---

## [paper_framing.md]

paper_framing.md 中旧数字多出现在变更说明语境中（描述"从旧值到新值的修正"），属于历史记录不需修改。但以下几处仍以旧值作为当前 claim：

- **Core Claims 区域 Claim 2 段**: "去掉 cmd_rep 从 +17.6pp 变为 -6.5pp" — 这是变更记录，OK
- **Headline result template** 段: 已更新，无残留旧值。OK
- **writing_plan.yaml core_claim (line 11-15)**: "fundamentally structural" + "embedding probes (0.906/0.751)" → "0.751" 需改为 "0.9763"；"fundamentally structural" 需改为 "zero-shot transfer dominance" framing

---

## [writing_plan.yaml]

- **Line 11-15** (meta.core_claim): "fundamentally structural" → 应改为 zero-shot transfer dominance
- **Line 11-15** (meta.core_claim): "0.751" → 应改为 "0.9763"
- **Line 26** (abstract bullet): "removing it improves OH F1 by +17.6pp" → **INVALID — 删除/替换**
- **Line 36** (introduction hook): "90% verbosity increase and 80% quality erosion" → 应改为 "77% / 75.5%" [SlopCodeBench 原文数字修正，已在 paper_framing.md 记录但未应用]
- **Line 37** (introduction bullet): "removing it improves OH F1 by +17.6pp" → **INVALID**
- **Line 96** (experiments setup): "20.9% stag" → 应改为 "21.45%" [轻微偏差]
- **Line 98** (experiments bullet): "Probe 0.528 zero-shot (0.751 with 50% finetune)" → 应改为 "0.5984 zero-shot; 0.968 with 50% finetune" [旧标签值]
- **Line 101** (experiments bullet): "92.3% firing rate + 71% FP on OH progress windows" → 应改为 "5.39% fire rate + 2.3% FP" [旧 embeddings 错误]
- **Line 215** (tab_oh_cmdrep caption): "cmd_rep has 92.3% firing rate and 71% false positive rate on OH progress windows" → 同上

---

## [Introduction] (sections/introduction.tex) — SlopCodeBench 数字

- **Line 6**: "recording verbosity increases of 90\% and quality drops of 80\%" → 应改为 "77\%" 和 "75.5\%" [paper_framing.md 2026-05-15 修正记录：与原文 arXiv:2603.24755 一致]

---

## 叙事一致性问题汇总

### INVALID 叙事（必须删除/重写）

| 位置 | 旧叙事 | 问题 |
|------|--------|------|
| abstract L8 | "removing it improves fine-tuned F1 by 17.6pp" | 标签 bug 产物，新数据反转 |
| intro L37-38 | "71% FP + removing improves 17.6pp" | 同上 |
| experiments §5.5 全段 | cmd_rep 是 OH 噪声源 | 同上 |
| conclusion L12 | "removing it improves...17.6pp" | 同上 |
| appendix L104-111 | cmd_rep noise + removal helps | 同上 |

### "fundamentally structural" → "zero-shot transfer dominance"

| 位置 | 说明 |
|------|------|
| abstract L6 | Finding 1 标题 |
| intro L28 | Finding 1 标题 |
| conclusion L7 | Summary 段 |
| writing_plan.yaml core_claim | meta 段 |

### Cross-agent gap 重算

旧叙事：structural GB 0.967 >> probe FT 0.751 (gap 21.6pp)
新现实：structural GB ~0.9984 vs probe FT 0.9763 (gap 2.21pp)

影响位置：
- experiments.tex L88 ("21.6pp above")
- experiments.tex L92-93 ("even full OH fine-tuning only reaches 0.751")
- introduction.tex L29 ("0.751 after full fine-tuning")
- The entire "structural features transfer while embeddings do not" narrative needs nuancing

### OH stag rate 6.6% → 21.45%

影响位置：
- introduction.tex L9, L20
- experiments.tex L20, Table L32
- (method.tex 无直接提及 overall stag rate)

---

## 优先级排序

1. **P0 — INVALID claims (必须删除)**: +17.6pp cmd_rep removal, 71% FP, "cmd_rep corrupts labels" 叙事
2. **P0 — 核心数字错误**: OH stag rate 6.6%→21.45%, probe FT 0.751→0.9763, cmd_rep fire rate 92.2%→5.39%, cross-agent gap 21.6pp→2.21pp
3. **P1 — Framing 更新**: "fundamentally structural" → "zero-shot transfer dominance"
4. **P1 — probe ZS 值**: 0.528/0.530 → 0.5984
5. **P2 — 支持文件**: writing_plan.yaml, paper_framing.md 残留旧值
6. **P2 — SlopCodeBench 数字**: 90%/80% → 77%/75.5%
