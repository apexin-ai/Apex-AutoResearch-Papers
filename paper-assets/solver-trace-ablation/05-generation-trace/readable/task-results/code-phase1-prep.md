# code phase1 prep

**solver trace ablation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase1_prep_20260513T101441_result.json`
- **Structured JSON:** [`9a521cd96b0bc583763d.json`](../../sessions/9a/9a521cd96b0bc583763d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`quality_percentile` fully removed. Remaining `quality` references are in `property_scorer.py` (scorer still computes quality for analysis, just not used in filtering) and comments — all correct.

完成情况：

**filters.py** — `PGPFStaticFilter` 改为 LC + SN + Confidence 三属性过滤，`quality_percentile` → `confidence_percentile`，`build_filter()` 同步更新。

**config.py** — `quality_percentile` → `confidence_percentile`（默认 50.0）。`num_generations=3`、`real_data_mix_ratio=0.5` 已确认。

**recursive_loop.py** — 四项检查全部通过：单 GPU（`device_map="auto"` + `CUDA_VISIBLE_DEVICES`）、`attention_mask` 显式传递、`del model; torch.cuda.empty_cache()`、批量生成 `batch_size=8`。无需修改。

**run_phase1.py** — 新建。支持 `--condition {5个条件|all}` + `--gpu {0|1}`，每条件独立 seed（42-46），输出 `summary.json` + `comparison.json`（含 degradation = ppl_gen2/ppl_gen0 - 1）。

---
