# ssh traj14b eval 3seed

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_traj14b-eval-3seed_20260523T104813_result.json`
- **Structured JSON:** [`0e433f78337fb91a9c22.json`](../../sessions/0e/0e433f78337fb91a9c22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## TRAJ 14B 3-seed Eval 结果

| Seed | Accuracy | F1 macro | Unparseable |
|------|----------|----------|-------------|
| s42  | 89.73%   | 89.66    | 0           |
| s123 | 88.57%   | 88.56    | 0           |
| s456 | 88.28%   | 88.17    | 0           |

**TRAJ 14B: 88.86 ± 0.77 (acc) / 88.80 ± 0.77 (f1)**

### 与其他 formulation 对比

| Model | Accuracy |
|-------|----------|
| CLS 14B  | 89.93 ± 0.80 |
| CWM 14B  | 89.50 ± 0.67 |
| TRAJ 14B | 88.86 ± 0.77 |

- CLS-TRAJ gap: **+1.07pp**
- CWM-TRAJ gap: **+0.64pp**

### 状态

- Predictions 文件：3 个 seed 均正确保存 1032 条 predictions，包含 `problem_id` 字段
- Per-test consistency: s42 76.8%, s123 73.0%, s456 76.7%
- CLS-TRAJ gap < 2pp → **TOST 等价性检验有意义**，三个 formulation 在 14B 尺度上性能非常接近

---
