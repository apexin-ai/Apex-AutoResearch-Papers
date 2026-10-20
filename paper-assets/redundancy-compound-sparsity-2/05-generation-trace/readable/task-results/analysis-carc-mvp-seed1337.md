# analysis carc mvp seed1337

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_carc_mvp_seed1337_20260512T111612_result.json`
- **Structured JSON:** [`b23b6e11a8f635529631.json`](../../sessions/b2/b23b6e11a8f635529631.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## CARC MVP seed1337 结果：**FAIL**

### 全局判定

| 条件 | 阈值 | 实际值 | 通过? |
|------|------|--------|-------|
| \|r(EMA, perturbation)\| | ≥ 0.4 | 0.113 | ✗ |
| perturbation diff | ≥ 10% | 5.26% | ✗ |

2×2 矩阵：两个条件均不满足 → **FAIL**

### 核心发现：两个信号在层间空间解耦

- **高相关层** (L30, L31, L33): |r| ≈ 0.40，但 perturbation diff 仅 2.5%~6.7%
- **高扰动差异层** (L41-45): diff 11%~21%，但 |r| 仅 0.21~0.32
- **没有任何单层同时满足两个条件**

### 其他指标
- PPL two-tier vs uniform: 均为 1.38，无差异
- EMA-surprisal 相关: r=0.1255（弱）
- Near-zero frac ratio: 1.16x（redundant 稍高，方向正确但效应微弱）
- 无 W&B run，无 seed42 对比

### 已注册
- Registry: `carc_mvp_seed1337` → DONE, conclusion=negative
- Artifact: `carc_mvp_seed1337_analysis.md`
- Memory: 更新完毕

---
