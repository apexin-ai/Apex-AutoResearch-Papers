# code re repair data filter v2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_re-repair-data-filter-v2_20260517T044147_result.json`
- **Structured JSON:** [`4bade190ddb21f9d8905.json`](../../sessions/4b/4bade190ddb21f9d8905.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 指标 | 值 |
|------|------|
| 筛选后 instances | **59** |
| simple (2-3 failing f2p) | 48 |
| medium (4-6 failing f2p) | 6 |
| complex (7+ failing f2p) | 5 |
| 输出文件 | `/home/sonny/exec-sim-repair-verifier/data/re_repair_v2/re_repair_instances_final.jsonl` |
| 筛选脚本 | `/home/sonny/exec-sim-repair-verifier/filter_final_instances.py` |

59 个 instances 在目标范围 50-80 内。分布偏向 simple 层（48/59），原因是大多数 SWE-bench Verified instances 本身 FAIL_TO_PASS test 数量不多（2-3 个），且 oracle 扩展覆盖的 96 个 (instance, mutation) 组合中，多数只有少量 f2p test 实际失败。

---
