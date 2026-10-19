# ops m1 disk cleanup

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_m1-disk-cleanup_20260513T085524_result.json`
- **Structured JSON:** [`6b5376d705e738c2bd4c.json`](../../sessions/6b/6b5376d705e738c2bd4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理结果

| 指标 | 值 |
|------|------|
| 删除 repo 目录数 | 33 个 |
| 释放空间 | ~571 MB |
| 当前磁盘 | 160G/169G used, 9.1G avail, 95% |
| m1_repos/ 剩余 | 20G（17 个目录，全属于 9 个活跃 repo） |
| 风险 | 无。仅删除了已完成提取且非活跃的 repo clone |

**核心问题**：m1_repos/ 仍占 20G，几乎全是活跃 repo 的 CodeQL DB：

| CodeQL DB | 大小 |
|-----------|------|
| cantools | 6.9G |
| paramiko | 4.4G |
| pygments | 3.6G |
| pyasn1 | 1.7G |
| python-docx | 1.4G |
| deepdiff | 917M |
| feedparser | 375M |
| furl | 68M |

这些 DB 在脚本运行期间无法删除。如果需要更多空间，需要等脚本处理完某个 repo 后再逐个清理其 CodeQL DB，或者查看磁盘其他大目录是否有可清理的空间。

---
