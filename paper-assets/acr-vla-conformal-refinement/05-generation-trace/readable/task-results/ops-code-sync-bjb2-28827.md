# ops code sync bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_code-sync-bjb2-28827_20260521T185321_result.json`
- **Structured JSON:** [`5b17d84dab623c0577f2.json`](../../sessions/5b/5b17d84dab623c0577f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**memory.md 记录已过时**——bjb2-28827 的 evaluate.py 已经是最新版本，不需要 git pull。

| 服务器 | evaluate.py 大小 | md5 | git HEAD | mtime |
|--------|---------|-----|----------|-------|
| bjb2-28827 | 33058 | `29b6b00c...` | `8a50cef` (adaptive_k mode with K2 L2 threshold trigger) | 2026-05-21 23:50:13 |
| bjb1-32546 | 33058 | `29b6b00c...` | 非 git 仓库 | 2026-05-21 23:49:20 |
| bjb2-40593 | 33058 | `29b6b00c...` | `9130bf3` (--mode adaptive_k with K2 L2 threshold-based adaptive inference) | 2026-05-21 23:50:28 |

- 三台服务器的 `src/evaluate.py` 工作区内容**完全一致**
- bjb2-28827 import 验证通过（需 `conda activate base`）
- bjb2-28827 和 bjb2-40593 的 evaluate.py 都是未提交的本地修改（git status `M src/evaluate.py`），但两边工作区内容已同步
- bjb1-32546 的 `/root/acr-vla-conformal-refinement` 不是 git 仓库（仅有文件，无 `.git`）
- 可以直接在 bjb2-28827 部署 π0.5 CRM eval (runs 3-4)

建议把 memory.md 中关于 bjb2-28827 evaluate.py 旧版本的记录更新掉。

---
