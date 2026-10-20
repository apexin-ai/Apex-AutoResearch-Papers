# ssh rtx6000 gemini sonnet recovery

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rtx6000-gemini-sonnet-recovery_20260524T151858_result.json`
- **Structured JSON:** [`9c3736cbb65ecaab04bb.json`](../../sessions/9c/9c3736cbb65ecaab04bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Gemini 和 Sonnet 的采集进程已停止（没有匹配的进程）。Gemini 最后修改时间 23:05，已无新写入。

汇报如下：

---

## 结果

### rtx6000-4x 恢复：**不可行**
- `rtx6000-4x` 不在可用服务器列表中（仅有 `autodl-8gpu` 和 `westd-25068`）
- `westd-25068` 连接失败（端口 25068 不通，IP 36.103.198.204）
- **无法从其他服务器恢复 Gemini/Sonnet 采集**

### Gemini & Sonnet 采集状态
- **Gemini 2.5 Pro**: 11,253 行，进程已停止，最后修改 23:05:25
- **Claude Sonnet 4.6**: 14,255 行，进程已停止，最后修改 23:05:25
- 两者均因 OpenRouter 403 停采，无可用非中国 IP 服务器恢复

### DeepSeek & Qwen3 采集状态（autodl-8gpu）
- **DeepSeek V4 Pro** (PID 592328): 运行中，已运行 19h43m，当前 10,007 行，文件持续增长（23:19 仍在写入）
- **Qwen3 235B** (PID 592432): 运行中，已运行 18h20m，当前 12,134 行，文件持续增长（23:19 仍在写入）

### 本地 judge 进度
- LLaMA 3.3 70B: 15,668 行
- Mistral Large 2: 118 行（极少，可能也有问题）
- Qwen2.5 72B: 10,793 行

### 需要关注
1. Mistral Large 2 只有 118 行，可能采集异常
2. Gemini/Sonnet 需要非中国 IP 才能恢复，当前无可用服务器

---
