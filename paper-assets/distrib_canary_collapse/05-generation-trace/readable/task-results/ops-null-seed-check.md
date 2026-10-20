# ops null seed check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_null_seed_check_20260524T021631_result.json`
- **Structured JSON:** [`208094dc741aada4925e.json`](../../sessions/20/208094dc741aada4925e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Null seed 实验状态

| Seed | 状态 | Gen 进度 | PermG_fwd (FPR) |
|------|------|----------|-----------------|
| s45  | done (EXIT=0) | 11/11 | **2/6** |
| s47  | done (EXIT=0) | 11/11 | **0/6** |
| s46  | running | 2/11 (gen_1 数据生成中) | — |
| s48  | running | 2/11 (gen_1 数据生成中) | — |
| s49  | running | 2/11 (gen_1 数据生成中) | — |
| s50  | running | 2/11 (gen_1 数据生成中) | — |

**注意：** 服务器上只有 `batch_d102_6pair.py`（6-pair，排除 mauve），没有 `run_5method_analysis_d102.py`。已用 6-pair 版本分析。

### 时间估算

- s45 历史数据：gen_0→gen_10 约 3h34m（~21 min/gen）
- s46-s50 gen_1 开始于 ~02:11 UTC，还有 9 gens 
- **预计完成：~05:30-06:00 UTC**（约 3-3.5 小时后）

### s45 FPR 详情

s45 的 2/6 PermG FPR 来自：
- `token_entropy<distinct_2`: perm_granger sig
- `token_entropy<distinct_3`: perm_granger sig

s47 完全干净（0/6 PermG fwd, 0/6 rev）。

### 下一步

等 s46/48/49/50 完成后运行 D102，汇总 6-seed null FPR。如果 s45 的 2/6 是孤例（其余 5 seed 都是 0/6），则 pooled FPR = 2/36 ≈ 5.6%，接近名义 α=0.05。

---
