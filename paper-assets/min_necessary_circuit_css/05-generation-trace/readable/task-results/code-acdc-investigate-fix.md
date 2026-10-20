# code acdc investigate fix

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_acdc-investigate-fix_20260512T154604_result.json`
- **Structured JSON:** [`9b8e5bbffdcf44dc7af7.json`](../../sessions/9b/9b8e5bbffdcf44dc7af7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结果

1. **`tao_exps=[-2]`** — 只有 **1 个 threshold**（τ=0.01），不需要修复
2. **之前的 Worker 报告有误** — 不存在 5 个 threshold 问题
3. **进度倒退原因**：之前 kill 了正在运行的进程，ACDC 没有缓存机制，重启后从头开始
4. **EAP-IG 和 EP 缓存完好**（分别 1.3MB），只有 ACDC 在重跑
5. **当前状态**：49.6%（16119/32491），6.87 it/s，剩余 ~40 分钟
6. **预计完成时间**：约 40 分钟后 ACDC 完成，随后 CSS/Cross-tabulation/Evaluation 阶段耗时较短

不需要任何代码修改，让它继续跑即可。

---
