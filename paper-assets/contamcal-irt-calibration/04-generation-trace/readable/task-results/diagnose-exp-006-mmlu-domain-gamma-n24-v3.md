# diagnose exp 006 mmlu domain gamma n24 v3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_006_mmlu_domain_gamma_n24_v3_20260516T133716_result.json`
- **Structured JSON:** [`2ccb9aefc2bbdaf7a71e.json`](../../sessions/2c/2ccb9aefc2bbdaf7a71e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已收集足够信息，写诊断报告。

---

## 诊断报告：exp_006_mmlu_domain_gamma_n24_v3 失败原因

### 失败根因：CmdStan 子进程 EPERM（Operation not permitted）

**直接原因**：Stan MCMC 采样时 chain 1 和 chain 4 返回 exit code 1，错误信息为 `Operation not permitted`。CmdStanPy 因 `retcodes=[1, 0, 0, 1]` 抛出 RuntimeError，终止整个脚本。

**关键 log 片段**：
```
2026-05-16 21:22:15,511 [ERROR] Chain [4] error: code '1' Operation not permitted
2026-05-16 21:22:15,615 [ERROR] Chain [1] error: code '1' Operation not permitted
...
RuntimeError: Error during sampling:
  retcodes=[1, 0, 0, 1]
```

### 根因分析

**并发 Stan 进程资源竞争**。两个 Stan 实验同时运行在同一容器：
- `mmlu_domain_gamma_n24_v3` (PID 781756)：正在 fit Social_Sciences (21 models × 2000 items, 4 chains)
- `pooled_irt_n25` (PID 785832)：同时做 MMLU pooled IRT fitting (4 chains)

证据：`results_pooled_n20/mmlu/` 的创建时间为 **21:22** — 与崩溃时间 **精确一致**。

**EPERM 触发机制**（最可能）：
- 容器 cgroup pids.max = 20480，当前 pid.current = 2806（已恢复）
- 两个实验同时 8 个 Stan 子进程 + 多线程，在 /tmp（根分区，仅 7GB 剩余）同时写大量 CSV 采样输出
- AutoDL 容器可能有 seccomp 配置在负载高峰时阻止了 `sched_setaffinity` 或 `clone` 等 syscall
- 或者 /tmp 空间在并发写入时瞬时耗尽导致文件操作失败（当前 /tmp = 5.9GB 残留，根分区仅 77% → 7GB free）

**排除 OOM**：系统有 1TB RAM，仅用 52GB。

### 完成状态

| Domain | 状态 |
|--------|------|
| STEM_Math | ✅ 完成 (v1) |
| STEM_Science | ✅ 完成 (v1) |
| STEM_CS_Eng | ✅ 完成 (v1) |
| Medical | ✅ 完成 (v1) |
| Humanities | ✅ 完成 (v2/v3) |
| Social_Sciences | ✅ 有结果 (rhat=1.54, ess=7.1, 质量差) |
| Business_Law | ❌ 未开始 |
| Other | ❌ 未开始 |

### exp_006_pooled_irt_n25 状态

PID 785832 **已死亡**（ps 返回空）。但其输出 `results_pooled_n20/` 有完整的 mmlu、gsm8k、arc_challenge 三个 benchmark 结果，最后文件 21:30。**可能已正常完成**（它完成后退出，不是崩溃）。

### 修复建议

1. **清理 /tmp**：`rm -rf /tmp/tmp*`（释放 5.9GB 残留 Stan 临时文件）
2. **串行重跑**：确保没有其他 Stan 进程并发运行
3. **只跑剩余 domains**：`--domains Business_Law Other`
4. **Social_Sciences 质量问题**：rhat=1.54, ESS=7.1 说明收敛很差（也可能就是该 domain 的数据特性），考虑加 warmup 或 adapt_delta 重跑
5. **设置 TMPDIR**：`export TMPDIR=/root/autodl-tmp/tmp_stan`，避免根分区 /tmp 空间限制
6. **添加 skip-existing 逻辑**：脚本没有跳过已有结果的 domain，每次重跑都从头开始

---
