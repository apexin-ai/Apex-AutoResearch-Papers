# audit abstract body crosscheck

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_abstract-body-crosscheck_20260523T191628_result.json`
- **Structured JSON:** [`062904ad77c9a0ac0853.json`](../../sessions/06/062904ad77c9a0ac0853.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data needed for cross-referencing. Let me compile the report.

## Abstract + 正文数字交叉核对报告

### ✅ 已核对一致

- **"F1=0.97--1.0"** in abstract.tex:6 ← Table 2 (evidence_hierarchy): 9-class DD-Full=.997, AA-Full=.972, FITD=1.000; range 0.972–1.000 rounds to 0.97–1.0
- **"vanilla 0.26--0.31"** in abstract.tex:6 ← Table 2: Vanilla DD=.312, AA=.258 → 0.258–0.312 ≈ 0.26–0.31
- **"F1=0.504"** in abstract.tex:6 ← Table 5 (mixed_llm): 9-class AA OOD = .504±.107
- **"0.837 vs 0.596"** in abstract.tex:6 ← Table 6 (human_data): JB-MLM=.837±.013, 9-class=.596±.087
- **"58--68%"** FPR in abstract.tex:6 ← OASST2 baseline FPR=57.5%≈58%, WildChat 9-class FPR=68.1%
- **"24.3×"** speedup in abstract.tex:6 ← Appendix efficiency (line 818): exp46 matched comparison 318.53ms/13.12ms=24.3×
- **"43×"** fewer parameters in abstract.tex:6 ← 8B(Qwen3-8B)/186.7M(DeBERTa+BiGRU)=42.85≈43×
- **"1.8%"** Llama Guard in abstract.tex:4 / experiments.tex:23 ← 5/278 pooled recall = 1.8%; 278 = 38(Crescendo)+80(DD)+80(FITD)+80(AA)
- **"0.312 on OOD Deceptive Delight"** in introduction.tex:14 ← Table 1: Vanilla DD-Full=.312±.026
- **"0.818"** mixed-LLM 9-class in conclusion.tex:8 ← Table 5: 9-class DD OOD=.818±.096
- **"AA=1.000 vs 9-class 0.946"** RoBERTa-large in conclusion.tex:8 ← Table 4 (cross_encoder): RoBERTa-large vanilla AA=1.000, 9-class AA=.946
- **"68.1%"** WildChat FPR in conclusion.tex:8 / experiments.tex:217 ← Table wildchat_fpr: 9-class Mean=68.1±6.4%
- **"F1=0.541±0.207"** topic OOD in conclusion.tex:5 ← Table 2: Topic DD-Full=.541±.207
- **"within 3.9 pp"** scrambled labels in conclusion.tex:5 ← Table 2 AA: Binary=.990, Scrambled=.951 → max gap=3.9 pp
- **"participation ratio 3.7--9.4 vs 25--32"** in conclusion.tex:5 ← Table representation: Binary PR=3.7, 9-class=9.4; JB-MLM=24.6, Vanilla=31.9
- **"−57.9 pp"** zero-padding collapse in conclusion.tex:12 ← Table length_independence Part C: AA padded Δ=−57.9 pp
- **"Δ≤1 pp"** mean pooling vs BiGRU in conclusion.tex:8 ← Table temporal: Frozen max gap=1.0 pp (AA: .972 vs .962)
- **"N=155"** length-matched in conclusion.tex:12 ← Table length_independence: 80 jailbreak + 75 benign = 155
- **"κ=0.78"** in experiments.tex:211 / conclusion.tex:27 ← Appendix strategy heatmap caption: κ=0.78
- **"184M vs 355M"** in conclusion.tex:27 ← DeBERTa-v3-base=184M, RoBERTa-large=355M
- **"125M--355M"** in conclusion.tex:27 ← RoBERTa-base=125M to RoBERTa-large=355M
- **"12--14 pp"** dual-OOD drop in conclusion.tex:24 ← Table dual_ood: WildChat drops ~14 pp, OASST2 drops ~12 pp → range 12–14 pp
- **"~60 pp from vanilla"** MLM bridge in experiments.tex:117 ← .914−.312=.602≈60 pp
- **"71 pp gap"** TF-IDF vs 9-class in experiments.tex:60 ← .972−.261=.711≈71 pp
- **"3--23× lower cross-seed variance"** in experiments.tex:119 ← AA: .080/.026≈3×; DD: .115/.005=23×
- **"d=−0.14 on DD, d≈0 on FITD"** TOST in introduction.tex:27 ← Table tost_sensitivity: DD d=−0.136, FITD d=0.000
- **"d=0.44"** ActorAttack in introduction.tex:27 / experiments.tex:118 ← Table tost_sensitivity: AA d=0.440
- **"0.628→0.312"** vanilla DD degradation in experiments.tex:59 ← Table full_prefix: Vanilla DD K=1=.628, Full=.312

---

### ⚠️ 不一致

1. **Introduction "over 60 percentage points" classification vs MLM** (introduction.tex:22)
   - 期望: classification vs MLM 最大差值 ~53 pp (mixed-LLM DD: .818−.289=52.9 pp)
   - 实际: "over 60 pp" 的差距是 classification vs **vanilla** (.997−.312=68.5 pp), 不是 vs MLM
   - → 需修复: 改为 "over 60 percentage points over vanilla" 或 "over 50 percentage points over MLM"

2. **Discussion "all DAPT variants exceed vanilla by ≥40 pp on ToxicChat"** (conclusion.tex:8)
   - 期望: 所有 DAPT 变体 ≥40 pp
   - 实际: Table 6 数据 — JB-MLM 42.4pp ✓, Wiki-MLM 37.8pp ✗, Binary 29.2pp ✗, Scrambled 20.3pp ✗, 9-class 18.3pp ✗, Topic 8.3pp ✗
   - → 需修复: 改为 "18--42 pp" 或 "all jailbreak-domain DAPT variants exceed vanilla"

3. **Discussion "DD/AA Δ ≤ 2.5 pp" for length-matched** (conclusion.tex:12)
   - 期望: DD 和 AA 都 ≤2.5 pp
   - 实际: Table length_independence Part C — DD Δ=−2.5pp ✓, AA Δ=−57.9pp ✗
   - 且下一句就说 "−57.9 pp ActorAttack collapse", 前后矛盾
   - → 需修复: 改为 "DD $\Delta \leq$ 2.5 pp" 去掉 "/AA", 或明确说 "DD shows negligible change ($\Delta$=−2.5 pp) while AA collapses"

4. **experiments.tex "25 OASST2 to 1.0%" vs appendix table 1.5%** (experiments.tex:217)
   - 期望: 与 OASST2 adaptation curve 表一致
   - 实际: Appendix Table oasst2_curve 行 N=25 → FPR=1.5%（不是 1.0%）
   - Abstract 和 conclusion 写 "0--1.5%" 与表一致; experiments.tex 写 "1.0%" 不一致
   - → 需修复: experiments.tex 改为 "25 OASST2 to 1.5\%"

5. **Appendix full_prefix 9-class DD-Full = .994 vs 主表 .997** (appendix.tex:56 vs experiments.tex:48,86)
   - Table 1 (main_results): .997±.005; Table 2 (evidence_hierarchy): .997±.005
   - Appendix Table full_prefix: .994±.005
   - Seed-level 数据 (s42=1.000, s123=1.000, s456=.990) → mean=.997, 确认主表正确
   - → 需修复: Appendix full_prefix 的 DD-Full 从 .994 改为 .997 (或核实是否使用了不同 checkpoint)

6. **Abstract "base scale (125M--184M)" vs Introduction "three scales (125--355M)"** (abstract.tex:4 vs introduction.tex:27)
   - Abstract: "thirteen encoder configurations at base scale (125M--184M parameters)"
   - Introduction: "thirteen encoder configurations at three scales (125--355M)"
   - 13个配置含 3 个 RoBERTa-large (355M), 不全是 base scale
   - → 需修复: abstract 改为 "at base to large scale (125M--355M)" 或与 introduction 一致

7. **experiments.tex "All DAPT variants exceed vanilla by 18--42 pp"** (experiments.tex:205)
   - Topic 也是 DAPT 变体, 但 Topic−Vanilla = 8.3 pp (< 18 pp)
   - → 需修复: 改为 "Most DAPT variants exceed vanilla by 18--42 pp" 或注明排除 Topic

8. **Discussion "label-free MLM detection (F1≥0.97)" 缺少限定** (conclusion.tex:5)
   - MLM DD-Full = 0.914±0.115 (< 0.97); 仅 K≤5 时 ≥0.97
   - experiments.tex 正确限定为 "MLM recovers to ≥0.97 at K≤5"
   - → 需修复: Discussion 应加限定 "at early prefixes" 或 "at K≤5"

9. **Conclusion "with 10 conversations" 过度简化** (conclusion.tex:17)
   - WildChat: N=10 → 0% ✓; OASST2: N=25 → 1.5% (不是 N=10)
   - Introduction 正确写 "10--25 conversations"
   - → 需修复: 改为 "with 10--25 conversations"

10. **Limitations "n ≤ 49"** (conclusion.tex:24)
    - OASST2 表最大 N=50, WildChat 实验也有大样本
    - 不清楚 49 的来源
    - → 需确认: 如果指 adaptation 用的最大 conversation 数, 应为 n≤50

---

### ❌ 无法溯源

- **"0.191--0.449 F1 (across prefix lengths)"** in introduction.tex:14 — GPT-5.5 per-prefix F1 不在任何表中; LLM-judge 表仅有 full-conversation F1=.383. Full 值落在声称范围内但无法验证两端.

---

### 四舍五入一致性

- **0.97 vs 0.972**: Abstract/Conclusion 写 "F1=0.97--1.0", 实际 9-class AA-Full=.972. 作为范围下界, 0.97 是 0.972 的合理简写. ✓
- **0.26 vs 0.258**: Vanilla AA=.258 简写为 0.26. 一致. ✓
- **0.31 vs 0.312**: Vanilla DD=.312 简写为 0.31. 一致. ✓
- **58% vs 57.5%**: OASST2 FPR=57.5% 取整为 58%. 一致. ✓

---
