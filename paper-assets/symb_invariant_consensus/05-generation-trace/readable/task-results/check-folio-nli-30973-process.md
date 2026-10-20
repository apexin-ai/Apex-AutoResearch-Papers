# check folio nli 30973 process

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_folio-nli-30973-process_20260523T165243_result.json`
- **Structured JSON:** [`1f6177c962bdb89f7781.json`](../../sessions/1f/1f6177c962bdb89f7781.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### FOLIO NLI combo 实验：正在运行，但卡在模型加载阶段

3 个 NLI combo 进程都在运行，**全部跑在 CPU 上**（`--device cpu`），且日志显示只完成了模型权重加载，尚未开始推理：

| Verifier | PID | 状态 | 日志进度 |
|----------|-----|------|----------|
| DeBERTa-large-mnli | 35767 | 运行中（CPU 2174%） | 加载完权重，无推理输出 |
| BART-large-mnli | 35904 | 运行中（CPU 2190%） | 加载完权重，无推理输出 |
| RoBERTa-large-mnli | 36041 | 运行中（CPU 2195%） | 加载完权重，无推理输出 |

输出目录 `/root/autodl-tmp/results/` 为空，尚无结果文件。

这 3 个进程各占 ~2.5GB 内存，CPU 使用率极高（2100%+），说明它们在 CPU 上做密集计算——可能在逐条推理但速度极慢，日志没有进度打印。

### GPU 使用情况

| GPU | 显存占用 | 利用率 | 用途 |
|-----|---------|--------|------|
| GPU 0 | 3 MiB | 0% | 空闲 |
| GPU 1 | 3 MiB | 0% | 空闲 |
| GPU 2 | 88275/97887 MiB | 33% | vLLM Llama-3.1-8B (port 8002) |

### 其他实验

- ProofWriter multi-seed 实验（seed 456）正在跑，进度 **471/600**，ETA ~178 分钟
- ProofWriter seed 789 的 tmux session 存在但对应 python 进程未显示在 ps 中（可能已结束或尚未启动）

### 关键问题

NLI combo 3 个进程都用 `--device cpu`，GPU 0 和 GPU 1 完全空闲。如果这是有意为之可以忽略，否则改用 GPU 能大幅加速。

---
