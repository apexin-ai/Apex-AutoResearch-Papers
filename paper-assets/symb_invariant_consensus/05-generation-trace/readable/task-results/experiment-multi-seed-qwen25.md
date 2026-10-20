# experiment multi seed qwen25

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_multi-seed-qwen25_20260522T032516_result.json`
- **Structured JSON:** [`d785366abf9699e494a4.json`](../../sessions/d7/d785366abf9699e494a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验状态汇总：

**已完成：**
- vLLM Qwen2.5-14B 部署在 cuda:1 port 8002
- seed=42 基线提取完成

**正在运行：**
- Master 脚本 PID=510872 串行运行 6 个实验
- 当前：FOLIO seed=123 — 4/204，~64s/prob，ETA ~3.5h
- 接下来：FOLIO seed=456 → 789 → PW seed=123 → 456 → 789

**seed=42 基线：**

| 条件 | SC | SICA | Δ |
|------|-----|------|---|
| Qwen2.5-14B × FOLIO | 77.5% | 75.5% | -1.96pp |
| Qwen2.5-14B × PW | 73.5% | 71.5% | -2.00pp |

**时间估算：**
- 3 × FOLIO (204题) ≈ 3×3.5h = 10.5h
- 3 × PW (600题) ≈ 3×10.7h = 32h
- 总计 ≈ ~42h，预计全部完成时间约 5/24 凌晨

Master 脚本 log 在 `/tmp/multi_seed_qwen25_master.log`，各 seed 的 log 分别在 `/tmp/qwen25_folio_seed{123,456,789}.log` 和 `/tmp/qwen25_pw_seed{123,456,789}.log`。

需要我定期检查进度吗？

---
