# audit claim consistency

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_claim_consistency_20260518T054521_result.json`
- **Structured JSON:** [`fa89ee15da09a03f171d.json`](../../sessions/fa/fa89ee15da09a03f171d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集完毕。以下是完整审计报告。

---

## 审计结果

### 旧值残留检查（D131/D132）

| 旧值 | 搜索结果 | 状态 |
|------|---------|------|
| 0.614 (SciERC greedy) | 全文无匹配 | ✅ 已全部更新为 0.644/0.645 |
| 0.752 (SciERC oracle) | 仅 `appendix.tex:1057` | ✅ 该处是 tab:t_degeneracy 中 T=0.8 的 SJ mean 值，非 SciERC oracle |
| 13.8pp (SciERC headroom) | 无残留 | ✅ 所有 13.8 均指 Few-NERD degeneracy（正确用法） |
| 0.205 (旧 SciERC LP ρ) | 多处匹配 | ✅ 0.205 是 tab:quality_estimation 中 mean-LP 的正确值；tab:fewnerd 中 max-LP 为 0.215，两者是不同指标 |
| +0.42pp (旧 SciERC LP Δ) | 无残留 | ✅ 所有 0.42 均为 ρ 值，非 LP Δ |
| 47.4% (旧 CoNLL degen) | 全文无匹配 | ✅ 已更新为 59.1% (N=8) / 48.3% (N=16) |
| 89.2% (旧 LLaMA degen) | 全文无匹配 | ✅ 已更新为 86.4% |
| -0.07pp (旧 Table 3 LP Δ) | 全文无匹配 | ✅ 已废弃 |

**结论：所有 D131/D132 旧值均已清除。**

---

### 跨章节一致性

| 数值 | 出现位置 | 一致? | 说明 |
|------|---------|-------|------|
| ρ "up to 0.42" | abstract:4, intro:12, intro:30, conclusion:4 | ⚠️ | 实际最大 ρ=0.451 (CoNLL Qwen EM)。Figure caption 正确写 "ρ up to 0.45 on CoNLL"，但 Abstract/Intro/Conclusion 都写 "up to 0.42" |
| AUROC "up to 0.82" | abstract:4, intro:12, intro:20, conclusion:4 | ✅ | 0.816 四舍五入至 0.82 |
| +1.36pp Few-NERD | abstract:5, intro:13/38, exp:91/109/117, disc:5, conc:5, app:1182 | ✅ | 全部一致 |
| +0.52pp N-scaling | intro:13/38, exp:135, disc:16, conc:5 | ✅ | 全部一致 |
| 14–59% degeneracy | abstract:7, intro:15/34, conc:7 | ✅ | 13.8%≈14%, 59.1%≈59% |
| SciERC oracle 0.778 | exp:68 (tab:selection), exp:89 | ✅ | tab:fewnerd implied oracle=0.776, footnote已解释差异 |
| SciERC greedy 0.645 vs 0.644 | exp:69 (tab:selection: 0.645), exp:108 (tab:fewnerd: 0.644), exp:173 fn (0.644 3-seed mean), app:984 fn (0.640 N-scaling) | ✅ | 三处差异均有 footnote 解释 |
| ρ=−0.881, p=0.004, n=8 | intro:39, exp:120, disc:31, app:1203 | ✅ | |
| Non-tied +2.9pp, p=0.004 | exp:92, disc:15, app:556, app:624 | ✅ | |
| Within-inst ρ=0.248 | disc:12, app:557, app:626 | ✅ | intro:34 写 "ρ≈0.24" 是四舍五入 |
| T=1.2 degeneracy 12.5%, ρ=0.225 | intro:35, disc:28/29, app:1044/1059 | ✅ | |
| LoRA rank=8: degen 7.2%, ρ≈0.24 | exp:168, disc:30, related:23 | ✅ | |

---

### 发现的不一致

#### 1. ⚠️ "ρ up to 0.42" 低于实际最大值
- **位置**: abstract:4, intro:12, intro:30, conclusion:4
- **问题**: 全文多处声称 "ρ up to 0.42"，但 tab:quality_estimation 中 CoNLL Qwen EM ρ=0.451。Figure caption (intro:20) 正确写 "ρ up to 0.45 on CoNLL"
- **影响**: 低报了最大 ρ 值；与 Figure caption 不一致

#### 2. ⚠️ RE free-form LP gain: discussion 引用 +2.35pp，appendix 数据不匹配
- **位置**: discussion:21 写 "+2.35 pp, p=0.025"
- **Appendix 数据**: 
  - app:771: 4-seed mean = +1.84±0.12pp (seeds: +1.69, +1.76, +2.00, +1.91)
  - app:687 (RE extension): "+1.8±0.1 pp across 4 seeds"
  - app:810 (Panel B, seed=42): +1.69pp
- **问题**: +2.35pp 不匹配 appendix 中任何数值。最接近的是 constrained→free-form 的 swing (+1.69−(−0.68)=+2.37)，但这是方向变化量，不是 selection gain over greedy
- **影响**: 可能是过时数值或计算错误

#### 3. ⚠️ Few-NERD N=8 degeneracy: 14.6% vs 13.8%
- **位置**: experiments:135 写 "14.6% → 7.0%"（N=8→16 scaling）
- **Tab:fewnerd** (experiments:109): 13.8%
- **Tab:fewnerd_full** (appendix:1171): 13.8%
- **问题**: N-scaling 段引用 14.6%，但 tab:fewnerd 和 tab:fewnerd_full 均为 13.8%。可能是不同 subset/seed 导致，但缺少解释
- **影响**: 轻微数值不一致

#### 4. ⚠️ Few-NERD N=8 headroom: 12.1pp vs 12.4pp
- **位置**: experiments:135 写 "12.1 → 15.4 pp"（N=8→16）
- **Tab:fewnerd** (experiments:109): 12.4pp
- **问题**: 同上，可能是不同 subset/seed。差异 0.3pp
- **影响**: 轻微

#### 5. ⚠️（已知，非错误）SciERC LP Δ 三个不同值
- **+0.2pp**: tab:selection (2-seed mean, mean-LP) — experiments:89
- **+0.61pp**: tab:fewnerd (gold-filtered, max-LP, single-seed) — experiments:108, conclusion:6
- **+0.39pp**: N-scaling table (gold-filtered, seed=42) — appendix:978
- **状态**: 所有差异已有 footnote 解释。但 conclusion 使用 +0.61pp 而 introduction 使用 +0.2pp，可能造成读者困惑

---

### 未找到来源的 Claims

| Claim | 位置 | 说明 |
|-------|------|------|
| RE free-form +2.35pp, p=0.025 | discussion:21 | Appendix 数据（+1.84±0.12pp 4-seed mean, +1.69pp seed=42）均不匹配此值 |

---

### 总结

- **旧值残留**: 0 处。D131/D132 修正已完全传播。✅
- **发现的不一致**: 5 处
  - **需修改 (2)**:
    1. `discussion.tex:21` — RE free-form LP gain "+2.35pp" 与 appendix 数据不匹配，需核实数据源并修正
    2. `abstract.tex:4`, `intro.tex:12`, `intro.tex:30`, `conclusion.tex:4` — "ρ up to 0.42" 应改为 "ρ up to 0.45" 以匹配 Figure caption 和 tab:quality_estimation 实际最大值，或加限定语（如 "ρ up to 0.42 on the primary and cross-dataset test beds"）
  - **建议核实 (2)**: Few-NERD N-scaling 段中的 14.6%/12.1pp 与 tab:fewnerd 的 13.8%/12.4pp 不一致（可能是不同 evaluation subset，建议加 footnote 说明）
  - **已知差异 (1)**: SciERC LP Δ 在不同表格中有三个值（+0.2/+0.61/+0.39pp），已有 footnote 解释

---
