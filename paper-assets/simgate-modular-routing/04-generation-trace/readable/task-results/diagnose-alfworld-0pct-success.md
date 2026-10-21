# diagnose alfworld 0pct success

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_alfworld-0pct-success_20260514T143540_result.json`
- **Structured JSON:** [`525379521063625feb1d.json`](../../sessions/52/525379521063625feb1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

实验实际上**没有 0% 成功率**，数据如下：

| 策略 | 成功率 |
|------|--------|
| Internal（无 action list） | 2/50 (4%) |
| Deterministic（有 action list） | 25/50 (50%) |

**根因**：Internal mode 低成功率是因为 Qwen2.5-7B 用自然语言名称（"table"/"couch"/"kitchen"）而 ALFWorld 用特定命名（"countertop 1"/"sofa 1"），`match_to_admissible()` 匹配失败后 fallback 到 `admissible[0]`（任意动作），模型就在错误位置反复打转。

**这不是 bug**。Internal mode 设计意图就是测试无外部计算时的表现。4% vs 50% 的差距正是有价值的 counterfactual 信号（46% det-preferred 标签率）。

**建议：不要 kill 实验，继续跑完 140 episodes。** 数据对训练 router 是有用的。

报告已写入 `artifacts/alfworld_cf_diagnosis.md`。

---
