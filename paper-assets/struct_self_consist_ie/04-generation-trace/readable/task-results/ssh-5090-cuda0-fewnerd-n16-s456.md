# ssh 5090 cuda0 fewnerd n16 s456

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5090_cuda0_fewnerd_n16_s456_20260521T151948_result.json`
- **Structured JSON:** [`0fc85d65a64bc196cde5.json`](../../sessions/0f/0fc85d65a64bc196cde5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已启动并注册监控。

**实验状态：**
- **PID**: 54271（主进程），54567（vLLM EngineCore）
- **GPU 0**: 29832 MiB 占用，模型加载完成
- **进度**: 正在渲染 37648 条 prompts，随后开始 vLLM 批量推理
- **参数**: `seed=456, n_samples=16, temperature=1.0, collect_logprobs, dataset=fewnerd`
- **模型路径**: `checkpoints/qwen3-8b-fewnerd-exp021-merged/qwen3-8b-fewnerd-exp021-merged`（注意嵌套目录，外层缺 tokenizer 文件）
- **日志**: `output/fewnerd_n16_s456.log`
- **Cron**: `exp_fewnerd_n16_s456_v2`，300s 轮询

预计运行 4-6h。

---
