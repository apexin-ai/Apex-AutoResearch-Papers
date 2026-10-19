# diag task suite and server prep

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_task_suite_and_server_prep_20260516T134946_result.json`
- **Structured JSON:** [`8a5db13c4b9b300b9c3f.json`](../../sessions/8a/8a5db13c4b9b300b9c3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已收集全部信息。以下是结论：

---

## A. pi0_libero 训练的 task suite

**结论：pi0_libero 训练在所有 LIBERO suite 上（libero_spatial/object/goal/10/90），不是单一 suite。**

证据：
- 该 checkpoint 来自 HuggingFace `lerobot/pi0_libero_base`（README 中的 `model_id`）
- 训练数据为 `physical-intelligence/libero`（config.py 里 `repo_id="physical-intelligence/libero"`）——这是完整的 LIBERO 数据集
- README 示例用的是 `--env.task=libero_object`
- openpi 的 `examples/libero/main.py` 默认 `task_suite_name="libero_spatial"`

**我们用 `libero_spatial` 跑评测是合理的，不存在 suite 不匹配问题。** 如果 0% 成功率，原因不在 task suite。

---

## B. openpi server 启动 + client eval 完整命令

**Server（Terminal 1）：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/openpi
python scripts/serve_policy.py \
    --env LIBERO \
    --policy:Checkpoint \
    --policy.config pi0_libero \
    --policy.dir /root/autodl-tmp/checkpoints/pi0_libero \
    --port 8000
```

**Client eval（Terminal 2）：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/openpi
python examples/libero/main.py \
    --host 0.0.0.0 \
    --port 8000 \
    --task_suite_name libero_spatial \
    --num_trials_per_task 20
```

注意：
- `serve_policy.py` 使用 tyro CLI，`--policy:Checkpoint` 选择 Checkpoint 子命令
- `pi0_libero` config 有 `extra_delta_transform=True`，所以 server 会自动做 DeltaActions → AbsoluteActions 转换
- client 直接把 server 返回的 action 传给 env.step()

---

## C. Action 语义验证

**LIBERO env 期望的 action**：
- 维度：7（6 DoF arm delta + 1 gripper）
- 格式：`[dx, dy, dz, dax, day, daz, gripper]`
  - 前 6 维：**delta** end-effector pose（position delta + axis-angle delta）
  - 第 7 维：gripper（-1 = close, +1 = open），绝对值
- Range：无硬 clip。从 norm_stats 看，q01/q99 大致为：
  - actions[:6]：约 [-3.3, +2.7]（弧度空间，axis-angle 较大）
  - actions[6]：严格 [-1, +1]

**openpi pi0_libero 输出**：
- 模型输出经过 MEAN_STD unnormalize → 再经过 AbsoluteActions（加回 state） → LiberoOutputs 取前 7 维
- 最终输出是**绝对** action（position + orientation + gripper）
- client 的 `env.step(action.tolist())` 直接传入

**MetaBrain 输出 [-1.02, 1.06]**：
- 如果 MetaBrain 直接输出这个范围而没有经过 unnormalize + AbsoluteActions 转换，**是不匹配的**
- openpi 的 raw action 真实范围（unnormalized 后）远大于 [-1, 1]：q01=-3.3, q99=+2.7
- MetaBrain 输出看起来像是**归一化空间**（normalized to ~[-1,1]），没有经过 postprocess

**关键问题：MetaBrain 的 `predict_action` 是否做了 unnormalize + AbsoluteActions？** 如果没有，0% 成功率完全可以解释——action 在错误的空间里。`evaluate_libero_plus.py` 有 `--no_delta_actions` 参数和 `use_delta_actions` 逻辑，需确认那个 code path 是否正确执行了反归一化。

---
