# ops check recovery datagen

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-recovery-datagen_20260515T183458_result.json`
- **Structured JSON:** [`30f8531399fe888ff83b.json`](../../sessions/30/30f8531399fe888ff83b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

**进程**: PID 158010 **仍在运行**，已运行 4h29m

**进度**: 300/760 (39.5%)
- 日志最后更新：01:47（约 48 分钟前），打印 "Processed 300/760"
- 进度每 100 条打印一次，当前正在处理 301-400 区间
- 进程活跃：有 socket 打开（API 调用中）

**速度估算**:
- 0~300 条耗时 ~3h42m → ~0.74 min/条
- 剩余 460 条 → 预计还需 ~5.7h
- **预计完成时间：~07:30（北京时间，5月16日）**

**输出**:
- 输出路径：`data/recovery_paired/recovery_paired.jsonl`（脚本在全部处理完后一次性写入，目前尚未生成）
- 使用模型：`openai/gpt-5.2`，通过 `http://47.94.22.126/v1` 代理
- 输入数据：760 条 injected variants × 501 条 source trajectories

**注意**: 脚本把所有结果攒在内存里最后才写文件，中途无增量输出。如果进程中断，已处理的 300 条结果会丢失。

---
