# diag exp005 noise prop v2 check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp005_noise_prop_v2_check_20260514T032138_result.json`
- **Structured JSON:** [`526aa585dbba2704d185.json`](../../sessions/52/526aa585dbba2704d185.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_005_noise_prop_v2 状态报告

**进程状态**：已死。本地和服务器均无 noise_prop 进程。

**失败原因**（两个独立问题）：
1. **`/tmp` tmpfs 磁盘满**：ME 模型生成 ~1GB Stan CSV（9000 tau + 9000 log_lik × 4 chains），耗尽 3.9GB tmpfs。Simple 模型写 CSV 时 4 chains 全部 retcode=1。
2. **ME 模型严重欠识别**：10231 参数 vs 9000 观测 → Rhat=1.945。

**Partial results**：output_v2/ 为空，无可用结果。

**诊断结论**（已跑过独立诊断）：
- σ_e=0.3 simple model：收敛良好，γ_mean=0.458 (true=0.5)，Rhat=1.007
- σ_e=0.1 simple model：收敛但 γ 偏高 57.5%（0.788 vs 0.5）— 模型 identifiability 问题，非 bug

**v3 已在启动中**：另一个 worker（PID 338967）已于 03:21 被派出启动 v3。v3 脚本已存在（03:19 创建），修复了两个根因：
- Stan 输出写本地磁盘（不用 /tmp）
- 换用 analytic ME 模型（1231 参数 vs 10231）
- Simple 先跑、ME 后跑
- 断点续跑 + 每次 fit 后清理 chain CSV

**建议**：不需要额外操作。v3 已在被启动，预计运行 ~11-12 小时。γ bias 在 σ_e=0.1 处的问题是模型本身的 identifiability 限制（30 models 不够分离 γ 和 θ 在低噪声条件下），v3 结果可以量化这个边界，作为论文的 limitation 讨论素材。

---
