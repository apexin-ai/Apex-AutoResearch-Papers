# ssh diagnose 5090 pretrained failure

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose_5090_pretrained_failure_20260522T073013_result.json`
- **Structured JSON:** [`ff8171436eacd4a8e4a8.json`](../../sessions/ff/ff8171436eacd4a8e4a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型加载成功，vLLM 正常启动。修复有效。

## 诊断结论

**根因**：ModelScope `snapshot_download` 在 `cache_dir` 下创建了嵌套目录结构 `Qwen/Qwen2___5-7B-Instruct/`，导致 `/root/autodl-tmp/models/Qwen2.5-7B-Instruct/` 顶层目录没有 `config.json`，vLLM 验证失败立即退出。

**修复**：已在顶层目录创建符号链接指向嵌套子目录中的所有模型文件。dry-run 验证通过，模型正常加载（14.25 GiB，4.6s）。

4 张 5090 GPU 全部空闲，可以重新提交 3 个 pretrained 实验。需要我现在重新提交吗？

---
