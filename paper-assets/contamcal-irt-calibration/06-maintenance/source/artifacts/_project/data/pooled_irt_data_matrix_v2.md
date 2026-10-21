## Pooled IRT Data Matrix v2 (Fixed) — 2026-05-15

### Bug 修复
- `arc` → `arc_challenge` (JSON 字段名匹配)
- humaneval: `accuracy` → `pass@1` (指标键匹配)

### 覆盖情况（排除 deprecated）
| Benchmark | N_aligned | N_irt |
|-----------|-----------|-------|
| MMLU | 36 | 45 |
| GSM8K | 36 | 46 |
| ARC_challenge | 36 | 45 |
| HumanEval | 36 | 46 |

### Deprecated (6)
- Qwen2.5-1.5B_base_pretrained — base_pretrained 参考基线
- Qwen2.5-3B_d000_s42_v3_aligned — D018 LoRA 超参损伤
- 4× v1 DEPRECATED 目录

### 空目录 (9，正在跑或待跑)
- 0.5B base_pretrained / base_pretrained_aligned / d000_s42_para / raw
- 1.5B d005_s123_aligned / d025_s123_aligned
- 3B d000_s123_aligned / d000_v3_s42_aligned / d005_s42_aligned

CSV: /root/autodl-tmp/exp001/eval_summary_matrix.csv
脚本: /root/contamcal-irt-calibration/scripts/gen_eval_matrix.py