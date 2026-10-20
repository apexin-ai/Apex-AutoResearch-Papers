# audit appendix consistency

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_appendix-consistency_20260523T191656_result.json`
- **Structured JSON:** [`fdad72e010bd3238f5dd.json`](../../sessions/fd/fdad72e010bd3238f5dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Appendix 一致性核对报告

### ✅ 核对一致

- **κ=0.78** (Limitations) ← `fig:strategy_heatmap` caption (appendix:171) "κ=0.78"
- **184M vs 355M** (Limitations) ← `tab:cross_encoder` (experiments:148,158) DeBERTa-v3-base 184M, RoBERTa-large 355M
- **125M--355M** (Limitations) ← `tab:cross_encoder` RoBERTa-base 125M ~ RoBERTa-large 355M
- **PR 3.7--9.4 vs 25--32** (Discussion) ← `tab:representation` (appendix:617-629) Binary=3.7, 9-class=9.4; JB-MLM=24.6, Wiki-MLM=25.0, Vanilla=31.9. "25--32" 是对 24.6-31.9 的四舍五入，可接受
- **17 pp removal degradation** (Discussion) ← `tab:svd_necessity` (appendix:696) DD: 1.000→0.831 = 16.9pp ≈ 17pp
- **+18--42 pp ToxicChat** (Discussion range) ← `tab:human_data` (experiments:189-202) 9-class 0.596−0.413=18.3pp, JB-MLM 0.837−0.413=42.4pp
- **0.818 mixed-LLM** (Discussion) ← `tab:mixed_llm` (appendix:257) 9-class DD OOD = .818±.096
- **68.1% WildChat FPR** (Discussion) ← `tab:wildchat_fpr` (appendix:445) 9-class Mean = 68.1±6.4
- **−57.9 pp padding** (Discussion, 数值) ← `tab:length_independence` Part C (appendix:784) AA padded Δ=−57.9 pp
- **TOST table (tab:tost_sensitivity)** — caption 写 "10 seeds" ✅，3 行数据 (DD/FITD/AA) ✅，experiments:118 引用 "p < 10^{-8}, d = −0.14" 与表中 p=2.06×10^{-9}, d=−0.136 一致
- **n≤49 adaptation samples** — 见下方不一致项
- **Label/Ref** — 所有 `\ref` 均有对应 `\label`，无 broken refs；所有 `\label` 均有对应 `\ref`，无 orphan labels

---

### ⚠️ 不一致

1. **Discussion "≥40 pp" 错误** (conclusion.tex:18)
   - 正文: "all DAPT variants exceed vanilla by ≥40 pp on ToxicChat"
   - 实际: 只有 JB-MLM (42.4pp) 超过 40pp。其余: Wiki-MLM 37.8pp, Binary 29.2pp, Scrambled 20.3pp, 9-class 18.3pp, Topic 8.3pp
   - **建议**: 改为 `$\geq$18\,pp` 或与同句已有的 "+18--42 pp" 保持一致

2. **Limitations 错误 Table 引用** (conclusion.tex:32)
   - 正文: "dual-OOD evaluation drops 12--14 pp without adaptation (Table~\ref{tab:main_results})"
   - 实际: `tab:main_results` 不含 dual-OOD 数据。dual-OOD 数据在 `tab:evidence_hierarchy` (底部 rows) 和 Appendix `tab:dual_ood`
   - **建议**: 改为 `Table~\ref{tab:evidence_hierarchy}`

3. **DD-Full 9-class 数值: .997 vs .994**
   - `tab:main_results` (experiments:48): **.997**±.005
   - `tab:evidence_hierarchy` (experiments:86): **.997**±.005
   - `tab:full_prefix` (appendix:56): **.994**±.005
   - `tab:full_prefix` 的 K=5 列 = .997, Full 列 = .994。正文表格可能误用了 K=5 的值作为 Full
   - 同样问题存在于 **Scrambled**: evidence_hierarchy .997 vs full_prefix .994

4. **Limitations n≤49 错误** (conclusion.tex:32)
   - 正文: "validated on only two platforms ($n \leq 49$)"
   - 实际: OASST2 adaptation curve 最大 N=50 (`tab:oasst2_curve`, appendix:474)
   - **建议**: 改为 `$n \leq 50$`

5. **Discussion "zero-padding" 术语错误** (conclusion.tex:21)
   - 正文: "the −57.9 pp ActorAttack collapse under zero-padding"
   - 实际: 实验是用 **benign conversation turns** 填充，不是 zero-padding (appendix:795: "Padding experiments append benign turns after the complete attack sequence")
   - **建议**: 改为 "benign-turn padding" 或 "dilution padding"

6. **12--14 pp 范围略不精确** (experiments:217, conclusion:32, appendix:504)
   - 从 `tab:evidence_hierarchy`: DD .997→.855 = 14.2pp, AA .972→.842 = 13.0pp → 实际范围 13--14pp
   - 从 `tab:dual_ood`: DD .994→.855 = 13.9pp, AA .981→.842 = 13.9pp → 两者均 ~14pp
   - "12" 没有数据支撑。Minor issue，但如 #3 的 .997/.994 不一致被修正后范围会变

---

### ❌ 待确认

- **Discussion "all DAPT variants exceed vanilla by ≥40 pp" 是否应排除 Topic?** 如果 "DAPT variants" 语义上不含 Topic (因其被归类为 "misaligned supervision")，那范围应为 18--42pp，但 ≥40pp 仍然错误。需确认作者意图。

---

### Label/Ref 检查
- **Orphan labels**: 无
- **Broken refs**: 无

---
