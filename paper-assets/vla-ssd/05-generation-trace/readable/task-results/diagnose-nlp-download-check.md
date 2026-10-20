# diagnose nlp download check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_nlp_download_check_20260522T095455_result.json`
- **Structured JSON:** [`bdff74feb699898701d8.json`](../../sessions/bd/bdff74feb699898701d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

**下载路径**: `/root/autodl-tmp/models/Llama-2-7b-chat-hf/`

**文件状态**:

| 文件 | 大小 | 状态 |
|------|------|------|
| `model-00002-of-00002.safetensors` | 3.50 GB / 3.50 GB | 已完成 |
| `model-00001-of-00002.safetensors` | 5.99 GB / 9.29 GB (64%) | 下载中（在 `._____temp/` 内） |
| config/tokenizer 等元数据 | — | 已完成 |

**下载进程**: PID 612753，已运行 4h23m，当前速度 ~350 KB/s，预计剩余 **~2h50m**。

**wait_and_run**: PID 613207 在等下载完成，日志仍显示 "Waiting for model download to complete..."。

**其他缓存副本**: `hf_cache/modelscope/shakechen/` 和 `.modelscope_cache/shakechen/` 只有元数据，无权重文件（看起来是之前失败/不完整的尝试）。

**结论**: 下载正常进行中，速度偏慢（AutoDL 代理限速），预计还需约 3 小时完成。

---
