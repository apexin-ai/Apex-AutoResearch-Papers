# ops diagnose cqa1 stale running

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-cqa1-stale-running_20260521T212441_result.json`
- **Structured JSON:** [`bf3012819f41735e8445.json`](../../sessions/bf/bf3012819f41735e8445.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个实验已更新为 DONE。

## 诊断结果汇总

**cqa1-33015 上 6 个 SmolVLA 实验均已完成，全部 0.0% SR（500 episodes, Wilson CI 95%: [0, 0.76%]）。**

| 实验 | Mode | k_ratio | SR | 结论 |
|------|------|---------|-----|------|
| l2norm_k070 | L2-norm | 0.7 | 0.0% | hypothesis confirmed |
| l2norm_k030 | L2-norm | 0.3 | 0.0% | hypothesis confirmed |
| random_k070 | Random | 0.7 | 0.0% | hypothesis confirmed |
| random_k030 | Random | 0.3 | 0.0% | hypothesis confirmed |
| random_k090 | Random | 0.9 | 0.0% | hypothesis confirmed |
| random_k050 | Random | 0.5 | 0.0% | hypothesis confirmed |

SmolVLA cliff-edge behavior 完全确认：无论 pruning method（L2-norm / random）还是 keep ratio（0.3–0.9），只要移除任意比例的 vision tokens，SR 直接归零。所有 10 个 task 均跑满 280 max steps 无一成功。

Registry 已全部更新：metrics → log_path → checkpoint_path → conclusion=success → status=DONE。

---
