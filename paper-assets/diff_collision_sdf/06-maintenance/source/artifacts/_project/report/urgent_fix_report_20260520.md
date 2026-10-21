# 紧急修复报告 2026-05-20

## 1. Kill seed 0 确认

- 原 PID 49555 (`python -u scripts/train_baseline.py --scene spatial_bowl --seed 0 --gpu 0`) 已 kill (SIGTERM)
- 该进程使用旧版代码启动（含 `--gpu 0` 参数，当前脚本已无此参数）
- GPU 0 内存已释放

## 2. extra_delta_transform 修复

**代码中无需修改。** `train_baseline.py:80` 已经是 `extra_delta_transform=False`。

PID 49555 是用旧版本代码启动的（启动命令含已废弃的 `--gpu` 参数），旧版本可能有 `extra_delta_transform=True`。当前代码在某次更新中已修复。

`train_a1_sdf_aux.py:215` 也已经是 `extra_delta_transform=False`。

## 3. seed 1 和 object_pudding 状态

两者均使用当前（正确）版本代码启动，`extra_delta_transform=False`：

| 任务 | PID | 启动命令 | Step ~70 Loss | 状态 |
|------|-----|---------|--------------|------|
| baseline_spatial_bowl_s1 | 94453 | `python -u scripts/train_baseline.py --scene spatial_bowl --seed 1` | 0.16-0.27 | ✅ 正常 |
| baseline_object_pudding_s0 | 95429 | `python -u scripts/train_baseline.py --scene object_pudding --seed 0` | 0.15-0.23 | ✅ 正常 |

**无需 kill 或重启。**

## 4. seed 0 重启

- 新 PID: 100319 (cuda:0)
- Conda 环境: libero (与其他 baselines 一致)
- WANDB_MODE=disabled
- 前 10 步 loss: 0.25, 0.23, 0.33, 0.25, 0.25, 0.24, 0.21, 0.25, 0.29, 0.27
- ✅ Loss ~0.2，正常

注意：首次尝试用 conda base 启动失败（缺 flax 模块），发现现有 baselines 使用 conda libero 环境。

## 5. A1 LoRA 修复

**文件**: `/root/colliforce-vla/scripts/train_a1_sdf_aux.py`，`on_step_start` 方法（行 139-156）

**修改前** (line 139-145):
```python
def on_step_start(self, global_step, model):
    if global_step == self.warmup_phase_steps and self.phase == 1:
        self.phase = 2
        _m = model.module if hasattr(model, "module") else model
        for p in _m.parameters():
            p.requires_grad = True
        logging.info("Phase 2: unfroze backbone at step %d", global_step)
```

**修改后**:
```python
def on_step_start(self, global_step, model):
    if global_step == self.warmup_phase_steps and self.phase == 1:
        self.phase = 2
        _m = model.module if hasattr(model, "module") else model
        n_unfrozen = 0
        for name, p in _m.named_parameters():
            if "lora" in name.lower():
                p.requires_grad = True
                n_unfrozen += p.numel()
        n_total_trainable = n_unfrozen
        for p in self.sdf_decoder.parameters():
            n_total_trainable += p.numel()
        for p in self.ee_extractor.parameters():
            n_total_trainable += p.numel()
        logging.info(
            "Phase 2: unfroze %d LoRA params at step %d (total trainable: %d)",
            n_unfrozen, global_step, n_total_trainable,
        )
```

**原因**: 旧代码 Phase 2 解冻全部 ~3.5B backbone 参数，修复后只解冻 LoRA 参数 (~26M)。
Optimizer 创建时已包含全部 model.parameters()，设 requires_grad=True 即可让 LoRA 参数参与梯度更新。

## 6. A1 启动状态

- Dry-run 完成：step 1 loss=0.2692, step 2 loss=0.2801 ✅
- 正式训练 PID: 101662 (cuda:3)
- 前 6 步 loss: 0.268, 0.280, 0.258, 0.282, 0.253, 0.215
- VRAM: 13.4 GB (Phase 1 backbone frozen，远低于 90 GB 限制)
- ✅ 训练正常

## 7. 最终 4 卡 GPU 状态

| GPU | PID | 任务 | VRAM | 状态 |
|-----|-----|------|------|------|
| cuda:0 | 100319 | baseline_spatial_bowl_s0 (重启) | 37.4 GB | ✅ 训练中 |
| cuda:1 | 94453 | baseline_spatial_bowl_s1 | 37.4 GB | ✅ 训练中 |
| cuda:2 | 95429 | baseline_object_pudding_s0 | 37.4 GB | ✅ 训练中 |
| cuda:3 | 101662 | a1_sdf_spatial_bowl_s0 | 13.4 GB | ✅ 训练中 |

所有 4 卡满负荷运行。
