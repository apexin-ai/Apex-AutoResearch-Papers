# analysis anova table1 compile

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_anova_table1_compile_20260528T073309_result.json`
- **Structured JSON:** [`c33d7867eed33d498015.json`](../../sessions/c3/c33d7867eed33d498015.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

## 完成报告

### Phase 1: Eval 结果
两个 eval 均已完成（westd-34685），结果从 poll logs 提取并写入 registry：
- **full_occ_ln_v2_s3_eval** (Cell 2): **CAR=0.762**, TSR=0.948
- **detach_ln_v2_s3_eval** (Cell 4): **CAR=0.778**, TSR=0.930

### Phase 2: 全量 v2 数据

| Cell | Condition | n | CARs | Mean±SD |
|------|-----------|---|------|---------|
| 1 | Full OCC BN (ON+BN) | 3 | 0.654, 0.746, 0.776 | **0.725±0.064** |
| 2 | Full OCC LN (ON+LN) | 4 | 0.798, 0.792, 0.740, 0.762 | **0.773±0.027** |
| 3 | Detach BN (OFF+BN) | 4 | 0.794, 0.762, 0.736, 0.774 | **0.767±0.024** |
| 4 | Detach LN (OFF+LN) | 3 | 0.802, 0.826, 0.778 | **0.802±0.024** |
| — | Vanilla | 3 | 0.768, 0.748, 0.720 | **0.745±0.024** |

### Phase 3: ANOVA 结果

**2×2 Factorial ANOVA (Type II, N=14):**
| Source | F | df | p | η² |
|--------|---|----|----|-----|
| Gradient flow | 3.20 | 1,10 | 0.104 | 0.180 |
| Norm type | **4.49** | 1,10 | **0.060** | **0.253** |
| Interaction | 0.10 | 1,10 | 0.763 | 0.005 |

- Norm type 主效应接近显著 (p=0.060)，交互效应可忽略
- Cell 4 vs Vanilla: Cohen's d=2.36 (very large), uncorrected p=0.045

### Phase 4 & 5: 论文更新 + PDF 编译
已更新：Abstract、Table 1、Table 2 (factorial)、Results 文本、Appendix (ANOVA table, pairwise d)、Figure caption、stat power section

**PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/_project/paper/main.pdf` (19 pages)

---
