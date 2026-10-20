# ops j16 theta 5domains check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_j16_theta_5domains_check_20260517T153900_result.json`
- **Structured JSON:** [`8d6e3fba0b7609a0582d.json`](../../sessions/8d/8d6e3fba0b7609a0582d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**状态: 失败** — 0/5 domains 有 θ

**详情:**
- 脚本 `j16_theta_5domains` 仅完成了 Medical 的 MCMC 采样（23:18→23:26，481s），但在采样后提取 θ/写入文件前进程被杀
- 其余 4 个 domain（Humanities, Social_Sciences, Business_Law, Other）未被处理
- 无 error/traceback，推测 OOM-killed（CmdStan fit.stan_variable("theta") 时内存峰值）

**文件状态:**

| Domain | irt_results.json | theta | 备注 |
|--------|-----------------|-------|------|
| STEM_Math | 1790B, 22:41 | YES | 早期独立运行成功 |
| STEM_Science | 1743B, 22:50 | YES | 同上 |
| STEM_CS_Eng | - | YES | 同上 |
| Medical | 772B, 20:39 | NO | j16 run 完成采样但未写入 |
| Humanities | ?, 20:49 | NO | 未被 j16 run 处理 |
| Social_Sciences | ?, 21:04 | NO | 同上 |
| Business_Law | ?, 21:17 | NO | 同上 |
| Other | 768B, 21:29 | NO | 同上 |

**需要重新运行** 5 个 domain 的 IRT fitting with theta extraction。建议减少 `iter_sampling` 或分批运行以降低内存峰值。

---
