# code cheetah tcn and ablation configs

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cheetah_tcn_and_ablation_configs_20260520T082823_result.json`
- **Structured JSON:** [`0465cb4a6265973a12da.json`](../../sessions/04/0465cb4a6265973a12da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已创建。

总结：

- **兼容性**：TCN 完全环境无关，仅操作 `dt_embedding` 的高斯噪声注入（`networks.py:256-258`），Cheetah 只需换 `--task dmc_cheetah_run`
- **6 个实验命令**已生成：Walker 多 seed (029a/b)、Cheetah 跨环境 (030a/b)、剂量响应 σ=0.1 (029c)、dt=1 对照 (029d)
- 所有命令标准化了 `--gate_subsample_max_dt 2`（之前 σ=0.2 实验漏了此参数）
- GPU 需求：dmc_proprio 纯 MLP，~5GB 显存，单卡可并行 2 个实验
- 输出路径：`artifacts/code/ablation_commands.md`

---
