# code ess only baseline

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ess_only_baseline_20260515T071521_result.json`
- **Structured JSON:** [`52794c8b584d0964bf1e.json`](../../sessions/52/52794c8b584d0964bf1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修改正确。注意任务要求脚本路径和 `pretrain_weighted.py` 路径在 `training/` 下，但代码实际在 `artifacts/training/`。服务器端的 `training/` 目录会包含脚本，而服务器上的 `pretrain_weighted.py` 路径可能也是 `training/pretrain_weighted.py`（通过 sync_code）。脚本中 `python training/pretrain_weighted.py` 的路径需要与服务器目录结构一致。

完成。修改总结：

**`artifacts/weighting/alpha_eff.py`**：新增 `find_ess_only_b(q_scores, n_min, b_max=20.0, tol=0.01)` — 二分搜索找 `max{b : ESS(b) ≥ n_min}`。

**`artifacts/training/pretrain_weighted.py`**：
- import 新增 `find_ess_only_b`
- argparse choices 加入 `ess_only`
- `compute_loss` 新增 `ess_only` 分支，调用 `find_ess_only_b` 计算 b*

**`training/run_ess_only_seed42.sh`**：新建运行脚本（已 chmod +x）

**`artifacts/ess_only_implementation.md`**：实现文档

---
