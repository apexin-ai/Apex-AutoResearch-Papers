# audit plan 001b data completeness

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_plan-001b-data-completeness_20260514T040936_result.json`
- **Structured JSON:** [`4f9f364f133ca1c7014f.json`](../../sessions/4f/4f9f364f133ca1c7014f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是 plan-001b 全部 task 的数据状态：

## plan-001b 数据审计结果

**数据目录**: `/root/autodl-tmp/simgate-modular-routing/results/plan_c/`

| Task | Episodes | 文件大小 | 目标 | 状态 |
|------|----------|----------|------|------|
| find-non-living-thing | 40 | 429K | 40 | ✅ |
| grow-fruit | 20 | 197K | 20 | ✅ |
| inclined-plane-determine-angle | 20 | 191K | 20 | ✅ |
| identify-life-stages-2 | 20 | 194K | 20 | ✅ |
| find-animal | 20 | 198K | 20 | ✅ |
| identify-life-stages-1 | 20 | 197K | 20 | ✅ |
| lifespan-longest-lived-then-shortest-lived | 20 | 199K | 20 | ✅ |
| measure-melting-point-unknown-substance | 20 | 190K | 20 | ✅ |
| freeze | **17** | 1.1M | 20 | ❌ 缺 3 eps |
| lifespan-longest-lived | **wc -l 超时** | **150GB** | 20 | ❌ 文件损坏 |
| chemistry-mix | 目录不存在 | — | 20 | ❌ 未收集 |

## 关键发现

**8/11 tasks 已完成**（包括之前认为"需确认"的 find-animal、identify-life-stages-1、lifespan-longest-lived-then-shortest-lived，实际都已有 20 eps 完整数据）。

**3 个未完成 task：**

1. **lifespan-longest-lived** — 150GB 异常文件（正常约 200KB），是正常大小的 ~75 万倍。创建于今天 09:10，最后修改 12:11，当前已停止增长。该文件独占数据盘 150GB/250GB（60%），磁盘用量 73%。**需要删除并重新收集。**

2. **freeze** — 17/20 eps，缺 3 eps。文件大小 1.1M（比其他 task 大，可能 freeze episodes 内容更长），但不完整。

3. **chemistry-mix** — plan_c 目录下完全没有此 task。prescreening 里有 5 eps，但不属于 plan-001b 数据路径。**需要从头收集 20 eps。**

**measure-melting-point-unknown-substance 已完成** — 已有 20 eps（190K），不需要当前 GPU0 v5 再收集。

---
