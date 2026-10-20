# diagnose exp 080

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-080_20260519T204134_result.json`
- **Structured JSON:** [`e77f21d07d7e05c5ded9.json`](../../sessions/e7/e77f21d07d7e05c5ded9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：exp-080 **未失败，正在正常运行**

### 状态

| 指标 | 值 |
|------|-----|
| Bash wrapper PID 279841 | **存活** |
| Python PID 279846 | **存活** |
| 进度 | **44/200** (logiqa_043 刚完成，正在处理 logiqa_044) |
| 最后日志时间 | 2026-05-20 04:42:05（刚刚） |
| ETA | ~95 分钟（剩余 156 条） |
| vLLM (port 8000) | **正常**，所有请求返回 HTTP 200 |
| GPU 0 (vLLM for exp-080) | RTX PRO 6000, 89889/97887 MiB, 96% util |

### 误报原因

Cron 监控将其标记为 "process dead 5×" 是**误报**。可能原因：
- 监控检查的是 PID 279841（bash nohup wrapper），该进程状态为 `S`（sleeping），实际 python 子进程 279846 状态为 `Sl`（正常运行）
- 监控可能依赖 sentinel 文件或 W&B 心跳，而该实验不产出这些信号

### 产出

- `results.json`: 100KB, 2714 行（包含已完成的 44 条结果）
- `intermediates/`: 44 个 JSON 文件 (logiqa_000 ~ logiqa_043)
- `train.log`: 109KB，无错误

### 结论

**不需要任何干预。** 实验正在正常推进，预计再 ~95 分钟完成全部 200 条。建议检查 cron 监控逻辑，可能需要改为检查子进程 PID 或增加 `train.log` 活跃性检测。

---
