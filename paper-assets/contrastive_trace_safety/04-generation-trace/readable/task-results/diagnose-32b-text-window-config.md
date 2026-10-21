# diagnose 32b text window config

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_32b_text_window_config_20260517T022011_result.json`
- **Structured JSON:** [`5d8e339b637bc792886c.json`](../../sessions/5d/5d8e339b637bc792886c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本和日志已经完全确认。关键信息如下：

## 结果

`run_bootstrap.py` 中 `MODEL_CONFIGS` 明确定义了每个模型的 window，且 **HS probe 和 Text probe 使用相同的 window**（脚本中 `build_temporal_features` 对 HS 和 Text 都传入同一个 `window` 参数）。

| 模型 | HS probe W | Text probe W | 一致？ |
|------|-----------|-------------|--------|
| R1-8B | 15 | 15 | ✅ |
| **R1-32B** | **10** | **10** | ✅ |
| **QwQ-32B** | **5** | **5** | ✅ |

run.log 也确认了实际执行：
- R1-32B: `Training HS temporal probe (layer_idx=10, W=10)` + `Training Text temporal probe (W=10)`
- QwQ-32B: `Training HS temporal probe (layer_idx=2, W=5)` + `Training Text temporal probe (W=5)`

**结论**：每个模型内部 HS 和 Text 使用了相同的 W，对比条件公平。但三个模型之间 W 不同（15/10/5），这是因为每个模型有不同的最优 window（根据之前的 hyperparameter search）。tab:hs_vs_text 中的对比是 within-model 的，所以这不构成问题。

---
