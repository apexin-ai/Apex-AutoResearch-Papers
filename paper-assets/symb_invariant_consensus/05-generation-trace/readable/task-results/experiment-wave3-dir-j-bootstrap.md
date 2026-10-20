# experiment wave3 dir j bootstrap

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_wave3-dir-j-bootstrap_20260520T090123_result.json`
- **Structured JSON:** [`9549cd7043261e02e30f.json`](../../sessions/95/9549cd7043261e02e30f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Direction J 实验完成。结果汇总：

| Round | Accuracy | Flips | Improved | Degraded |
|-------|----------|-------|----------|----------|
| R0 (SC) | **54.41%** | - | - | - |
| **R1** | **56.86%** | 32 | 15 | 10 |
| R2 | 54.41% | 16 | 5 | 10 |
| R3 | 54.90% | 11 | 5 | 4 |
| R4 | 54.41% | 10 | 4 | 5 |
| R5 | 52.45% | 6 | 1 | 5 |

**关键发现：**
- **R1 峰值 +2.45pp**（56.86%），净改正 5 题（15 improved - 10 degraded）
- 后续轮次围绕基线振荡，翻转数递减（32→16→11→10→6）但信噪比下降
- **与 CEGIS 一致：R1 捕获主要信号，迭代不能持续改善**
- 翻转精度约 47%（R1: 15/32），略好于随机但不够稳健
- Per-type: True 73.6%, False 34.9%, Unknown 46.4%（False 类最弱）

结论：Bootstrapped Gold Approximation 在 R1 有微弱正信号，但迭代 self-refinement 不收敛到更好的解。结果保存在 `results/direction_j_bootstrap/`。

---
