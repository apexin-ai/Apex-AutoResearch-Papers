# analysis diagnose tail512 crash

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_diagnose_tail512_crash_20260519T141336_result.json`
- **Structured JSON:** [`d721246af7336c85e8a3.json`](../../sessions/d7/d721246af7336c85e8a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告：`qwen7b_full_trace_tail512_seed42`

### 进程状态
**无运行进程** — 训练和评估均已结束，进程正常退出。

### Checkpoint 状态
**完整** — 3 个中间 checkpoint + final：

| Checkpoint | 时间 |
|---|---|
| checkpoint-148 | May 19 21:15 |
| checkpoint-296 | May 19 21:33 |
| checkpoint-444 | May 19 21:51 |
| **final/** | May 19 21:52 |

`final/` 包含 adapter 权重 (`adapter_model.safetensors`, 154MB)、tokenizer、training_args。

### Eval 状态
**已完成** — `final/eval_results.json` 和 `final/predictions.jsonl` (1190 条) 均存在。

| 指标 | 值 |
|---|---|
| **Accuracy** | 93.61% (CI: 92.18–94.96%) |
| Majority baseline | 71.51% |
| **Lift** | +22.10pp |
| Pass F1 | 0.954 |
| Fail F1 | 0.894 |

### 问题原因
**实验已正常完成，cron 误报。** 原因：
1. 无 `.sentinel` 文件 — 训练脚本未写 sentinel，cron 依赖 sentinel 判断完成状态，因此报 miss
2. 无 W&B 目录 — 此次实验未配置 W&B 上报
3. `logs/` 下无此实验日志 — 可能未用 tee 重定向（logs 里最新的是 May 18 的其他实验）

### 建议下一步
1. **无需重跑** — 训练和 eval 均正常完成，结果质量良好（93.6% accuracy, +22pp lift）
2. **补写 sentinel**（如果 cron 需要）— 手动创建 sentinel 文件让监控系统识别完成状态
3. **注册结果** — 将 eval_results.json 纳入实验汇总

---
