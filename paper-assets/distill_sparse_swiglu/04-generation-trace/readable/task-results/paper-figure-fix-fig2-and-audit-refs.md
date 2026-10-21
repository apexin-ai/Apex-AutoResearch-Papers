# paper figure fix fig2 and audit refs

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fix_fig2_and_audit_refs_20260515T233926_result.json`
- **Structured JSON:** [`1e826fec762b9f3ce149.json`](../../sessions/1e/1e826fec762b9f3ce149.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. fig2 重新生成 ✓
- `figures/paper/gen_fig2.py` 中 28.5% 数据点已从 8.76 修正为 **8.98**
- PDF 和 PNG 已重新生成，`artifacts/_project/chart/` 副本已同步

### 2. TEAL baseline 补充
- **50%**: 23.31 — 已有 ✓
- **70%**: 17.91 — **新增** ✓（来自 kl_sparsity70_s42_v2 的 teal_sparse_ppl_static_baseline）
- **28.5%**: **无数据**，未补充
- TEAL 两点用虚线连接，70% 处 TEAL=KL=17.91（重合），50% 处 Δ=11.31

### 3. 8.76 引用审计
全量搜索结果——`gen_fig2.py` 是唯一需要修改的文件，已修复。其余引用均为保留旧值的历史记录，无需改动：

| 文件 | 性质 | 操作 |
|------|------|------|
| `figures/paper/gen_fig2.py:29` | 数据点 | ✅ 已修正为 8.98 |
| `registry.yaml:1996` | `teal_sparse_ppl_old_wrong_target: 8.76` | 保留（显式标记旧错误值） |
| `registry.yaml:1997,2011` | 注释说明旧值来源 | 保留 |
| `decisions.yaml:271,273` | 决策记录（记录发现问题的过程） | 保留 |
| `logs/workers/*` | Worker 执行日志 | 不可变历史记录 |

---
