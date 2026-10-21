# ops restart phi4 olmo2 downloads

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart-phi4-olmo2-downloads_20260518T181048_result.json`
- **Structured JSON:** [`c847d31a6ae999083473.json`](../../sessions/c8/c847d31a6ae999083473.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个下载进程都在运行，日志尚未有输出（刚开始连接）。

汇总：
- **Phi-4** 下载已重启，PID **49771**（实际 Python 进程），缺 `model-00005-of-00006.safetensors`
- **OLMo-2** 下载已重启，PID **49929**（实际 Python 进程），缺 `model-00003-of-00006.safetensors`
- 原 `huggingface-cli` 已废弃，改用新版 `hf` CLI 启动
- 两个模型都是公开仓库，无需 HF token
- `hf download` 默认会跳过已有文件，只下载缺失部分

---
