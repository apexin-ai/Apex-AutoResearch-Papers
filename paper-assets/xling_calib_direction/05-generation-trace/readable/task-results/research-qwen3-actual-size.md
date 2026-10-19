# research qwen3 actual size

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_qwen3_actual_size_20260521T013319_result.json`
- **Structured JSON:** [`b82dcbedecf56363ab22.json`](../../sessions/b8/b82dcbedecf56363ab22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已确认，结果写入 `artifacts/qwen3_size_check.md`。

**核心结论**：

- **实际权重大小：~125 GB**（32 个 safetensors 分片，30 个 ~4GB + 1 个 3.31GB + 1 个 1.24GB）
- **之前估的 208 GB 不准确**，可能是下载中途统计、混合了其他 cache、或 du 参数问题
- HF cache 不会真正翻倍（snapshots 是软链接），但用 `--local-dir` 下载最干净，实际需要 ~130 GB 磁盘空间

---
