# launch mf3 eval n500 westb1

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_mf3_eval_n500_westb1_20260522T120617_result.json`
- **Structured JSON:** [`fa0745ddb891a50bf3bf.json`](../../sessions/fa/fa0745ddb891a50bf3bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程跑了 1.5 分钟，CPU 779%（多核加载权重），GPU 还没分配显存——模型正在从磁盘加载到 CPU 内存。这个阶段正常，等模型 `.to(device)` 后 GPU 显存才会涨。

当前状态汇总：

| 项目 | 结果 |
|------|------|
| **旧进程 Kill** | PID 179898 已终止 |
| **新进程** | Bash wrapper PID 202359，实际 Python PID **202364** |
| **GPU 1** | 模型加载中（CPU 阶段），权重即将转移到 GPU |
| **日志** | 模型路径正确，检测到 Non-uniform MLP（剪枝后模型特征） |
| **nvidia-smi** | GPU 0: 空闲 0MiB / GPU 1: 3MiB（即将涨到 ~16GB） |

N=500 eval 已启动，预计模型加载完成后开始推理（约 500×78s ÷ 加速 ≈ 数小时内完成）。可通过以下命令后续跟踪：
```
tail -f results/eval_gsm8k_grpo_qwen_math_cka_only_20_n500.log
```

---
