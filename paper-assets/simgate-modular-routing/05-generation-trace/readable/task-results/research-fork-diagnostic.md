# research fork diagnostic

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_fork-diagnostic_20260513T073419_result.json`
- **Structured JSON:** [`b6a20ccebeea3509cd2c.json`](../../sessions/b6/b6a20ccebeea3509cd2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。所有数据已收集，以下是完整结论。

---

## 诊断结论

### 1. fork_and_lookahead 没有 bug

Fork 机制完全正确，验证结果：
- `score_before` 与主环境一致 ✓
- action replay 无误 ✓
- `activate stove` → delta=+2.0 ✓
- `activate oven` → delta=+2.0 ✓
- `focus on X` → delta=-100.0 ✓
- `connect X to Y` → delta=0.0 ✓

### 2. -100.0 的来源

**来自 ScienceWorld 环境本身**，不是代码 sentinel。所有 `focus on X` 动作在 boil 任务中会立即返回 `score=-100, done=True`，终结 episode。代码中无 -100 字面值；`get_score()` 从 `info.get("score", 0)` 透传环境值。

统计：
| 模式 | 触发 -100 的 episode 数 |
|------|------------------------|
| always-internal | 5/9 |
| always-deterministic | 3/9 |
| oracle-routing | 4/9 |

### 3. Oracle 全选 internal 的原因

**两个因素叠加：**

**a) Tie-break 偏向 internal**（`phase1_signal.py:233`）：
```python
if internal_delta >= best_det_delta:  # >= 意味着相等时选 internal
```

**b) 95%+ 步骤的 internal_delta 和 det_delta 都是 0.0**。boil 任务的 reward 极度稀疏——只有 `activate stove/oven` 等关键操作给 +2.0/+1.0 分。LLM 生成的动作（`connect X to Y`）对任务完全无效，所以 1-step lookahead 看到的 delta 几乎全是 0。

8 个 episode × 30 步中，非零 delta 的 oracle 步骤只有 24 个，其中大部分是 -100（`focus on` 惩罚），正面信号只有 Ep2 和 Ep3 各 2-3 步。

### 4. 修复建议

| 问题 | 修复 | 优先级 |
|------|------|--------|
| Oracle tie-break 永远偏向 internal | 改为 `>` 或 delta=0 时随机选 | 中（影响 oracle 数据质量） |
| `focus on` 导致 -100 death | fork 已能检测，但 always-internal 无保护。可加黑名单或让 fork 过滤 delta < 0 的动作 | 高 |
| 稀疏 reward 下 1-step lookahead 无信号 | 这是根本瓶颈。考虑 N-step rollout 或启发式中间打分 | 高（架构层面） |
| LLM 生成低质量动作 | prompt 优化或用 valid_actions 过滤 | 高 |

### 5. 是否需要停 GPU 实验？

**不需要**。Fork 机制正确，实验数据有效。数据准确反映了 1-step lookahead 在稀疏 reward 下的局限性——这本身就是有意义的 Phase 1 信号。

但有一个值得注意的问题：当前 oracle routing（4/9 hit -100）比 always-deterministic（3/9）**更差**，因为 oracle 的 tie-break 让它跟随 internal 路径，而 internal 路径更容易撞上 `focus on` 死局。这意味着当前 oracle 不是真正的 upper bound。

---
