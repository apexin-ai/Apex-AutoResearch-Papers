# ops scale 003 status check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scale_003_status_check_20260518T181725_result.json`
- **Structured JSON:** [`3882b4569456d56e762a.json`](../../sessions/38/3882b4569456d56e762a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### qwen25_14b_scale_003 — 正在运行

| 项目 | 状态 |
|------|------|
| PID | 20700 |
| GPU | cuda:0, 32,372 MiB / 97,887 MiB, 92% util |
| tmux | `qwen25_14b_scale_003` (May 18 03:10 创建) |
| 当前阶段 | **Phase 3.3b — 正在生成 d3**（5000 samples with LoRA(d2)，模型权重已加载完成，推理中）|

**已完成阶段：**
- d0→d1 训练: loss=0.3451, 3 epochs, adapter 已存 `lora_depth_0`
- d1→d2 生成 + d2 训练: loss=0.2141, 3 epochs, adapter 已存 `lora_depth_1`, `lora_depth_2`
- d3 生成: 模型加载完毕，正在推理

**results 目录为空的原因：** 启动命令的 `{ ... tee run_003.log; } > ~/runs/....log 2>&1` 结构中，外层 redirect 捕获了 stdout，导致 tee 的文件输出无效。实际日志在 `/root/runs/recursive_gen_depth_est/qwen25_14b_scale_003.log`（186 行）。

### 额外发现：detectgpt_baseline 也在跑

| 项目 | 状态 |
|------|------|
| PID | 78073 (今天 02:10 启动) |
| GPU | cuda:1, 3,652 MiB |
| 阶段 | 加载 perturbation model (t5-large) |

---
