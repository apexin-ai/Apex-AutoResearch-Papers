# fix framing reviewer corrections

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_framing-reviewer-corrections_20260513T073508_result.json`
- **Structured JSON:** [`21ce8f26043aad1b09d8.json`](../../sessions/21/21ce8f26043aad1b09d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 项修正全部完成：

| 修正 | 内容 | 状态 |
|---|---|---|
| **1** | C1 evidence strength: Strong → **Moderate** (single model, single run, n=19-20) | ✅ |
| **2** | FM3 主要证据改为 hgate-dpo003-merged 4-run 数据 (+4.2pp~+10.4pp, mean +7.2pp/+14.3% rel, 4/4 consistent)；mvp-004 降为 auxiliary | ✅ |
| **3** | `anonymous2026expert_persona` → `hu2026expert_persona`（paper_framing.md 4处 + literature_map.yaml 3处） | ✅ |
| **4** | literature_map.yaml 全部 how_we_differ 从 Plan A 改为 Plan B 措辞（21 个条目中 18 个需要更新，已全部完成） | ✅ |
| **5** | FM2 添加 base rate caveat: question_rate baseline=0.044, 52.3% drop 绝对变化仅 ~0.044→~0.021，标注需同时报告绝对值和相对变化 | ✅ |

---
