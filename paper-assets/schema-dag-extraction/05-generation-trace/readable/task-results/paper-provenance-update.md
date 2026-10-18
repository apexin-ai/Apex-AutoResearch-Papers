# paper provenance update

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_provenance_update_20260522T104704_result.json`
- **Structured JSON:** [`952116245c9aef5e7ba6.json`](../../sessions/95/952116245c9aef5e7ba6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

YAML valid. All claims now have evidence except C008 (background framing, tier3 by design).

## 报告

**v24 → v25 更新完成**

| 指标 | v24 | v25 |
|------|-----|-----|
| Claims | 39 | 53 |
| Traced (tier2) | 32 | 52 |
| Untraced (tier3) | 10 | 1 |
| Tables | 6 | 6 |
| Figures | 3 | 3 |
| Coverage | 32/42 (76%) | 52/54 (96%) |

### 原 untraced 项处理 (C033-C039, 7 项)

全部映射到 bootstrap/three-way 实验：
- **C033-C035**: 三组回归斜率 → `exp_fewrel_80pool_16sub_bootstrap`, `exp_fewrel_16rel_bootstrap`, `exp_fewrel_formal_80rel`
- **C036-C038**: 三组 extreme-batch Δ → 同上 + `bootstrap_ci_analysis`
- **C039**: permutation tests → `exp_fewrel_16rel_bootstrap` + `exp_fewrel_80pool_16sub_bootstrap`

### 新增 claims (C040-C053, 14 项)

| ID | 内容 | 来源实验 |
|----|------|----------|
| C040 | DocRED count curve + BCS gap 23.3pp | exp_docred_confusability |
| C041 | DocRED IntraSub ρ=0.843 | exp_docred_error_taxonomy |
| C042 | DocRED ridge VIF=50.9, R²=0.594 | exp_docred_confusability (D071) |
| C043 | LLaMA-70B decline -30.7pp, BCS +10.94pp | exp_llama70b_cross_model |
| C044 | Gemini Flash ρ=-0.943, BCS +17.6pp | exp_gemini_flash_cross_model |
| C045 | Few-shot BCS gap widens 18.46→22.79pp | exp_fewshot_bcs_v2 |
| C046 | Schema intervention negative -8.83pp | exp_schema_intervention |
| C047 | Format-independent (p=0.97) | exp_paired_constrained |
| C048 | SDGD-zero MAVEN F1=0.123 | exp_sdgd_zero_maven |
| C049 | BCS range matched eliminates interaction | exp_bcs_range_matched |
| C050 | Prompt sensitivity 7/8 negative | exp_prompt_sensitivity |
| C051 | TOST interaction p=0.285 | exp_fewrel_formal_80rel |
| C052 | FewRel pairwise r=0.187 freq-controlled | exp_fewrel_partial_corr_freq |
| C053 | 25-batch 3-seed replication | exp_d051_count_curves_25 |

### 剩余 tier3

仅 **C008**（background framing statement），无对应实验，保留 tier3。

### 注意

C034 的 r=-0.637 可能是 D039 MEAN 修正前的值，需对照当前论文文本确认是否已更新。

---
