# data bm25 precompute

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_bm25_precompute_20260512T111113_result.json`
- **Structured JSON:** [`1b951246e77f5a92941f.json`](../../sessions/1b/1b951246e77f5a92941f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**10 个 repos 全部处理完毕**，总耗时约 31.5 秒。

| Repo | 文件数 | BM25 Mean ± Std | Max | 耗时 |
|------|--------|-----------------|-----|------|
| black | 286 | 887.9 ± 8974.2 | 442297.0 | 9.6s |
| click | 40 | 831.9 ± 1795.8 | 14010.5 | 0.6s |
| fastapi | 440 | 311.0 ± 1769.1 | 47647.9 | 6.7s |
| flask | 53 | 572.8 ± 1016.5 | 7367.8 | 0.5s |
| httpx | 26 | 636.6 ± 861.0 | 5745.5 | 0.2s |
| pydantic | 192 | 1472.4 ± 2793.6 | 25905.7 | 6.6s |
| pytest | 132 | 1389.9 ± 2320.2 | 26252.3 | 3.8s |
| requests | 27 | 459.2 ± 731.3 | 4359.7 | 0.2s |
| rich | 148 | 566.6 ± 1203.4 | 11217.0 | 2.0s |
| typer | 285 | 138.7 ± 462.0 | 9474.7 | 1.3s |

**产出文件**（均在 `/root/structfuse/mvp_data/bm25/`）：
- 10 个 per-repo JSON：`&lt;repo>_bm25.json`（含文件列表 + top-20 pairwise scores）
- `bm25_all.jsonl`：32,580 条 JSONL 记录
- `bm25_summary.json`：统计摘要

**脚本位置**：`/root/structfuse/extraction/precompute_bm25.py`

**问题**：无。BM25 分数分布高度右偏（std >> mean），符合预期——大部分文件对相关性低，少数高度相关文件对得分极高。black 的 max 异常高（442K），可能由某个超长文件导致。

---
