# prepare eval configs westd

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prepare_eval_configs_westd_20260521T125833_result.json`
- **Structured JSON:** [`fc3e19dfdd31d645302e.json`](../../sessions/fc/fc3e19dfdd31d645302e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个配置文件已创建并验证通过。

### 产出汇总

**配置文件路径：**
- SFT baseline OOD: `/root/autodl-tmp/cost-verify-agent-rl/RAGEN/config/_alfworld_sft_baseline_ood_eval_v2.yaml`
- Seed 6 OOD: `/root/autodl-tmp/cost-verify-agent-rl/RAGEN/config/_alfworld_exp029_seed6_ood_eval.yaml`

**与原 SFT OOD eval 模板的差异：**
- `gpu_memory_utilization`: 0.2 → 0.85（独占卡）
- SFT v2: `CUDA_VISIBLE_DEVICES: "3"`, experiment_name: `sft-baseline-ood-eval-v2`
- Seed 6: `CUDA_VISIBLE_DEVICES: "2"`, experiment_name: `exp029-seed6-ood-eval`, seed 沿用训练配置 (train=789, val=321)

**Seed 6 checkpoint 状态：**
- FSDP checkpoint 已存在：`/root/autodl-tmp/checkpoints/exp029-seed6/global_step_15/actor/`（world_size=2 的分片权重）
- **HF 转换尚未完成**——`huggingface/` 子目录只有 tokenizer 文件，无 `*.safetensors`
- Seed 6 config 的 `model_path` 设为 `/root/autodl-tmp/checkpoints/exp029-seed6/global_step_15_hf`，**运行前需先做 FSDP→HF 转换**

**启动命令模板：**
```bash
# SFT baseline OOD eval (cuda:3)
RAY_ADDRESS=local python3 train.py --config-name _alfworld_sft_baseline_ood_eval_v2

# Seed 6 OOD eval (cuda:2) — 需先完成 FSDP→HF 转换
RAY_ADDRESS=local python3 train.py --config-name _alfworld_exp029_seed6_ood_eval
```

---
