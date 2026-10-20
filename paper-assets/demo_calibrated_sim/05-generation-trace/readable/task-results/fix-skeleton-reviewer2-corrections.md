# fix skeleton reviewer2 corrections

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_skeleton-reviewer2-corrections_20260513T082220_result.json`
- **Structured JSON:** [`a3baeebd86dd0123f963.json`](../../sessions/a3/a3baeebd86dd0123f963.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修正完成。总结：

| 修正项 | 改动 |
|--------|------|
| **硬伤 1: LoRA 引用** | `\cite{rafailov2023dpo}` → `\cite{hu2021lora}`，`literature_map.yaml` 新增 `hu2021lora` 条目 |
| **硬伤 2: DPO pair 数量** | 1,563 确认正确（服务器 `dpo_pairs_v2.jsonl` = 1563 行，`max_steps=1173` = `ceil(1563/4)*3`）；数据源从 `[dpo-002, dpo-003]` 改为 `[aave-corpus-gen]` |
| **建议 3: Table 2 格式** | per-run 原始值改为 mean±SD（aave: $-23.3±23.4$, indian: $-21.9±19.3$, overcorrected: $-18.0±7.5$），加脚注 "See Appendix for per-run breakdown" |
| **建议 4: 18-turn** | "18-turn task" → "multi-turn task episode"（服务器无 turn 数日志） |
| **建议 5: mvp-003** | "precision-validated in mvp-003" → "precision-validated on a held-out annotation set" |

`artifacts/` 和 `artifacts/_project/paper/` 两份副本均已同步修改。

---
