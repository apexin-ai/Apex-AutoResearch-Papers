# code split isolation check

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_split-isolation-check_20260514T124904_result.json`
- **Structured JSON:** [`c3fd539d2a27f7a49acc.json`](../../sessions/c3/c3fd539d2a27f7a49acc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：存在严重泄漏

**221 / 344 个原始 test instances 泄漏到了 holdout train set，涉及 5,744 / 8,101 个 test windows（70.9%）。**

### 泄漏根因

`split_by_instance` 的逻辑是：
1. `sorted(set(instance_ids))` 获取唯一 instance 列表
2. `random.Random(42).shuffle(unique)` 打乱
3. 按 70/15/15 比例切分

Holdout 过滤掉 outcome_bp 后移除了 14 个 instance（2285 → 2271），导致 `sorted(set(...))` 产生不同列表。**相同 seed 对不同长度列表的 shuffle 结果完全不同**，instance 被重新分配到了不同的 split。

### 分配详情

| 原始 test 的 344 个 instances 去向 | 数量 |
|---|---|
| → Holdout train | **221** (泄漏) |
| → Holdout val | 50 |
| → Holdout test | 71 |
| → 被移除 | 2 |

### 对 cross-evaluation 分数的影响

Holdout 模型在原始测试集上得到的 macro-F1=0.8593 **被严重膨胀**：测试集中 70.9% 的 windows 来自 holdout 训练时见过的 instance。这些 instance 的 windows（虽然部分被 outcome_bp 过滤掉了）在训练集中仍有大量同 instance 的 windows，模型对这些 instance 的模式已经 overfit。

---
