# infra 8b readiness check

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_8b_readiness_check_20260520T103245_result.json`
- **Structured JSON:** [`248fd771b967e58d4f31.json`](../../sessions/24/248fd771b967e58d4f31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报结果：

**Qwen3-8B — 未完成，仍在下载中**
- 当前大小：4.8G，缺少所有 `.safetensors` 模型权重文件（0个）
- 已有：config.json、tokenizer_config.json、tokenizer.json 等元数据文件
- 下载进程 PID 12091 仍在运行（已跑 33 分钟）

**Qwen3-32B — 未完成，仍在下载中**
- 当前大小：9.7G
- 下载进程 PID 12163 仍在运行（已跑 33 分钟）

**vLLM — 已就绪**
- vLLM=0.21.0，安装正常

**磁盘**
- /root/autodl-tmp: 250G 总量，已用 17G，剩余 234G（7%），空间充足

8B 模型完整大小约 16G（8个 safetensors 文件），当前只下了元数据，权重文件还没开始写入或正在下载中。需要继续等待。

---
