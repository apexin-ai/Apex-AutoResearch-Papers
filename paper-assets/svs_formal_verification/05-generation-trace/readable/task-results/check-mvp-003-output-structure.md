# check mvp 003 output structure

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_mvp_003_output_structure_20260514T105839_result.json`
- **Structured JSON:** [`ae86b9350f6fbb3b9fbf.json`](../../sessions/ae/ae86b9350f6fbb3b9fbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已确认清楚。汇报如下：

---

## mvp_003 输出数据结构

### 文件位置
`/root/outputs/results_partial.json`（27KB，1125 行，JSON 完整闭合）

### 统计
- **11 个 problem**（`gold_label` 出现 11 次）
- **88 条 chain**（`chain_id` 出现 88 次），平均每 problem 8 条

### 数据结构

**Problem 级别（top-level array 的每个元素）：**
| 字段 | 类型 | 说明 |
|------|------|------|
| `problem_id` | string | 如 `"pw_20952"` |
| `gold_label` | string | Ground truth: `"True"` / `"False"` / `"Unknown"` |
| `selected_answer` | string | SVS 选出的答案 |
| `sc_answer` | string | Self-Consistency 选出的答案 |
| `group_scores` | dict | 按答案分组的聚合分数 |
| `correct_svs` | bool | SVS 是否答对 |
| `correct_sc` | bool | SC 是否答对 |
| `chain_verifications` | list | **per-chain 详细数据** |

**Chain 级别（`chain_verifications` 的每个元素）：**
| 字段 | 类型 | 说明 |
|------|------|------|
| `problem_id` | string | 所属问题 |
| `chain_id` | int | chain 编号 |
| `answer` | string | 该 chain 给出的答案 |
| `total_claims` | int | chain 中的 claim 总数 |
| `formalized_claims` | int | 被形式化的 claim 数 |
| `ic_score` | float | **Per-chain IC score** ✅ |
| `fc_score` | float | Per-chain FC score |
| `ic_sat` | bool | IC 是否 SAT |
| `mcs_size` | int | 最大一致子集大小 |

### P2 分析所需数据确认

1. **Per-chain IC score** ✅ — 字段 `ic_score`，float 值，已有
2. **Chain 正确性标注** ⚠️ — **chain 级别没有直接的 correct 字段**。`correct_svs` / `correct_sc` 只在 problem 级别。但可以通过 `chain.answer == problem.gold_label` 推导每条 chain 是否正确
3. **数据格式** ✅ — 标准 JSON，结构清晰

### 采样数据（problem `pw_20952`，8 条 chain）

```
chain_id=0: answer=True, ic_score=0.333, fc_score=0.333, ic_sat=true,  mcs=4/12
chain_id=1: answer=True, ic_score=0.692, fc_score=0.692, ic_sat=true,  mcs=9/13
chain_id=2: answer=True, ic_score=0.667, fc_score=0.667, ic_sat=true,  mcs=6/9
chain_id=3: answer=True, ic_score=0.643, fc_score=0.643, ic_sat=true,  mcs=9/14
chain_id=4: answer=True, ic_score=0.733, fc_score=0.767, ic_sat=false, mcs=22/30
chain_id=5: answer=True, ic_score=0.538, fc_score=0.538, ic_sat=true,  mcs=7/13
chain_id=6: answer=True, ic_score=0.615, fc_score=0.615, ic_sat=true,  mcs=8/13
chain_id=7: answer=True, ic_score=0.750, fc_score=0.750, ic_sat=true,  mcs=6/8
```

### 结论
P2 分析所需数据**基本齐全**。唯一需要补的是 chain 级别的正确性标注，但可以用 `chain.answer == gold_label` 直接推导，不需要修改 mvp_003 代码。

---
