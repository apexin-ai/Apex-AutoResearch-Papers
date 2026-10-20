# code best of n eval r2

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_best-of-n-eval-r2_20260513T162010_result.json`
- **Structured JSON:** [`b2eca76ccbe83dd9877a.json`](../../sessions/b2/b2eca76ccbe83dd9877a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行正常。5 样本 dry-run 结果：

**脚本路径**: `/root/autodl-tmp/prov_grounded_uie/src/eval_best_of_n.py`

**关键设计**:
- 三层评估：Best-of-8 chosen（完整 metrics）、Worst-of-8 rejected（下限对照）、Monte Carlo score-based ablation（N=1,2,4,8）
- 从 `evaluate.py` 直接 import `compute_re_f1`/`compute_evi_f1`/`compute_attribution_precision`，从 `rewards.py` import `parse_json_output`
- 支持 `--max_samples` 做小规模测试，`--mc_trials` 控制 Monte Carlo 次数

**Dry-run 结果（5 样本）**:

|  | RE-F1 | Evi-F1 | AP |
|---|---|---|---|
| SFT Baseline | 0.4337 | 0.3652 | 0.9529 |
| Worst-of-8 | 0.4027 | 0.2858 | 0.9333 |
| Best-of-8 | 0.6799 | 0.5858 | 0.9667 |

Score-based E[max]: N=1→0.728, N=2→0.758, N=4→0.779, N=8→0.798

总共 975 个候选样本可用，全量运行用默认参数即可。

---
