# research data dedup check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_data-dedup-check_20260513T152028_result.json`
- **Structured JSON:** [`c2c8424f4ab64e1899c7.json`](../../sessions/c2/c2c8424f4ab64e1899c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。以下是结论：

---

## 调查结果

### 1. 数据是否完全重复？**否。** 两个 task 的数据不是重复的。

**实锤证据：**
- Action histories 完全不同（每个 episode 的每个 step 都不同）
- 步数不同（如 ep0: melt 17步 vs change 18步）
- always_deterministic 有 6 个 episode 分数不同
- oracle_routing 有 2 个 episode 分数不同
- 触发 -100 的具体 action 不同（如 ep0: "focus on workshop" vs "focus on inventory"）

### 2. 为什么 always_internal 的 20 个 scores 完全相同？

**结构性巧合**，由三个因素叠加导致：

**(a) 共享世界状态**：ScienceWorld 中 "melt" 和 "change-the-state-of-matter-of" 的 variation 0-19 生成完全相同的初始环境（同样的房间、物品、布局）。只有 task description 不同（"melt water" vs "change the state of matter of water"）。

**(b) 相同的失败机制**：LLM 表现极差，只会做 "connect X to Y" 之类的无意义动作。在 11/20 个 episode 中，LLM 随机执行了 "focus on [错误对象]" → 触发 ScienceWorld 的 **-100 即死惩罚**。两个 task 中被 focus 的对象不同（如 workshop vs inventory），但惩罚一样。

**(c) 极度稀疏的分数分布**：只有 3 种可能的结果：
| 结果 | 含义 | 出现次数 |
|------|------|---------|
| -100 | LLM 随机触发 "focus on [错误对象]" | 11/20 |
| 0 | 30 步内无进展且未触发 focus | 7/20 |
| 3 | 意外执行了 "activate stove/oven"（两个 task 都给分） | 2/20 |

同一 variation 是否触发 "focus on" 取决于 LLM 在相同环境中是否倾向于尝试 focus 动作，这与 variation 的世界状态高度相关，因此两个 task 呈现相同的 -100/0/3 模式。

### 3. 如何向 Reviewer 解释？

> "melt" 和 "change-the-state-of-matter-of" 在 ScienceWorld 中是不同 task（不同 scoring function，det 分数已验证不同），但共享相同的 environment variations。Internal model (Qwen2.5-7B) 在两者上都表现极差（无法理解 task），分数被 "focus on wrong object → -100" 的失败模式主导，导致 always_internal 分数巧合相同。这本身也揭示了一个有意义的发现：当 agent 的内部策略退化为随机探索时，不同 task 的 scoring signal 会趋同。

---
