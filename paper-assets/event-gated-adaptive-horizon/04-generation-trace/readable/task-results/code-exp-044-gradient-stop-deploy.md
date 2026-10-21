# code exp 044 gradient stop deploy

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_044_gradient_stop_deploy_20260522T090437_result.json`
- **Structured JSON:** [`08252a9494a9c44d69f2.json`](../../sessions/08/08252a9494a9c44d69f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署验证完成。

## 汇报

### 1. 代码修改
**无需修改** — `reward_dt_emb_detach` 功能已存在于代码中：
- **configs.yaml:129** — `reward_dt_emb_detach: false`（默认关闭）
- **models.py:377-386** — 实现方式是 backward hook：计算 reward loss 对 `dt_embedding.weight` 的梯度，注册 hook 在反向传播时将该分量从总梯度中减去。这比简单 `.detach()` 更精确，因为 dt_emb 通过 GRU 融入 deter state，无法在 feature 层面 detach。

### 2. Dry-run 验证
`--reward_dt_emb_detach True` 参数正常读取，模型初始化和训练均无报错，metrics.jsonl 正常写入。

### 3. 训练提交
- **PID**: 68371
- **tmux session**: `exp_044_gradient_stop_walker`
- **GPU**: cuda:1（CUDA_VISIBLE_DEVICES=1，命令中 --device cuda:0）
- **日志**: `~/runs/event-gated-adaptive-horizon/exp_044_gradient_stop_walker.log`

### 4. 部署验证
- 进程存活（/proc/68371 存在）
- evaluation 完成（eval_return=37.4，10 episodes）
- metrics.jsonl 有 6 行，训练已开始
- 训练 step 正在推进中

### 5. 代码结构说明
`reward_dt_emb_detach` 是 partial-SGS 的一种变体（models.py:340 注释说明）。它和 `full_sgs`（减去所有 head 梯度）及 `sgs_mode='obs_decoder_only'`（减去 obs decoder 梯度）三者互斥（elif chain），只需通过 config flag 选择。

---
