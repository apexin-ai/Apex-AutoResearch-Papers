# code shard merge prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_shard-merge-prep_20260516T050024_result.json`
- **Structured JSON:** [`a8ecbedea7d530120c99.json`](../../sessions/a8/a8ecbedea7d530120c99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完成，脚本正常工作。当前状态：

**合并结果：9592 / 9784，缺 192 个 index**（从 7488 开始的连续区间），说明 shard 还没跑完。

各 shard 贡献：
| Shard | 行数 | 去重后保留 |
|-------|------|-----------|
| v3 | 7488 | 6256 |
| shard2 | 1872 | 1416 |
| shard3 | 1232 | 1232 |
| shard4 | 688 | 688 |

当前指标（不完整，仅供参考）：
- Overall accuracy: 65.15% (unparseable→pass)
- Unparseable rate: 73.81%
- Parseable-only accuracy: 38.61%

脚本已部署到远程 `/home/sonny/exec-sim-repair-verifier/merge_cwm8b_shards.py`，等 shard 全部跑完后执行 `python merge_cwm8b_shards.py`（不加 `--dry-run`）即可输出合并 JSONL 和 metrics.json。

---
