# diagnose eval openvla l2norm k095 object seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_openvla_l2norm_k095_object_seed42_20260526T131516_result.json`
- **Structured JSON:** [`a071165c66bb04775b36.json`](../../sessions/a0/a071165c66bb04775b36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成。**Overall SR = 70.60% (353/500)**，结果已保存。

各 task 明细：

| Task | 描述 | SR |
|------|------|----|
| 1 | pick up the alphabet soup and place it in the basket | 48.0% (24/50) |
| 2 | pick up the cream cheese and place it in the basket | 52.0% (26/50) |
| 3 | pick up the salad dressing and place it in the basket | 82.0% (41/50) |
| 4 | pick up the bbq sauce and place it in the basket | 60.0% (30/50) |
| 5 | pick up the ketchup and place it in the basket | 88.0% (44/50) |
| 6 | pick up the tomato sauce and place it in the basket | 66.0% (33/50) |
| 7 | pick up the butter and place it in the basket | 54.0% (27/50) |
| 8 | pick up the milk and place it in the basket | 84.0% (42/50) |
| 9 | pick up the chocolate pudding and place it in the basket | 86.0% (43/50) |
| 10 | pick up the orange juice and place it in the basket | 86.0% (43/50) |

结论：实验正常完成，进程已退出（cron 报 process gone 是因为跑完了）。结果文件在 `/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_l2norm_prune_k095_object_seed42.json`。无需重跑。

---
