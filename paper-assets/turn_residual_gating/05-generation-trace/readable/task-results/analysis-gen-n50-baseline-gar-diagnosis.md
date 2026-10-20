# analysis gen n50 baseline gar diagnosis

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gen_n50_baseline_gar_diagnosis_20260520T194141_result.json`
- **Structured JSON:** [`1a5217a184d1196c1f73.json`](../../sessions/1a/1a5217a184d1196c1f73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整了。以下是诊断结论：

---

## 诊断结果

### Q1: N=5 hardcoded 每个对话生成几个 turns？
**10 个 user turns**（CONVERSATIONS_DATA 每个子列表 10 个问题），实际生成时受 1800 token 上限约束，`avg_gar_per_turn` 有 **10 个值**，说明 5 个对话都跑满了 10 轮。

### Q2: N=50 --data-file 分支每个对话生成几个 turns？
**2-7 个 user turns**，取决于 eval_200.json 每条对话的 user 消息数。日志确认：Conv 4/6/11/14/17/20/26 等只有 2 turns，Conv 9 有 7 turns。

### Q3: 两个分支的 turn 数一致吗？
**严重不一致。** Hardcoded=10 turns，data-file 的前 50 条中 `num_turns` 分布：

| num_turns (total msg) | user turns | 出现次数 |
|---|---|---|
| 4 | 2 | ~15 |
| 6 | 3 | ~17 |
| 8 | 4 | ~12 |
| 10-14 | 5-7 | ~6 |

**mean = 3.6 user turns, min = 2, max = 7**

### Q4: mid_turns_avg_gar 定义在两个分支是否相同？
**代码相同，但结果语义完全不同。** 关键逻辑：

```python
min_turns = min(len(c) for c in beta_gar_curves)  # 所有曲线截断到最短
aligned = [c[:min_turns] for c in beta_gar_curves]
avg_gar = np.mean(aligned, axis=0).tolist()

if len(avg_gar) > 2:
    mid_gar = np.mean(avg_gar[2:8])   # 跳过 turn 0-1
else:
    mid_gar = np.mean(avg_gar)         # 包含所有 turns
```

- **N=5**: min_turns=10 → avg_gar 有 10 个值 → 走 `if` 分支 → `mean(avg_gar[2:8])` = **0.028**
- **N=50**: min_turns=**2**（因为有 2-turn 对话）→ avg_gar 只有 2 个值 → 走 `else` 分支 → `mean(avg_gar)` = mean([0.1297, 0.0725]) = **0.101**

### Q5: eval_200.json 前 50 条 user turn 数分布
min=2, max=7, mean=3.6, median=3

### Q6: GAR 偏高的根因

**不是数据质量问题，是 min_turns 对齐 + mid_gar 分支逻辑的 artifact。**

两步叠加：
1. **min_turns 截断**：50 个对话中只要有 1 个 2-turn 对话，所有曲线都被截到 2。后续 turns 的 GAR（普遍更低）全部被丢弃。
2. **mid_gar else 分支**：len=2 时不跳过 early turns，直接平均 turn 0+1。而 turn 0 的 baseline GAR（~0.13）天然比 turn 2+ 的（~0.02）高 6 倍。

N=5 的 mid_gar 测的是 **turn 2-7 的衰减后 GAR**，N=50 测的是 **turn 0-1 的 early GAR**。两者不可比。

### 修复建议
- **方案 A**：过滤掉 user turns < 5 的对话，保证 min_turns ≥ 5
- **方案 B**：不做 min_turns 截断对齐，改为每个对话单独算 mid_gar（跳过 turn 0-1），再跨对话取均值
- **方案 C**：固定 mid_gar 永远取 `avg_gar[2:min(8, len)]`，不足 3 turns 的对话不参与 mid_gar 统计

---
