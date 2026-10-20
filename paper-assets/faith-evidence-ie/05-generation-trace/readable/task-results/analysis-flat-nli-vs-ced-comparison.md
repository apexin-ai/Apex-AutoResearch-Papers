# analysis flat nli vs ced comparison

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_flat_nli_vs_ced_comparison_20260515T232837_result.json`
- **Structured JSON:** [`ca861303399364561a7d.json`](../../sessions/ca/ca861303399364561a7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。脚本已部署到 `rtx5090-4x:/root/autodl-tmp/scripts/seed_comparison.py`。

**当前状态**：
- CED RSFT: 3/3 seeds 就绪 (s42, s43, s44)
- flat-NLI RSFT: 1/3 seeds 就绪 (s42)，s43 re-eval 和 s44 eval 待完成

**Dry-run 结果**（仅 s42 可比）：

| Metric | CED (3-seed) | fNLI (1-seed) | Δ |
|--------|-------------|--------------|---|
| rel_f1 | 0.4610±0.0102 | 0.4539 | -0.0072 |
| evi_f1 | 0.8124±0.0035 | 0.8043 | -0.0081 |
| EDCR | 0.6449±0.0140 | 0.6431 | -0.0019 |

统计检验需 ≥2 matched seeds，当前不足。

**用法**：
```bash
# 一次性报告
python3 /root/autodl-tmp/scripts/seed_comparison.py

# Watch 模式：每 60s 检查新 eval 结果
python3 /root/autodl-tmp/scripts/seed_comparison.py --watch 60
```

输出写到 `/root/autodl-tmp/eval_results/seed_comparison.{md,json}`。

---
