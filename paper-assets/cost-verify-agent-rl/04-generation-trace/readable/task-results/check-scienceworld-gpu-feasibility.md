# check scienceworld gpu feasibility

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_scienceworld_gpu_feasibility_20260524T042942_result.json`
- **Structured JSON:** [`b24dbcfacb0d79491011.json`](../../sessions/b2/b24dbcfacb0d79491011.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 脚本已写入。现在汇总全部结果。

---

## 产出汇总

### 1. 可行性判断：**可行，无需降级**

### 2. 显存估算

当前 bjb1 实际观测（hsweep_h10_seed2，单卡 Qwen3-1.7B step-independent GRPO）：

| 组件 | 占用 |
|------|------|
| 观测总占用 | **44.4 GB** / 95.6 GB |
| 剩余 | **51.2 GB** |

显存分解（Qwen3-1.7B bf16, 单卡）：

| 组件 | GPU | 说明 |
|------|-----|------|
| Actor model | ~3.4 GB | bf16, FSDP shard=1（单卡无分片） |
| Ref model | ~3.4 GB | 同上 |
| Gradients | ~3.4 GB | bf16 |
| vLLM KV cache | ~33.5 GB | gpu_memory_utilization=0.35 × 95.6 GB |
| Optimizer (AdamW) | **0 GB** | optimizer_offload=True，在 CPU 上 |
| Activations | ~1-3 GB | gradient_checkpointing=True |
| **合计** | **~44-47 GB** | 与观测 44.4 GB 吻合 |

**ScienceWorld episode-level vs 当前 step-independent 的差异**：
- 序列更长（max_actions_per_traj=100 vs 50），但 `ppo_max_token_len_per_gpu=65536` 封顶了每 GPU 的 token 总量，activation 峰值不会显著变化
- vLLM max_model_len=20480 不变 → KV cache 分配一致
- **结论**：~51 GB 剩余空间足够应对 episode-level 的额外 activation 开销

### 3. Cell D Config

`_scienceworld_cell_d_grpo.yaml` **尚未创建**。launch script `run_scienceworld_cell_d.sh` 已存在，设置为单卡 (`CUDA_VISIBLE_DEVICES=0`)。主要参数建议基于 Cell C v6 修改：
- `n_gpus_per_node: 1`
- `CUDA_VISIBLE_DEVICES: "0"`
- 其余参数（optimizer_offload、gradient_checkpointing、gpu_memory_utilization=0.35、ppo_max_token_len_per_gpu=65536）维持不变即可

### 4. 前置依赖

SFT v2 checkpoint (`/root/autodl-tmp/checkpoints/scienceworld_sft_v2/final/`) **在 bjb1 上不存在**。需先完成 SFT v2 训练或从其他服务器同步。

### 5. Dry-run 脚本

已写入 `/root/cost-verify-agent-rl/scripts/dryrun_scienceworld_cell_d.sh`。会优先用 SFT v2 checkpoint，fallback 到 ALFWorld SFT（同模型架构/大小）做显存估算。

---

### 6. 第二张 GPU 原因

**结论：云平台侧 GPU 分配变更，非硬件故障。**

证据：
- `/dev/nvidia1` 存在，`/dev/nvidia0` **不存在**
- 当前可见 GPU（Bus `38:00.0`）的 Device Minor = 1，说明它是物理机上编号为 1 的卡
- `/proc/driver/nvidia/gpus/` 泄露了宿主机的 9 张 GPU 目录（物理机共 9 张卡）
- `0000:16:00.0` (Device Minor 0) 在 driver 层可见但无设备节点
- `CUDA_VISIBLE_DEVICES` 未设置，`/etc/environment` 无 CUDA 相关配置

**判断**：SeetaCloud 共享服务器的容器级 GPU 分配从 2 张减为 1 张。原来分配的 `/dev/nvidia0`（Bus 16:00.0）被平台回收了。需要联系 SeetaCloud 确认 GPU 配额是否发生变更，或重新申请第二张卡。

---
