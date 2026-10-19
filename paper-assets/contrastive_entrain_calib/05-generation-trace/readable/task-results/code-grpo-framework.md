# code grpo framework

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo_framework_20260518T075453_result.json`
- **Structured JSON:** [`29e62853026c2f110033.json`](../../sessions/29/29e62853026c2f110033.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法验证通过。文件已写入 `artifacts/training/grpo_framework.py`。

骨架包含 7 个核心组件：

| 组件 | 职责 |
|------|------|
| `ActivationExtractionHook` | 训练时 forward hook，捕获目标层 hidden states |
| `MultiTurnRolloutGenerator` | 多轮对话 rollout 生成 + 关键 turn 激活提取 |
| `DirectionAlignmentReward` | R1: 激活沿 d_syc/d_gen 的 cosine 投影 |
| `ContrastiveConsistencyReward` | R2: 跨 condition 投影差对比 |
| `BehavioralReward` | R3: DeBERTa NLI 行为评分 |
| `DCGRPOTrainer` | 完整训练循环（rollout → 激活提取 → 三路 reward → GRPO 更新 → 方向重校准） |
| `DCGRPOConfig` | 全部超参数（LoRA rank 64, reward weights, 方向重校准间隔 500 步等） |

所有具体实现标注 `TODO`，接口签名、参数类型、返回值类型、数学公式注释均已定义。方向格式与 `compute_directions.py` 输出对齐 `(num_layers, 2, hidden_dim)`，token 位置检测逻辑预留了从 `extract_activations.py` 移植的接口。

---
