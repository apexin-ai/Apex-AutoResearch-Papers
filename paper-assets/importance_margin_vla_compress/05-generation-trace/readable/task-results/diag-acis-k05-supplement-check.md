# diag acis k05 supplement check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_acis_k05_supplement_check_20260518T150310_result.json`
- **Structured JSON:** [`314509743febdf5ceb85.json`](../../sessions/31/314509743febdf5ceb85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

---

## 汇报

### 第一部分：eval_acis_k05_supplement_200eps

**状态：已完成** (EXIT_CODE=0)，GPU 1 已空闲。

**结果与预期严重不符。** 预期全 0% SR，实际 overall 47.5%：

| Task | Description | SR |
|------|-------------|-----|
| 6 | pick up the butter and place it in the basket | **48%** (24/50) |
| 7 | pick up the milk and place it in the basket | **40%** (20/50) |
| 8 | pick up the chocolate pudding and place it in the basket | **64%** (32/50) |
| 9 | pick up the orange juice and place it in the basket | **38%** (19/50) |
| **Overall** | | **47.5%** (95/200), 95% CI [40.7%, 54.4%] |

ACIS k=0.5 zero_mask pruning 并没有摧毁 task 能力。Registry 已更新：conclusion=negative，metrics 已填入。

### 第二部分：Fig 2 PDF

`degradation_curve.pdf` 确认存在：
- 大小：30,268 bytes (~30KB)
- 时间戳：May 18 22:13（约 50 分钟前）

符合预期（三曲线版本，~30KB，时间戳近期）。

---
