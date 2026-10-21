# code fix baseline relaunch

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_baseline_relaunch_20260519T220914_result.json`
- **Structured JSON:** [`a83b45274167932b5e6a.json`](../../sessions/a8/a83b45274167932b5e6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

## 结果

**根因**：旧版 `train_baseline.py` 的 `--gpu` 参数在脚本内部设置 `CUDA_VISIBLE_DEVICES`，存在时序和环境冲突风险，导致非 cuda:0 的 GPU 上权重未正确加载。

**修复**：删除 `--gpu` 参数，改用外部 `CUDA_VISIBLE_DEVICES` 环境变量控制 GPU 选择；增加 `model.safetensors` 文件存在性验证。

**Dry-run 验证** (cuda:3)：Step 1 loss=0.2664, Step 2 loss=0.1695 ✓

**重启的实验**：
| 场景 | Seed | GPU | PID | 初始 Loss |
|------|------|-----|-----|-----------|
| spatial_bowl | 1 | cuda:1 | 94453 | ~0.22-0.28 ✓ |
| object_pudding | 0 | cuda:2 | 95429 | ~0.18-0.19 ✓ |

注意：conda 环境用 `libero` 而非 `base`；wandb 未配置 API key，已用 `WANDB_MODE=disabled` 启动。

---
