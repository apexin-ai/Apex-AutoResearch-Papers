# research check xvla suite support

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check-xvla-suite-support_20260520T224929_result.json`
- **Structured JSON:** [`f24da3a2ab9b19c7c68c.json`](../../sessions/f2/f24da3a2ab9b19c7c68c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

## 结论

### 1. `--suite` 参数：**已完全支持**

eval 脚本（`eval_xvla_pruning_libero.py`）已有 `--suite` 参数，支持的 choices：
- `libero_spatial`
- `libero_object`（默认）
- `libero_goal`
- `libero_10`（即 LIBERO-Long）
- `libero_90`

`SUITE_MAX_STEPS` 字典也已为每个 suite 配置了 max_steps（spatial/object/goal=800, libero_10=900）。

### 2. domain_id 映射：**所有 LIBERO suite 共用 domain_id=3**

X-VLA 的 domain_id 是 embodiment-level 的 soft prompt 索引（模型有 30 个 domain），不是 task suite 级别的。所有 LIBERO suite 用同一个 Franka 机器人，所以 **domain_id=3 对所有 4 个 suite 通用**，无需改动。

### 3. X-VLA 模型训练范围：**应该覆盖全部 LIBERO suite**

- README 显示 "X-VLA 0.9B (Libero Edition)"，训练数据标注为 Bridge Data V2，但模型名为 `X-VLA-Libero`，说明在 LIBERO 上做了 fine-tune
- X-VLA 论文声称在 6 个 simulation 上评测并取得 SOTA，LIBERO 是其中之一
- 因此模型很可能在全部 LIBERO suite 上训练过，其他 suite 不会是 zero-shot（不会是 0%）

### 4. LIBERO 库：**4 个 suite 都已安装可用**

在 cqa1 上验证：libero_object、libero_spatial、libero_goal、libero_10 各有 10 个 task。

### 5. 需要的代码改动：**零改动**

直接跑：
```bash
# Spatial
CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_pruning_libero.py \
    --model_path /root/autodl-tmp/X-VLA-Libero \
    --suite libero_spatial --keep_ratio 0.5 --num_episodes 50

# Goal
... --suite libero_goal ...

# Long (LIBERO-10)
... --suite libero_10 ...
```

### 6. 现有 eval 结果状态

- **X-VLA pruning**：目前全部在 `libero_object` 上（k=0.1~0.95，seed 42/43/44）
- **SmolVLA smart compress**：已有 spatial 和 goal 的结果（`eval_smart_compress_m32_libero_spatial.json`、`eval_smart_compress_m32_libero_goal.json`）
- X-VLA 的 spatial/goal/long baseline 和 pruning 实验**尚未开始**

---
