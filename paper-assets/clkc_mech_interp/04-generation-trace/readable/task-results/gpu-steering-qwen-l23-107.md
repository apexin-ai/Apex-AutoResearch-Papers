# gpu steering qwen L23 107

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_steering-qwen-L23-107_20260522T125514_result.json`
- **Structured JSON:** [`0fd22f4e6eb7e27f4426.json`](../../sessions/0f/0fd22f4e6eb7e27f4426.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动，registry 和 cron 均已注册。

**汇总：**
- **PID**: 485320（GPU 子进程 485325）
- **模型**: `/root/models/Qwen3-8B`（base，非 Instruct；Instruct 目录为空）
- **数据**: 798 train + 168 test = 966 样本（test 中 84 conflict / 168 total）
- **Probe accuracy @ L23**: 73.2%
- **GPU 占用**: ~15GB on cuda:0
- **配置**: L23 / last-token / 6 alphas (-20, -10, -5, 5, 10, 20)
- **预估运行时间**: 168 test × 6 alphas + baseline = ~1200 次生成，单卡约 30-60 分钟
- **Cron**: 每 8 分钟轮询日志，完成后自动汇报并更新 registry

---
