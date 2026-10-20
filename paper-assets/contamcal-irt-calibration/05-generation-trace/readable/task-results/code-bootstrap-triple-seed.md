# code bootstrap triple seed

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bootstrap-triple-seed_20260520T121153_result.json`
- **Structured JSON:** [`7551c2b4d50d75569d8b.json`](../../sessions/75/7551c2b4d50d75569d8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

交付总结：

**脚本**: `/root/contamcal-irt-calibration/analysis/bootstrap_triple_seed.py` (583 行)

**Dry-run 结果**:

| 测试 | 状态 |
|------|------|
| `--seeds 42`: 发现 25/25 文件 (5 家族 × 5 dosage) | 通过 |
| n=1 退化为 point estimate，无 bootstrap 报错 | 通过 |
| `--seeds 42,123,0`: 发现 35/75 文件，OLMo-2 有 3 seeds | 通过 |
| OLMo-2 三种子 bootstrap CI 正常计算 (Δd100: +1.35pp [-0.55, +2.60], p=0.039) | 通过 |
| OLMo-2 Spearman ρ 计算 (3 pairs, mean=0.033) | 通过 |
| Pattern 分类: Phi-4=Immune, Qwen14B=U-collapse, Qwen7B=V-recovery, Gemma/OLMo=Benefit-sat | 通过 |
| OLMo-2 跨种子不一致 (s42=Benefit-sat, s123=Immune, s0=Benefit-sat) 正确标记 No | 通过 |
| LaTeX table 语法正确 | 通过 |
| 输出文件: `bootstrap_results.txt` + `bootstrap_table.tex` | 通过 |

**数据来源**: s42 从 `analysis/results/gsm8k/mmlu_summary.csv` 读取；s123/s0 从 `results/mmlu_eval/{family}/d{dosage}_s{seed}/mmlu_results.json` 读取。两种格式自动合并，JSON 优先于 CSV。

---
