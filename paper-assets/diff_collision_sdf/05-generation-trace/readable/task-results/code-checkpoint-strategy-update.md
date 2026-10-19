# code checkpoint strategy update

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_checkpoint_strategy_update_20260520T065625_result.json`
- **Structured JSON:** [`f96358b4b1b27a4ac6c2.json`](../../sessions/f9/f96358b4b1b27a4ac6c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

情况清楚了。总结一下当前状态和需要的操作：

## 修改汇报

### 修改的文件（两台服务器相同）
**`openpi/scripts/train_pytorch.py`** — `save_checkpoint` 函数：
- 添加 `loss=None` 参数
- 新增 best model 保存逻辑（保存到 `checkpoint_dir/best/`）
- 新增 checkpoint 清理逻辑（`SAVE_TOTAL_LIMIT = 5`，超过 5 个自动删最旧的）
- 调用处传入 `loss=loss.item()`

**训练脚本本身无需修改** — 三个脚本的 `--save_interval` 默认值已经是 2000。

### 当前实验状态

| 服务器 | 实验 | 当前 step | save_interval | 状态 |
|--------|------|-----------|---------------|------|
| westd-35807 | baseline_spatial_seed0 | ~8274 | 2000 | 运行中 |
| westd-35807 | baseline_spatial_seed1 | ~8567 | 2000 | 运行中 |
| westd-35807 | baseline_object_seed0 | ~8601 | 2000 | 运行中 |
| westd-35807 | a1_sdf_spatial_seed0 | 6499 | 2000 | **崩溃**（磁盘满） |
| westd-45947 | a3_spatial_seed0 | ~2500 | **500** | 运行中 |
| westd-45947 | a3_object_seed0 | ~2000 | **500** | 运行中 |

### 热更新情况

**所有运行中实验都无法热更新** — Python 模块在启动时已加载到内存，文件修改不影响运行中进程。需要重启才能生效。

### 重启优先级

1. **westd-45947 A3（高优先级）** — save_interval=500，生成 checkpoint 过快，需要尽快重启
2. **westd-35807 A1（必须重启）** — 已崩溃，必须恢复
3. **westd-35807 Baselines（低优先级）** — save_interval 已是 2000，当前每个实验只有 4 个 checkpoint，在 step 12000 前不会超过 5 个。可以继续跑，择机重启

### 重启命令

**westd-45947 A3（需要先 kill 旧进程）：**
```bash
# Kill
kill 33877 33956

# 重启 spatial_bowl (恢复 checkpoint 2500)
CUDA_VISIBLE_DEVICES=0 nohup python scripts/train_a3_hook.py --scene spatial_bowl --seed 0 --save_interval 2000 --batch_size 32 --gpu 0 --resume > /root/autodl-tmp/logs/a3_gradient_spatial_bowl_s0_v2.log 2>&1 &

# 重启 object_pudding (恢复 checkpoint 2000)
CUDA_VISIBLE_DEVICES=1 nohup python scripts/train_a3_hook.py --scene object_pudding --seed 0 --save_interval 2000 --batch_size 32 --gpu 0 --resume > /root/autodl-tmp/logs/a3_gradient_object_pudding_s0_v2.log 2>&1 &
```

**westd-35807 A1（恢复 checkpoint 6000）：**
```bash
CUDA_VISIBLE_DEVICES=3 nohup python scripts/train_a1_sdf_aux.py --scene spatial_bowl --seed 0 --resume > /root/autodl-tmp/logs/a1_sdf_spatial_bowl_s0_v4.log 2>&1 &
```

是否现在执行重启？

---
