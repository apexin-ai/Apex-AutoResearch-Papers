# ops fp16 status check

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fp16-status-check_20260524T194956_result.json`
- **Structured JSON:** [`b67c4d228bbd6e8a4fcf.json`](../../sessions/b6/b67c4d228bbd6e8a4fcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## FP16 Baseline V3 状态：运行中（模型下载重试）

**结果文件** (`fp16_baseline.json`) 已存在但**不完整**：

| 模型 | 指标 | AWQ | FP16 |
|------|------|-----|------|
| Qwen2.5-14B-Instruct | MMLU | 0.71 | **null** |
| Qwen2.5-14B-Instruct | ARC | 0.84 | **null** |

FP16 评测失败，原因：`"4 file(s) failed to download out of 13."`

**当前状态**：正在重新下载 FP16 模型权重，进度约 18-27%，速度 ~1.3 MB/s，各分片（3.2-3.7GB）预计还需 30-40 分钟。

- 日志创建时间：02:33（已运行约 1h17m）
- 日志最后更新：03:50（仍在活跃写入）

下载速度很慢（AutoDL 从 HuggingFace 下载的典型问题）。如需加速，可考虑切换到 ModelScope 源。

---
