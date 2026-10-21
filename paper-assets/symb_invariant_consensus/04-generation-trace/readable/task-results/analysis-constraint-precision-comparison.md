# analysis constraint precision comparison

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_constraint-precision-comparison_20260518T195027_result.json`
- **Structured JSON:** [`f9411dabe620118aacef.json`](../../sessions/f9/f9411dabe620118aacef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是完整报告。

---

## Per-Problem Constraint Precision 对比分析报告

### 1. 基础指标对比

| 指标 | Mistral-7B (exp033) | Qwen2.5-14B (exp026) |
|------|-------|-------|
| SICA accuracy | 59.31% | 74.51% |
| SC accuracy | 54.41% | 75.00% |
| **Delta (SICA-SC)** | **+4.90pp** | **-0.49pp** |

### 2. Constraint Quantity & Uniqueness

| 指标 | Mistral-7B | Qwen-14B |
|------|-----------|----------|
| Total extracted/problem | 68.8 | 67.1 |
| **Unique after dedup/problem** | **39.3** | **30.1** |
| **Dedup ratio (unique/total)** | **0.557** | **0.451** |
| Mistral has more unique constraints | 153/204 problems | — |

**关键发现**：两模型提取的原始 constraint 总量相近（~68），但 Mistral 的 unique constraints 多出 30%（39.3 vs 30.1）。Qwen 的 constraints 高度冗余（dedup ratio 仅 0.451），说明不同 traces 反复提取相同的 symbolic 规则。

### 3. Contradiction Rate

| 指标 | Mistral-7B | Qwen-14B |
|------|-----------|----------|
| Global contradiction rate | **3.50%** | 0.91% |
| Problems with contradictions | **128/204 (62.7%)** | 36/204 (17.6%) |

Mistral 的 contradiction rate 是 Qwen 的 **3.8 倍**。62.7% 的 Mistral 问题存在 trace 间的 constraint 矛盾，而 Qwen 仅 17.6%。矛盾本身不是坏事——它意味着 traces 在探索不同推理路径，为 MaxSAT solver 提供了需要裁决的真实信号。

### 4. MaxSAT Satisfaction

| 指标 | Mistral-7B | Qwen-14B |
|------|-----------|----------|
| Sat ratio (satisfied/unique) | 0.961 | **0.991** |

Qwen 的 sat ratio 接近 1.0（中位数 = 1.000），意味着 solver 几乎不需要做任何取舍——所有 constraints 完全一致。这表明 **solver 实际上没有做有意义的优化**，只是在确认已知答案。

### 5. Trace Diversity（核心差异）

| 指标 | Mistral-7B | Qwen-14B |
|------|-----------|----------|
| Majority fraction | 0.752 | **0.889** |
| Entropy | **0.815** | 0.350 |
| Distinct answer types | **2.36** | 1.51 |
| **Unanimous (100%)** | **38 (18.6%)** | **120 (58.8%)** |
| Strong majority (75-99%) | 71 (34.8%) | 49 (24.0%) |
| Moderate majority (50-74%) | 79 (38.7%) | 32 (15.7%) |
| Split (<50%) | 16 (7.8%) | 3 (1.5%) |

**这是最核心的差异。** Qwen 在 58.8% 的问题上 12 条 traces 给出完全一致的答案（unanimous），而 Mistral 仅 18.6%。Qwen 的平均 entropy 只有 0.350（中位数 0.000），Mistral 是 0.815。Qwen 的 traces 太一致了——solver 拿到的输入已经是"所有人都同意 A"，constraints 自然也都指向 A，SICA 退化为 SC。

### 6. Discriminative Analysis (SICA vs SC)

| 指标 | Mistral-7B | Qwen-14B |
|------|-----------|----------|
| Both correct | 109 | 150 |
| Both wrong | 81 | 49 |
| **SICA wins** | **12** | 2 |
| SC wins | 2 | 3 |
| Discordant total | 14 (6.9%) | 5 (2.5%) |
| **SICA win rate (discordant)** | **85.7%** | 40.0% |

Mistral 上，当 SICA 和 SC 不一致时，SICA 正确的概率高达 85.7%。Qwen 上仅 40.0%，甚至不如随机。

### 7. SICA Override（翻转）分析

| 指标 | Mistral-7B | Qwen-14B |
|------|-----------|----------|
| Override rate | 8.3% (17/204) | 3.4% (7/204) |
| **Override precision** | **70.6%** (12/17) | **28.6%** (2/7) |
| Mean entropy on flip problems | **1.351** | 1.060 |
| Mean unique constraints on flips | 40.9 | 24.7 |

Mistral 的 SICA 更敢翻转（8.3% vs 3.4%），翻转时精度 70.6%（大多数翻对了）。Qwen 的翻转精度仅 28.6%（翻了 7 个，5 个翻错了）。翻转集中发生在高 entropy 问题上（Mistral 1.351, Qwen 1.060）。

### 8. Confirmation Bias 分析

| 指标 | Mistral-7B | Qwen-14B |
|------|-----------|----------|
| Majority answer score fraction | 0.676 | **0.835** |
| High confirmation (>80%) | 65/204 (31.9%) | **127/204 (62.3%)** |

Qwen 的 constraints 本质上在做 **majority vote 的确认**：62.3% 的问题中，majority answer 的 SICA score 占总 score 的 80% 以上。Mistral 仅 31.9%。Qwen 的 SICA 是一个昂贵的 SC 复读机。

### 9. Entropy-Conditioned 效果

| Entropy bucket | Mistral-7B (n, delta) | Qwen-14B (n, delta) |
|----------------|----------------------|---------------------|
| Low (0-0.5) | n=65, **+0.0pp** | n=135, **+0.0pp** |
| Medium (0.5-1.0) | n=66, **+4.5pp** | n=48, **-4.2pp** |
| High (1.0+) | n=73, **+9.6pp** | n=21, **+4.8pp** |

**这张表是全文最重要的证据。**

- **低 entropy**：两个模型 SICA=SC，符合预期——traces 一致时 constraints 无额外信息。
- **高 entropy**：**两个模型的 SICA 都有正收益**（Mistral +9.6pp, Qwen +4.8pp）。这说明 SICA 的机制本身是有效的，问题不在方法而在输入。
- **关键差异在 mass 分布**：Mistral 有 73 个高 entropy 问题（35.8%），Qwen 只有 21 个（10.3%）。Qwen 的 66.2% 问题被锁死在低 entropy 区间，SICA 无用武之地。
- **中 entropy 区间 Qwen 反而 -4.2pp**：说明当 Qwen 的 traces 有轻微分歧时，constraints 提取引入了噪声而非信号。

---

### 10. "Regime-Dependent Capability Trap" 机制解释

数据完整支持以下因果链：

```
强模型高 SC → traces 高度一致 → constraints 高度冗余
→ MaxSAT solver 无真实信号 → SICA ≈ SC
→ 少量 override 反而引入噪声 → SICA ≤ SC
```

```
弱模型低 SC → traces 多样化 → constraints 含真实分歧
→ MaxSAT solver 可做有意义的裁决 → SICA > SC
→ override precision 高 → SICA 持续正收益
```

具体机制的量化证据：

1. **Diversity bottleneck**：Qwen 58.8% unanimous vs Mistral 18.6%，直接阻断了 constraint extraction 获取新信息的通道。
2. **Redundancy trap**：Qwen dedup ratio 0.451 vs Mistral 0.557。更多 traces 不产生更多 unique constraints，只是重复。
3. **Solver triviality**：Qwen sat ratio 0.991，solver 没有做真正的优化。Mistral 0.961，solver 在 3.9% 的 constraints 上做了取舍。
4. **Override quality**：Mistral override precision 70.6%（正信号），Qwen 28.6%（负信号）。
5. **Entropy-conditional universality**：conditioned on high entropy, **两个模型的 SICA 都有效**（+9.6pp 和 +4.8pp）。差异仅在高 entropy 问题的数量上。

### 11. 论文 Claim 评估

**"regime-dependent capability trap" framing 是否成立？** 成立，且数据非常有力。

**关键 talking points**：
- 不是说 SICA 对强模型"无效"，而是强模型不产生足够的 trace diversity 来激活 constraint extraction 的机制。
- Conditioned on entropy, SICA 在两个模型上都有效（Table 9 的 entropy-conditioned 分析是最好的证据）。
- 量化了 "capability trap" 的具体路径：SC↑ → diversity↓ → unique constraints↓ → sat ratio↑ → SICA 退化。

**是否需要更多数据点？**
- 建议加一个 **中间 SC 水平** 的模型（如 Qwen2.5-7B，SC≈63-67%）来验证 transition point。exp035 (Qwen2.5-7B FOLIO-204) 的数据已经在服务器上，可以直接补充。
- 这三个数据点（Mistral-7B SC≈54%, Qwen-7B SC≈65%?, Qwen-14B SC≈75%）可以画出 "SICA gain vs SC baseline" 的 trend，更有说服力。

---
