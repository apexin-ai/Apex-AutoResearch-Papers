# eval 1 7b sft baseline ood

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_1_7b_sft_baseline_ood_20260521T105002_result.json`
- **Structured JSON:** [`6d31ac6aa514be9792c2.json`](../../sessions/6d/6d31ac6aa514be9792c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

配置文件已就绪（99 行）。汇总：

## 产出

### 1. SFT Checkpoint 确认
- **路径**: `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4/`（两台服务器都有）
- **model.safetensors**: 3.4GB
- 包含完整的 tokenizer、config、generation_config

### 2. Eval 配置
- **文件**: `westd:/root/cost-verify-agent-rl/RAGEN/config/_alfworld_sft_baseline_ood_eval.yaml`
- 基于 `_alfworld_7b_sft_eval_ood.yaml` 模板适配 1.7B
- `val_only: True`, `resume_mode: "disable"`, 直接从 model_path 加载
- 134 OOD tasks (AlfworldSG_OOD), τ=0.4, do_sample=True
- 2 GPU, CUDA_VISIBLE_DEVICES: "0,1"

### 3. GPU 可用性
| 服务器 | GPU | 占用 | 任务 | 进度 | 预计剩余 |
|--------|-----|------|------|------|----------|
| bjb1 | 0,1 | 46/98 GB | Seed 4 | 4/15 (27%) | ~5h |
| westd | 0,1 | 64/98 GB | Seed 5 | 8/15 (53%) | **~2h** |
| westd | 2,3 | 97/98 GB | Seed 6 | 5/15 (33%) | ~4h |

### 4. 执行策略
**等 Seed 5 完成**（westd cuda:0,1，预计 ~2 小时后释放）。届时用 `submit_training_job` 提交：
```
config: _alfworld_sft_baseline_ood_eval
server: westd-47453
gpu_ids: 0,1
exp_id: sft_baseline_ood_eval
```

Eval 预计耗时 ~20-30 分钟（1.7B 模型 + 134 tasks，纯 inference）。

---
