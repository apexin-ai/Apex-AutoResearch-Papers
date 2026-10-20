# research scorer improvement

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_scorer-improvement_20260515T161830_result.json`
- **Structured JSON:** [`6a553208f3362618308f.json`](../../sessions/6a/6a553208f3362618308f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有代码和数据已读取完毕。以下是完整分析报告。

---

## 1. 当前 Scorer 逻辑总结

```python
# InvariantScorer.score() 伪代码
def score(maxsat_result, traces, candidates):
    answer_traces = {answer: {trace_indices}} from traces  # 每个答案由哪些 trace 产生
    
    for each candidate:
        score = 0
        for each constraint in maxsat_result.satisfied:  # ← 只看 satisfied
            if constraint.source_traces ∩ candidate的trace集合 ≠ ∅:
                score += constraint.weight  # weight = 跨trace出现频次
        scores[candidate] = score
    
    return scores

# InvariantScorer.select_answer() 伪代码
def select_answer(scores, answer_counts):
    top = argmax(scores)
    if tie: break by SC frequency (answer_counts)
    return top
```

**关键设计特征**：
- **仅使用 satisfied 约束作为正信号**，excluded 约束完全丢弃
- 约束到候选答案的映射通过 `source_traces` 间接关联（约束来自哪些 trace → trace 产出了哪个答案）
- 平局时 fallback 到 SC 投票频次

## 2. "SICA=SC" 的精确根因

**根因不是单一的，而是两层叠加**：

### 第一层（结构性）：SC 一致 → 单候选 → SICA 无选择空间

6 个问题的 SC 投票分布：

| 问题 | SC 分布 | 候选数 | SICA 能否不同？ |
|------|---------|--------|----------------|
| P0 (II_01) | {73: 12} | 1 | **不可能** |
| P1 (II_02) | {} | 0 | 两者都为空 |
| P2 (II_03) | {45: 11} | 1 | **不可能** |
| P3 (II_04) | {33: 12} | 1 | **不可能** |
| P4 (II_05) | {80: 1} | 1 | **不可能** |
| P5 (II_06) | {55: 12} | 1 | **不可能** |

**所有 6 题都只有 1 个候选答案（或 0 个）。** 当 `candidates` 列表长度 ≤ 1 时，scorer 的输出被完全决定——不存在任何评分逻辑能改变结果。

### 第二层（评分层）：即使有多候选，信号也不足

以 P4 (aime2024_II_05) 为例（虽然只有 1 个候选，但假设有 2 个）：
- 42 unique constraints → 40 excluded, 2 satisfied (weight=4)
- **scorer 只从 2 条 satisfied 约束中提取信号**，这 2 条总权重仅 4
- 40 条 excluded 约束蕴含的信息（"哪些推理路径自相矛盾"）被完全丢弃
- 即使有第二个候选答案，2 条约束的区分能力极弱

**P4 的 SICA 分数为 `{"80": 0.0}`**——连 satisfied 约束都没覆盖到答案 "80" 的 trace。这说明 satisfied 的 2 条约束的 `source_traces` 与产出 "80" 的 trace (只有 1 条) 不重叠。Scorer 实际上给了唯一候选 0 分，只是因为没有竞争者才选了它。

### 根因总结

```
SICA=SC 的原因 = 
    (1) 强模型 + k=12 → SC 几乎总是 unanimous → 单候选
  + (2) Scorer 仅用 satisfied 正信号 → 高矛盾率时信号近零
  + (3) Excluded 约束信息完全浪费 → 无法利用"矛盾模式"区分
```

问题 (1) 是数据/模型层面的，scorer 改不了。但 (2)(3) 意味着：即使未来遇到多候选场景，当前 scorer 在高矛盾率下依然无力。

---

## 3. 三个改进方向分析

### 方向 A：矛盾约束作为负信号

**思路**：`score(answer) = Σw(satisfied ∩ answer_traces) - α·Σw(excluded ∩ answer_traces)`

被 excluded 的约束来自某些 trace，这些 trace 产出了某个答案。如果答案 X 的 trace 产出了大量被排除的约束，说明 X 的推理路径更不自洽。

**实现复杂度**：简单。`excluded` 已在 `MaxSATResult` 中，`source_traces` 已有。只需在 `score()` 中加一个循环 + 超参 α。约 10 行代码。

**能否解决 P4 问题**：
- **单候选时**：不能。负信号也只是让唯一候选的分数更低，不改变选择。
- **多候选时**：能区分。假设候选 A 的 trace 产出 30 条 excluded，候选 B 的 trace 产出 10 条 excluded → B 的惩罚更小 → 倾向选 B。
- **核心价值**：当 satisfied 稀少但 excluded 丰富时，负信号成为主要区分力。

**风险**：
- 深度推理 trace 可能产出更多约束（包括更多冲突），但答案未必错。惩罚约束数量多的 trace 可能反而惩罚了更好的推理。
- α 超参敏感：过大则噪声约束主导，过小则无效。
- 约束 excluded 的原因可能是"与其他约束矛盾"而非"该约束本身错误"——一条正确约束如果与 39 条错误约束矛盾，也会被 MAX-SAT 排除（因为排除 1 条比排除 39 条权重损失小）。

**额外实验**：需要。至少在有多候选分歧的数据集上验证 α 的效果。

---

### 方向 B：放松 MAX-SAT（weighted partial MAX-SAT 保留更多约束）

**当前实现的误解**：当前 `MaxSATSolver` **已经是** weighted partial MAX-SAT（z3.Optimize + add_soft）。不是 hard MAX-SAT。

**真正的问题**：当 42 条约束中存在大量互相矛盾的子集时，MAX-SAT 的最优解必然排除大量约束——这是数学性质，不是实现问题。

**可能的放松方向**：

**(B1) 松弛为分组一致性**：不全局求解，而是按 trace 分组求解。每组 trace 的约束内部一致性高（来自同一推理链），跨组才有矛盾。保留组内分数，降低跨组权重。
- 复杂度：中等。需重构 solver 为分组模式。
- 风险：失去跨 trace 约束验证的核心优势。

**(B2) 约束置信度加权**：给每条约束一个 prior 置信度（如基于表达式复杂度、提取器信心分），在 MAX-SAT 中用 `weight × confidence` 代替 `weight`。
- 复杂度：中等。需要 constraint_extractor 输出 confidence score。
- 风险：confidence 本身可能不准。

**(B3) 多解集合**：不取 MAX-SAT 唯一最优解，枚举 top-K 满足集（或随机采样近优解），用解的分布来评估约束的"鲁棒性"。
- 复杂度：复杂。z3.Optimize 不直接支持枚举多解，需 blocking clauses 循环。
- 潜力最大但工程量大。

**能否解决 P4 问题**：B1/B2 可能将 satisfied 从 2 条提升到更多，增强正信号。但如果约束确实深度矛盾（P4 的 42 条几何约束大量冲突），放松也有限。

**额外实验**：B2 最值得先试（在 extractor 加 confidence 字段），B3 有长期价值但需大量工程投入。

---

### 方向 C：satisfied 过少时的 fallback（矛盾模式区分）

**思路**：当 `len(satisfied) / len(total) < threshold`（如 < 0.2），切换评分策略。不再看"谁被 satisfied 约束支持"，而看"谁被 excluded 约束牵连最少"。

```python
# Fallback 逻辑伪代码
if satisfied_ratio < threshold:
    for each candidate:
        excluded_exposure = Σw(excluded ∩ candidate_traces)
        score[candidate] = -excluded_exposure  # 越少被牵连越好
    # 或更精细：score = satisfied_support - excluded_exposure
```

**实现复杂度**：简单。约 15 行代码，加一个 threshold 超参。

**能否解决 P4 问题**：
- 单候选：同样不能（根因在第一层）。
- 多候选 + 高矛盾率场景：**这是最直接的解法**。当 satisfied 信号不足时，用"最少矛盾"策略等价于"排除法"——本质上是 Occam's razor 的变体。

**风险**：
- threshold 选择需要调优。太高则频繁 fallback，降低 satisfied 约束的作用；太低则 fallback 太少。
- Fallback 策略本质上和方向 A 的负信号思路重叠，区别是 A 混合使用、C 切换使用。
- 如果所有候选的 excluded_exposure 都接近（约束均匀分布在各 trace 上），区分力仍然弱。

**额外实验**：需在多候选 + 高矛盾率数据上验证。可用 AMC/MATH 中更难的题或故意降低模型能力以制造分歧。

---

## 4. 推荐方向

**推荐 A+C 组合，分两步实施**：

**第一步：方向 C（fallback）**——简单、风险低、直接解决高矛盾率场景的评分真空。即使当前数据集 SC 一致，未来扩展到更难题目或更弱模型时，这是必要的安全网。

**第二步：方向 A（负信号）**——作为非 fallback 模式的增强。在 satisfied 信号充足时，负信号提供额外区分力。与 C 配合形成完整评分体系：
- 正常模式：`score = positive_signal - α·negative_signal`（方向 A）
- Fallback 模式：`score = -negative_signal`（方向 C）

**不优先推荐 B 的原因**：B 的各变体要么改动大（B3）、要么需要上游配合（B2 需 extractor 改），且核心问题（约束深度矛盾时信号衰减）是 MAX-SAT 的数学性质，solver 层面的放松效果有限。

## 5. 额外发现

### 发现 1：单候选问题比 scorer 问题更紧迫

**6/6 题 SICA=SC 的最大原因不是 scorer 不好，而是从没出现过多候选。** 即使 scorer 完美，单候选下 accuracy gain 永远是 0pp。

改进 scorer 之前，应优先确认：在什么数据分布下 SC 会产生分歧（多候选）？如果目标数据集上 SC 几乎总是 unanimous，需要考虑：
- 提高 k（如 k=32）以增加多样性
- 使用 temperature > 0 增加 trace 多样性
- 选择更难的 benchmark（AIME 2024 II 前 6 题对当前模型偏简单）

### 发现 2：P4 的 sica_scores = {"80": 0.0} 暴露了一个边界情况

P4 有 2 条 satisfied 约束（weight=4），但 score("80") = 0.0。这意味着 **satisfied 约束的 source_traces 与产出 "80" 的 trace 不重叠**。

可能的解释：10 条 trace 提取了约束，但只有 1 条 trace 产出了有效答案 "80"（sc_vote_count=1）。那条 trace 的约束可能全被排除了，而 satisfied 的 2 条来自没有产出有效答案的 trace。

这暴露了一个设计假设漏洞：**scorer 假设 "产出约束的 trace" 和 "产出答案的 trace" 高度重叠，但实际可能不是。** 约束来自推理过程，答案来自最终输出——一个 trace 可能推理详细（产出多约束）但答案解析失败，或推理简略但答案正确。

### 发现 3：权重定义值得审视

`UniqueConstraint.weight = 跨 trace 出现频次`。这意味着一条被 3 个 trace 独立得出的约束权重为 3。但这假设"频次 = 可靠度"，在高矛盾场景下可能不成立——一条被 8 个 trace 支持的错误约束（如系统性偏差）会有很高权重，把正确的低频约束挤掉。

---
