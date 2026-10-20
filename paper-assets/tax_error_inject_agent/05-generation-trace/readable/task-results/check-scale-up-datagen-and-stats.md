# check scale up datagen and stats

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_scale-up-datagen-and-stats_20260516T161758_result.json`
- **Structured JSON:** [`cc660f6e1295eec0a317.json`](../../sessions/cc/cc660f6e1295eec0a317.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 任务 1: Scale-up Datagen 状态

| 项目 | 状态 |
|------|------|
| 目录 | `data/trajectories_scaleup_p1/` |
| 成功 trajectories | **797 条** |
| 失败 trajectories | 2736 条（成功率 22.6%） |
| 最后 API 调用 | `2026-05-16T13:26:43` (traj_2770)，约 **11 小时前** |
| 活跃进程 | **无 datagen 进程在跑** |
| 当前 GPU 占用 | 1 个 eval 进程 (llama31-taxei-s123 injected eval, seed 42, PID 298593) |

**结论**：Scale-up datagen 已停止，797 条成功数据已收集。没有生成进程在运行，需要重启。

---

## 任务 2: 统计检验结果摘要

| 测试 | 结果 |
|------|------|
| **Levene (方差)** | TaxEI vs Random: p=0.027 ✓ 显著 |
| **F-test (方差比)** | F=50.34, p=0.020 ✓ |
| **Bootstrap CI (均值差)** | TaxEI−Random = −0.043, 95% CI [−0.142, 0.014] ✗ 跨零 |
| **ANOVA (三组均值)** | F=0.628, p=0.565 ✗ 不显著 |
| **Fisher (检测率)** | TaxEI 75% vs Random 53%, p=0.047 ✓ 显著, OR=2.6 |
| **Cohen's d** | −0.695 (中大效应，但 n=3 无统计功效) |

**核心发现**：TaxEI 跨 seed 方差显著更大（seed-sensitive），但均值无差异；检测能力显著优于 Random（OR=2.6）。报告已注册为 `art_20260516_3e5761`。

---
