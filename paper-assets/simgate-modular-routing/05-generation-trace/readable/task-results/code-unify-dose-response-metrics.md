# code unify dose response metrics

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_unify-dose-response-metrics_20260518T171302_result.json`
- **Structured JSON:** [`700c7c935502e61c69f9.json`](../../sessions/70/700c7c935502e61c69f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。结果：

- `--help` 正常输出
- `--test` dry-run 验证通过：
  - Wilson CI 100/200 → DR=0.5000, CI=[0.4314, 0.5686] ✓
  - 边界情况 0/0、0/100 ✓
  - Retry DR 基本平稳（低 improvement）；Reflexion DR 从 0.55 降到 0.11（高 improvement）✓
  - Cross-validation mock 输出正确 ✓
  - JSON 已保存到 `analysis/unified_dose_response_data.json`

脚本位于 `westd-18266:/root/autodl-tmp/simgate-modular-routing/analysis/unify_dose_response_metrics.py`，数据到位后用 `--retry-dir` / `--reflexion-dir` 指定路径即可一键运行。

---
