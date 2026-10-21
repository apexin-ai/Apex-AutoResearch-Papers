# run exp001 auroc evaluation

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp001_auroc_evaluation_20260518T113345_result.json`
- **Structured JSON:** [`5240e06d804ea9772448.json`](../../sessions/52/5240e06d804ea9772448.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## EXP-001 扩展数据 AUROC 评估 — 完整结果

### 0. Ground Truth 校验
- 原始 200 pairs，LLM 校验发现 **19 pairs 存在 GT 错误**（9.5%），已移除
- 最终保留 **181 pairs**（362 条记录），domain 分布：math 34, science 37, geography 38, history 35, commonsense 37

### 1. 5-Fold Stratified CV

| Fold | Test Pairs | Best AUROC | Best Layer | Position | L0 AUROC |
|------|-----------|------------|------------|----------|----------|
| 0 | 37 | 0.8189 | L21 | asst_first | 0.5391 |
| 1 | 36 | 0.8056 | L19 | asst_first | 0.5556 |
| 2 | 36 | 0.8565 | L19 | asst_first | 0.5440 |
| 3 | 36 | 0.8619 | L32 | asst_first | 0.5293 |
| 4 | 36 | 0.7917 | L35 | asst_first | 0.5054 |

**Mean AUROC: 0.8269 ± 0.0278**

### 2. Bootstrap 95% CI (full data)
- Best layer: L19, position: asst_first
- AUROC = **0.8159**, 95% CI [**0.7698**, **0.8576**]

### 3. V2 → Expanded Transfer
- v2 directions applied to expanded data: AUROC = **0.7989** (L27, asst_first)
- L0 baseline: 0.5190
- Delta: +0.2799

### 4. Layer 0 Baseline
- 所有 fold 的 L0 AUROC 在 0.50-0.56 范围，接近随机（符合预期，浅层无区分力）

### 5. STOP-GATE 判定

**PASS** ✓ (mean CV AUROC 0.8269 ≥ 0.80 threshold)

关键观察：
- 所有 fold 一致选择 **asst_first** position，信号集中在中深层 (L19-L35)
- Bootstrap CI 下界 0.77，上界 0.86，置信区间不跨 0.80 很远但 mean 稳过线
- V2 directions 迁移到扩展数据 AUROC=0.80，说明方向向量具有一定泛化性，但不如重新训练（0.83 vs 0.80）

---
