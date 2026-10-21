# ssh urgent status check v2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_status_check_v2_20260521T202603_result.json`
- **Structured JSON:** [`e7259dd9536f67af9e38.json`](../../sessions/e7/e7259dd9536f67af9e38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有已完成的结果已提取。下面是完整状态报告。

---

## 实验状态

| 实验 | Trained | Untrained Phase 1-2 (R², L1) | Untrained Phase 4 (Classification) | Untrained Phase 5 (Counterfactual) |
|------|---------|------|------|------|
| **tracvla_long_v1** | **完成** | **完成** | 运行中 (L24/31) | 未开始 |
| **tracvla_goal_v1** | **完成** | **完成** | 运行中 (L22/31) | 未开始 |

**预计剩余时间：~2.5h**（Phase 4 剩 ~10-30min，Phase 5 各 ~2h）

---

## 完整 Metrics

### 1. tracvla_long_v1

#### R² Probing (image_mean / last_preaction)

| Layer | **Trained** img | **Trained** last_pre | **Untrained** img | **Untrained** last_pre |
|-------|-------|----------|----------|----------|
| L0 | 0.795 | **0.616** | 0.768 | **0.564** |
| L4 | 0.803 | 0.773 | 0.779 | 0.685 |
| L8 | 0.810 | 0.792 | 0.791 | 0.700 |
| L11 | 0.816 | **0.817** | 0.779 | **0.716** |
| L16 | **0.826** | 0.808 | 0.790 | 0.746 |
| L20 | 0.824 | 0.798 | 0.801 | 0.723 |
| L24 | 0.818 | 0.750 | 0.788 | 0.722 |
| L28 | 0.812 | 0.614 | 0.779 | 0.717 |
| L29 | 0.805 | **0.545** | 0.776 | 0.713 |
| L30 | 0.799 | **0.434** | 0.775 | 0.707 |
| L31 | 0.790 | **0.619** | 0.759 | 0.717 |

**关键差异**：Trained last_preaction 有 strong inverted-U（peak L11=0.817 → collapse L30=0.434）。Untrained last_preaction 平坦（0.564→0.746 缓升后 plateau ~0.71-0.72，无 collapse）。

#### L1 Attention Profile

| | Trained | Untrained |
|---|---------|-----------|
| Instruction dominant | 30 | **32** |
| Mixed | 2 (heads 13, 22) | **0** |
| Image dominant | 0 | 0 |

#### Cross-instruction Classification (Trained only)
所有层 img_mean=1.0, last_preaction=1.0（L0_last_pre=0.983）。

#### Counterfactual Sensitivity (Trained only)

| Condition | Cohen's d | MSE |
|-----------|-----------|-----|
| empty | **1.473** | 0.161 |
| wrong | 1.418 | 0.157 |
| shuffled | 1.391 | 0.147 |
| paraphrased | 1.161 | 0.125 |

---

### 2. tracvla_goal_v1

#### R² Probing

| Layer | **Trained** img | **Trained** last_pre | **Untrained** img | **Untrained** last_pre |
|-------|-------|----------|----------|----------|
| L0 | 0.803 | **0.612** | 0.788 | **0.537** |
| L4 | 0.810 | 0.795 | 0.797 | 0.654 |
| L8 | 0.829 | 0.783 | 0.808 | 0.688 |
| L11 | 0.824 | 0.786 | 0.803 | 0.694 |
| L16 | 0.827 | 0.788 | 0.784 | **0.705** |
| L20 | **0.839** | 0.784 | 0.790 | 0.682 |
| L24 | 0.839 | 0.741 | 0.781 | 0.681 |
| L28 | 0.817 | **0.605** | 0.762 | 0.680 |
| L29 | 0.821 | **0.502** | 0.759 | 0.665 |
| L30 | 0.812 | **0.307** | 0.756 | 0.655 |
| L31 | 0.805 | **0.574** | 0.729 | 0.671 |

**关键差异**：与 long 一致。Trained last_preaction 有 dramatic collapse（L30=0.307，甚至比 long 更极端）。Untrained 平坦 plateau ~0.65-0.70。

#### L1 Attention Profile

| | Trained | Untrained |
|---|---------|-----------|
| Instruction dominant | 27 | **32** |
| Mixed | **5** (heads 2,6,13,22,24) | **0** |
| Image dominant | 0 | 0 |

Goal 实验 trained 比 long 多 3 个 mixed heads（5 vs 2）。

#### Cross-instruction Classification (Trained only)
所有层≈1.0。L0: img=0.996, last_pre=0.915。

#### Counterfactual Sensitivity (Trained only)

| Condition | Cohen's d | MSE |
|-----------|-----------|-----|
| empty | **1.524** | 0.140 |
| wrong | 1.405 | 0.137 |
| shuffled | 1.336 | 0.135 |
| paraphrased | 1.213 | 0.125 |

---

## Untrained 已有数据小结（仅记数字，不下结论，遵守 C001）

已完成的 untrained phases：
- **R²**：两个实验均为 flat profile（无 inverted-U collapse）
- **L1**：两个实验均 32/32 instruction dominant（0 mixed）

待完成：untrained cross-instruction classification + counterfactual（~2.5h 后出结果）。

---
