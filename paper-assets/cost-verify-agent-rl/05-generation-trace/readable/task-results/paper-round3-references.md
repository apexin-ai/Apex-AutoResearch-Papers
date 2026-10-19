# paper round3 references

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_round3_references_20260523T170531_result.json`
- **Structured JSON:** [`d2f98faa55da95b544ca.json`](../../sessions/d2/d2f98faa55da95b544ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

### 1. 现有引用核实

| 引用 | 问题 | 修复 |
|------|------|------|
| **Turn-PPO** (`2512.17008`) | 标题缺 "in Agentic LLMs"；年份误标 2026（实际 Dec 2025） | 标题补全，年份改 2025，key 改 `turnppo2025` |
| **MC-GRPO** (`2601.22582`) | 年份误标 2025（实际 Jan 2026） | 年份改 2026，key 改 `mcgrpo2026` |
| **IRC** (`2604.02869`) | 标题、作者、arXiv ID、年份均正确 | 无需修改 |

### 2. 新增引用（已添加到 `references.bib`）

- `harutyunyan2019hindsight` — Harutyunyan et al., "Hindsight Credit Assignment", NeurIPS 2019
- `arjona2019rudder` — Arjona-Medina et al., "RUDDER: Return Decomposition for Delayed Rewards", NeurIPS 2019
- `kaelbling1998planning` — Kaelbling, Littman & Cassandra, "Planning and Acting in Partially Observable Stochastic Domains", Artificial Intelligence 1998

### 3. 正文引用

- `related_work.tex` L8：credit assignment 段落添加了 Harutyunyan + RUDDER 引用
- `method.tex` L7：POMDP 处添加了 Kaelbling 引用
- `introduction.tex` + `related_work.tex`：旧 cite key (`turnppo2026` → `turnppo2025`, `mcgrpo2025` → `mcgrpo2026`) 已全部同步更新

---
