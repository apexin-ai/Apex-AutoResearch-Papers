# code openvla eval script

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_openvla_eval_script_20260525T061547_result.json`
- **Structured JSON:** [`d550a9f9550b0d36c947.json`](../../sessions/d5/d550a9f9550b0d36c947.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本结构完整。下面总结产出。

---

## 产出

**脚本**: `artifacts/eval_safelibero_openvla.py`

### 与旧版本的关键修改

| 项目 | 旧版 | 新版 |
|------|------|------|
| 图像预处理 | 无旋转 | 180° 旋转 (`[::-1, ::-1]`) |
| unnorm_key | `bridge_orig` | `libero_object` |
| 旋转格式 | Euler→axis-angle 转换 | 直接使用（LIBERO 数据已是 axis-angle） |
| gripper 后处理 | 两步（normalize + invert） | `action[-1] = -np.sign(2*action[-1]-1)` |
| warmup | 10 步 dummy | 50 zero-steps + 10 gripper-closed（与 pi0 eval 一致） |
| 成功检测 | `done` flag | `env.check_success()` |
| env 分辨率 | 256 | 224 |
| frozen 定义 | total EE disp < 1mm | max EE disp from initial < 0.1mm |
| CLI | `--suite` only | `--scene object_pudding` + `--suite` |
| 新增指标 | — | smoothness, displacement 分布（all/safe episodes）, real_safe_rate |

### 安装依赖

```bash
pip install torch torchvision transformers timm tokenizers pillow scipy
pip install flash-attn --no-build-isolation  # 可选，加速推理
# prismatic 通过 trust_remote_code=True 自动加载
```

### 启动命令

```bash
# 全部 4 tasks, 800 episodes
python scripts/eval_safelibero_openvla.py \
    --model_path openvla/openvla-7b \
    --scene object_pudding \
    --gpu 1 \
    --n_episodes 200 \
    --output_dir /root/autodl-tmp/eval_results/openvla_base/

# 单 task 测试
python scripts/eval_safelibero_openvla.py \
    --model_path openvla/openvla-7b \
    --scene object_pudding \
    --task_id 0 \
    --n_episodes 2 \
    --max_steps 50 \
    --gpu 0
```

### 预估资源

- **显存**: ~16GB (bf16), ~10GB (int8), ~7GB (int4)
- **速度**: ~0.3s/step → ~90s/episode → ~5h per task (200 eps) → ~20h total (800 eps, 1 GPU)
- 可用 4 GPU 并行（每 GPU 跑 1 task），缩短到 ~5h

---
