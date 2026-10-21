# audit abstract dpo crosssection

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_abstract-dpo-crosssection_20260523T143606_result.json`
- **Structured JSON:** [`60cecd4df91c5a21aca3.json`](../../sessions/60/60cecd4df91c5a21aca3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到了 d102_1_7b_k1_s42 (ign_f1=0.5122)。现在我有全部数据来编写审计报告。

---

## 审计报告

### 审计项 5: Abstract 数值追溯

```
[PASS] "-5.63pp Ign-F1 at 1.7B"
  值=−5.63 | 来源=appendix tab:training_tax (line 188), dev matched@2048 fair eval
  验证=tab:training_tax Qwen3-1.7B Evi Tax = −5.63, Subset=971/985
  注意: Abstract 未标注 dev/test。此值为 dev training-time tax，非 test（test SFT tax=−4.86, test RSFT tax=−5.43）。
  虽然 traceable，但 abstract 中省略 "dev" 标注可能引起 reviewer 追问。
```

```
[PASS] "+0.25±0.47pp at 4B"
  值=+0.25±0.47 | 来源=appendix tab:training_tax (line 189), 3-seed mean
  验证=tab:training_tax 4B row: +0.25±0.47(3), per-seed range −0.19 to +0.73pp
```

```
[PASS] "Cohen's d=2.58"
  值=2.58 | 来源=appendix tab:variance_ci (line 135), LLaMA-3.1-8B row
  验证=tab:variance_ci LLaMA-3.1-8B Cohen's d = 2.58 ✓
```

```
[PASS] "51.19 Ign-F1, std 0.09pp" (1.7B RSFT 3-seed)
  值=51.19±0.09 | 来源=tab:scaling (experiments.tex line 81)
  验证=SSH 追溯:
    s42: d102_1_7b_k1_s42/metrics.json → ign_f1=0.51217 (51.22)
    s43: rsft_1_7b_s43_r2_eval/metrics.json → ign_f1=0.51090 (51.09)
    s44: rsft_1_7b_s44_r2_eval/metrics.json → ign_f1=0.51252 (51.25)
    mean=(51.22+51.09+51.25)/3=51.19 ✓  std=0.085≈0.09 ✓
  注意: 另有 plan_006 s42 eval 给出 50.50（旧版 eval），paper 未使用。
```

```
[PASS] "50.19, std 3.23pp" (8B SFT 3-seed)
  值=50.19±3.23 | 来源=tab:scaling (experiments.tex line 83)
  验证=SSH 追溯:
    s42: qwen3_8b_sft_eval/metrics.json → ign_f1=0.50512 (50.51)
    s43: 8b_sft_s43/metrics.json → ign_f1=0.53245 (53.24)
    s44: plan019_8b_sft_s44_eval/metrics.json → ign_f1=0.46806 (46.81)
    mean=(50.51+53.24+46.81)/3=50.19 ✓  std=3.23 ✓
```

```
[PASS] "Spearman ρ=1.0"
  值=1.0 | 来源=appendix §generalization_full (line 218)
  验证=text: "model ranking is perfectly preserved (Spearman ρ=1.0; Table tab:test_results)"
  experiments.tex line 110 同值 ✓
```

---

### 审计项 6: DPO matched@2048 追溯

```
[PASS] DPO 1ep: ign_f1=0.3223
  来源=dpo_rebuilt_1ep_eval/metrics.json → ign_f1=0.32231 ✓
  Rel-F1=33.37 (f1=0.33375, ×100=33.37)
  Evi-F1=80.90 (evi_f1=0.80896, ×100=80.90)
  EDCR=0.8123 (edcr=0.81229)
  eval config: max_new_tokens=2048, split=dev, seed=42, quantize=false
  所有4个指标精确匹配论文 tab:spectrum 和 experiments.tex §spectrum
```

```
[PASS] DPO 3ep: ign_f1=0.3076
  来源=dpo_rebuilt_3ep_eval/metrics.json → ign_f1=0.30765 ✓
  Rel-F1=31.45 (f1=0.31446, ×100=31.45)
  Evi-F1=84.84 (evi_f1=0.84838, ×100=84.84)
  EDCR=0.7503 (edcr=0.75030)
  eval config: max_new_tokens=2048, split=dev, seed=42, quantize=false
  所有4个指标精确匹配 ✓
```

```
[NOTE] DPO eval 使用 max_new_tokens=2048，而 tab:spectrum 中 SFT/RSFT 使用 @1024。
  tab:spectrum 未标注不同方法使用不同 eval 协议。
  影响: DPO Rel-F1 在 @2048 下为 33.37，若换 @1024 可能不同
  （paper_table_data.json 的 dpo_ced_1ep_fixed @1024 版 EDCR=0.7139 vs @2048 的 0.8123）。
  建议: 在 tab:spectrum caption 中注明 DPO 数据使用 @2048 eval。
```

---

### 审计项 7: 跨章节一致性

```
[PASS] SFT baseline (4B) Rel-F1/Evi-F1/EDCR
  experiments.tex Tab 1:     Rel-F1=44.39, Evi-F1=79.61, EDCR=0.6797
  method.tex EDCR 示例:      EDCR=0.6797 ✓
  appendix tab:spectrum:     Rel-F1=44.39, Evi-F1=79.61, EDCR=0.6797 ✓
  来源: 3-seed mean (s42=40.49/39.74, s43=44.29/43.65, s44=48.38/47.34 Rel-F1/Ign-F1)
```

```
[PASS] RSFT CED mean — experiments.tex vs appendix tab:ablation_full
  experiments.tex Tab 1: Ign-F1=44.82, Rel-F1=45.80, Evi-F1=80.96, EDCR=0.6487 (3-seed: s42/43/44)
  appendix tab:ablation_full: Ign-F1=44.66, Rel-F1=45.63, Evi-F1=81.15, EDCR=0.6503 (4-seed)
  appendix tab:spectrum: Rel-F1=45.80, Evi-F1=80.96, EDCR=0.6487 (=3-seed) ✓
  差异原因: ablation 用 4-seed mean 含 s45(44.16)，Tab 1 用 3-seed 排除 s45
  ablation 正文 (line 42) 已解释: "The three-seed mean (44.82, seeds 42/43/44) is slightly higher
  because it excludes the lowest seed (s45: 44.16)"
  算术验证:
    3-seed: (44.23+45.12+45.11)/3=44.82 ✓
    4-seed: (44.23+45.12+45.11+44.16)/4=44.66 ✓
```

```
[PASS] DPO 1ep/3ep — experiments.tex vs appendix tab:spectrum
  experiments.tex §spectrum (line 46): 33.37/80.90/0.8123 → 31.45/84.84/0.7503
  appendix tab:spectrum (lines 332-333): 完全一致 ✓
  method.tex: 无 DPO 数值引用，无冲突
```

```
[PASS] 1.7B evidence tax — abstract vs analysis.tex vs appendix
  abstract: "−5.63pp" = dev training-time tax (matched@2048)
  experiments.tex §5.4 (line 59): "−5.63pp; Appendix training_tax" = same ✓
  appendix tab:training_tax (line 188): −5.63 ✓
  appendix tab:test_tax (line 255): −4.86 = test SFT training-time tax (不同指标)
  appendix tab:rsft_test_tax (line 278): −5.43 = test RSFT inference-time tax (不同指标)
  experiments.tex (line 69): "RSFT maintains strong evidence benefit (−5.43pp‡), comparable to SFT (−4.86pp)"
    → −5.43 指向 tab:rsft_test_tax ✓, −4.86 指向 tab:test_tax ✓
  analysis.tex: 无 tax 数值引用
  结论: −5.63 / −4.86 / −5.43 是三个不同指标，各自在正确语境中使用，无矛盾。
```

---

### 汇总

| 审计项 | 子项 | 状态 | 说明 |
|--------|------|------|------|
| 5.1 | −5.63pp 1.7B | PASS | dev tax, 未标 dev |
| 5.2 | +0.25±0.47 4B | PASS | |
| 5.3 | Cohen's d=2.58 | PASS | |
| 5.4 | 51.19±0.09 1.7B RSFT | PASS | 3-seed 精确验证 |
| 5.5 | 50.19±3.23 8B SFT | PASS | 3-seed 精确验证 |
| 5.6 | Spearman ρ=1.0 | PASS | |
| 6.1 | DPO 1ep metrics | PASS | 4 指标精确匹配 |
| 6.2 | DPO 3ep metrics | PASS | 4 指标精确匹配 |
| 7.1 | SFT 4B 跨表 | PASS | |
| 7.2 | RSFT CED mean | PASS | 3-seed vs 4-seed 已解释 |
| 7.3 | DPO 跨表 | PASS | |
| 7.4 | 1.7B tax 跨章节 | PASS | 三个不同指标各自正确 |

### 需关注项（非错误）

1. **DPO eval 协议差异**: tab:spectrum 中 DPO 使用 @2048 eval，而同表 SFT/RSFT 使用 @1024。两者的 Rel-F1 和 EDCR 在不同 token 限制下差异显著（@1024 DPO EDCR=0.7139 vs @2048 EDCR=0.8123）。建议在 table caption 或 footnote 中标注。

2. **Abstract −5.63 缺 dev 标注**: 该值为 dev set training-time tax, 但 abstract 未说明。Test set 对应值为 −4.86（SFT）或 −5.43（RSFT）。虽然可追溯，但 reviewer 可能追问。

3. **1.7B RSFT s42 存在两个不同 eval**: plan_006 版 (50.50) 和 d102 版 (51.22)。论文使用 d102 版。两者均为 @1024，差异可能源于 eval 代码修复（ign_f1 计算方式）。旧版 eval 数据仍在服务器上，可能造成后续混淆。

---
