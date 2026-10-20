# code ctrl contam pilot submit

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ctrl-contam-pilot-submit_20260520T152532_result.json`
- **Structured JSON:** [`8b7a63e6024043b48721.json`](../../sessions/8b/8b7a63e6024043b48721.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型下载约 57%，预计还需 ~25-30 分钟。已完成的准备工作：
- 杀掉了低效的 HF 并行下载（释放带宽给 ModelScope）
- 修复了 train.py 中缺失的 ModelScope 模型路径模式 `Qwen/Qwen2___5-7B-Instruct`
- 验证了 4 个 condition 的训练数据完整

等待下载完成后继续 dry-run 和训练提交。

---
