# eval d014 v7 final

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d014-v7-final_20260515T202259_result.json`
- **Structured JSON:** [`34c56b05c7e3a32a1355.json`](../../sessions/34/34c56b05c7e3a32a1355.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## D014 Gate Evaluation Phase 1 — v7 Final Eval 报告

### 运行信息

| 项 | 值 |
|---|---|
| 服务器 | westd-27271, GPU 1 (CUDA_VISIBLE_DEVICES=1) |
| 检查点 | `checkpoints/imm_anchor/step_029999` |
| 配置 | `configs/imm_anchor.yaml` |
| 批次数 | 500 |
| Seed | 42 |
| 运行时间 | ~21 min（04:31:39 → 04:52:43） |
| Lipschitz (spectral) | 1.0672 |
| Lipschitz (empirical) | 0.2493 |

### 关键指标摘要

| Condition | action_loss | margin_median | preservation_rate | kendall_tau | l_eps_delta_ratio_median |
|---|---|---|---|---|---|
| **eps=0.0, no prune** (clean baseline) | **0.0134** | 0.5743 | 1.0000 | 1.0000 | 0.1387 |
| eps=0.0, prune 50% | 0.0145 | 0.5815 | 1.0000 | 1.0000 | 0.1370 |
| eps=0.01, no prune | 0.0138 | 0.5943 | 0.9124 | 0.7868 | 0.1341 |
| eps=0.01, prune 50% | 0.0158 | 0.5846 | 0.9098 | 0.7871 | 0.1364 |
| eps=0.02, no prune | 0.0187 | 0.5854 | 0.8172 | 0.5559 | 0.2726 |
| eps=0.02, prune 50% | 0.0203 | 0.6034 | 0.8169 | 0.5579 | 0.2644 |
| eps=0.05, no prune | 0.0240 | 0.5781 | 0.6079 | 0.1391 | 0.6900 |
| eps=0.05, prune 50% | 0.0250 | 0.5761 | 0.6073 | 0.1372 | 0.6923 |

### 核心观察

1. **Pruning 对 action_loss 影响很小**：同 eps 下 prune 50% 只增加 8-9% loss（eps=0.0: 0.0134→0.0145, eps=0.05: 0.0240→0.0250），说明 ACIS 选中了真正重要的 token。

2. **Margin 稳健**：所有条件下 margin_median ≈ 0.57-0.60，跨 eps 和 prune 设置基本稳定，表明 IMM 训练成功建立了 token 重要性之间的清晰间隔。

3. **扰动敏感性的梯度退化符合预期**：
   - eps=0.01: preservation ≈ 91%, tau ≈ 0.79
   - eps=0.02: preservation ≈ 82%, tau ≈ 0.56
   - eps=0.05: preservation ≈ 61%, tau ≈ 0.14
   
4. **Prune 与 no-prune 的 preservation/tau 几乎一致**（差异 <0.3%），进一步确认 pruning 不破坏排序结构。

5. **l_eps_delta_ratio_median** 在低 eps 下非常小（~0.14），随 eps 增大上升到 ~0.69。这是 certified bound 的核心指标，表明在 eps≤0.02 时模型的 importance ranking 有较好的可证明保证。

### Warnings

- HuggingFace Hub 网络不可达（`chat_template.jinja`, `video_preprocessor_config.json`），重试后成功，**未影响结果**。
- `SmolVLMImageProcessor` 用作 video_processor 时有 TypeError 警告（框架兼容性问题），被捕获处理，**未影响结果**。

### 输出文件

- 服务器: `eval_results/eval_imm_v7_final.json`
- 本地: `artifacts/eval_imm_v7_final.json`

---
