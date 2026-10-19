# ops deploy procrustes and run plan012

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy_procrustes_and_run_plan012_20260520T234634_result.json`
- **Structured JSON:** [`ab651fa1bbd75af96c17.json`](../../sessions/ab/ab651fa1bbd75af96c17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

---

## 产出

### 1. transfer_eval.py 部署确认
- `/root/xling_calib_direction/code/transfer_eval.py` ✓ (含 `procrustes_align`, `orthogonal_procrustes`, `n_proj_pairs`)
- `/root/xling_calib_direction/transfer_eval.py` ✓
- `scipy.linalg.orthogonal_procrustes` 导入正常

### 2. CSV 路径
`/root/xling_calib_direction/results/linproj_procrustes_sensitivity.csv` — 280 行数据 (8层 × 5语言 × 7 N值)

### 3. 关键发现

**ΔAUROC 与 N 的关系：**
- N 增大普遍改善 ΔAUROC（std 也缩小）
- 但改善幅度强烈依赖于 **ZS baseline 强度**

**核心模式：Procrustes 效果取决于 ZS AUROC**

| ZS AUROC 范围 | Procrustes 效果 | 典型案例 |
|---|---|---|
| < 0.50 (below chance) | **大幅改善** ΔAUROC +0.10~+0.14 | hi@L8/L12/L16, sw@L12 |
| 0.50~0.55 | 小幅改善 +0.02~+0.06 | ar/ko@L0/L4/L8 |
| > 0.60 | **损害** ΔAUROC -0.01~-0.05 | zh/ar/ko@L20/L24/L27 |

**最大受益者：Hindi**
- Layer 8: ZS=0.43 → Proc=0.57 (ΔAUROC=**+0.14**, N=1000)
- Layer 12: ZS=0.45 → Proc=0.56 (ΔAUROC=+0.12)
- Layer 16: ZS=0.46 → Proc=0.58 (ΔAUROC=+0.12)

**ECE 行为更复杂：**
- 早期层（0, 4, 8）ZS ECE 很差（0.44-0.67），Procrustes 大幅改善 ECE（最大 ΔECE=-0.36@L4 zh）
- 中高层（16-27）ZS ECE 较好（0.25-0.37），Procrustes 反而恶化 ECE

**Swahili 是例外：** 在中高层，Procrustes 几乎对 sw 无效甚至有害（ΔAUROC 始终为负@L16/L20/L27），但在 L8/L12 的 ECE 改善显著

### 4. N 增大是否改善 ΔAUROC？
**是，但有上限**。大多数情况下 N=200→1000 的边际收益递减。对于 ZS>0.60 的层，即使 N=1000 也无法使 ΔAUROC 转正。

---
