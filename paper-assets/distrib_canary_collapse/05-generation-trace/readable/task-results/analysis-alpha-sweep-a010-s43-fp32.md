# analysis alpha sweep a010 s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a010_s43_fp32_20260519T050246_result.json`
- **Structured JSON:** [`6e5be55a6271a0905e49.json`](../../sessions/6e/6e5be55a6271a0905e49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结果

### Drift (fp32 vs bf16)

| Metric | fp32 s43 | bf16 s43 | 变化 |
|--------|----------|----------|------|
| token_entropy | **-4.49%** | -13.1% | 幅度缩小 ~3x |
| distinct_1 | **-22.08%** | -29.1% | 幅度缩小 |
| distinct_2 | **-23.47%** | -40.3% | 幅度缩小 ~1.7x |
| distinct_3 | **-16.39%** | -31.9% | 幅度缩小 ~2x |
| perplexity | **-18.04%** | -38.9% | 幅度缩小 ~2x |

fp32 将所有 drift 幅度大致减半。

### Lead-lag 检测

| Method | fp32 s43 | bf16 s43 |
|--------|----------|----------|
| perm_granger_fwd | **0/8** | 0/8 |
| perm_granger_rev | **0/8** | 0/8 |
| ty_granger | 6/8 | 0/8 |
| threshold_onset | 4/8 | 3/8 |
| consensus_k4 | 4/8 (名义) | 0/8 |
| **k4 after C003** | **0/8** | 0/8 |

TY 的 6/8 表面上是改善，但 C003 约束指出 alpha<=0.50 时 TY 不可靠（部分 pair 的 df_resid=1）。排除 TY 后，所有 4 个 k=4 的 pair 都降回 k=3，k_gte4 归零。

### 结论

**Canary 盲区在 fp32 精度下仍成立（precision-invariant）：**
- PermG 硬零（0/8），与 bf16 一致
- k_gte4 经 C003 修正后为 0/8，与 bf16 一致
- fp32 减轻了 collapse 的严重程度（drift 约减半），但不改变检测失败的本质

报告和 JSON 已写入 `artifacts/alpha_sweep_a010_s43_fp32/report/`。

---
