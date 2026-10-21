# Baseline 训练权重加载 Bug 修复报告

## 1. 根因分析

### 现象
- v1 运行：spatial_bowl seed 1 初始 loss=177，object_pudding seed 0 初始 loss=536
- 正常值：初始 loss ~0.2
- seed 0 spatial_bowl 在 cuda:0 上正常（loss 0.22→0.063）

### 根因
v1 版本的 `train_baseline.py` 使用 `--gpu` 参数在脚本内部设置 `CUDA_VISIBLE_DEVICES`：

```python
# 旧代码（有bug）
if not int(os.environ.get("WORLD_SIZE", "1")) > 1:
    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)
```

问题：
1. **时序问题**：在 Python 进程中设置 `CUDA_VISIBLE_DEVICES` 可能在 CUDA 运行时已经初始化之后才生效，导致设备映射失败
2. **与外部环境冲突**：当启动命令已通过 `export CUDA_VISIBLE_DEVICES=X` 设置了环境变量，脚本内部再次设置可能导致不一致
3. **seed 0 在 cuda:0 正常**是因为 `--gpu 0` 等同于默认行为，不触发上述时序问题

v2 修复时在 `train_pytorch.py` 中添加了 DIAG 诊断输出，同时确保了 `pytorch_weight_path` 正确传递到 config。v2 运行时通过外部设置 `CUDA_VISIBLE_DEVICES` 并配合 `--gpu` 参数，权重加载正常。

### 补充发现
- `train_pytorch.py` 中没有应用 `freeze_filter`，所有参数都参与训练（全量微调而非 LoRA）
- PI0Pytorch 模型不实现 LoRA，`gemma_2b_lora`/`gemma_300m_lora` variant 仅影响 JAX 模型架构
- 这对 baseline 实验（vanilla fine-tune）是正确行为

## 2. 修复内容

### `scripts/train_baseline.py` 改动
1. **删除 `--gpu` 参数**：不再在脚本内部设置 `CUDA_VISIBLE_DEVICES`，改用外部环境变量
2. **增加权重文件验证**：启动前检查 `model.safetensors` 文件是否存在（而非仅检查目录）
3. **增加 weight path 日志**：便于排查
4. **更新 Usage docstring**：明确使用 `CUDA_VISIBLE_DEVICES=X` 前缀

### 未修改
- `openpi/scripts/train_pytorch.py`：保持现有 DIAG 输出（有助于调试），不修改权重加载逻辑

## 3. Dry-run 验证结果

在 cuda:3 上运行 `--scene spatial_bowl --seed 99 --dry_run`：
- 权重加载：`missing=0, unexpected=0`
- 权重校验：`action_in_proj.weight mean=-0.000354, std=0.177879`（与文件一致）
- Step 1 loss: **0.2664**
- Step 2 loss: **0.1695**
- 结论：权重正确加载，loss 在正常范围

## 4. 重启实验

### 运行中的实验

| 场景 | Seed | GPU | PID | 初始 Loss (前10步) | 状态 |
|------|------|-----|-----|-------------------|------|
| spatial_bowl | 0 | cuda:0 | 49555 | 0.22→0.063 (已有) | 继续运行 |
| spatial_bowl | 1 | cuda:1 | 94453 | 0.25, 0.23, 0.27, 0.22, 0.24, 0.24, 0.23, 0.28, 0.26, 0.22 | 已启动 ✓ |
| object_pudding | 0 | cuda:2 | 95429 | 0.18, 0.19 (持续增长中) | 已启动 ✓ |
| (空闲) | - | cuda:3 | - | - | 可用 |

### 启动命令
```bash
# spatial_bowl seed 1
CUDA_VISIBLE_DEVICES=1 WANDB_MODE=disabled python -u scripts/train_baseline.py --scene spatial_bowl --seed 1

# object_pudding seed 0
CUDA_VISIBLE_DEVICES=2 WANDB_MODE=disabled python -u scripts/train_baseline.py --scene object_pudding --seed 0
```

### 日志路径
- `/root/autodl-tmp/logs/baseline_spatial_bowl_seed1_v3.log`
- `/root/autodl-tmp/logs/baseline_object_pudding_seed0_v3.log`

## 5. 环境备注
- conda 环境: `libero`（不是 `base`）
- wandb 未配置 API key，使用 `WANDB_MODE=disabled`
