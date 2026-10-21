# code p8 latency overhead

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_p8_latency_overhead_20260518T133749_result.json`
- **Structured JSON:** [`a4d040236222db308bfd.json`](../../sessions/a4/a4d040236222db308bfd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

推理正常，第一个 doc 3.4 秒。按 ~3-5s/doc 估算，551 docs unconstrained 约 30-45 分钟，constrained 可能稍长。总计约 1.5-2 小时完成。

当前状态：
- **P8 实验已启动**，westd-21461 cuda:1
- **Unconstrained 阶段**正在运行，13/551 docs 完成
- 完成 unconstrained 后自动跑 constrained (full_s1)，最后自动运行 `analyze_latency.py` 计算 overhead ratio
- 输出文件：
  - `/root/autodl-tmp/schema_outputs/p8_timing_unconstrained.jsonl`
  - `/root/autodl-tmp/schema_outputs/p8_timing_constrained.jsonl`
  - `/root/autodl-tmp/schema_outputs/p8_latency_report.json`（最终统计）
- Registry: `p8_latency_overhead` → RUNNING

预计 1.5-2 小时后全部完成。需要我定期检查进度还是完成后通知你？

---
