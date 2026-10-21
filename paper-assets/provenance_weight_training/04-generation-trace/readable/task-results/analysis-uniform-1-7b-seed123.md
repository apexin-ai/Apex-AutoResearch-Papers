# analysis uniform 1 7b seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_uniform_1_7b_seed123_20260519T040528_result.json`
- **Structured JSON:** [`2fb7988386f3e95ec52d.json`](../../sessions/2f/2fb7988386f3e95ec52d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 结果

**uniform_1_7b_seed123**: eval PPL = **13.26**, loss = 2.5851, 6103 steps

## 1.7B 两种子对比

| Method | seed42 | seed123 | Mean±Std |
|--------|--------|---------|----------|
| Adaptive | 13.27 | 13.25 | 13.26±0.01 |
| Uniform | 13.50* | **13.26** | 13.38±0.12 |
| Δ (adaptive−uniform) | −0.23 | **−0.01** | −0.12±0.11 |

\* seed42 uniform 是 Plan B（resumed optimizer）

## 结论：**negative**

seed123 的公平对比（均为 from-scratch）显示 adaptive (13.25) 与 uniform (13.26) 几乎无差异（Δ = −0.01）。seed42 的大差距（Δ = −0.23）很可能是 Plan B optimizer confound 导致的伪信号。**1.7B 尺度的 adaptive 优势不成立。**

对论文的影响：需要重新考虑 1.7B 结果的叙事角度。报告已写入 artifacts 并注册，registry 状态已更新为 DONE。

---
