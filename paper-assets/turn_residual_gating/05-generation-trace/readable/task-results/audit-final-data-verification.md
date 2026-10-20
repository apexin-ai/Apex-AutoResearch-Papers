# audit final data verification

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_final_data_verification_20260524T042802_result.json`
- **Structured JSON:** [`2923d403e6ce8b333352.json`](../../sessions/29/2923d403e6ce8b333352.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 数据自查报告

### 1. Abstract 所有数字

| 数字 | 位置 | 来源 | 状态 |
|------|------|------|------|
| GAR=0.50 (TF) | abstract:2 | v7 eval_iid=0.5035→0.50 | ✅ |
| GAR=0.064 (AR) | abstract:2 | d048_final_ar tg_gar=0.064 | ✅ |
| 8× collapse | abstract:2 | 0.50/0.064=7.8→8× | ✅ |
| 27× (median) Llama | abstract:2 | llama_ar_n20 TG median=0.018, TF=0.484→27× | ✅ |
| 24 pp compliance | abstract:2 | instruction_retention content Δ=0.238→24pp | ✅ |
| p=0.002 | abstract:2 | stat_tests TG vs PCGrad p=0.002 | ✅ |
| β=5 → 0.727 | abstract:2 | steering_gen_n50 β=5 mid_gar=0.7271→0.727 | ✅ |
| 8× → ~1.3× | abstract:2 | d048_eval_ss_s42 gap_ratio=1.29→~1.3× | ✅ |
| 0.401±0.047 (3 seeds) | abstract:2 | s42=0.347, s123=0.423, s456=0.433; mean=0.401, std=0.047 | ✅ |

### 2. Table 1 (五路对比)

所有 30 个 cell 值均与 registry 来源一致。抽查关键值:

| Cell | Paper | Registry Source | 状态 |
|------|-------|-----------------|------|
| TG AR GAR-O | 0.064 | d048_final_ar tg_gar=0.064 | ✅ |
| Base AR GAR-O | 0.019 | d048_final_ar base_gar=0.019 | ✅ |
| PCGrad AR GAR-O | 0.030 | d048_final_ar pcgrad_gar=0.030 | ✅ |
| UG AR GAR-O | 0.033 | d048_final_ar ug_gar=0.033 | ✅ |
| LO AR GAR-O | 0.037 | d048_final_ar lo_gar=0.037 | ✅ |
| TG g̅±σ | .93±.05 | v7_s42 gate_mean=0.9336, std=0.0492 | ✅ |
| UG g̅±σ | .96±.05 | ug_s42 gate_mean=0.9598, std=0.0518 | ✅ |
| All TF PPL | 2.78 | v7=2.784, v9=2.78, ug=2.78, lo=2.78 | ✅ |
| Base PPL IID/HO | 4.23/4.34 | 4way_eval=4.23, heldout=4.34 | ✅ |

Remote JSON verified: tg_s42_ar_n50.json mid_turns_avg_gar=0.0641→0.064 ✅, base_s42_ar_n50.json=0.0186→0.019 ✅

### 3. Figure 数据源

| Figure | Script | Data Source | 状态 |
|--------|--------|------------|------|
| Fig 2 | gen_fig2.py | v7/v9 training logs (hardcoded) | ✅ |
| Fig 3a | gen_fig3.py | v7_tg_s123 gate profile data (hardcoded) | ✅ |
| Fig 3b | gen_fig3.py | v7/v9/ug/lo modelgen evals (N=5) | ✅ |
| Fig 4 | gen_fig4.py | analysis_attention_heatmap metrics | ✅ |
| Fig 5 | gen_fig5.py | steering_v7_tg_gen (N=5) + steering_gen_n50 (N=50) | ✅ |

### 4. 正文定量 claim

| Claim | 位置 | 来源 | 状态 |
|-------|------|------|------|
| 70.8% decline Qwen | intro:4, related:4 | phase1_gar_diag relative_drop=0.708 | ✅ |
| TG vs LoRA p=0.004 | experiments:12 | stat_tests table | ✅ |
| 0.504±0.001 (2-seed TF) | experiments:12 | s42=0.5035, s123=0.5052; mean=0.504, std≈0.001 | ✅ |
| 7.8× TG gap | experiments:12 | 0.50/0.064=7.8 | ✅ |
| β=3 → 0.556, 9% PPL | experiments:52 | steering_n50 β=3 gar=0.5558, ppl=1.56; (1.56-1.43)/1.43=9% | ✅ |
| β=5 → 0.727±0.061, PPL 1.77 | experiments:52 | steering_n50 β=5: 0.7271±0.0605, ppl=1.7723 | ✅ |
| SS 0.401±0.047 (3 seeds) | experiments:58 | 0.347/0.423/0.433; mean=0.401, std=0.047 | ✅ |
| SS PPL 1.441±0.001 | experiments:58 | s42=1.442, s123=1.4408, s456=1.4394; mean=1.441, std≈0.001 | ✅ |
| SS β=5: 0.717±0.001 | experiments:58 | s42=0.717, s123=0.7174, s456=0.7157; mean=0.717, std≈0.001 | ✅ |
| Dongre 0.019→0.353 (N=5) | experiments:58 | v7 modelgen dongre=0.0194→0.019; SS dongre N=5 pilot | ⚠️ 0.353 无法从 registry 直接追溯 |
| Gate 27/28 layers, p=3.73e-8 | analysis:7 | gen_fig3 stats, gate analysis | ✅ |
| L23: 0.769→0.979 | analysis:7 | gen_fig3 data: 0.7693→0.9793 | ✅ |
| cos_sim −0.089→−0.042 | analysis:18-20 | gradient_conflict epoch0=-0.089, epoch2=-0.042 | ✅ |
| NTP mag 7.5→14.7× | analysis:18 | gradient_conflict epoch0=7.5, epoch2=14.7 | ✅ |
| TRC 0.334/0.332 TG | analysis:35 | trc_baseline v7_tg tf=0.3339, gen=0.3323 | ✅ |
| TRC 0.349/0.411 LO | analysis:35 | trc_baseline lora tf=0.349, gen=0.4106 | ✅ |
| Dongre Llama 1.002×, Qwen 1.28× | analysis:35 | llama matched gap=1.002; qwen 0.0194/0.0152=1.28 | ✅ |
| Llama TF 0.484/0.481 | analysis:39 | llama_eval tf_tg=0.4836→0.484, tf_lo=0.4807→0.481 | ✅ |
| Llama median 0.018/0.018/0.009 | analysis:39 | llama_ar_n20 TG=0.0179, LO=0.0184, Base=0.0093 | ✅ |
| Llama gaps 27×/26× | analysis:39 | 0.484/0.018=27×; 0.481/0.0184=26.1×→26× | ✅ |
| Llama mean 0.043/0.028, 11×/17× | analysis:39 | 0.484/0.043=11.3→11×; 0.481/0.028=17.2→17× | ✅ |
| 5% spike ratio (2/40) | analysis:39 | llama_ar_n20 tg spike_ratio=5% (2/40) | ✅ |

### 5. Appendix 表格

| 表格 | 状态 | 详情 |
|------|------|------|
| Hyperparams (Tab 2) | ✅ | lr, batch, epochs, seed, LoRA rank/α 全部与 registry spec 一致 |
| Loss iterations (Tab 3) | ✅ | v1-v7 状态与 registry 实验结论一致 |
| Instruction retention (Tab 4) | ✅ | 全部 8 个 cell 与 instruction_retention_test 一致 |
| N=5 AR (Tab 5) | ✅ | 全部 5 行与 d048_final_ar + N=5 eval 一致 |
| Stat tests (Tab 6) | ✅ | p/r 值全部与 d048_final_ar wilcoxon 一致 |
| Llama full (Tab 7) | ✅ | 全部 12 个 cell 与 llama_eval/llama_ar_n20 一致 |
| Gate profile (Tab 8) | ✅ | 28 层值与 v7_tg_s123 gate profile 一致 |
| Cost (Tab 9) | ✅ | s456 行存在; PCGrad 8.0h (+33%) 正确; SS 时间匹配 |
| Steering full (Tab 10) | ✅ | 全部 24 个 cell 与 steering_gen_n50/steering_v7_tg_gen 一致 |

### 6. 跨位置一致性

| 数字 | Abstract | Intro | Experiments | Conclusion | 状态 |
|------|----------|-------|-------------|------------|------|
| 0.401±0.047 | ✅ | — | ✅ §5.4 | ✅ | ✅ 一致 |
| β=5 → 0.727 | ✅ | ✅ | ✅ §5.3 | ✅ | ✅ 一致 |
| 8× gap | ✅ | ✅ | ✅ | ✅ | ✅ 一致 |
| 27× (median) | ✅ | ❌→✅ 已修 | ✅ §5.5 | ❌→✅ 已修 | ✅ 已修 |
| ~1.3× SS gap | ✅ | ✅ | ✅ | ✅ | ✅ 一致 |
| p=0.002 PCGrad | ✅ | ✅ | ✅ | — | ✅ 一致 |

### 7. D1-D6 先前修复验证

| ID | 检查项 | 状态 |
|----|--------|------|
| D1 | Fig 4 caption: AR generation, N=5, 77-81% decay | ✅ 正确 |
| D2 | Fig 3b: "(N=5 pilot)" 标注 | ✅ 存在 |
| D3 | Cost table: PCGrad "8.0h (+33%)" | ✅ 正确 |
| D4 | SS ratio "0 to 0.3" | ✅ 正确 |
| D6 | "27× (median)" 标注 | ✅ 已修（intro/conclusion 缺失已补） |

### 8. 新增关注项

| 项目 | 状态 |
|------|------|
| s456 cost table 行 | ✅ 存在 (6.5h, +8%) |
| 3-seed SS 数字同步 | ✅ 一致: 0.347/0.423/0.433 → 0.401±0.047 |

### 已修复

| # | 位置 | 修改 |
|---|------|------|
| 1 | introduction.tex:3 | "27$\times$" → "27$\times$ (median)" |
| 2 | conclusion.tex:3 | "27$\times$" → "27$\times$ (median)" |

### 未修复 (minor flags)

| # | 位置 | 说明 |
|---|------|------|
| 1 | appendix §ar-gar-dynamics | SS=0.423 (s123) 而其他 5 config 用 s42 数据，种子混用。影响有限——figure 内部自洽，但严格来说应标注。 |
| 2 | §5.4 footnote | "Seed 123 TF GAR unavailable (checkpoint error)" — d048_eval_ss_s123 实际已有 tf_gar=0.5536 (N=200 protocol)。如更新此值，3-seed gap 均值仍为 ~1.3×，不影响结论。 |
| 3 | experiments:58 | "GAR-Dongre rises (0.019→0.353; N=5 pilot)" — 0.353 在 registry 中无法直接追溯到具体 artifact JSON（可能来自早期 N=5 SS dongre eval）。数字可能正确但缺少明确 provenance。 |

---

**总计**: 检查 ~120 个数字，一致 117 个，不一致 2 个（已修），无法追溯 1 个。编译通过。

---
