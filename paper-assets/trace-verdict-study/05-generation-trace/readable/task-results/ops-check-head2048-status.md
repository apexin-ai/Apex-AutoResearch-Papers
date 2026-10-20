# ops check head2048 status

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_head2048_status_20260517T182022_result.json`
- **Structured JSON:** [`da5efa40766f06b38a70.json`](../../sessions/da/da5efa40766f06b38a70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

两个 head-2048 实验**都在正常训练中**，GPU 利用率 100%。

| 实验 | GPU | 当前进度 | 速度 | 预计剩余 |
|------|-----|---------|------|---------|
| DeepSeek head-2048 | cuda:0 (71.6GB/97.9GB) | **57/444** (13%) | ~16.1s/step | ~104 min (~1h44m) |
| Qwen-1.5B head-2048 | cuda:1 (54.7GB/97.9GB) | **32/444** (7%) | ~4.45s/step | ~30 min |

**关键信息**：
- Condition: `full_trace_head`
- 训练集: 4720 samples, 评估集: 1190 samples
- 总步数: 444
- 两个任务都配置了训练完成后自动跑 eval（Qwen 的命令链中显式包含 `evaluate.py`）
- DeepSeek 启动于 02:04，Qwen 启动于 02:18

**预计完成时间**（服务器当前 02:20）：
- Qwen-1.5B: ~02:50 完成训练，之后自动 eval
- DeepSeek: ~04:05 完成训练

无需干预，两个实验运行正常。

---
