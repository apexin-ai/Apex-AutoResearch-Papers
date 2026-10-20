# verify a000 threshold ty

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_a000_threshold_ty_20260520T000205_result.json`
- **Structured JSON:** [`f6bda3123df96d38a1c1.json`](../../sessions/f6/f6bda3123df96d38a1c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| 数据源 | threshold_fwd | TY_fwd | naive_fwd |
|--------|-------------|--------|-----------|
| `analysis/5method_leadlag.json` | **3/8** | **1/8** | 6/8 |
| `analysis_mauve/5method_leadlag.json` | **4/8** | **3/8** | 6/8 |

### 对比不一致来源

- **CSV 旧值** (threshold=4/8, TY=2/8) — 与两个文件都不完全匹配。threshold=4/8 匹配 `analysis_mauve/`，但 TY=2/8 两边都不匹配（analysis=1/8, analysis_mauve=3/8）。
- **D111 审计** (threshold=3/8, TY=1/8) — 完全匹配 `analysis/5method_leadlag.json`。

### 两个分析目录的差异根因

`analysis/` 和 `analysis_mauve/` 使用了不同的 threshold 判定逻辑（字段名不同：`canary_onset` vs `onset_canary`），且 threshold onset 检测结果完全相反——`analysis/` 中 token_entropy 作为 canary 全部 onset=None（不显著），ece 有 3 个显著；`analysis_mauve/` 中 token_entropy 有 4 个显著，ece 全部不显著。TY 结果也大幅不同（analysis_mauve 的 TY 对 token_entropy pairs 给出极低 p 值）。

**结论：D111 读取的 `analysis/5method_leadlag.json` 是正确来源，值为 threshold=3/8, TY=1/8。CSV 旧值 (4/8, 2/8) 可能来自 `analysis_mauve/` 的某个旧版本或手工计算错误，与现有两个文件均不完全吻合。**

---
