# research ratequant analysis

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ratequant_analysis_20260514T003022_result.json`
- **Structured JSON:** [`c411d192182096bfaaf3.json`](../../sessions/c4/c411d192182096bfaaf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。以下是完整分析。

---

## RateQuant 深度分析

### 1. Catastrophic Allocation

**RateQuant 的处理方式：** RateQuant 的 Algorithm 1 greedy allocation 仅有 bound constraint (`b_min ≤ b_i ≤ b_max`)，**没有 cardinality constraint**。算法初始化所有 head 为 `b_min`，然后贪心地将剩余 bit 分配给 weighted marginal gain 最大的 head。

**是否会出现 catastrophic allocation：** 不太会，但原因不同于有 constraint——RateQuant 的 action space 是 **consecutive integers {2,3,4,5,6}**，不是 {2,4,8,16}。在 `b_min=3, b_max=6` 的典型设置下，最差也只是 3-bit，不会出现大量 head 被压到 2-bit 的极端情况。即使在 `b_min=2` 的激进设置（2.5 avg bits），由于整数粒度很细（每步只降 1 bit），greedy 算法自然地分散 bit budget，不容易产生极端聚集。

**关键差异：** 我们的 action space {2,4,8,16} 是**非均匀间距**的——2-bit 和 4-bit 之间有 2 bit 的跳跃，4-bit 和 8-bit 之间有 4 bit 的跳跃。这意味着 MCKP solver 在 budget pressure 下更容易将大量 head 推向 2-bit（因为 2→4 的 marginal cost 是 2 bit，而非 1 bit）。RateQuant 的 {3,4,5,6} 间距均匀，catastrophic allocation 在结构上就更难发生。

**对 paper framing 的建议：** 这是一个重要 differentiation point。可以论证：当 action space 粒度不均匀（实际硬件支持的 {2,4,8,16}），cardinality constraint 变得 essential，而 RateQuant 绕过了这个问题只是因为它限制在 consecutive integer bit-widths 上。

---

### 2. Compounding Effects / Non-additivity

**RateQuant 的 distortion model：** 明确假设 additivity。目标函数为：

```
J(b) = Σ w_i · D(b_i)
```

每个 head 的 distortion 独立计算，总 distortion 是加权求和。**没有任何 cross-head interaction term。**

**是否讨论了 compounding effects：** 没有直接讨论。但 Appendix M limitations 中承认：

> "Per-head independence assumption may not hold for architectures with strongly coupled heads"

这是他们唯一一次提及 head 间可能存在耦合，但没有实验验证，也没有提出解决方案。

**Gain ratio theorem 也假设 independence：** Theorem 3 的 `J_u / J* = AM/GM` 完全基于 separable objective，不考虑任何 non-linear interaction。

**与我们的对比：** 我们有直接的实验证据——unconstrained MCKP 将 75/112 heads 分配 2-bit，PPL 从 15.45 爆炸到 36.92。这 **不可能** 用 additive model 解释（additive model 预测的 PPL 应该更低，因为 solver 是在 additive objective 上取最优）。这是 non-additivity 的直接经验证据。

**RateQuant 之所以没发现这个问题，** 可能因为：(a) consecutive integer 间距让极端 allocation 不易发生；(b) 他们没有测试过真正极端的压缩场景（主要在 2.5-4.0 bits，`b_min=2` 或 3）。

**对 paper framing 的建议：** 这是核心 contribution。可以这样 frame：RateQuant 的 additive assumption 在 moderate compression（3-6 bit 范围）下 works，但在 discrete heterogeneous action spaces with large bit-width gaps（{2,4,8,16}），additive model 的 systematic error 被放大到 catastrophic 程度。Cardinality constraint 是对这种 systematic error 的 principled regularization。

---

### 3. Continuous to Discrete

**RateQuant 的方案：** 实际上分两层：

- **Theorem 2（continuous solution）：** `b_i* = b̄ + (ln w_i − ln w̄) / ln β`，输出连续值。这是分析用的 closed-form，不直接用于实际分配。
- **Algorithm 1（discrete solution）：** 直接在 **integer** 空间上贪心分配，不需要 rounding。Proposition 6 证明当 D(b) convex 时，greedy 在 integer grid 上是 optimal。

**关键限制：** Proposition 6 的 optimality guarantee 依赖于 **consecutive integer** bit-widths（polymatroid structure）。对于 non-consecutive discrete set {2,4,8,16}，greedy 不保证 optimal，因为 marginal cost 不均匀（2→4 花 2 bit，4→8 花 4 bit），polymatroid structure 被破坏。

**我们的优势：** 我们直接在 {2,4,8,16} 上做 MCKP，这是 NP-hard 但可以用 DP 精确求解（head 数量 ~100 级别，完全可行）。不需要 consecutive integer 假设，不需要 rounding。

**实际硬件考量：** 现实中 GPU kernel 只高效支持 {2,4,8,16}-bit，不支持 3-bit 或 5-bit。RateQuant 分配 3-bit 或 5-bit 后，要么需要用 nearest supported bit-width（引入额外误差），要么需要 custom kernel（工程开销大）。这是 RateQuant 从 theory 到 deployment 的 gap。

**对 paper framing 的建议：** 强调 practical discrete action space 的重要性。RateQuant 的 consecutive integer 假设在理论上 elegant，但在 deployment 中 mismatch with hardware capabilities。我们的 MCKP formulation 天然匹配硬件支持的 bit-width set。

---

### 4. Granularity

**RateQuant：** **Per-head**，与我们相同。他们在 Qwen3 上操作 8 KV heads × N layers（Qwen3-8B 有 36 layers = 288 heads for K+V combined，或 144 per K/V）。

**额外粒度——K/V separation：** RateQuant 将 K 和 V 作为独立通道分配，允许 asymmetric budget split。在 2.5 avg bits 时，自动发现 K 需要 2.85 bits、V 需要 2.15 bits。

**与我们的对比：** 我们也是 per-KV-head。RateQuant 的 K/V separation 是额外一层粒度，我们目前是否也做了 K/V 分别优化？如果没有，这可以是一个 future work 方向，也是 RateQuant 的一个优势点。

---

### 5. 实验设置对比

| | RateQuant | 我们 |
|---|---|---|
| **模型** | Qwen3-4B/8B/32B | Qwen2.5-7B |
| **KV heads** | 8 per layer | 4 per layer (GQA=4) |
| **Eval** | WikiText-2 PPL + ARC-C/HellaSwag/PIQA/WinoGrande | WikiText-2 PPL |
| **Bit range** | {2,3,4,5,6} consecutive integers | {2,4,8,16} discrete |
| **压缩率** | 2.5-4.0 avg bits（~2.5-4× vs FP16） | 4× compression |
| **Calibration** | 16 seq × 512 tokens, 1.6s | PPL-based profiling |
| **Ablation** | distortion model mismatch, K/V separation, sensitivity metric | constrained vs unconstrained, cardinality k sweep |
| **Baseline quantizer** | KIVI, QuaRot, TurboQuant | uniform 4-bit |

**关键实验差异：**
- RateQuant 没有 ablation 关于 constraint/allocation strategy（因为他们没有 constraint）
- RateQuant 没有测试 {2,4,8,16} discrete action space
- RateQuant 的 headline result 是在 KIVI 2.5 bits 上的 70% PPL reduction（49.3→14.9），但这主要 benefit 来自 distortion model calibration 而非 constraint
- 他们的 "failure mode" 是 distortion model mismatch（用错 β），不是 catastrophic allocation

---

## 对 paper_framing.md Differentiation Section 的建议

当前 framing 已经很好，补充几点：

1. **Action space gap 是根本性差异**：RateQuant 的 optimality guarantee（Proposition 6）仅对 consecutive integers 成立。对实际硬件支持的 {2,4,8,16}，他们的 greedy 不 optimal，且 rounding 引入未量化误差。这不是 implementation detail，是 theoretical gap。

2. **Additive failure 的强化论证**：RateQuant Appendix M 自己承认 "per-head independence assumption may not hold"，但没有提供 evidence 或 solution。我们的 PPL=36.92 实验是这个 assumption failure 的第一个定量证据，cardinality constraint 是第一个 solution。

3. **可以用 RateQuant 的 Theorem 3 反过来论证**：他们的 gain ratio = AM/GM 是在 additive assumption 下的 upper bound。如果 non-additivity 存在，实际 gain 可能远低于这个 bound（甚至为负，如我们的 unconstrained case）。

4. **弱化"RateQuant 也失败"的说法**：RateQuant 在 consecutive integer 上实际 works well（49.3→14.9）。不要说 RateQuant 失败，而要说 RateQuant 的 framework 无法 extend 到 practical discrete bit-widths without our constraint mechanism。

5. **K/V separation 可以借鉴**：RateQuant 的 K/V asymmetric allocation 是值得考虑的 extension。在 MCKP formulation 中，这只需要将 K-head 和 V-head 作为独立 item 处理，constraint 分别施加。

Sources:
- [RateQuant Paper (arXiv)](https://arxiv.org/abs/2605.06675)
- [RateQuant HTML Full Text](https://arxiv.org/html/2605.06675)

---
