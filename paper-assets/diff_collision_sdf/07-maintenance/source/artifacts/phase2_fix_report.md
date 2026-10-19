# Phase 2 转换 Bug 修复报告

**日期**: 2026-05-23
**状态**: 已修复，4 个训练已恢复运行

## Bug 描述
`on_step_start` 中 Phase 转换条件 `global_step == self.warmup_phase_steps` 在 resume 时不触发。Resume 从 step 6000 开始，永远不等于 5000，导致 LoRA 一直冻结。

## 修复内容

### Fix A: Phase 转换条件 `==` → `>=`
**文件**: `scripts/train_a1_sdf_aux_pi05.py` 行 199（原 181）
```python
# 修复前
if global_step == self.warmup_phase_steps and self.phase == 1:
# 修复后
if global_step >= self.warmup_phase_steps and self.phase == 1:
```

### Fix B: Resume 时从 checkpoint 恢复 phase 状态
在 `on_model_created` 末尾新增 18 行：读取最新 checkpoint 的 `aux_metadata.pt`，若 `phase >= 2` 则直接恢复 phase 并解冻 LoRA。避免 resume 时重复执行 LoRA warmup。

## 4 个训练恢复状态

| GPU | 实验 | 恢复 step | Phase 2 触发 | 显存 | action_loss |
|-----|------|-----------|-------------|------|-------------|
| cuda:0 | s1_l005 (lambda=0.005) | 6000 | step 6000 | 27045 MiB | ~0.03 |
| cuda:1 | s1_l01 (lambda=0.01) | 6000 | step 6000 | 27045 MiB | ~0.03 |
| cuda:2 | s2_l005 (lambda=0.005) | 6000 | step 6000 | 27045 MiB | ~0.03 |
| cuda:3 | s2_l01 (lambda=0.01) | 6000 | step 6000 | 27045 MiB | ~0.03 |

所有训练在恢复后第一个 step 即触发 Phase 2，LoRA 33.47M 参数解冻，100 步 grad warmup 已启动。

## 同步状态

| 服务器 | train_a1_sdf_aux_pi05.py | train_pi05_lora_baseline.py |
|--------|--------------------------|----------------------------|
| westd-35807 | Fix A + B 已应用 | 已同步 |
| westd-45947 | Fix A + B 已应用 | 已同步 |

## 注意事项
- westd-45947 上的训练 (~step 8000+) 不受影响（已过 Phase 2 转换），但脚本已同步修复以防未来 resume
- Baseline 脚本已有 `>=` 修复（本地 artifacts 版本），现已同步到两台服务器
