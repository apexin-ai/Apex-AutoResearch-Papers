# ops westd gpu2 seed42 ood eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_gpu2_seed42_ood_eval_20260522T122752_result.json`
- **Structured JSON:** [`2ba1089ede3d2121099a.json`](../../sessions/2b/2ba1089ede3d2121099a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Seed42 eval 进程存活但 vLLM 引擎初始化较慢（可能是两个 Ray 实例共享 CPU 资源导致）。两个 tmux session 都在运行。我先给出最终报告。

---

## 汇报

### 1. GPU 2: seed42 OOD eval — 启动成功（初始化中）

- FSDP checkpoint 从 bjb1 转换为 HF 格式（在 bjb1 上完成，2B param Qwen3, 15.6s）
- HF 模型 SCP 到 westd: `/root/autodl-tmp/checkpoints/exp029_seed42_step5_hf/` (4.06 GB model.safetensors)
- Config: `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_seed42_step5_ood_eval.yaml`
  - `system.CUDA_VISIBLE_DEVICES: "2"`, `seed.val: 321`, `val_only: True`, 134 OOD tasks
- tmux session: `ragen_eval_gpu2`，进程存活
- GPU 2 已分配 8149 MiB（模型加载完成），vLLM KV cache 尚未分配（可能因两个 Ray 实例共享 CPU 资源导致初始化较慢）
- 日志: `/root/autodl-tmp/logs/ragen_seed42_ood_eval.log`

### 2. GPU 3: seed2 step15 OOD eval — 运行中

- Seed2 step15 checkpoint **已在 westd**（`/root/autodl-tmp/cost-verify-agent-rl/backups/exp029-seed2-bjb1/exp029-seed2/global_step_15/actor/`）
- FSDP→HF 转换完成: `/root/autodl-tmp/checkpoints/exp029_seed2_step15_hf/` (4.06 GB)
- Config: `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_seed2_step15_ood_eval.yaml`
  - `system.CUDA_VISIBLE_DEVICES: "3"`, `seed.val: 321`, `val_only: True`, 134 OOD tasks
- tmux session: `ragen_eval_gpu3`
- GPU 3: **90467 MiB** — vLLM 全速推理中
- 日志: `/root/autodl-tmp/logs/ragen_seed2_ood_eval.log`

### 3. Task C: seed4/seed6 pipeline 确认

**seed4** (来源: `/root/runs/cost-verify-agent-rl/exp029_seed4_ood_eval_v2.log`):
- ✅ **RAGEN pipeline** (train.py + Hydra config `_alfworld_exp029_seed4_ood_eval`)
- ✅ **seed.val = 321**
- ✅ enable_response_mask = False
- ✅ 134 AlfworldSG_OOD tasks, group_size=1
- model_path: `qwen_exp029_seed4_step15_hf`

**seed6** (来源: `/root/runs/cost-verify-agent-rl/exp029_seed6_step15_ood.log`):
- ✅ **RAGEN pipeline** (train.py + Hydra config `_alfworld_exp029_seed6_ood_eval`)
- ✅ **seed.val = 321**
- ✅ enable_response_mask = False
- ✅ 134 AlfworldSG_OOD tasks, group_size=1
- model_path: `qwen_exp029_seed6_step15_hf`
- ⚠️ 该次 run 以 EXIT_CODE=1 结束（Ray worker registration failed，跑了约 7 小时后崩溃）

**注**: `table1_ood/` 下的日志是另一套 standalone eval 脚本（非 RAGEN train.py），使用了不同的 checkpoint 路径（`exp029-seed{4,6}/global_step_15_hf`）。

---
