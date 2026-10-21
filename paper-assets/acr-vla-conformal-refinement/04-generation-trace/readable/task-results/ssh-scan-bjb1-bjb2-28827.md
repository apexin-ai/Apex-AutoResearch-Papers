# ssh scan bjb1 bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_scan-bjb1-bjb2-28827_20260523T233833_result.json`
- **Structured JSON:** [`c920ea320e53d1cb7ed6.json`](../../sessions/c9/c920ea320e53d1cb7ed6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

adapt-tau025-obj-s45 已在 registry 中标记为 DONE。所有 GPU 均在忙，无空闲 GPU 可部署新实验。

---

## 扫描报告

### 收割结果
| 实验 | SR | 状态 |
|------|-----|------|
| eval-supp-crm-obj-s46 (Object CRM s46) | **79.5%** | 刚收割 DONE |
| eval-supp-adapt-tau025-obj-s45 (Object Adapt s45) | **78.0%** | 已在 registry DONE |

### bjb1-32546 — 6/6 GPU 占满

| GPU | 实验 | 进度 | 预计剩余 |
|-----|------|------|----------|
| cuda:0 | Spatial K2mean s46 | 1/10 tasks | ~4-5h |
| cuda:1 | Long VLA s45 | 8/10 tasks | **~1h** (最快释放) |
| cuda:2 | Long Adapt s45 | 7/10 tasks | ~1.5h |
| cuda:3 | Long CRM s45 | 7/10 tasks | ~1.5h |
| cuda:4 | Long Reconvla s45 | 7/10 tasks | ~1.5h |
| cuda:5 | Obj Reconvla s45 | 4/10 tasks | ~3h |

### bjb2-28827 — 6/6 GPU 占满

| GPU | 实验 | 进度 | 预计剩余 |
|-----|------|------|----------|
| cuda:0 | Goal VLA s46 | 3/10 tasks | ~5h |
| cuda:1 | Goal K2mean s46 | 2/10 tasks | ~5-6h |
| cuda:2 | Goal Reconvla s46 | 2/10 tasks | ~5-6h |
| cuda:3 | Goal CRM s46 | 2/10 tasks | ~5-6h |
| cuda:4 | Long K2mean s45 | 6/10 tasks | **~2-3h** |
| cuda:5 | Goal Adapt s46 | 2/10 tasks | ~5-6h |

### 部署计划（等 GPU 释放）

**bjb1 最快释放顺序**：cuda:1 (~1h) → cuda:2/3/4 (~1.5h) → cuda:5 (~3h) → cuda:0 (~5h)

释放后按优先级部署：
1. cuda:1 释放 → Object VLA-only s46
2. cuda:2 释放 → Object Adaptive s46
3. cuda:3 释放 → Spatial VLA-only s46
4. cuda:4 释放 → Spatial CRM s46
5. cuda:5 释放 → Spatial Reconvla s46

**bjb2 最快释放**：cuda:4 (~2-3h) → 部署 Long VLA-only s46

当前无法部署。建议 1-2h 后重新扫描收割 Long s45 实验。

---
