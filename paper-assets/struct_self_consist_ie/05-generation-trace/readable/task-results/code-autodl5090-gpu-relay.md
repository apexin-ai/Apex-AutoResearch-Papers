# code autodl5090 gpu relay

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_autodl5090_gpu_relay_20260518T203354_result.json`
- **Structured JSON:** [`9121e18bd79541a14ed3.json`](../../sessions/91/9121e18bd79541a14ed3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 GPU 满载：

| GPU | 任务 | 状态 |
|-----|------|------|
| cuda:0 | FewNERD s789 shard0 (0-12549) | 启动中 |
| cuda:1 | LLaMA FewNERD 训练 | 运行中（不碰）|
| cuda:2 | FewNERD s789 shard1 (12549-25098) | 启动中 |
| cuda:3 | FewNERD s789 shard2 (25098-37648) | 启动中 |

## 汇报

**已完成的 SciERC 温度消融 (全部 12 个实验)：**

| T | seed 42 | seed 123 | seed 456 | 平均 headroom |
|---|---------|----------|----------|--------------|
| 0.5 | 0.078 | 0.083 | 0.080 | 0.080 |
| 0.8 | 0.105 | 0.111 | 0.105 | 0.107 |
| 1.0 | 0.118 | 0.114 | 0.113 | 0.115 |
| 1.2 | 0.130 | 0.130 | 0.118 | 0.126 |

关键发现：greedy F1 跨温度稳定（~0.662），oracle headroom 随温度单调递增（0.08→0.13），证实温度提高增加样本多样性。

**当前运行中的任务：**
- cuda:0/2/3：Qwen FewNERD seed=789 分 3 片并行推理（~12.5K/shard），预计 ~1.5h 完成
- cuda:1：LLaMA FewNERD 训练（继续运行）

**接力时间线：**
1. 04:31 → 原 3 任务启动（T=0.5 s123, T=0.8 s123, T=0.5 s456）
2. 04:35 → 完成，接力启动 T=0.8 s456, T=1.2 s456, T=1.0 s42
3. 04:42 → 完成，接力启动 T=1.0 s123, T=1.0 s456
4. 04:47 → 温度消融全部完成，接力启动 FewNERD 3-shard 并行推理

---
