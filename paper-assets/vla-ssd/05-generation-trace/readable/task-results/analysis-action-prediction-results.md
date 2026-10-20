# analysis action prediction results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_action-prediction-results_20260515T144353_result.json`
- **Structured JSON:** [`6788d3ce301187ea5d1b.json`](../../sessions/67/6788d3ce301187ea5d1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。下面是完整结果报告。

---

## Action Prediction 33 层 Sweep 完整结果报告

### 1. Best Layer 总览

| 模型 | Best Layer | per_task_mean_R² | overall_R² | Gripper Acc |
|------|-----------|-----------------|-----------|-------------|
| **Trained** | 19 | **0.6831** | 0.6770 | 0.8989 |
| **Untrained** | 32 | **0.6164** | 0.6067 | 0.8726 |
| **DINOv2** | 0 (single) | **0.6759** | 0.6689 | 0.9001 |

### 2. Per-dim R² at Best Layer

| 维度 | Trained (L19) | Untrained (L32) | DINOv2 (L0) |
|------|--------------|----------------|-------------|
| dx | 0.5885 | 0.5345 | 0.5405 |
| dy | 0.7629 | 0.7067 | 0.7324 |
| dz | 0.5854 | 0.5102 | 0.5865 |
| drx | 0.3712 | 0.3658 | 0.3970 |
| dry | 0.1649 | 0.2037 | 0.1754 |
| drz | 0.6654 | 0.6361 | 0.6600 |
| gripper | 0.6815 | 0.6066 | 0.6779 |

### 3. Per-task R² at Best Layer

| Task | Trained (L19) | Untrained (L32) | DINOv2 (L0) |
|------|--------------|----------------|-------------|
| KITCHEN_SCENE3 (stove+moka) | 0.6775 | 0.6453 | 0.6791 |
| KITCHEN_SCENE4 (bowl+drawer) | 0.7174 | 0.6614 | 0.6974 |
| KITCHEN_SCENE6 (mug+microwave) | 0.7066 | 0.6257 | 0.6733 |
| KITCHEN_SCENE8 (2 moka pots) | 0.6521 | 0.5551 | 0.6414 |
| LIVING_ROOM1 (soup+cheese→basket) | 0.6509 | 0.5370 | 0.6181 |
| LIVING_ROOM2 (soup+tomato→basket) | 0.6315 | 0.5457 | 0.6621 |
| LIVING_ROOM2 (cheese+butter→basket) | 0.6547 | 0.5876 | 0.6357 |
| LIVING_ROOM5 (2 mugs→2 plates) | 0.6778 | 0.6204 | 0.6715 |
| LIVING_ROOM6 (mug+pudding) | 0.6043 | 0.5550 | 0.6114 |
| STUDY_SCENE1 (book→caddy) | 0.8586 | 0.8307 | 0.8691 |

### 4. Gate 判定

| Gate | 条件 | 数值 | 结果 |
|------|------|------|------|
| **G1** | trained best R² > 0.3 | 0.6831 > 0.3 | **PASS** |
| **G2** | Δ(trained - untrained) > 0.15 | 0.6831 − 0.6164 = **0.0668** | **FAIL** |
| **G3** | Δ(trained - DINO) > 0.15 | 0.6831 − 0.6759 = **0.0072** | **FAIL** |

### 5. Per-layer Trained vs Untrained（33 层完整对比）

| Layer | Trained | Untrained | Δ (T−U) | T>U |
|-------|---------|-----------|---------|-----|
| 0 | 0.0076 | 0.0076 | +0.0001 | ~ |
| 1 | 0.4502 | 0.5731 | −0.1229 | **No** |
| 2 | 0.5603 | 0.5334 | +0.0269 | Yes |
| 3 | 0.5692 | 0.5695 | −0.0003 | **No** |
| 4 | 0.5625 | 0.0461 | +0.5164 | Yes |
| 5 | 0.5688 | 0.1643 | +0.4046 | Yes |
| 6 | 0.5521 | 0.5136 | +0.0385 | Yes |
| 7 | 0.6093 | 0.4815 | +0.1277 | Yes |
| 8 | 0.6095 | 0.1688 | +0.4407 | Yes |
| 9 | 0.6068 | 0.2724 | +0.3344 | Yes |
| 10 | 0.6311 | 0.4287 | +0.2025 | Yes |
| 11 | 0.6395 | 0.2250 | +0.4145 | Yes |
| 12 | 0.6505 | 0.4513 | +0.1991 | Yes |
| 13 | 0.6712 | 0.4907 | +0.1805 | Yes |
| 14 | 0.6574 | 0.2017 | +0.4558 | Yes |
| 15 | 0.6630 | 0.4559 | +0.2071 | Yes |
| 16 | 0.6691 | 0.5412 | +0.1279 | Yes |
| 17 | 0.6659 | 0.3675 | +0.2984 | Yes |
| 18 | 0.6647 | 0.5198 | +0.1449 | Yes |
| **19** | **0.6831** | 0.4044 | **+0.2788** | Yes |
| 20 | 0.6700 | 0.5469 | +0.1231 | Yes |
| 21 | 0.6578 | 0.5352 | +0.1226 | Yes |
| 22 | 0.6686 | 0.4122 | +0.2564 | Yes |
| 23 | 0.6537 | 0.3776 | +0.2761 | Yes |
| 24 | 0.6556 | 0.5266 | +0.1290 | Yes |
| 25 | 0.6579 | 0.5227 | +0.1352 | Yes |
| 26 | 0.6430 | 0.1836 | +0.4594 | Yes |
| 27 | 0.6407 | 0.5123 | +0.1283 | Yes |
| 28 | 0.6562 | 0.3160 | +0.3402 | Yes |
| 29 | 0.6442 | 0.4993 | +0.1449 | Yes |
| 30 | 0.6428 | 0.4933 | +0.1495 | Yes |
| 31 | 0.6322 | 0.4485 | +0.1837 | Yes |
| **32** | 0.6266 | **0.6164** | +0.0102 | Yes |

**关键观察：**

- Trained 31/33 层 > Untrained（仅 layer 1、3 例外）
- Trained 的 per-layer 变化平稳（0.45–0.68），untrained 极度不稳定（0.05–0.62），多层 probe 训练疑似未收敛（layer 4/5/8/11/14/26 等 R² < 0.25）
- **Best-vs-best 比较（G2）差距仅 0.0668**，因为 untrained 的 layer 32（最后一层）恰好表现很好
- **DINO 单层 R² = 0.6759**，与 trained best 几乎持平（Δ=0.0072），trained 无明显优势
- 在 same-layer 对比中，trained 在大多数层大幅领先 untrained（中间层 Δ 常 > 0.2），但 gate 用的是 best-vs-best

---
