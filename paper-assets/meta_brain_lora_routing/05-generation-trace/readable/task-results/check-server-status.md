# check server status

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_server-status_20260516T011322_result.json`
- **Structured JSON:** [`dcd1d686a238feb5f755.json`](../../sessions/dc/dcd1d686a238feb5f755.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 1 状态汇总

### 所有 PID 均已死亡，GPU 全部空闲

| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| 0-3 | RTX PRO 6000 Blackwell (98GB) | 0 MiB | 0% |

---

### 1. LoRA Visual Training (`phase1_lora_visual.log`)
- **状态**: ❌ **失败**
- **错误**: `wandb.errors.UsageError: No API key configured`
- 启动时在 `wandb.init()` 就崩了，没有进行训练
- **但**: `checkpoints/phase1/visual/` 有之前的 checkpoint（时间戳 00:17-00:24），含 `best/` 和 `epoch_0/`（adapter 14MB，val_loss=6.237，仅跑了 5 step）——这应该是更早一次运行的产物
- **修复**: 加 `--no_wandb` 或先 `wandb login`

### 2. LoRA Universal r16 (`phase1_lora_universal_r16.log`)
- **状态**: ❌ **失败**
- **错误**: `unrecognized arguments: --run_name universal_r16_visual_bootstrap`
- 参数名错误，脚本不支持 `--run_name`
- **无 checkpoint 产出**

### 3. Physical Demo Collection (`phase1_physical_demo_collection.log`)
- **状态**: ✅ 完成，但 **0% 成功率**
- 490 episodes，0 成功，0 文件保存
- 耗时 55.9 min
- 输出目录 `data/expert_demos/physical/` 为空

### 4. Spatial Demo Collection (`phase1_spatial_demo_collection.log`)
- **状态**: ✅ 完成，但 **0% 成功率**
- 624 episodes，0 成功，0 文件保存
- 耗时 89.9 min
- 输出目录 `data/expert_demos/spatial/` 只有 `_tmp_bddl/`，无实际 demo

### 5. Sensor Noise (PID 182966)
- **状态**: 进程已死
- **无日志文件**（`phase1_sensor_noise.log` 不存在）

---

### 已有 Checkpoint
| 路径 | 大小 | 说明 |
|------|------|------|
| `checkpoints/phase1/par_router/best_router.pt` | 2MB | 之前训好的 |
| `checkpoints/phase1/visual/best/adapter_model.safetensors` | 14MB | val_loss=6.237, step=5, rank=16 |

### 结论
- 4 个任务全部结束，0 个成功产出有用结果
- 两个 LoRA 训练因配置问题（wandb key / 参数名错误）启动即失败
- 两个 demo collection 跑完但成功率 0%——baseline 模型在 physical/spatial 扰动下完全无法完成任务，这说明 demo 收集策略可能需要调整（或者这就是预期的——baseline 本身就不该能应对这些扰动）
- 4 张 98GB GPU 全部空闲，可立即重新利用

---
