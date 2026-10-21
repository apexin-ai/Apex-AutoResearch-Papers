# ops d025 rrf prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d025_rrf_prep_20260516T233433_result.json`
- **Structured JSON:** [`8cb35d24941d2939f4e5.json`](../../sessions/8c/8cb35d24941d2939f4e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

d025 RRF 已完成。结果汇总：

## 输出位置
- **Exposure 格式（IRT 输入）**: `/root/autodl-tmp/exp003/rrf_d025/exposure_scores.json`
- **Aggregated exposure**: `/root/autodl-tmp/exp003/rrf_d025/exposure_aggregated.json`
- **Per-model JSON + CSV**: `/root/autodl-tmp/exp003/rrf_d025/per_model/`（129,773 行）

## 处理的模型（8 个 respondents）

| Model | mmlu | gsm8k | arc_challenge |
|-------|------|-------|---------------|
| Qwen2.5-0.5B_d025_s42 | ✓ | ✓ | ✓ |
| Qwen2.5-0.5B_d025_s123 | ✓ | ✓ | ✓ |
| Qwen2.5-1.5B_d025_s42 | ✓ | ✓ | ✓ |
| Qwen2.5-1.5B_d025_s123 | ✓ | ✓ | ✓ |
| Qwen2.5-3B_d025_v3_s42 | ✓ | ✓ | ✓ |
| Qwen2.5-3B_d025_s123 | ✓ | ✓ | ✓ |
| Llama-3.2-3B_d025_s42 | ✓ | ✓ | ✓ |
| Qwen2.5-3B_d025_s42_old_alpha16 | mmlu only | — | — |

## 注意事项
1. `Qwen2.5-3B_d025_s42_old_alpha16` 是废弃的 alpha16 checkpoint（只有 mmlu），应从 ALPHA16_BLOCKLIST 中加入这个名字或在下游排除
2. Llama-3.2-3B_d025_s42 的 mmlu 是从 individual signal files (s1+s2) 融合的（缺 s4_selfcritique_mmlu），RRF 仅基于 2 个 signal 而非 3 个

## 复现命令
```bash
# Exposure 格式（IRT 用）
/root/miniconda3/bin/python3.12 /root/contamcal-irt-calibration/exp003/rrf_aggregation.py \
  --signal-root /root/autodl-tmp/exp002/signals \
  --dosage-filter d025 \
  --output-dir /root/autodl-tmp/exp003/rrf_d025 \
  --generate-exposure

# Per-model 格式 + CSV
/root/miniconda3/bin/python3.12 /root/contamcal-irt-calibration/exp003/rrf_aggregation.py \
  --signal-root /root/autodl-tmp/exp002/signals \
  --dosage-filter d025 \
  --output-dir /root/autodl-tmp/exp003/rrf_d025/per_model \
  --csv
```

---
