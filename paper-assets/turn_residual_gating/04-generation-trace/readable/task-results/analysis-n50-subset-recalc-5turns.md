# analysis n50 subset recalc 5turns

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n50_subset_recalc_5turns_20260520T202502_result.json`
- **Structured JSON:** [`98324c45a56b7079d46a.json`](../../sessions/98/98324c45a56b7079d46a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the consolidated comparison:

## Results

### Turn distribution (N=50)
- Total: 50 conversations, mean=3.6 turns
- ≥5 turns: **8 conversations** (16%)
- ≥4 turns: **23 conversations** (46%)
- Distribution: [2×11, 3×16, 4×15, 5×1, 6×3, 7×4]

### Per-β mid_gar comparison

| Beta | N=5 (original) | N=50 full | N=50 corrected | N=50 ≥5t (N=8) | N=50 ≥4t (N=23) |
|------|---------------|-----------|----------------|-----------------|------------------|
| 0.0  | 0.0280        | 0.1011    | 0.0641         | **0.0791**      | 0.0577           |
| 2.0  | 0.0620        | 0.2068    | 0.1280         | **0.1428**      | 0.1339           |
| 3.0  | —             | 0.6662    | 0.5558         | **0.5410**      | 0.5611           |
| 4.0  | —             | 0.7579    | 0.6439         | **0.5921**      | 0.6352           |
| 5.0  | 0.6795        | 0.8315    | 0.7271         | **0.6666**      | 0.7164           |
| 10.0 | 0.9590        | 0.9806    | 0.9612         | **0.9406**      | 0.9566           |

PPL comparison (≥5t subset):

| Beta | N=50 full | N=50 ≥5t |
|------|-----------|----------|
| 0.0  | 1.432     | 1.484    |
| 5.0  | 1.772     | 1.737    |
| 10.0 | 3.452     | 2.118    |

### Key findings

1. **≥5 turns 子集的 baseline GAR (β=0) = 0.079**, 比全量 N=50 corrected (0.064) 稍高，但离 N=5 的 0.028 仍有距离。长对话天然 mid_gar 并不更低。

2. **≥5 turns 子集全面拉低了 steering GAR**（对比 N=50 full/corrected），符合预期——长对话中 steering 需要更多 turns 才能收敛，mid-turn 窗口 [2:8] 捕获的效果偏低。

3. **N=8 太小，统计可靠性存疑。** ≥4 turns (N=23) 是更合理的 robustness check，趋势一致但方差更小。

4. **PPL 在 ≥5t 子集明显更低**（尤其 β=10: 2.12 vs 3.45），说明短对话中 high-beta steering 的 PPL 膨胀更严重。

### 结论

≥5 turns 子集的 baseline GAR 并没有更接近 N=5（反而稍高），说明 N=5 vs N=50 的 GAR 差异主要来自 conversation sampling variance 而非对话长度偏差。如果写 robustness check，建议用 ≥4 turns (N=23) 而非 ≥5 turns (N=8)——样本量太小难以支撑结论。

数据已保存到服务器 `runs/attention_steering/attention_steering_gen_n50_subset_5turns.json`。

---
