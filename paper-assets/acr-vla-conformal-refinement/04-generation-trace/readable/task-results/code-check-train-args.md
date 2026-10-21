# code check train args

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check-train-args_20260513T041004_result.json`
- **Structured JSON:** [`07de90cf02ed6a89d274.json`](../../sessions/07/07de90cf02ed6a89d274.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 成功启动，SmolVLA 模型已加载，precompute 正在运行。以下是完整产出：

---

## 1. train_crm.py 完整参数列表

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `--benchmark` | str | `object` | `object/spatial/goal/long/90` |
| `--epochs` | int | `50` | 训练轮数 |
| `--batch_size` | int | `32` | |
| `--lr` | float | `1e-3` | |
| `--seed` | int | `42` | |
| `--output_dir` | str | `/root/autodl-tmp/checkpoints/crm/` | 模型存放 |
| `--cache_dir` | str | `/root/autodl-tmp/crm_cache/` | precompute 缓存 |
| `--K` | int | `10` | 采样数 |
| `--obs_dim` | int | `960` (=OBS_DIM) | VLM hidden_size |
| `--hidden_dim` | int | `256` | CRM 隐层 |
| `--aug_noise_min` | float | `0.02` | |
| `--aug_noise_max` | float | `0.1` | |
| `--aug_ratio` | float | `0.5` | 增强比例 |
| `--precompute` | flag | `False` | 只做 precompute |
| `--auto` | flag | `False` | 缓存缺失时自动 precompute 再 train |
| `--smolvla_path` | str | `lerobot/smolvla_base` | |
| `--max_demos_per_task` | int | `50` | |
| `--val_split` | float | `0.1` | |
| `--log_every` | int | `50` | |

## 2. evaluate.py 完整参数列表

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `--benchmark` | str | `object` | `object/spatial/goal/long/90` |
| `--checkpoint` | str | `None` | CRM 权重路径 (crm_best.pt) |
| `--n_rollouts` | int | `20` | 每个 task rollout 次数 |
| `--max_steps` | int | `300` | 每次 rollout 最大步数 |
| `--seed` | int | `42` | |
| `--K` | int | `10` | |
| `--mode` | str | `crm_perdof` | `vla_only/crm_scalar/crm_perdof` |
| `--smolvla_path` | str | `lerobot/smolvla_base` | |
| `--obs_dim` | int | `960` | |
| `--hidden_dim` | int | `256` | |
| `--render` | flag | `False` | |
| `--output_file` | str | `None` | 结果 JSON 输出路径 |

## 3. 硬编码常量 (utils.py)

```python
ACTION_DIM = 6    # 6 DOF, no gripper
H_EFF = 5         # effective horizon (truncated from chunk_size=50)
CHUNK_SIZE = 50   # SmolVLA native chunk_size
OBS_DIM = 960     # VLM hidden_size
```

H_EFF **硬编码为 5**，不通过命令行传入。

## 4. 正确的命令

**Precompute（Phase 1）：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export HF_HUB_OFFLINE=1 && export MUJOCO_GL=egl && \
cd /root/acr-vla-conformal-refinement && \
python -u src/train_crm.py --precompute --benchmark object
```

**Train（Phase 2，缓存就绪后）：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export HF_HUB_OFFLINE=1 && export MUJOCO_GL=egl && \
cd /root/acr-vla-conformal-refinement && \
python -u src/train_crm.py --benchmark object --epochs 50
```

**或一步到位（auto 模式）：**
```bash
python -u src/train_crm.py --auto --benchmark object --epochs 50
```

**Evaluate：**
```bash
python -u src/evaluate.py --benchmark object \
  --checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt \
  --mode crm_perdof --n_rollouts 20 \
  --output_file /root/autodl-tmp/results/eval_object.json
```

## 5. Dry-run 结果

**通过。** 日志输出：
- 参数解析正确
- CUDA 可用
- LIBERO demos 加载成功：500 trajectories → 72507 training samples
- SmolVLA 模型权重加载完成（489 weights loaded）
- Precompute 推理正在进行中（PID=28349，后台运行）

注：当前 precompute 缓存目录 (`/root/autodl-tmp/crm_cache/object/`) 为空，precompute 正在后台生成特征。完成后会写入 `manifest.json`。

---
