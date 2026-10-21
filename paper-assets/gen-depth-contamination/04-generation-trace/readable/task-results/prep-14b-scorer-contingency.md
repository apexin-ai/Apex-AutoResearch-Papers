# prep 14b scorer contingency

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_14b_scorer_contingency_20260518T002139_result.json`
- **Structured JSON:** [`405fae0aec138ae06d0e.json`](../../sessions/40/405fae0aec138ae06d0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

准备完成。总结：

**模型**: Qwen2.5-14B-Instruct-AWQ (4-bit, 9.4GB) 已在 `/root/autodl-tmp/.hf_cache/Qwen2.5-14B-Instruct-AWQ/`，加载后占 9.98GB GPU 显存，单张 4090D 轻松容纳。

**脚本**:
- `scripts/score_14b_confound.py` — 加载 AWQ 模型，复用 run_pipeline.py 的 feature extraction + analysis
- `scripts/exp_14b_scorer_confound.sh` — 一键启动，只需确认 `SRC_DATA_DIR` 指向 exp_14b_c4 数据

**Dry-run 验证通过**: 模型加载 9.4s，batch-16 forward 0.08s (5ms/sample)，峰值显存 13.09GB。

**预估运行时间**: ~15-20 min（含 feature extraction + analysis）。

**待**: exp_14b_c4 数据就绪后，执行 `CUDA_VISIBLE_DEVICES=0 bash scripts/exp_14b_scorer_confound.sh` 即可。

报告已写到 `artifacts/14b_scorer_contingency/prep_report.md`。

---
