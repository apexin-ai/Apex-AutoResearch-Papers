# analyze plan019 8b sft s43 eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_plan019_8b_sft_s43_eval_20260519T170951_result.json`
- **Structured JSON:** [`cc882da65ad78f66d434.json`](../../sessions/cc/cc882da65ad78f66d434.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成，结果如下：

```
ign_f1:      0.5324
f1:          0.5457
ign_prec:    0.5319
ign_recall:  0.5330
precision:   0.5550
recall:      0.5367
evi_f1(TP):  0.8333
evi_f1_joint(DREEAM): 0.4430
edcr:        0.5805
format_compliance_rate: 100.0%
n_predictions: 13933
n_truncated: 139/985
wandb_run_id: none
```

**8B SFT 3-seed 统计：**

```
s42 = 0.5128
s43 = 0.5324  ← 本次
s44 = 0.4604

8b_sft_3seed_mean = 0.5019
8b_sft_3seed_std  = 0.0372
```

**对比基准：**

| 配置 | ign_f1 | 对比 |
|------|--------|------|
| 8B SFT 3-seed mean | 0.5019 (±0.0372) | — |
| 1.7B RSFT s42 | 0.5122 | > 8B SFT mean (+0.0103) |
| 8B RSFT mean | 0.5414 | > 8B SFT mean (+0.0395) |

s43 是 3 个 seed 中最高的（0.5324），s44 严重拖低均值。高方差（0.0372）削弱了统计显著性——1.7B RSFT 的 0.5122 落在 8B SFT 的 1σ 范围内（0.5019±0.0372 = [0.4647, 0.5391]）。"1.7B RSFT surpasses 8B SFT" 的 claim 在数值上成立（+0.0103），但需要 1.7B RSFT 多 seed 才能做显著性检验。

---
