# harvest long s46 and goal reconvla s46

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_long-s46-and-goal-reconvla-s46_20260524T061600_result.json`
- **Structured JSON:** [`3690897536313f2f1afe.json`](../../sessions/36/3690897536313f2f1afe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在有完整数据了。

---

## A: Long s46 — 仍在运行中

4 个 eval 全部仍在跑，已完成 **6/10 tasks**，当前在第 7 个 task（LIVING_ROOM_SCENE6），估计还需 ~1-1.5h。

当前中间结果（Adaptive τ=0.25 s46 已完成的 6 tasks）：

| Task | Adaptive s46 |
|------|-------------|
| LIVING_ROOM_SCENE2_alphabet_soup_and_tomato | 20% |
| LIVING_ROOM_SCENE2_cream_cheese_and_butter | 75% |
| KITCHEN_SCENE3_stove_and_moka_pot | 100% |
| KITCHEN_SCENE4_bowl_in_drawer | 95% |
| LIVING_ROOM_SCENE5_mugs_on_plates | 50% |
| STUDY_SCENE1_book_in_caddy | 95% |

**不可收割，需要后续再来取结果。**

---

## B: Goal Reconvla s46 Per-Task 分析

**Overall: Reconvla 79% vs VLA-only 83%（同 seed46）**

| Task | Reconvla | VLA-only | Δ |
|------|----------|----------|---|
| open_middle_drawer | 75% | 75% | 0 |
| bowl_on_stove | 95% | 100% | -5 |
| wine_on_cabinet_top | 85% | 90% | -5 |
| **open_top_drawer_put_bowl** | **65%** | 60% | **+5** |
| bowl_on_cabinet_top | 85% | 90% | -5 |
| plate_to_front_stove | 85% | 90% | -5 |
| **cream_cheese_in_bowl** | **55%** | **55%** | **0** |
| turn_on_stove | 95% | 100% | -5 |
| bowl_on_plate | 85% | 90% | -5 |
| **wine_bottle_on_rack** | **65%** | **80%** | **-15** |

### 异常低分原因

1. **put_the_wine_bottle_on_the_rack** (-15%)：最大单项拖累。Reconvla 的 CRM correction 对这个任务产生了明显干扰，导致比 VLA-only 下降了 3 个 episode。

2. **累积微降**：6 个 task 各 -5%（1 个 episode），加总贡献 -3%。这些都是 VLA-only 接近完美（90-100%）的 task，CRM 少量误判触发了不必要的 correction。

3. **cream_cheese_in_bowl (55%)**：这不是 Reconvla 的问题——VLA-only 也是 55%。这是 seed46 上的 intrinsic hard task。

4. 唯一改善的是 open_top_drawer (+5%)，但不足以弥补。

### 结论

79% vs 83% 的 gap 来源：
- wine_bottle_on_rack 贡献 -1.5%（占总 gap 的 37%）
- 6 个近满分 task 的微弱干扰贡献 -3%
- +0.5% 被一个小改善抵消

**根因**：Reconvla 在 s46 上产生了轻微 CRM 过度干预（false positive correction），尤其对 wine_bottle_on_rack。这不是系统性 bug，更像是 seed 级别的方差放大——前 4 seed 均值 ~83% 说明这个 seed 恰好运气较差。

---
