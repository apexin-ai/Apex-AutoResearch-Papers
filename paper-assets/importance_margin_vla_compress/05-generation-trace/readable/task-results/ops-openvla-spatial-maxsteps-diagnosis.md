# ops openvla spatial maxsteps diagnosis

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_openvla-spatial-maxsteps-diagnosis_20260521T011112_result.json`
- **Structured JSON:** [`66c301da4f52706a0635.json`](../../sessions/66/66c301da4f52706a0635.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已恢复原状。

---

## 汇报

### 1. WebSearch 找到的推荐 max_steps

| Suite | 标准 max_steps | 最长 demo | 来源 |
|-------|---------------|-----------|------|
| LIBERO-Spatial | **280** | 193 | [LightVLA LIBERO.md](https://github.com/LiAutoAD/LightVLA/blob/main/LIBERO.md), [LeRobot docs](https://huggingface.co/docs/lerobot/libero) |
| LIBERO-Object | **280** | 254 | 同上 |
| LIBERO-Goal | **300** | 270 | 同上 |
| LIBERO-10/Long | **520** | 505 | 同上 |

**所有 VLA 论文（OpenVLA, OpenVLA-OFT, LightVLA）均使用 280 steps 跑 Spatial 并报告 84-96% SR。**

### 2. A/B 测试结果

| 设置 | max_steps | Episodes | SR | 结论 |
|------|-----------|----------|------|------|
| A (原始) | 280 | 10 (prior) | **0%** | 失败 |
| B (测试) | 600 | 5 | **0%** | 失败 |

max_steps 从 280 提升到 600（2.14x），SR 仍然是 0%。**max_steps 排除，不是根因。**

### 3. 我们的 SUITE_MAX_STEPS 设置

当前脚本的值与所有文献一致，**无需修改**：
- spatial: 280 ✓
- object: 280 ✓
- goal: 300 ✓
- libero_10: 520 ✓

### 4. 真正需要排查的方向

0% SR on Spatial（同一 checkpoint 在 Object 上 93%）更可能的原因：
- **Checkpoint 质量问题**：该 checkpoint 可能不是官方最佳版本，或下载不完整（虽然文件结构看起来完整）
- **Image preprocessing 差异**：`img[::-1, ::-1]` 双翻转是否与 OpenVLA 训练预处理一致
- **Action 归一化/反转逻辑**：`normalize_gripper_action` 和 `invert_gripper_action` 的实现是否正确
- **Prompt format 不匹配**：task description 格式是否与训练时一致
- **Spatial tasks 本身的特殊性**：需要更精确的空间推理能力，可能暴露了微调质量问题

### 5. 无需更新的实验

由于 max_steps 被排除为原因，不存在因 max_steps 需要重跑的实验。

---
