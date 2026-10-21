# research c4 patch locations

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_c4_patch_locations_20260519T203740_result.json`
- **Structured JSON:** [`ad5f54952cb4c455ee6c.json`](../../sessions/ad/ad5f54952cb4c455ee6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have a comprehensive picture. Here's the full inventory:

---

## 所有匹配位置

### introduction.tex

```
L12  | VOTA: exception events + assertion-point comparisons + loop compression | loop提及(定义)
L30  | Two-tier diagnostic hierarchy: Tier~1 signals (exceptions, assertions) generalize across three models (≥99%), while Tier~2 (loop compression) is model-dependent: Qwen +10.9pp, DeepSeek +7.9pp, CodeLlama +0.6pp | Tier定义 + loop提及 + Tier数据
```

### method.tex

```
L23  | VOTA: Exception events + assertion-point comparisons + loop compression | loop提及(定义)
L26  | loop\_only: Only loop compression summaries. | loop提及(定义)
```

### experiments.tex

```
L4   | (1) Do Tier~1 exception signals generalize across models? | Tier提及(RQ)
L27  | loop\_only & 86.05±0.52 & --- & 77.06 & 81.26 \\ | loop数据(cross-model表)
L28  | no\_trace & 75.13 & 67.31 & 76.47 & 73.36 \\ | no_trace数据(对比基准)
L50  | no\_trace scales monotonically: 67.31%(1.5B)→75.13%(7B)→76.47%(13B) | no_trace数据
L67  | loop\_only is evaluated across three models to test Tier~2 generalization | Tier定义 + loop提及
L68  | reveals a two-tier hierarchy: Tier~1 (exception\_only) generalizes... while Tier~2 (loop\_only) is model-dependent | Tier定义(核心)
L72  | (表caption) Tier~1 signals achieve near-perfect accuracy... | Tier提及
L78  | 表头: Tier 列 | Tier提及
L80  | ae\_only ... Tier 1 | Tier数据
L81  | exception\_only ... Tier 1 | Tier数据
L84  | loop\_only & loop compression & 86.05 & ... & 2 | Tier数据 + loop数据
L96  | Tier~1 signals are individually sufficient | Tier声明
L98  | Tier~2 loop\_only lifts over no\_trace are model-dependent: Qwen-7B +10.92pp (86.05%), DeepSeek +7.90pp (81.26%), CodeLlama +0.59pp (77.06%, n.s.) | Tier数据 + loop数据(核心)
L171 | Calibration mirrors the tier hierarchy: exception\_only ECE=0.0027 vs 0.171 for no\_trace | Tier提及(calibration)
L172 | all three tested architectures achieve ECE <0.007 under exception\_only | Tier提及
```

### discussion.tex

```
L4   | non-exception components (variable states, loop iterations, control flow) | loop提及(叙述)
L25  | \paragraph{Tier hierarchy and methodological implications.} | Tier定义(段标题)
L26  | two-tier structure (Tier~1 ≥99%; Tier~2 = 77.1--86.1%) suggests a fallback design... resort to Tier~2 only when no exception is raised (model-dependent, +0.6--10.9pp over no-trace) | Tier定义 + Tier数据 + loop提及
L30  | Tier~1 and Tier~2 exhibit contrasting cross-model stability: exception\_only spans 0.56pp, while loop\_only spans 8.99pp (77.06--86.05%), with lifts following +10.9 > +7.9 > +0.6pp (the last not significant) | Tier数据 + loop数据(核心)
L31  | N=3 models is insufficient to establish a continuous relationship | Tier声明(hedging)
```

### conclusion.tex

```
L4   | lower-density loop signals are model-dependent (+0.6--10.9pp) | loop提及 + Tier数据
```

### appendix.tex

```
L21  | Loop Only & Qwen-2.5-7B & 86.05 ... (per-class breakdown) | loop数据(表)
L95  | loop\_only & 42 & ~2.1 (training steps/cost表) | loop提及
L129-132 | Component 3: Loop compression (VOTA算法伪代码) | loop提及(算法定义)
L186-187 | [LOOP] No loops detected. (VOTA示例) | loop提及(示例)
L219 | loop\_only & 85.63 & 85.88 & 86.64 & 86.05±0.52 (per-seed表) | loop数据
L533 | calibration quality mirrors the Tier~1/2 hierarchy | Tier提及
L534 | Tier~1 conditions (ae\_only: ECE=0.0004; exception\_only: ECE=0.0027) | Tier数据
L535 | VOTA slightly worse than either Tier~1 component alone | Tier提及
L576 | ae\_only ⊂ VOTA ⊂ loop\_only ⊂ no\_trace (error containment) | loop提及
L577 | loop\_only and full\_trace share highest overlap (Jaccard ~0.65) | loop提及
```

---

## 汇总分析

### 需要 patch 的位置（措辞与 CodeLlama loop_only=negative 矛盾）

| 位置 | 问题 |
|------|------|
| **discussion.tex:26** | "Tier~2 = 77.1--86.1%" — 下限 77.1% 是 CodeLlama loop_only 的 77.06%，而 CodeLlama no_trace 是 76.47%，lift 仅 +0.59pp (n.s.)。将 77.1% 作为 Tier 2 的"范围下限"暗示它仍是有效的，但实际上它是 negative result（与 no_trace 无统计显著差异）。需要改为类似 "Tier~2 is effective for Qwen/DeepSeek (+7.9--10.9pp) but not for CodeLlama (+0.6pp, n.s.)" |
| **introduction.tex:30** | "Tier~2 (loop compression) is model-dependent: Qwen +10.9pp, DeepSeek +7.9pp, CodeLlama +0.6pp over no trace" — 措辞暗示三个模型都有正向 lift，只是程度不同。但 CodeLlama +0.6pp 是不显著的，应该明确标注 n.s. 或说"two of three models" |
| **conclusion.tex:4** | "lower-density loop signals are model-dependent (+0.6--10.9pp)" — 同上，范围写法暗示所有值都是有意义的正向 lift |

### 可能需要 patch 的位置（措辞模糊，取决于 framing 决策）

| 位置 | 问题 |
|------|------|
| **experiments.tex:67** | "loop\_only is evaluated across three models to test Tier~2 generalization" — "generalization"一词偏正面，但 CodeLlama 上未能 generalize。取决于你是否想把"未 generalize"也算"测试 generalization 的结论" |
| **experiments.tex:68** | "Tier~2 (loop\_only) is model-dependent" — 这句本身 OK，但紧接着没说 CodeLlama 是 negative。读者可能理解为"程度不同但都有效" |
| **discussion.tex:30** | "lifts following +10.9 > +7.9 > +0.6pp (the last not significant)" — 这句已经标注了 n.s.，但"lifts"一词暗示三者都是正向结果，只是最后一个不显著。是否改为"the last indistinguishable from no-trace" |
| **discussion.tex:26** | "resort to Tier~2 only when no exception is raised (model-dependent, +0.6--10.9pp over no-trace)" — fallback 建议隐含 Tier 2 总是有用的，但 CodeLlama 上它无用 |
| **appendix.tex:533-535** | "calibration quality mirrors the Tier~1/2 hierarchy" — 如果 CodeLlama loop_only calibration 也没改善，则此声明需要加 caveat |

### 无需改动的位置

| 位置 | 理由 |
|------|------|
| **experiments.tex:4** | RQ 只提 Tier 1，不涉及 loop |
| **experiments.tex:27-28** | 纯数据表，77.06 和 76.47 如实呈现 |
| **experiments.tex:72, 78, 80-81, 84** | 表格定义和数据，如实标注 Tier 1/2 |
| **experiments.tex:96** | 只讨论 Tier 1 |
| **experiments.tex:98** | **已经正确标注** "CodeLlama +0.59pp (77.06%, n.s.)" — 这是最详细的数据行，无需修改 |
| **experiments.tex:171-172** | 只讨论 calibration 中的 exception_only |
| **discussion.tex:4** | 一般性叙述 "loop iterations"，非实验上下文 |
| **discussion.tex:31** | 已经 hedge "N=3 models is insufficient" |
| **method.tex:23, 26** | 纯定义，无声明 |
| **appendix.tex** L21, 95, 129-132, 186-187, 219, 576-577 | 数据表/算法/描述性文本，无夸大声明 |

---
