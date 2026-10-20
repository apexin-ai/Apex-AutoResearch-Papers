# ssh action delta collect

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_action-delta-collect_20260515T151912_result.json`
- **Structured JSON:** [`1e15b0e30b1a6f53fb26.json`](../../sessions/1e/1e15b0e30b1a6f53fb26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。以下是完整报告。

---

## Action-Delta 实验完整报告

### 一、Per-Layer R² 对比表（33层 × trained/untrained）

| Layer | Trained R² | Untrained R² | Δ(T-U) |
|------:|----------:|------------:|-------:|
| 0 | 0.0000 | 0.0000 | 0.0000 |
| 1 | 0.0246 | 0.0289 | **-0.0043** |
| 2 | 0.0321 | 0.0155 | 0.0166 |
| 3 | 0.0350 | 0.0229 | 0.0121 |
| 4 | 0.0322 | 0.0149 | 0.0173 |
| 5 | 0.0453 | 0.0000 | 0.0453 |
| 6 | 0.0385 | 0.0000 | 0.0385 |
| 7 | 0.0456 | 0.0000 | 0.0456 |
| 8 | 0.0507 | 0.0000 | 0.0507 |
| 9 | 0.0518 | 0.0000 | 0.0518 |
| 10 | 0.0553 | 0.0000 | 0.0553 |
| 11 | 0.0550 | 0.0000 | 0.0550 |
| 12 | 0.0581 | 0.0000 | 0.0581 |
| 13 | 0.0583 | 0.0000 | 0.0583 |
| **14** | **0.0594** | 0.0000 | **0.0594** |
| 15 | 0.0555 | 0.0000 | 0.0555 |
| 16 | 0.0566 | 0.0136 | 0.0430 |
| 17 | 0.0568 | 0.0000 | 0.0568 |
| 18 | 0.0581 | 0.0000 | 0.0581 |
| 19 | 0.0576 | 0.0131 | 0.0445 |
| 20 | 0.0565 | 0.0168 | 0.0397 |
| 21 | 0.0536 | 0.0131 | 0.0405 |
| 22 | 0.0536 | 0.0163 | 0.0374 |
| 23 | 0.0483 | 0.0099 | 0.0384 |
| 24 | 0.0520 | 0.0149 | 0.0371 |
| 25 | 0.0576 | 0.0122 | 0.0454 |
| 26 | 0.0500 | 0.0000 | 0.0500 |
| 27 | 0.0527 | 0.0180 | 0.0348 |
| 28 | 0.0490 | 0.0000 | 0.0490 |
| 29 | 0.0561 | 0.0173 | 0.0388 |
| 30 | 0.0500 | 0.0170 | 0.0331 |
| 31 | 0.0399 | 0.0125 | 0.0275 |
| 32 | 0.0499 | 0.0485 | 0.0015 |

**Trained peak**: Layer 14, R²=0.0594
**Untrained peak**: Layer 32, R²=0.0485（其余中间层几乎为 0）

### 二、Gate 判定

#### G1-delta: Trained peak R²(action-delta) > 0.05?
**PASS** — Layer 14 R² = 0.0594 > 0.05

#### G2-delta: Δ(trained - untrained) > 0.03, 且 ≥5/10 tasks 一致?
**PASS** — 
- Peak layer Δ = 0.0594 - 0.0000 = 0.0594 > 0.03 ✓
- Per-task consistency: **10/10 tasks** trained > untrained at layer 14（untrained 全部 ≈ 0）✓

关键发现：untrained 在 layers 5-15, 17-18, 26, 28 的 R² 几乎为零，而 trained 在这些层达到 0.04-0.06。唯一例外是 **layer 32**（untrained 0.0485 vs trained 0.0499，Δ仅0.0015），说明最后一层的 action-delta 信息并非训练产生。

### 三、Best Layer (14) Per-Dim R²

| Dim | Trained L14 | Untrained L14 | DINO L0 |
|-----|----------:|-------------:|--------:|
| dx | 0.1783 | -0.0000 | 0.1744 |
| dy | 0.2665 | -0.0000 | 0.2588 |
| dz | 0.3576 | -0.0000 | 0.3745 |
| drx | 0.0942 | -0.0000 | 0.0840 |
| dry | 0.0511 | -0.0000 | 0.0563 |
| drz | 0.1735 | -0.0000 | 0.1765 |
| gripper | 0.0357 | -0.0000 | 0.0365 |

dz（垂直位移变化）最可预测，dy 次之。

### 四、Per-Task R² at Best Layer

| Task (short) | Trained L14 | Untrained L32 | DINO L0 |
|---|----------:|-------------:|--------:|
| KITCHEN3_stove_moka | 0.0521 | 0.0305 | 0.0482 |
| KITCHEN4_bowl_drawer | 0.0606 | 0.0637 | 0.0595 |
| KITCHEN6_mug_micro | 0.0398 | 0.0258 | 0.0419 |
| KITCHEN8_two_moka | 0.0388 | 0.0291 | 0.0359 |
| LIVING1_soup_cream | 0.0641 | 0.0621 | 0.0710 |
| LIVING2_soup_tomato | 0.0648 | 0.0539 | 0.0667 |
| LIVING2_cream_butter | 0.0914 | 0.0814 | 0.0926 |
| LIVING5_two_mugs | 0.0613 | 0.0440 | 0.0666 |
| LIVING6_mug_pudding | 0.0463 | 0.0392 | 0.0430 |
| STUDY1_book_caddy | 0.0775 | 0.0521 | 0.0839 |

Per-task consistency（trained L14 > untrained L14）: **10/10 tasks**（untrained L14 全为~0）

### 五、DINO Action-Delta 结果

| Metric | Value |
|--------|------:|
| Overall R² | **0.0604** |
| per_task mean R² | 0.0609 |
| gripper accuracy | 0.5700 |

**DINO R²(0.0604) ≈ Trained peak R²(0.0594)**。DINO 视觉特征对 action-delta 的预测能力与训练后的 VLA 相当，说明 action-delta 信号主要来自视觉信息（场景几何），而非 VLA 训练习得的动作知识。

### 六、PCA-1024 实验状态

| 实验 | 进度 | 状态 |
|------|------|------|
| action_prediction_pca1024 | Layer 30/33 | 运行中（PID 617024） |
| action_delta_pca1024 | Layer 26/33 | 运行中（PID 617376） |

最新 PCA 结果摘要：
- action_prediction_pca1024 L29: R²=0.6218（对比全维度 ~0.66 衰减不大）
- action_delta_pca1024 L25: R²=0.0538（对比全维度 ~0.058 基本一致）

预计 10-15 分钟内全部完成。

### 七、关键结论

1. **Action-delta 信号非常弱**（peak R²≈0.06），远低于 action-prediction（R²≈0.66）
2. **DINO ≈ Trained VLA**：DINO 单层即可匹配 VLA 33 层最优，action-delta 信号主要反映场景几何结构而非训练获得的动作规划
3. **Untrained 中间层完全无信号**（layers 5-28 ≈ 0），但 layer 32（最后一层）有 R²=0.0485，接近 trained
4. **PCA-1024 损失极小**：降维 75% 后 R² 几乎无衰减，说明 action-delta 信号在低维子空间中

---
