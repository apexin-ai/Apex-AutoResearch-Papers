# analysis post a075 analysis prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_post_a075_analysis_prep_20260515T075714_result.json`
- **Structured JSON:** [`9f887c4d378116f6ac1f.json`](../../sessions/9f/9f887c4d378116f6ac1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

准备文档已写入 `artifacts/a075_analysis_prep.md`。

汇总：
- **已完成 α 点**：a000_s42, a025_s42, a050_s42 各有完整 gen_0–gen_10 + all_metrics.json
- **a075 进度**：gen_0–gen_3 完成，gen_4 正在跑，约 36%（4/11 generations），还剩 7 个 generation
- **分析脚本**：`cross_alpha_analysis.py` 存在，支持 `--alpha-dirs`, `--n-perms`, `--update-registry`
- **完成后一键执行**：

```bash
cd /root/autodl-tmp/distrib_canary_collapse && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
python cross_alpha_analysis.py \
  --alpha-dirs a000_s42 a025_s42 a050_s42 a075_s42 \
  --n-perms 5000 \
  --update-registry
```

产出写到 `results/analysis/cross_alpha_v{N}.json`。

---
