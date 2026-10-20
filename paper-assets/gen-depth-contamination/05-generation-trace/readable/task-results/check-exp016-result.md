# check exp016 result

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp016_result_20260516T032029_result.json`
- **Structured JSON:** [`c20456a1a8f05899410c.json`](../../sessions/c2/c20456a1a8f05899410c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在（可能已被删除或从未创建），无需处理。

---

## exp-016 检查报告

**状态：失败**

**失败阶段：** 数据生成 — depth 4，51% (160/313 batches)

**失败原因：** 进程被杀，日志中无 traceback/exception。日志在 2026-05-16 11:07:46 CST 停止更新。系统 load average 15+，疑似 OOM。无 depth_4 残留文件（写入未 flush 到磁盘）。

**已完成部分：**
- depth 0-3 各 5000 条（共 20,000 条）
- 数据文件完整，可复用

**缺失部分：**
- depth 4、depth 5 数据生成
- feature extraction
- classification（K* 和 pairwise AUC）
- 结果目录为空

**与 exp-017 (Instruct, K\*=2) 的对比：** 无法进行，exp-016 未产出 K* 和 AUC 结果。

**重跑建议：** depth 0-3 数据已完好，重跑时可从 depth 4 断点续跑（如果脚本支持），或确保服务器负载较低时重新执行全流程。当前服务器 load average 15+，建议等负载降低后再提交。

---
