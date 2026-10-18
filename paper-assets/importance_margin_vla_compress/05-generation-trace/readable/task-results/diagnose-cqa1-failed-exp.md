# diagnose cqa1 failed exp

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1_failed_exp_20260527T134725_result.json`
- **Structured JSON:** [`265f0c609283f9b23ec4.json`](../../sessions/26/265f0c609283f9b23ec4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

发现了 — 进程 PID 330514 和 tee PID 330515 都还在运行。CUDA_VISIBLE_DEVICES=1，对应 GPU 1（99% 利用率，21GB 占用）。实验没有失败，仍在正常运行。

## 诊断摘要

**实验状态：正常运行中，未失败。**

- **进程**：PID 330514 仍在运行（State: R），tee PID 330515 在等待管道输入（State: S）。进程链完整。
- **GPU**：CUDA_VISIBLE_DEVICES=1 → 物理 GPU 1，当前 21141 MiB / 24564 MiB，利用率 99%，活跃计算中。
- **日志**：最后一条记录于 21:46:37，完成 Task 0（50 episodes, SR=10.0%）。之后没有新输出是因为 Task 1 还在跑前 10 个 episodes（脚本每 10 episodes 才打印一次）。Task 0 耗时 35.7 分钟，预计 Task 1 下一条日志约在 ~21:53 出现。
- **磁盘**：136G/250G（55%），空间充足。
- **日志无任何错误**：无 OOM、Traceback、segfault、killed。
- **Cron 误报原因**：Cron 检查时实验尚未完成全部 10 个 Task，没有找到最终 success marker，误判为失败。

**结论：无需重启。实验正在正常执行中，预计总时长 ~6 小时（10 tasks × ~35 min/task）。**

---
