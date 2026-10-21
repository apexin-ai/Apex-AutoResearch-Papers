# code gemma27b filtering

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gemma27b_filtering_20260524T093951_result.json`
- **Structured JSON:** [`4b5ec1a00011f55e30a5.json`](../../sessions/4b/4b5ec1a00011f55e30a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已开始（17:51:00）。MMLU + HellaSwag evaluation 通常需要 20-30 分钟。Pipeline 确认正常。

实验概要：
- **9 runs** (3 strategies × 3 seeds) 在 cuda:3 上串行执行
- **Training**: ~3.5 min/run（79 steps × 2.6s）
- **Eval** (MMLU + HellaSwag): ~25-30 min/run
- **总预计时间**: ~4.5-5 小时
- **PID**: 169724

关键发现（from dry run）：
- OBD classifier on Gemma-27B features: acc=0.8984, AUC=0.9184
- Binary filter: 5000→1558 docs（removed 3442）
- Filter precision=0.6970, recall=0.9596（高召回但误杀较多 clean docs）

等第一个 eval 完成后（~18:20 左右）我可以再来检查结果。需要我定期检查进度吗？

---
