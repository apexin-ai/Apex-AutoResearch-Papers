# prep eval script s1s2 check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_eval_script_s1s2_check_20260524T142930_result.json`
- **Structured JSON:** [`1a0df99f81cab0d7da28.json`](../../sessions/1a/1a0df99f81cab0d7da28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。`eval_commands_d012_final.md` 已经包含完整的 6 模型 eval 命令模板，但缺少 `MUJOCO_GL=osmesa`。以下是完整确认。

## 1. Eval 架构

Pi0.5 eval 是 **双进程 pipeline**：
- `serve_policy.py` — 加载 checkpoint 到 GPU 并通过 websocket 提供推理服务
- `eval_pi05_safelibero.py` — 连接 websocket，运行 episode（仅 CPU）

Checkpoint 路径在 `serve_policy.py` 的 `--policy.dir` 中指定，`eval_pi05_safelibero.py` 本身不需要 checkpoint 参数。

## 2. Checkpoint 路径确认

6 个路径模式一致：

| 模型 | Checkpoint 路径 |
|------|----------------|
| s0_l005 | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l005/30000/` |
| s0_l01 | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l01/30000/` |
| s1_l005 | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l005/30000/` |
| s1_l01 | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l01/30000/` |
| s2_l005 | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed2_l005/30000/` |
| s2_l01 | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed2_l01/30000/` |

s0 两个路径从 registry 确认无误（s0_l005 notes 有 "30000/"，s0_l01 spec 有 `checkpoint_path`）。s1/s2 路径按相同命名规则推断，训练命令中的 `--scene object_pudding --seed {1,2} --lambda_sdf {0.005,0.01}` 会生成对应目录。

## 3. 现有 D012 Final 命令的问题

`artifacts/eval_commands_d012_final.md` 已经是完整的 6 模型命令，唯一缺失是 **`MUJOCO_GL=osmesa`**（ROADMAP 明确提到的渲染死锁修复）。需要在每个 tmux 窗口的环境设置中加上：

```bash
export MUJOCO_GL=osmesa
```

## 4. 更新后的命令

现有 artifact 只需在公共环境设置中追加一行，其余完全可用。以下是修正后的公共环境 block：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export JAX_PLATFORMS=cpu
export MUJOCO_GL=osmesa
export PYTHONPATH=/root/colliforce-vla/openpi/src:$PYTHONPATH
cd /root/colliforce-vla
```

### Batch 1: westd-35807 (4 GPU, 4 模型并行)

每个 tmux window 格式：
```bash
# s1_l005 为例（其他 3 个换 seed/lambda/GPU/port/output）
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export JAX_PLATFORMS=cpu MUJOCO_GL=osmesa
export PYTHONPATH=/root/colliforce-vla/openpi/src:$PYTHONPATH
cd /root/colliforce-vla

CUDA_VISIBLE_DEVICES=0 python openpi/scripts/serve_policy.py \
    --env libero --policy:checkpoint --policy.config pi05_libero \
    --policy.dir /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l005/30000 \
    --port 8000 &
SERVE_PID=$!; sleep 60

python scripts/eval_pi05_safelibero.py \
    --port 8000 --suite safelibero_object --safety_level II --n_episodes 50 \
    --seed 7 --output_path /root/autodl-tmp/eval_results/d012_final/eval_d012_final_s1_l005.json

kill $SERVE_PID
```

| Window | GPU | Port | Checkpoint seed/lambda | Output |
|--------|-----|------|----------------------|--------|
| s1_l005 | 0 | 8000 | seed1_l005 | `eval_d012_final_s1_l005.json` |
| s1_l01 | 1 | 8001 | seed1_l01 | `eval_d012_final_s1_l01.json` |
| s2_l005 | 2 | 8002 | seed2_l005 | `eval_d012_final_s2_l005.json` |
| s2_l01 | 3 | 8003 | seed2_l01 | `eval_d012_final_s2_l01.json` |

### Batch 2: westd-45947 (2 GPU, 2 模型并行)

同样格式，GPU 0/1, Port 8000/8001, s0_l005 和 s0_l01。

## 5. 启动前必须确认的事项

1. **s1/s2 训练是否完成** — registry 显示 `conclusion: failed` 但那是因为 SSH 断连无法诊断，训练进程本身可能已完成。SSH 恢复后第一步：
   ```bash
   ls /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed{1,2}_l{005,01}/30000/
   ```
2. **磁盘空间** — `df -h /root/autodl-tmp/`（之前发生过磁盘满崩溃）
3. **训练进程已退出** — `nvidia-smi` 确认 GPU 已释放，否则显存不够加载 serve_policy
4. **s2_l01 异常关注** — D012 final 文档提到该 run SDF loss 持续偏高（~0.067 vs ~0.033），需在 eval 后特别检查是否为 outlier

---
