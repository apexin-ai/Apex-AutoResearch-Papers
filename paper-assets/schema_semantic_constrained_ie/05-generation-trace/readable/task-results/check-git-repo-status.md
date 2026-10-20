# check git repo status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_git-repo-status_20260526T121345_result.json`
- **Structured JSON:** [`01eebbe356847fd2340c.json`](../../sessions/01/01eebbe356847fd2340c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 服务器连接状态
- **westd-16980**: 连接失败（端口 16980 不通，实例已关机）
- **westd-21461**: 连接失败（端口 21461 不通，实例已关机）

### 2. GitHub 匿名仓库状态

| 项目 | 值 |
|------|----|
| 最新 commit | `7ef1fe4` "Pre-submission cleanup and anonymity verification" |
| 日期 | 2026-05-25 09:06:27 UTC |
| 前一 commit | `e85c3af` "Initial release: OntoCoDec code for anonymous review" (May 23) |
| 文件数 | 34 个文件 |
| 状态 | clean, main 分支 |

### 3. 关键发现

**两台服务器从未有 `.git/` 目录**（May 25 备份记录明确标注）。GitHub 匿名仓库是独立创建的，不是从服务器 push 的。

**GitHub 仓库是精心整理的提交子集**：
- 代码重组到 `compiler/`, `evaluation/`, `experiments/`, `extraction/`, `figures/`, `ontology/`, `utils/` 子目录
- 做了匿名化处理（作者信息 → anonymous）
- **不含** paper/、data/、outputs/、checkpoints/ 等目录

**服务器代码比 GitHub 更完整**（基于 May 25 备份对比）：
- 服务器有 6 个额外 compiler 模块（beam_aware_processor, beam_grammar_processor, type_consensus_processor 等）
- 服务器 run_constrained_extraction.py 包含 EE 支持和 VocabTrimProcessor 等 GitHub 版本没有的功能
- 服务器根目录有 64 个 .py 文件 + scripts/ 下 59 个脚本，GitHub 只收录了其中一部分

### 4. .bib 修复
.bib 修复在本地 `artifacts/_project/paper/` 目录，GitHub 代码仓库不含论文文件，无需同步。

### 5. 结论

**无法确认服务器当前是否有 May 25 之后的改动**（服务器已关机）。GitHub 仓库本身是 May 25 最后更新的，作为匿名审稿代码仓库，它是一个刻意整理的子集，不会也不应该与服务器完全一致。

如需进一步同步，需要先开启服务器。

---
