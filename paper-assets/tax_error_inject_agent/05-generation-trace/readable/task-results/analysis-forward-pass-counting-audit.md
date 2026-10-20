# analysis forward pass counting audit

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_forward-pass-counting-audit_20260515T164729_result.json`
- **Structured JSON:** [`d0d7d240deb6cb632d85.json`](../../sessions/d0/d0d7d240deb6cb632d85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。结论如下：

---

## 审查结论

### 1. 确认：760 是 turn 级分类，不是 trajectory 级

`classify_sample()` 逐行检查每个 JSONL line（= 1个 turn）的 user content 是否包含 `[Error Type: ...]`。数据结构：

| 级别 | clean | injected | 总计 |
|------|-------|----------|------|
| **Trajectory** | 351 | 760 | 1,111 |
| **Turn（JSONL line）** | 4,358 | 4,671 | 9,029 |

### 2. 760 到底是什么

每条注入轨迹恰好有 **1个 turn** 包含 `[Error Type: ...]` 标签（min=1, max=1, mean=1.0）。760条注入轨迹 × 1个标签 turn/轨迹 = 760。

### 3. 8269 包含什么

- 4,358 个 clean 轨迹的全部 turns
- 3,911 个注入轨迹中**没有 error tag 的 turns**（注入轨迹平均 6.1 turns，只有 1 turn 有 tag → 其余 ~5.1 turns 被当作 "clean"）

**这是 bug：注入轨迹中 83.7% 的 turns 被错误归类为 clean。**

### 4. Loss 计算本身没问题

`prepare_batch()` 对每个 JSONL line 只算最后一个 assistant response 的 loss（prefix 部分 label=-100 被 mask 掉），per-sample mean CE over response tokens。计算逻辑正确。

问题纯粹在分类标签，不在 loss 计算。

### 5. paper_framing.md 的数字

paper_framing.md 说的 "4,358 clean + 4,671 injected = 9,029" 是 **turn 级计数**（trajectory 级是 351 + 760 = 1,111）。这个 framing 本身也值得商榷——称 4,671 turns 为 "injected" 但其中只有 760 turns 真正包含错误注入。

### 6. 修复建议

`classify_sample()` 应该改为 **trajectory 级分类**：如果一个 turn 属于注入轨迹（无论该 turn 本身是否包含 error tag），就标记为 "injected"。

两种实现方式：
- **方式 A**：在数据生成阶段给每行 JSONL 加一个 `"subset": "clean"|"injected"` 字段，forward pass 直接读
- **方式 B**：在 `load_data()` 中利用数据排列顺序——前 4,358 行为 clean，4,358 行之后为 injected（当前数据确实是这样排列的）

修复后预期结果：clean_n=4358, injected_n=4671，与 paper_framing 一致。

### 7. 论文应该用什么数字

| 指标 | 当前（错误） | 修复后（正确） |
|------|-------------|---------------|
| clean samples | 8,269 turns | 4,358 turns |
| injected samples | 760 turns | 4,671 turns |
| 分类依据 | turn 内有 error tag | 该 turn 所属轨迹是否被注入 |

---
