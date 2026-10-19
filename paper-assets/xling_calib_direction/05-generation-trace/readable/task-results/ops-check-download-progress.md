# ops check download progress

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-download-progress_20260521T045051_result.json`
- **Structured JSON:** [`5d3674e0524460705212.json`](../../sessions/5d/5d3674e0524460705212.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

```
45G     /root/autodl-tmp/models/Llama4-Scout-W4A16/
.incomplete 文件数: 7

22G     /root/autodl-tmp/models/Qwen3-235B-GPTQ-Int4/
.incomplete 文件数: 16

Filesystem      Size  Used Avail Use% Mounted on
/dev/md0        350G  155G  196G  45% /root/autodl-tmp
```

两个模型都还在下载中。Llama4-Scout-W4A16 已下载 45G（剩 7 个 incomplete 分片），Qwen3-235B-GPTQ-Int4 已下载 22G（剩 16 个 incomplete 分片），磁盘剩余 196G。

---
