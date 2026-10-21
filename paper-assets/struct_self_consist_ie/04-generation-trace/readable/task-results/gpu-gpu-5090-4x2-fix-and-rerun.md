# gpu gpu 5090 4x2 fix and rerun

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_gpu_5090_4x2_fix_and_rerun_20260514T124302_result.json`
- **Structured JSON:** [`d3746d8bd13aefa8b265.json`](../../sessions/d3/d3746d8bd13aefa8b265.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0/1 被其他 llamafactory 训练任务占用（非本项目），这就是 exp_001 两个实验初始化失败的原因：

| GPU | PID | 进程 | 显存 |
|-----|-----|------|------|
| 0 | 60975 | llamafactory-cli train train_config_llama.yaml | 29.7 GB |
| 1 | 55644 | llamafactory-cli train wnut17_lora.yaml | 25.5 GB |
| 2 | 62900 | exp_008_re_n16 (本项目) | 30.1 GB |
| 3 | — | 空闲 | — |

exp_008 在 GPU 2 正常运行。

**两个选择：**
1. 杀掉 GPU 0/1 上的 llamafactory 进程，释放显存后重跑 exp_001 两个 seed
2. 先在 GPU 3 跑一个 exp_001，等 GPU 0/1 的 llamafactory 跑完再跑另一个

是否可以 kill 掉这两个 llamafactory 进程？

---
