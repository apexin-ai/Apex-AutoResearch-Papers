# infra swebench continue

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_swebench-continue_20260512T025836_result.json`
- **Structured JSON:** [`9458494b0bda92d17145.json`](../../sessions/94/9458494b0bda92d17145.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pilot 已完成，无运行中的进程。

**状态汇总：**

| 项目 | 状态 |
|------|------|
| Docker | v29.1.3 ✓ |
| swebench | v4.1.0 ✓ |
| 脚本 | build_swebench_data.py 存在 (13.8KB) ✓ |
| Pilot 数据 | **已完成** ✓ |

**Pilot 数据统计 (7349 条)：**

| 维度 | 分布 |
|------|------|
| Labels | pass=5551, fail=1798 |
| Mutation | gold=2691, operator_swap=1828, boundary_removal=1341, off_by_one=1415, return_value=74 |
| Test type | p2p=7237, f2p=112 |
| Repos | 10 个 (xarray 3840 最多, django 296, sympy 1305 等) |

有少量 mutation 跳过（astropy-13236, pytest-7490, psf/requests-6028 的部分变异类型未完成）。

Pilot 阶段已全部执行完毕，数据产出在 `data/swebench_pilot/swebench_pilot_data.jsonl`。需要进入下一步（如全量运行或数据分析）吗？

---
