# check exp 028 status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_028_status_20260517T193938_result.json`
- **Structured JSON:** [`4c2c321e38058d2d035f.json`](../../sessions/4c/4c2c321e38058d2d035f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**总结**：

- **训练正常运行中**，96.3% 完成 (39654/41180)，预计 ~15 分钟后（~03:55 UTC）完成
- **无报错无中断**，4 GPU 全部健康，loss=0.0045 正常收敛
- **超时原因**：实际均速 1.55 it/s（含 checkpoint saving 减速），总耗时 ~7h24m，超出原始估算
- 训练完成后需手动触发后处理：`bash scripts/exp_028_postprocess/run_all.sh`

状态报告已写入 `artifacts/exp_028_status_check.md`。需要我 15 分钟后再次检查并触发后处理吗？

---
