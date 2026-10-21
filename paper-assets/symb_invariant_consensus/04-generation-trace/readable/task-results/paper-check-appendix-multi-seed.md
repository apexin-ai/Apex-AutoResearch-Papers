# paper check appendix multi seed

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_check-appendix-multi-seed_20260524T112255_result.json`
- **Structured JSON:** [`ed5732d48a02d2c819d3.json`](../../sessions/ed/ed5732d48a02d2c819d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### tab:multi-seed 当前状态

**5 个已完成条件全部有数据**：
| 条件 | Seeds | Δ Range | 状态 |
|------|-------|---------|------|
| Mistral-7B × FOLIO | 3 (123/456/789) | −2.45 to +2.94 | ✓ |
| Qwen2.5-14B × FOLIO | 4 | −2.01 to 0.00 | ✓ |
| Mistral-7B × PW | 4 | −3.33 to −1.33 | ✓ |
| LLaMA-8B × PW | 4 | −7.50 to −4.67 | ✓ |
| Qwen2.5-14B × PW | 4 | −2.50 to −0.83 | ✓ |
| Qwen3-14B × PW | 1/4 (seed42 only) | −0.17 | TBD 占位 |

### Qwen2.5-14B × PW 数据核验

**已存在且 per-seed 数据内部自洽。** 表中 Mean=73.21/71.50/−1.71 是从 per-seed 值精确计算的。memory.md 记录的 73.25/71.62/−1.63 有微小偏差（约 0.04-0.12pp），但表中数据基于 per-seed 行的算术一致性是对的。seed123 SICA=70.83% 已是 alphabetical 修正后的值。

### 具体改动

1. **添加 Qwen3-14B × PW 占位行**（lines 1421-1428）：seed42 填入已知数据 (SC=85.83, SICA=85.67, Δ=−0.17)，seeds 123/456/789 和 Mean 行标记为 *TBD*
2. **Caption** "five" → "six" model×dataset conditions
3. Qwen3 seeds 123/456/789 实验仍为 RUNNING 状态（自 May 23 20:15 UTC 起），结果出来后需补全 TBD 行并更新叙述段

---
