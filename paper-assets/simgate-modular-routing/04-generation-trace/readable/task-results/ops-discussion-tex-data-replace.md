# ops discussion tex data replace

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_discussion-tex-data-replace_20260515T160147_result.json`
- **Structured JSON:** [`db7a79ec1e60acb87372.json`](../../sessions/db/db7a79ec1e60acb87372.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有副本已包含 N=300 正式数据，无需替换。

**验证结果：**

| 副本 | 位置 | N=300 数据 | pilot-50 残留 |
|------|------|-----------|--------------|
| 服务器 `docs/paper/` | ✅ 81.0%, 76.7%, 84.3%, McNemar p=0.079, 17/30/253 | 无 |
| 服务器 `paper/` | ✅ 同上 | 无 |
| 服务器 `paper/latex_build/` | ✅ 同上 | 无 |
| 本地 `artifacts/_project/paper/latex/` | ✅ 同上（短版，与服务器一致） | 无 |
| 本地 `docs/paper/` | ✅ 同上（扩展版，含 figure/table/更多段落） | 无 |

注意：本地 `docs/paper/discussion.tex` 是扩展版本（44 行，含 `signal_reversal` 图、`cross-env` 表、Implications/Label imbalance/Penalty sensitivity 等段落），与服务器上的精简版（8 行，两段）内容不同，但两者的 N=300 数据均已正确。

---
