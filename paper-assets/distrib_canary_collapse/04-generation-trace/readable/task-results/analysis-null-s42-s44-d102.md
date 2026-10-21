# analysis null s42 s44 d102

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_null_s42_s44_d102_20260524T164250_result.json`
- **Structured JSON:** [`161257282ac55de7a0a5.json`](../../sessions/16/161257282ac55de7a0a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

## 配置一致性验证

| 参数 | s42 | s43 | s44 | s45-s50 标准 |
|------|-----|-----|-----|-------------|
| model | pythia-410m | pythia-410m | pythia-410m | pythia-410m |
| data_dir | wikitext103_5k | wikitext103_5k | wikitext103_5k | wikitext103_5k |
| steps_per_gen | 5000 | 5000 | 5000 | 5000 |
| num_generations | 10 | 10 | 10 | 10 |
| synthetic_ratio | 0.0 | 0.0 | 0.0 | 0.0 |
| precision | fp32 (默认, bf16=false) | fp32 | fp32 | fp32 |

配置完全一致。s42-s44 目录名无 `_fp32` 后缀但参数等价。

## 6-pair FPR 结果

| Seed | PermG FP (FDR) | K≥3 FP | Max K |
|------|---------------|--------|-------|
| s42 | 0/6 | 0/6 | 2 |
| s43 | 0/6 | 0/6 | 1 |
| s44 | 0/6 | 0/6 | 2 |
| **合计** | **0/18** | **0/18** | - |

**PermG FPR = 0.00, K≥3 FPR = 0.00**

与 8-pair 结果一致（s42-s44 均为 permg=0/8），6-pair ≤ 8-pair 验证通过。

BH-FDR 已按 6 pairs 重新计算（非原 8-pair FDR），consensus voting 遵循 D102 规则（xcorr 需 peak_lag < 0，C009 方向修正）。

Artifact 已注册：`D102_null_s42_s44_fpr.json` (art_20260524_4514c1)

---
