# run a2 reasoning traces cuda0

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_a2_reasoning_traces_cuda0_20260512T155751_result.json`
- **Structured JSON:** [`115bc8a55c8eab440e88.json`](../../sessions/11/115bc8a55c8eab440e88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

**A2: Attention vs EMA — Reasoning Traces**

| 指标 | 值 |
|------|-----|
| Last-chunk Spearman | **-0.2694** |
| Last-chunk Pearson | -0.1019 |
| Accumulated Spearman | -0.2562 |
| Accumulated Pearson | -0.2655 |
| **Verdict** | **complementary** |

**关键发现**：EMA scores 和 attention importance 呈现**负相关**（ρ ≈ -0.27），不仅不冗余，方向甚至相反。

Top layers（最强负相关）：
- Layer 13: ρ = -0.53
- Layer 11: ρ = -0.53  
- Layer 10: ρ = -0.51

Bottom layers（几乎无相关）：
- Layer 24-31: |ρ| < 0.05

**判定**：Global Spearman = -0.27 < 0.5 → **complementary**。EMA 和 attention 提供互补信号，hybrid 策略有意义。

产出文件：
- `/root/carc/results/a2_reasoning_traces.json`
- `/root/carc/figures/a2_reasoning_correlation.png`
- `/root/carc/figures/a2_reasoning_scatter.png`

---
