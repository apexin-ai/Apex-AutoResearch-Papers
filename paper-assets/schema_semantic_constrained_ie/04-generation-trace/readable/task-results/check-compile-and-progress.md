# check compile and progress

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_compile_and_progress_20260518T163708_result.json`
- **Structured JSON:** [`a9d663b85c83cfe8d922.json`](../../sessions/a9/a9d663b85c83cfe8d922.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. Bib 同步 + 编译

**同步**: 本地 `relwork_new_entries.bib` 比远程多 117 行（3 个已有条目 + 8 个 2026-05-18 新增条目），已追加到 westd-16980 远程文件。`new_citations.bib` 未被 `main.tex` 引用（`\bibliography{relwork_new_entries}` 仅此一个），未同步。

**编译**: **SUCCESS** — 17 pages, 0 bibtex warnings, 0 undefined citations, 0 errors。

**指定 cite key 检查** — 全部已定义：
| Key | 状态 |
|-----|------|
| `boostcd2025` | ✓ (已有) |
| `grammar_aligned_2024` | ✓ (新同步) |
| `formattax2026` | ✓ (新同步) |
| `dccd2026` | ✓ (新同步) |
| `slot2025` | ✓ (新同步) |
| `guidex2025` | ✓ (新同步) |
| `schema_rl2025` | ✓ (新同步) |
| `jsonschemabench2025` | ✓ (新同步) |

Worker 格式 key（`sakota2025boostcd`、`park2024grammaraligned` 等）仅存在于 `new_citations.bib`，但 main.tex 未使用这些 key，所以无影响。

### 2. P8b DocRED Latency (westd-21461)

- **Unconstrained**: 200/200 ✅ 已完成
- **Constrained**: **57/200** 进行中（tmux 活跃，当前 doc 57）
- 平均速度 ~20s/doc
- **预估完成**: 剩余 143 docs × ~20s ≈ **48 分钟后**（~01:30 UTC）

### 3. 70B DocRED (westd-16980)

- **Unconstrained**: **435/998** (cuda:0)
- **Constrained**: **435/998** (cuda:1)
- 两个任务并行运行，启动于 20:48 UTC，已运行 ~3h52m
- 速率 ~112 docs/h
- **预估完成**: 剩余 563 docs / 112 docs/h ≈ **5 小时后**（~05:40 UTC）

---
