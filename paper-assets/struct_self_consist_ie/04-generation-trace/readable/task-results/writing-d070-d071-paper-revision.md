# writing d070 d071 paper revision

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_d070_d071_paper_revision_20260515T093414_result.json`
- **Structured JSON:** [`0a2fa9cc87797bfa16bb.json`](../../sessions/0a/0a2fa9cc87797bfa16bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修订完成。以下是 21 项修改的完整清单：

### Must-Fix (3/3)
| 项目 | 修改内容 |
|------|---------|
| MF-1 | Abstract/Intro/Discussion 重构为两层叙事：Layer 1 (定义性，1-2句) + Layer 2 (LP compression 实证核心) |
| MF-2 | Contributions 重排为 C1=regime-specific bottleneck, C2=QE framework, C3=task complexity；删除 "first" claim |
| MF-3 | TOST δ* breakpoint 数据填入 appendix (NER 1.28-3.38pp, RE 2.86-6.53pp)；effect size + bootstrap CI 为主证据 |

### Should-Fix (9/9)
| 项目 | 修改内容 |
|------|---------|
| SF-1 | Introduction + Discussion 各加显式 constrained decoding regime scope 声明 |
| SF-2 | §4.1 替换 PENDING：确认 enable_thinking=True，空 thinking block 参与 loss，<0.3% token 占比 |
| SF-3 | Discussion/Conclusion 中所有 RE 结论标注 (preliminary, single benchmark) |
| SF-4 | Appendix "Cross-model transfer" → "Transfer across model families" |
| SF-5 | Abstract 精简为问题-发现-意义三段式，移除 ρ/AUROC 具体数字 |
| SF-6 | Discussion "exact match" → "EM" 缩写统一 |
| SF-7 | Method VC 脚注：Eq.6 无阈值为正式定义，报告 Δρ (NER +0.127, RE +0.019) |
| SF-8 | Eikema et al. 2025 已在 Discussion MBR 段落引用讨论 ✓ |
| SF-9 | Nédellec 增量贡献以 "extends in three directions" 定位，WNUT-17 non-obvious findings 突出 |

### Minor (9/9)
| 项目 | 修改内容 |
|------|---------|
| 1 | Figure 1 caption 已精简 ✓ |
| 2 | N=16 行已在 appendix，主文脚注指向 ✓ |
| 3 | FK excess agreement 加 one-sample t-test p<0.05 说明 |
| 4 | Semantic entropy 脚注已无具体数字 ✓ |
| 5 | he2024uncertainty 引用上下文修正为 "uncertainty transmission across label sequences" |
| 6 | Ethics Statement 已含 CoNLL-2003 Reuters license ✓ |
| 7 | Notation Table 已含 LP ✓ |
| 8 | 5 处 bib 条目核实通过 (ye2025uncertainty 未在论文中引用；其余 4 项正确) |
| 9 | N=8 single seed (seed=42) 注明，引用 3-seed stability (σ≤0.025) |

### D071 Narrative
- **Free-form ablation**: Discussion 新增 "Toward mechanistic confirmation" 段落，标注 [Planned experiment]
- **Constrained decoding bottleneck**: Abstract 末句 + Conclusion 均以此为主要结论
- **3 个 computation artifacts** 数据全部整合到论文

---
