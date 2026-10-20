# research ref audit A

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-audit-A_20260526T101518_result.json`
- **Structured JSON:** [`e5e3577196e1a5d2c104.json`](../../sessions/e5/e5e3577196e1a5d2c104.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审核报告已写入 `artifacts/ref-audit/audit_worker_A.md`。

**核查结果汇总：**

- 68 条全部为真实论文，**0 篇幻觉引用**
- **5 条严重错误（必须修正）：**
  1. **toolace-2025** — 第一作者姓氏错误："Zhang, Weiwen" → "Liu, Weiwen"
  2. **amitai2024explaining** — 第二作者名字错误："Guy Septon" → "Yael Septon"
  3. **reflexion-2023** — 遗漏第三作者 Edward Berman
  4. **agent-safetybench-2024** — 作者列表严重错误：含 2 名虚构作者、2 名错名，从 7 人膨胀为 9 人
  5. **automix-2024** — 作者列表严重错误：多人姓名错误、含非作者 "Niket Tandon"、遗漏 7+ 共同作者
- **6 条 Minor 问题**（作者顺序、标题缩写、venue 未更新等）
- **2 处正文引用上下文描述不够精确**（axis-2026 和 cso-2026 在 related_work.tex 中的描述与论文实际内容有偏差）

---
