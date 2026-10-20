# analysis d140 8b sft s42 with evi 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d140_8b_sft_s42_with_evi_2048_20260521T090051_result.json`
- **Structured JSON:** [`763c25a8cdde61b0df3d.json`](../../sessions/76/763c25a8cdde61b0df3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D140 8B SFT with-evidence @2048 结果

| 指标 | @2048 | @1024 基线 | Delta |
|------|-------|-----------|-------|
| **ign_f1** | **0.5012** | 0.4972 | +0.0040 (+0.8%) |
| ign_precision | 0.4690 | — | — |
| ign_recall | 0.5382 | — | — |
| f1 | 0.5219 | — | — |
| evi_f1_joint (DREEAM) | 0.4087 | — | — |
| evi_f1 (TP-only) | 0.8044 | — | — |
| EDCR | 0.7039 | — | — |
| format_ok_rate | 99.9% (984/985) | — | — |
| **truncated** | **236/985 (24.0%)** | 313/985 (31.8%) | **-77 docs (-7.8pp)** |
| predictions | 25,007 | — | — |
| inference_time | 10,486s (2h55m) | — | — |

**路径:**
- adapter: `/root/autodl-tmp/sft_output_qwen3_8b_bf16`
- log: `~/runs/faith-evidence-ie/d140_8b_sft_s42_with_evi_2048.log`
- output_dir: `/root/autodl-tmp/eval_results/d140_8b_sft_s42_with_evi_2048/`

**结论:** @2048 相比 @1024 截断率降低 7.8pp（313→236），但 ign_f1 仅提升 +0.004，收益微弱。多出的 token budget 减少了截断但几乎没有转化为更多正确预测。等 no-evidence @2048 配对实验完成后可做交叉对比。

---
