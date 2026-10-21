# audit abstract dpo crosscheck

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_abstract-dpo-crosscheck_20260523T143733_result.json`
- **Structured JSON:** [`baabdc6d84ac881d2843.json`](../../sessions/ba/baabdc6d84ac881d2843.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here is the full audit report:

---

## 审计项 5: Abstract 数值确认

```
[PASS] 1.7B evidence tax "-5.63pp Ign-F1"
  论文值=-5.63 | 源值=-5.63 (tab:training_tax, matched@2048 s42)
  源路径=appendix.tex:188

[PASS] 4B evidence tax "+0.25±0.47pp"
  论文值=+0.25±0.47 | 源值=+0.25±0.47 (tab:training_tax, 3-seed)
  源路径=appendix.tex:189

[PASS] Cohen's d=2.58 (LLaMA variance compression)
  论文值=2.58 | 源值=2.58 (tab:variance_ci, LLaMA-3.1-8B)
  源路径=appendix.tex:135

[PASS] 1.7B RSFT "51.19 Ign-F1, std 0.09pp"
  论文值=51.19±0.09 | 计算验证:
  s42=51.22 (d102_1_7b_k1_s42, ign_f1=0.51217)
  s43=51.09 (rsft_1_7b_s43_r2_eval, ign_f1=0.51090)
  s44=51.25 (rsft_1_7b_s44_r2_eval, ign_f1=0.51252)
  mean=(51.22+51.09+51.25)/3=51.1867→51.19 ✓
  std=sqrt(0.0145/2)=0.0851→0.09 ✓

[PASS] 8B SFT "50.19, std 3.23pp"
  论文值=50.19±3.23 | 计算验证:
  s42=50.51 (qwen3_8b_sft_eval, ign_f1=0.50512)
  s43=53.24 (8b_sft_s43, ign_f1=0.53245)
  s44=46.81 (plan019_8b_sft_s44_eval, ign_f1=0.46806)
  mean=(50.51+53.24+46.81)/3=50.1867→50.19 ✓
  std=sqrt(20.8293/2)=3.227→3.23 ✓

[PASS] Spearman ρ=1.0 (test-set model ranking)
  Dev RSFT ranking:  14B(58.86)>LLaMA(56.54)>8B(54.33)>1.7B(51.19)>4B(44.82)
  Test RSFT ranking: 14B(38.49)>LLaMA(35.54)>8B(33.53)>1.7B(29.33)>4B(25.01)
  Rankings identical → ρ=1.0 ✓
  源路径=appendix.tex:218 (tab:test_results)

[FAIL] Abstract 字数: ~251 words | EMNLP 2026 限制: 200 words
  超出约 51 words，需大幅精简
```

## 审计项 6: DPO tab:spectrum 追溯

```
[PASS] DPO 1ep Rel-F1
  论文值=33.37 | 源值=33.3745 (f1=0.33374518)
  源路径=/root/autodl-tmp/eval_results/dpo_rebuilt_1ep_eval/metrics.json

[PASS] DPO 1ep Evi-F1
  论文值=80.90 | 源值=80.8964 (evi_f1=0.80896379)
  源路径=同上

[PASS] DPO 1ep EDCR
  论文值=0.8123 | 源值=0.81229 (edcr=0.81228647)
  源路径=同上

[PASS] DPO 3ep Rel-F1
  论文值=31.45 | 源值=31.4464 (f1=0.31446396)
  源路径=/root/autodl-tmp/eval_results/dpo_rebuilt_3ep_eval/metrics.json

[PASS] DPO 3ep Evi-F1
  论文值=84.84 | 源值=84.8379 (evi_f1=0.84837901)
  源路径=同上

[PASS] DPO 3ep EDCR
  论文值=0.7503 | 源值=0.75030 (edcr=0.75029654)
  源路径=同上
```

注：审计规格中预期 DPO 1ep Rel-F1=33.38，但论文和源文件一致为 33.37（33.374... 四舍五入）。

## 审计项 6b: DPO 值跨位置一致性

```
[PASS] tab:spectrum (appendix:332-333) vs 源文件 — 完全一致
[PASS] fig_spectrum 脚本坐标 — 已确认 PASS (先前审计)
[PASS] experiments.tex:46 引用 "33.37→31.45, 80.90→84.84, 0.8123→0.7503" — 与 tab:spectrum 一致
[PASS] analysis.tex — 无具体 DPO 数字引用
[PASS] introduction.tex:18 — 仅定性描述 "DPO progressively trades extraction for evidence"，无数字
```

## 总结

| 审计项 | 结果 |
|--------|------|
| Abstract 6个数值 | 6/6 PASS |
| Abstract 字数 | **FAIL** (251 > 200) |
| DPO tab:spectrum 6个值 | 6/6 PASS |
| DPO 跨位置一致性 | 5/5 PASS |

唯一问题：**Abstract 超字数约 51 words**，需要精简到 200 words 以内才符合 EMNLP 2026 要求。

---
