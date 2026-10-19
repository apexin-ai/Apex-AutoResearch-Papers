# code 8b cell c v9 prep

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_8b_cell_c_v9_prep_20260519T163041_result.json`
- **Structured JSON:** [`3cdd17c4ab30bdd193ca.json`](../../sessions/3c/3cdd17c4ab30bdd193ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。以下是提交方案：

---

## v9 Config 确认

文件 `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_8b_cell_c_v9.yaml` 存在，关键配置：
- `actor.strategy: fsdp2` + `fsdp_config.offload_policy: True`
- `enable_gradient_checkpointing: true` + `enable_activation_offload: true`
- `n_gpus_per_node: 4`, `CUDA_VISIBLE_DEVICES: "0,1,2,3"`
- 模型: `qwen3_8b_sft_v1/checkpoint-231`, experiment: `8b-cell-c-v9-fsdp2-offload`
- Checkpoint 输出: `/root/autodl-tmp/checkpoints/8b-cell-c-v9/`
- val_before_train=True, val 32 episodes（符合 C003 ≥16 要求）

## FSDP2 代码支持验证

**通过。** 完整链路已确认：
- verl `fsdp_workers.py:513` — actor 初始化时检测 `fsdp_config.offload_policy`，创建 `CPUOffloadPolicy(pin_memory=True)` 传入 `apply_fsdp2()`
- verl `workers/config/engine.py:109` — `offload_policy: bool = False` 字段存在
- verl `workers/engine/fsdp/transformer_impl.py:336-345` — FSDP2 分支中 `offload_policy` → `CPUOffloadPolicy` 转换正确
- RAGEN `ragen/workers/fsdp_workers.py` — `ActorRolloutRefWorker.init_model()` 调用 `super().init_model()`，actor FSDP2 初始化完全走 verl 原生路径
- RAGEN 重写的 `update_actor` 只替换了 `self.actor` 为 `RagenDataParallelPPOActor`，不影响 FSDP2 sharding/offload 逻辑

## 磁盘空间

| 路径 | 总量 | 已用 | 可用 |
|------|------|------|------|
| `/root/autodl-tmp/` | 250G | 138G | **113G** |

模型 checkpoint 31G，加上 optimizer states + 训练 checkpoint 预计 ~50G，113G 可用空间充足。

## 完整启动命令

```bash
#!/bin/bash
# 8B Cell C v9: FSDP2 + CPU Offload
rm -rf /tmp/fast_downward_* /tmp/ray/* /tmp/tmp* 2>/dev/null

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/cost-verify-agent-rl/RAGEN
export WANDB_PROJECT=cost-verify-agent-rl
export CUDA_VISIBLE_DEVICES=0,1,2,3
python train.py --config-name _alfworld_8b_cell_c_v9
```

## 前置条件

- ScienceWorld SFT 当前占用全部 4 GPU，v9 必须等 SFT 完成后启动
- 模型 checkpoint 已就位（31G, 7 个 safetensors 分片）
- Config 中 `save_freq: 999` 表示训练期间基本不存 checkpoint（节省磁盘），只在结束时保存

---
