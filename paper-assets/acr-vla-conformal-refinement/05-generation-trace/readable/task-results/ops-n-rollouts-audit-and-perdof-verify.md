# ops n rollouts audit and perdof verify

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_n-rollouts-audit-and-perdof-verify_20260518T104245_result.json`
- **Structured JSON:** [`09ab37c0ff93e006f7a6.json`](../../sessions/09/09ab37c0ff93e006f7a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心发现：

## Part A: n_rollouts 审计结论

**seed45 在 bjb2-28827 上的早期批次系统性使用了 n_rollouts=20**，共 5 个文件受影响：

| 受影响数据 | 当前 SR | n_rollouts | 在论文核心数据中? |
|-----------|---------|------------|-----------------|
| VLA-only baseline seed45 | 9% | **20** | **是（Table）** |
| Scalar CRM seed45 | 9% | **20** | **是（Table）** |
| obs_only ε=0.1 seed45 | 14% | **20** | 是（magnitude curve） |
| obs_only uncapped seed45 | 12% | **20** | 是（magnitude curve） |
| perdof ε=0.2 seed45（原始） | 9% | **20** | 已有 r3 替换可用 |

**不受影响（全部 n_rollouts=10）：**
- obs_only ε=0.2 主结果（6 seeds）✅
- Argmin baseline（6 seeds）✅
- obs_only ε=0.2/0.3 seed45 ✅（在其他服务器重跑）
- perdof ε=0.1/0.3 seed45 ✅

**需要行动：VLA-only seed45 和 scalar seed45 必须用 n_rollouts=10 重跑。**

## Part B: perdof ε=0.2 核实

- seed45 原始值（9%，n_rollouts=20）必须替换为 r3（12%，n_rollouts=10）
- 修正后 n=6: [11, 9, 10, **12**, 9, 11] → **mean = 10.33%**（原 9.83%）
- Reviewer #37 的 14% 是错误的：混淆了 perdof **ε=0.03** seed42（14%）和 perdof **ε=0.2** seed42（11%）
- seed48 正在运行（eval-perdof-object-norm02-seed48），完成后可加入 n=7

报告已保存至 `artifacts/_project/report/n_rollouts_audit_report.md`。

---
