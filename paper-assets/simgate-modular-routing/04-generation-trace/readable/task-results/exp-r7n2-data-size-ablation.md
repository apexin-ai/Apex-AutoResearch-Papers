# exp r7n2 data size ablation

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_r7n2-data-size-ablation_20260516T005713_result.json`
- **Structured JSON:** [`3af86909de90071bbbb5.json`](../../sessions/3a/3af86909de90071bbbb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行中。Scale 25pct / seed 42: 进度 2/42 steps (~1.3s/it)。

7 scales × 3 seeds = 21 次训练，预计 2-3 小时完成。任务已提交:

- **exp_id**: `r7n2-data-size-ablation`
- **服务器**: westb-13313, GPU 0
- **tmux session**: `r7n2-data-size-ablation`
- **日志**: `~/runs/simgate-modular-routing/r7n2-data-size-ablation.log`
- **输出**: `results/ablation_data_size/summary.json`
- **配置**: 7 scales (25%-800%) × 3 seeds (42/43/44), Qwen3-1.7B LoRA r=16, lr=2e-5, epochs=3, effective_batch=32

完成后需检查 `summary.json` 中各 scale 的 balanced_acc mean±std，确认 100% 后是否饱和（improvement < 1pp）。

---
