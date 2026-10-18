# analyze eval pi05 l2norm k03 goal seed42 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_l2norm_k03_goal_seed42_postfix_20260524T111542_result.json`
- **Structured JSON:** [`88ae1d3003443e38c94d.json`](../../sessions/88/88ae1d3003443e38c94d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正常完成，无错误。

**Overall: libero_goal, L2norm, keep_ratio=0.3, seed=42 → SR = 51.8%**

| Task | Description | SR |
|------|-------------|-----|
| T0 | open the middle drawer of the cabinet | 70.0% |
| T1 | put the bowl on the stove | 18.0% |
| T2 | put the wine bottle on top of the cabinet | 76.0% |
| T3 | open the top drawer and put the bowl in | 26.0% |
| T4 | put the bowl on top of the cabinet | 68.0% |
| T5 | push the plate to the front of the stove | 44.0% |
| T6 | put the cream cheese in the bowl | 20.0% |
| T7 | turn on the stove | 98.0% |
| T8 | put the bowl on the plate | 76.0% |
| T9 | put the wine bottle on the rack | 22.0% |

参考对比：L2norm k=0.85 Goal=87.4% → k=0.3 Goal=51.8%，压缩到 30% token 后成绩下降约 36 个百分点。相比 Object suite k=0.3=30.4%，Goal suite 在极端压缩下表现明显更好。

---
