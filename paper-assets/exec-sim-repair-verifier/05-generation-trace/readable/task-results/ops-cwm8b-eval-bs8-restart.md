# ops cwm8b eval bs8 restart

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cwm8b-eval-bs8-restart_20260515T143738_result.json`
- **Structured JSON:** [`146e39557906ebec5a05.json`](../../sessions/14/146e39557906ebec5a05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认运行正常，bs=8 生效（每步 +8）。

**结果汇总：**

| 项目 | 值 |
|------|-----|
| 新 PID | 381618（实际 python3 进程） |
| 实际 batch_size | **8**（日志每步 +8：352→360→368） |
| 显存占用 | **20982 MiB** / 32607 MiB（cuda:3） |
| Auto-resume 起点 | 从第 **359** 条继续（resumed=359） |
| 剩余样本 | 9784 - 359 = **9425 条** |

**ETA 估算：**
- bs=8 每批约 57 秒（22:38:48 跳过完成 → 22:39:45 第一批，22:39:45 → 22:40:41 第二批）
- 剩余 9425 / 8 ≈ 1179 批 × 57s ≈ **18.7 小时**
- 预计完成时间：约 **5月16日 17:20**

---
