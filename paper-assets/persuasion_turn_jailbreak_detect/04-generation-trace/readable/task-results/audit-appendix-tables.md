# audit appendix tables

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_appendix-tables_20260523T104152_result.json`
- **Structured JSON:** [`7bbbcffb7cda832551af.json`](../../sessions/7b/7bbbcffb7cda832551af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。~80项数字交叉验证结果：

- **0项不一致**
- **73项完全一致**
- **7项需注意**（均为低-中严重度的记录完整性问题）

主要注意项：
1. **效率表 latency std ±1.2**：exp29 无 std 记录，exp46 std=1.61（不同硬件），来源不明
2. **Qwen3-8B ~5,200 ms**：exp10 registry 无 latency 数据，无法验证
3. **Ensemble 表 MLM AA single=.897**：seed-level 均值计算为 .893，差 0.4pp（可能 pooled F1 vs mean-of-F1 差异）
4. **exp62 silhouette 值**：registry 仅存 Fisher，silhouette 无记录

报告已写入 `artifacts/audit_appendix.md`。

---
