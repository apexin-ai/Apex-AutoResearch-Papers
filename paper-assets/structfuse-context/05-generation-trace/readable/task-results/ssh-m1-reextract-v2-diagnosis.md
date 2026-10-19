# ssh m1 reextract v2 diagnosis

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_m1_reextract_v2_diagnosis_20260513T230543_result.json`
- **Structured JSON:** [`a13fc545e4076b3a50f7.json`](../../sessions/a1/a13fc545e4076b3a50f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已充分，汇总诊断结果。

---

## m1_reextract_v2 诊断报告

### 1. 当前状态：**活跃运行中** ✓

- 启动: 2026-05-14 03:59:08（已运行 ~3h）
- 日志最后写入: 07:06:42，持续输出中
- 配置: 28,276 实例 / 82 repo groups / 4 workers
- 预估总耗时 60h，当前进度 ~15/82 groups

### 2. CodeQL pack 修复：**有效** ✓

- `codeql-pack.lock.yml` 已存在
- **2,469 次** `call_graph` 查询成功
- 新创建的 **15 个 CodeQL DB** 全部正常工作
- 后续所有 repo（cantools → pyparsing）**零失败**

### 3. 残留失败：18 次 WARNING，仅限前 4 个旧 repo

| 失败 query | 涉及 repo | 原因 |
|---|---|---|
| `bounded_dataflow.ql` ×4 | furl, pyasn1, feedparser, python-docx | 复用 v1 旧 DB |
| `call_graph.ql` ×14 | furl, python-docx | 复用 v1 旧 DB |

这 4 个 repo 启动时标记为 `reusing existing CodeQL database`——它们的 DB 是 v1（pack 缺失时期）创建的，格式可能不兼容。代码将失败降级为 WARNING 并继续处理。**04:02 之后零失败**。

### 4. 产出和资源

- `all.jsonl`: 44,173 行（含 v1 数据 + v2 新增）
- `skip_log_rerun.jsonl`: 582 行
- 磁盘: 97GB 可用，充足

### 5. 结论

| 问题 | 状态 |
|---|---|
| v2 运行中？ | ✓ 活跃运行，预计还需 ~13-16h |
| CodeQL pack 修复？ | ✓ 已修复，新建 DB 全部成功 |
| 是否有失败？ | 仅前 4 个旧 DB repo 有 18 次降级 WARNING，不影响整体 |
| 需要干预？ | **不需要**。可选：运行结束后对前 4 个 repo 删除旧 DB 重跑 |

---
