# code permutation test script

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_permutation_test_script_20260527T170848_result.json`
- **Structured JSON:** [`2502a64da180f91dc1c5.json`](../../sessions/25/2502a64da180f91dc1c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本和结果已生成并注册。核心发现：

**2-seed 模式 (当前)**
- 单尾 p = 0.0357 (1/28) — α=0.05 显著
- 双尾 p = 0.0714 (2/28) — 仅 α=0.10 边际显著
- Welch t: 单尾 p = 0.0035

**Sensitivity (3-of-9 模式)**

| s2 | Perm 单尾 | Perm 双尾 | α=0.05? |
|----|-----------|-----------|---------|
| 54 | 0.1071 | 0.2143 | NO |
| 55 | 0.0714 | 0.1548 | NO |
| **56** | **0.0476** | **0.0833** | **YES** |
| 57 | 0.0357 | 0.0595 | YES |
| 58 | 0.0119 | 0.0357 | YES |
| 59 | 0.0119 | 0.0357 | YES |

确认 Reviewer 判断：**s2 ≥ 56% 是单尾 permutation p < 0.05 的阈值**。s2 ≥ 58 时双尾也 < 0.05。

---
