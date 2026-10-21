# paper fix remote 4fixes p0

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_remote_4fixes_p0_20260523T202113_result.json`
- **Structured JSON:** [`8f3aaa37f15e48c203b4.json`](../../sessions/8f/8f3aaa37f15e48c203b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

这些都在 `\begin{comment}` 块和 `%` 注释中（scenario 预写文本，未激活），不影响最终论文输出。无需修改。

---

## 修改报告

### Fix 1 [P0]: 梯度范围过度声称 — **已修复 (3处)**

| 文件 | 修改前 | 修改后 |
|------|--------|--------|
| `main.tex:29` | `while all gradient-flow conditions maintain encoder gradient norms at 0.87--1.14× baseline and CAR within 1.7pp of Vanilla (78.0--79.7%).` | `while Full OCC and Random OCC maintain encoder gradient norms at 0.87--1.14× baseline and CAR within 1.7pp of Vanilla (78.0--79.7%). Depth and Cutoff achieve equivalent behavioral outcomes, consistent with the same mechanism.` |
| `conclusion.tex:5` | `All gradient-flow conditions maintain encoder gradients at 0.87--1.14× baseline and CAR within 1.7pp of Vanilla.` | `Full OCC and Random OCC maintain encoder gradients at 0.87--1.14× baseline and CAR within 1.7pp of Vanilla; Depth and Cutoff achieve equivalent behavioral outcomes, consistent with the same mechanism.` |
| `introduction.tex:11` | `All gradient-flow conditions maintain encoder gradients at 0.87--1.14× baseline and CAR within 1.7pp.` | `Full OCC and Random OCC maintain encoder gradients at 0.87--1.14× baseline and CAR within 1.7pp; Depth and Cutoff achieve equivalent behavioral outcomes, consistent with the same mechanism.` |

`discussion.tex:11` 和 `results.tex:70` 已正确限定为 "structured occupancy and random binary labels" / "Full OCC and Random OCC"，未改。

### Fix 2 [P0]: Dose-response 基线错误 — **已修复**

| 文件 | 修改前 | 修改后 |
|------|--------|--------|
| `results.tex:86` | `The three data points---Detach (0% of steps with gradient flow, CAR 0.746), Cutoff (70%, CAR 0.783), Full OCC (100%, CAR 0.797)---suggest a monotonic dose-response relationship...` | `Three data points---Vanilla (0% of steps with auxiliary gradient flow, CAR 0.780), Cutoff (70%, CAR 0.783), Full OCC (100%, CAR 0.797)---suggest a preliminary monotonic dose-response relationship... Detach is excluded from this curve: its auxiliary head forward pass introduces BatchNorm interference absent from Vanilla... The Detach deficit instead demonstrates that adding an auxiliary head without gradient flow compensation actively harms performance.` |

### Fix 3 [P1]: 术语统一 — **已修复**

| 文件 | 修改前 | 修改后 |
|------|--------|--------|
| `results.tex:14` | `a necessary condition rather than a graded benefit` | `the determining factor for safety preservation rather than a graded benefit` |

### Fix 4 [P2]: 方差倍数 — **无需修改**

`discussion.tex:37` 已经是 `$2.5$--$3.2\times$`，与目标一致。

---
