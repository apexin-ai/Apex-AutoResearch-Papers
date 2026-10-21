# ops fix nproc retry gsm8k mcmc

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-nproc-retry-gsm8k-mcmc_20260515T010511_result.json`
- **Structured JSON:** [`c6fb52c357ddfb4a9f38.json`](../../sessions/c6/c6fb52c357ddfb4a9f38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已成功启动，MCMC 正在采样。

## 汇报

### 1. nproc 诊断结果
- `ulimit -u` (Max processes): **unlimited** — 不是瓶颈
- **cgroup pids.max = 20480**（容器层面硬限制，只读不可修改）
- 当前使用: 2089/20480，余量充足
- 之前失败（retcodes=[0,1,1,1]）是暂态问题，可能当时并发进程更多

### 2. CmdStan 验证
4-chain 测试通过，所有 chain 正常完成。

### 3. 实验启动状态
| 实验 | tmux session | 状态 |
|------|-------------|------|
| S1-only GSM8K (N=8, 4chains×1000samples) | `exp006_s1only_gsm8k_v2` | MCMC warmup 中 |
| Oracle GSM8K extended (N=16, 4chains×4000samples) | `exp006_oracle_gsm8k_ext_v2` | MCMC warmup 中 |

S1-only 预计 ~6 分钟完成，Oracle extended 预计 ~30-40 分钟。需要我稍后检查结果吗？

---
