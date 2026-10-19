# fix table6 pending marker

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_table6-pending-marker_20260514T232915_result.json`
- **Structured JSON:** [`3b9705388b5fe16524ab.json`](../../sessions/3b/3b9705388b5fe16524ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 pending recalc 标记已添加，共 **10 处**：

**§4.1（第5行）**
1. `\placeholder{15,133} [pending recalc]` — structural instance count
2. `\placeholder{34.3%} [pending recalc]` — structural coverage rate
3. `\placeholder{65.7%} [pending recalc]` — 无结构数据比例（派生值）

**Table 6 标题（第130行）**
4. 添加 `&lt;!-- PENDING -->` 注释 + caption 加 `[PENDING RECALC]`

**Table 6 数据行（第134-138行）**
5. Small tier: `\placeholder{81.0%} [pending recalc]`
6. Medium tier: `\placeholder{47.2%} [pending recalc]`
7. Large tier: `\placeholder{34.3%} [pending recalc]`
8. XLarge tier: `\placeholder{31.4%} [pending recalc]`
9. Total row: `\placeholder{34.3%} [pending recalc]`

**Table 6 下方叙述段落（第140行）**
10. `\placeholder{104}` / `\placeholder{19}` [pending recalc] — 有/无 structural connectivity 的 repo 数量
11. "Structural coverage [pending recalc]" — 叙述性引用

未修改任何数字，均等待 m1_reextract_v2 完成后由脚本统一重算。

---
