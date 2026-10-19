# ops status check

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status-check_20260516T011018_result.json`
- **Structured JSON:** [`9d46d2999b7d1a56c64e.json`](../../sessions/9d/9d46d2999b7d1a56c64e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进程状态汇总

| 实验 | PID | 状态 | GPU | 运行时长 | 关键进度 |
|------|-----|------|-----|---------|---------|
| phase1_lora_visual | 216556 | **DEAD** | cuda:0 (空闲) | — | 启动即崩溃：`wandb.errors.UsageError: No API key configured` |
| phase1_spatial_demo_collection | 246213 | **DEAD** | cuda:1 (空闲) | 89.9 min | 已完成，**0/624 成功 (0.0%)** |
| phase1_physical_demo_collection | 228345 | **DEAD** | cuda:2 (空闲) | 55.9 min | 已完成，**0/490 成功 (0.0%)** |
| phase1_lora_universal_r16 | 216633 | **DEAD** | cuda:3 (空闲) | — | 启动即崩溃：`unrecognized arguments: --run_name` |
| sensor_noise per-step | 182966 | **DEAD** | — | — | 无日志文件 |

所有 tmux sessions 已不存在。4 张 GPU 全部空闲（0 MiB / 0%）。

## 产出检查

- **Spatial demos**: 目录存在 (`data/expert_demos/spatial/`) 但**空**，仅有 `_tmp_bddl` 临时目录，0 条成功 demo
- **Physical demos**: 目录存在 (`data/expert_demos/physical/`) 但**完全为空**，0 条成功 demo
- **Checkpoints**:
  - `phase1/visual/epoch_0/` — adapter_model.safetensors + optimizer.pt + metadata（val_loss=6.237, step=5, r=16, alpha=32）
  - `phase1/visual/best/` — adapter_model.safetensors + adapter_config.json（这是之前运行的产出，非本次）
  - `phase1/par_router/best_router.pt` — 存在（之前运行产出）
- **无 .jsonl 文件**产出

## 异常

1. **phase1_lora_visual** — 服务器未配置 wandb API key，脚本未用 `--no_wandb` 启动，导致 `wandb.init()` 直接报错退出
2. **phase1_lora_universal_r16** — 传了不存在的参数 `--run_name universal_r16_visual_bootstrap`，`train_lora_expert.py` 不支持该参数（argparse 直接拒绝）
3. **spatial/physical demo 收集均 0% 成功率** — 两个收集任务都跑完了全部 episode 但无一成功，说明 policy 在扰动场景下完全失效，或 success 判定逻辑有问题。这是最严重的问题——需要排查是 policy 本身不行、扰动强度过大、还是 success detector 有 bug

---
