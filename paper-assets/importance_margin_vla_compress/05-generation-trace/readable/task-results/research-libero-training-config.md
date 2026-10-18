# research libero training config

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_libero_training_config_20260516T125843_result.json`
- **Structured JSON:** [`9dbf143c3fb9f7dafd7e.json`](../../sessions/9d/9dbf143c3fb9f7dafd7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在整理完整产出。

---

## 产出汇总

### 1. SmolVLA 官方 LIBERO 训练配置详情

| 参数 | 值 |
|------|---|
| 模型 | SmolVLA 0.45B (SmolVLM2-500M + action expert) |
| 训练方式 | `train_expert_only=True`, freeze VLM + vision encoder |
| 数据集 | `HuggingFaceVLA/libero` |
| Steps | 100,000 |
| Batch size | 4 (单卡), 论文可能用更大 effective batch |
| LR | 1e-4, cosine decay → 2.5e-6, warmup 1000 steps |
| Chunk size | 50 (action horizon) |
| Flow matching | 10 denoising steps |
| LoRA | 官方**不用** LoRA，我们的项目用 rank=32/alpha=64 以兼容 IMM |
| 图像预处理 | resize+pad to 512×512 |
| 归一化 | state/action: MEAN_STD, images: IDENTITY |

### 2. LIBERO Obs/Action Space

- **Action**: 7-dim `[-1,1]`, 6D EEF delta (position+orientation) + 1D gripper, relative control
- **State**: 8-dim = eef_pos(3) + axis_angle(3) + gripper_qpos(2)
- **Images**: agentview (主视角) + wrist camera (手腕), env 默认 360×360
- **Dataset keys**: `observation.images.image`, `observation.images.image2`, `observation.state`, `action`
- **50 demos per task**, 每 suite 10 tasks

### 3. 配置文件已写入服务器

- `configs/libero_baseline.yaml` — LIBERO baseline (LoRA, no IMM)
- `configs/libero_imm.yaml` — LIBERO + IMM (inherits baseline)

### 4. 从 Aloha 适配到 LIBERO 的代码修改清单

| 文件 | 修改内容 |
|------|---------|
| `train.py` | 数据集加载基本无需改动（`load_dataset` 已用 LeRobot API，只需改 config 中的 repo_id）。`_adapt_projections` 已处理 state/action dim 变化。**需确认** camera key mapping 是否正确（从 `observation.images.top` → `observation.images.image/image2`） |
| `eval_success_rate.py` | **需要重写或新建** `eval_success_rate_libero.py`。当前只支持 aloha_sim AlohaInsertion-v0 环境。LIBERO 需要用 `lerobot.envs.libero.create_libero_envs` 创建多 suite、多 task 的 env，并用 `LiberoProcessorStep` 处理 obs |
| `imm/` 模块 | **基本不需要改**。ACIS 和 token selection 操作在 visual token 层面，与任务无关。`visual_dim=960`（SigLIP output）和 `action_dim=720`（expert hidden）不随 task 变化 |
| `evaluate.py` | 离线 metric 评估（margin stats, Lipschitz 等）不依赖 env，只需改 config 切换数据集即可 |
| 新增 | `eval_success_rate_libero.py` — 处理 4 suites × 10 tasks × 10 episodes 的 closed-loop rollout |

### 5. 预估训练时间（RTX PRO 6000 96GB）

- **Baseline 100K steps, bs=4**: 约 20-25 小时（A100 参考值 4h/20K steps, RTX PRO 6000 Blackwell 性能接近 A100，100K ≈ 5× ）
- **可优化**: batch_size 可提到 8-16（96GB 显存充裕），等比缩减 steps 或加速收敛
- **IMM 额外开销**: ACIS forward + margin loss 约增加 15-20% 训练时间

Sources:
- [SmolVLA LIBERO Training Issue #3287](https://github.com/huggingface/lerobot/issues/3287)
- [HuggingFaceVLA/smolvla_libero](https://huggingface.co/HuggingFaceVLA/smolvla_libero)
- [LIBERO Documentation](https://huggingface.co/docs/lerobot/en/libero)
- [SmolVLA Documentation](https://huggingface.co/docs/lerobot/en/smolvla)

---
