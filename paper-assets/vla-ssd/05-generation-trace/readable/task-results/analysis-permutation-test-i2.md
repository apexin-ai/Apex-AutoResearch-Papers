# analysis permutation test I2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_permutation_test_I2_20260518T150757_result.json`
- **Structured JSON:** [`244c14694b31a5f7b04e.json`](../../sessions/24/244c14694b31a5f7b04e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 指标 | 精确配对置换 p | MC 非配对 p |
|------|--------------|------------|
| **CV** (ctrl 2.74 vs inst 1.30) | **0.0156** | **0.0048** |
| **I²** (inst 0.87 vs ctrl 0.78) | 0.1562 | 0.1434 |

**CV 差异显著**：instruction heads 在所有 6 个连续 action 维度上一致地产生更低 CV（更均匀的扰动），精确置换 p=0.0156（2^6=64 种排列中仅 1 种 >= 观测值）。7 维（含 gripper）时 p=0.0078 更强。

**I² 差异不显著**：精确置换仅 32 种排列（2^5），最小可能 p=0.0312，分辨率不足以在 α=0.05 下检测 0.086 的 I² 差距。MC 非配对检验同样不显著（p=0.14）。这是统计功效不足（5 个 task），不代表效应不存在。

结果已保存至 `/root/autodl-tmp/vla-ssd/results/permutation_test_I2.json`，registry 已更新。

---
