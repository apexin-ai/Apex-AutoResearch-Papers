# ops provenance fix p0p1p2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_provenance-fix-p0p1p2_20260516T050611_result.json`
- **Structured JSON:** [`e61144d7a0da49c8ae9e.json`](../../sessions/e6/e61144d7a0da49c8ae9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修复完成：

- **P0**: C132(regex baseline), C133/C134/C135(DebugBench 三条独立 claim), C136(trace length ablation) 已添加；tab:regex_baseline, tab:debugbench, tab:trace_length 新建；tab:cross_model 已含 full_trace/DeepSeek=79.16%
- **P1**: C029 文本更新为 "VOTA_no_ae 99.40% ≈ VOTA 99.41% (statistically equivalent)"；tab:ablation VOTA_no_ae 确认为 99.40%
- **P2**: C092/C120 均已指向 deepseek_full_trace_seed42_v3 (0.7916), deprecated=false

`check_provenance_completeness` 工具有内部 bug（unhashable dict），但 YAML 经独立验证结构正确、所有值与 registry 精确匹配。

---
