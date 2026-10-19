# code eval pipeline verify

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-pipeline-verify_20260516T040341_result.json`
- **Structured JSON:** [`2975d580b4b1e77b165e.json`](../../sessions/29/2975d580b4b1e77b165e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

收集完所有信息。生成报告。

## 验证报告

### Part 1: 评测管线完整性

| # | 检查项 | 状态 | 说明 |
|---|--------|------|------|
| 1 | `task_classification.json` | **PASS** | 路径不在项目内，实际位于 `/root/LIBERO-plus/libero/libero/benchmark/task_classification.json`（1.9MB），4 个 split：libero_spatial=2402, libero_object=2518, libero_goal=2591, libero_10=2519 |
| 2 | `evaluate_libero_plus.py` 导入 | **PASS** | 全部依赖加载成功 |
| 3 | `meta_brain_assembly.MetaBrain` 导入 | **PASS** | 加载耗时 ~6s |
| 4 | `ablation_ladder.py` 导入 | **PASS** | — |
| 5a | par_router checkpoint | **PASS** | `checkpoints/phase1/par_router/best_router.pt` 存在 |
| 5b | LoRA expert checkpoints | **PASS** | `lora_visual_r16`/`lora_physical_r16`/`lora_universal_r16`/`lora_universal_r48` 均有 step_1000~9000 + final 全套 adapter；**注意**：当前 `final/` 时间戳 (11:48-11:52) 早于当前训练启动时间 (11:54)，是上一轮残留；当前训练仍在运行 |
| 5c | `checkpoints/phase1/visual/` | PASS | 旧期 epoch_0/best 存在（不同目录布局，老路径） |
| 6 | LIBERO 环境 | **PASS** | namespace package `libero` from `/root/LIBERO-plus/libero`，`libero.libero.benchmark` 可导入；`autodl-tmp/libero_demos/libero_object_image/` 存在 LeRobot 数据，`libero_plus_assets/assets.zip` (6.4GB) 未解压 |

### Part 2: 空闲 GPU 接力 spatial 训练验证

| # | 检查项 | 状态 | 说明 |
|---|--------|------|------|
| 7 | `phase1.augment_spatial` 导入 | **FAIL → 修复** | 任务描述中类名 `SpatialDistractorAugmentation` 错误，实际类名是 `SpatialAugmentation`（line 59）。导入 `from phase1.augment_spatial import SpatialAugmentation` 验证通过 |
| 8 | `phase1.data_loader.LiberoLeRobotDataset` 导入 | **PASS** | — |
| 9 | `train_lora_expert.py --help` | **PASS** | 支持 `--perturbation_type {visual,spatial,physical,universal}` |

### 当前 GPU 占用（含接力计划评估）

```
GPU0 visual          PID 391444  16:11 CPU
GPU1 physical        PID 391521  17:55 CPU
GPU2 universal_r16   PID 391663  17:24 CPU  ← 任务期望 spatial 接力此卡
GPU3 universal_r48   PID 391810  17:08 CPU
```

所有 4 卡满载训练中（~13GB / 97GB used，99% util）。当 GPU2 上的 `universal_r16` 完成后，启动 spatial 的命令应为：

```bash
cd /root/meta_brain_lora_routing && export CUDA_VISIBLE_DEVICES=2 && \
python phase1/train_lora_expert.py --perturbation_type spatial --gpu_id 0 \
  --lora_rank 16 --batch_size 16 --no_wandb
```

### 修复建议

唯一的 FAIL（#7）是任务描述本身的类名笔误，无需改代码：脚本内部用 `build_perturbation_augmenter(perturbation_type="spatial", ...)`（`train_lora_expert.py:234`）而非直接 import 类名，运行时不受影响。

### 结论

**评测管线全绿，可在 4 个 LoRA expert 训练完成后立即跑 `evaluate_libero_plus.py` + `ablation_ladder.py`。** spatial r16 训练入口和数据增强模块均已就绪，等 GPU2 释放即可接力。

---
