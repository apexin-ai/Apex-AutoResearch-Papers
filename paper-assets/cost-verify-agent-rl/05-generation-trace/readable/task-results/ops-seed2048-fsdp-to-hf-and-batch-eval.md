# ops seed2048 fsdp to hf and batch eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_seed2048_fsdp_to_hf_and_batch_eval_20260522T051704_result.json`
- **Structured JSON:** [`8c03cf361c26ae483b11.json`](../../sessions/8c/8c03cf361c26ae483b11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`VLLM_WORKER_MULTIPROC_METHOD=spawn` 修复生效。vLLM 成功加载模型（3.22 GiB），sft_baseline eval 已在跑 134 episodes OOD。GPU 0 使用中（83GB VRAM, 44% utilization）。

---

## 产出汇总

### 1. Seed 2048 最终 Metrics（collapse seed 确认）

| Step | train/success | resp_len/mean | val-env/success | val-core/reward@32 |
|------|--------------|---------------|-----------------|-------------------|
| 0 (SFT baseline) | — | — | 3.125% | 0.3125 |
| 1 | 4.69% | 15,511 | — | — |
| 5 (final) | 0.78% | 15,790 | **0.0%** | **0.0** |

完全 collapse：response length 近满（~16K），val success/reward 全零。

### 2. FSDP→HF 转换 — 完成

- 输入：`global_step_5/actor/`（FSDP v1, world_size=2）
- 输出：`global_step_5_hf/`（model.safetensors, 4.06GB bf16, Qwen3ForCausalLM 2B）
- Symlink：`/root/autodl-tmp/checkpoints/qwen_seed2048_step5_hf`
- 耗时 16.8s

### 3. Batch OOD Eval — 运行中

- PID=477638，cuda:0，`VLLM_WORKER_MULTIPROC_METHOD=spawn`
- 11 个 checkpoint（10 原有 + seed2048），134 episodes 每个，串行执行
- 首个（sft_baseline）已成功加载模型并初始化 134 games
- 修复了 vLLM v0.18.1 默认 `fork` 导致的 CUDA re-init 错误（根因：`VLLM_WORKER_MULTIPROC_METHOD` 默认 `fork`，RAGEN import 触发 CUDA init 后 fork 子进程无法重新初始化）

### 4. westd GPU 状态

| GPU | 状态 | VRAM |
|-----|------|------|
| cuda:0 | eval 运行中 | 83GB / 96GB |
| cuda:1-3 | 空闲 | 0-3 MiB |

---
