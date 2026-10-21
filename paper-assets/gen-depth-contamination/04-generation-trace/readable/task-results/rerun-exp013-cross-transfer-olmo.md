# rerun exp013 cross transfer olmo

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_rerun_exp013_cross_transfer_olmo_20260521T155907_result.json`
- **Structured JSON:** [`194969352abe76d6b13e.json`](../../sessions/19/194969352abe76d6b13e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果摘要：

**K\* Transfer Matrix (train=row, test=col):**

|              | OLMo | Pythia | Qwen |
|--------------|------|--------|------|
| **OLMo**     | 1    | 1 ✗    | 1 ✗  |
| **Pythia**   | 1 ✓  | 2      | 1 ✗  |
| **Qwen**     | 1 ✓  | 2 ✓    | 2    |

**Aggregate accuracy: 6/9 = 66.7%**（原始 ~80-92%）

核心发现：
- 所有 **X → OLMo** pair 正确预测 K\*=1
- **Qwen** 是最佳通用训练器（3/3 正确），**OLMo** 是最差训练器（1/3 正确）
- OLMo K\*从2降为1 引入非对称性：弱信号模型的分类器无法向上迁移 K\*
- 3个错误 pair 都是训练模型信号不足以捕捉测试模型 depth 1→2 的区别

结果已保存到：
- 服务器：`results/exp013_olmo_rerun/`
- 本地：`artifacts/exp013_cross_transfer_olmo_rerun.md`

---
