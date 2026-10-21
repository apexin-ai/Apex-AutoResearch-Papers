# debug sim rollout diagnosis

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_sim_rollout_diagnosis_20260516T080619_result.json`
- **Structured JSON:** [`74edfbc7cccca83390a0.json`](../../sessions/74/74edfbc7cccca83390a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有变体都 0% success、0 reward。mode collapse 太严重，调参无法缓解。

---

## 诊断结论

### 根本原因：LoRA 微调导致 flow matching ODE 推理 mode collapse

| 证据 | 值 |
|------|-----|
| 预训练模型 action chunk std | 0.104 |
| LoRA 模型 action chunk std | **0.006** (collapse) |
| 预训练模型 image sensitivity | 0.149 |
| LoRA 模型 image sensitivity | **0.024** (几乎忽略图像) |
| ODE 50步收敛结果 | 所有 noise 收敛到同一固定点 |
| LoRA scale=0.10 时 std | 0.067 (接近预训练) |

**机制**：LoRA 微调（alpha=64, rank=32, scale=2.0）改变了 velocity field 的全局结构，创建了一个退化不动点。`forward()` 因为有 GT action 混入 noise 能正确计算 loss（0.0187），但 `sample_actions()` 从纯 noise 出发时所有轨迹收敛到同一个与输入无关的常数 action。

### 次要 bug（已修复）

`gym_aloha/AlohaInsertion-v0` 注册的 `max_episode_steps=300`，但训练数据 episode 长度 = 400。已修复 `eval_sim.py` 传入 `max_episode_steps=args.max_steps`。

### 不是问题的方面
- Image 格式/尺寸（正确，prepare_images 会 resize）
- State 格式（14-dim，无归一化需求）
- Action 空间（14-dim，[-1,1]）
- Checkpoint 加载（0 missing/unexpected keys）
- ACIS/bypass 代码逻辑（三组都 collapse，baseline 同样 0%）

### 可行修复方案

1. **降低 LoRA alpha**（从 64 降到 16-32），重新训练 — 减小 LoRA 对 flow 全局结构的破坏
2. **训练时加入 generation loss** — 不仅用 forward (reconstruction)，定期用 sample_actions 反向传播
3. **训练步数减少** — 当前 30k 步可能过拟合了 velocity field 的局部结构
4. **换用 full fine-tuning** 或 **merge LoRA 后继续训练** — 避免 LoRA rank 限制导致的退化模式
5. **使用 action_head 独立训练** — 冻结视觉编码器只训 action decoder，可能不会破坏 flow

诊断报告已写入 `eval_results/sim_rollout_diagnosis.md`。

---
