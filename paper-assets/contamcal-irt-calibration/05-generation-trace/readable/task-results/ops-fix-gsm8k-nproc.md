# ops fix gsm8k nproc

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-gsm8k-nproc_20260515T011057_result.json`
- **Structured JSON:** [`ab495fc15cc437d83dd8.json`](../../sessions/ab/ab495fc15cc437d83dd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断与修复总结

### 诊断结果
| 检查项 | 值 | 是否瓶颈 |
|---|---|---|
| ulimit -u (max user processes) | unlimited | 否 |
| threads-max | 8,252,837 | 否 |
| limits.conf | 无活跃规则 | 否 |
| **cgroup pids.max** | **20,480** | **是（根因）** |
| 当前进程数 | 2,458 | 正常 |

**根因**：AutoDL 容器 cgroup `pids.max=20,480`。CmdStan 默认 `parallel_chains=min(chains, 4)=4`，在多个 GPU 训练/eval 实验并行运行时，4 条并行 MCMC 链加上其他进程逼近上限，触发 "Operation not permitted"。

### 修复内容
4 个文件添加 `parallel_chains` 可配置参数（默认 1，串行跑 chains）：
- `run_irt_calibration.py:fit_stan_model()` — 签名 + `model.sample()` 调用
- `run_exp006.py` — 新增 `--parallel-chains` CLI 参数（default=1）
- `joint_fit.py:run_joint_fit()` — 参数透传
- `run_irt_stan.py:run_stan_fit()` — 签名 + `model.sample()` 调用

### 重跑实验

| 实验 | PID | tmux session | log |
|---|---|---|---|
| exp006-pooled-s1only-gsm8k-v2 | 481020 | `exp006_s1only_gsm8k` | `/tmp/irt_s1only_gsm8k_v2.log` |
| exp006-oracle-gsm8k-extended-v2 | 481167 | `exp006_oracle_gsm8k_ext` | `/tmp/irt_oracle_gsm8k_ext_v2.log` |

s1only 实验已安全通过之前的崩溃点（60% Sampling），预计 ~20min 完成。oracle extended 实验（4×6000 iterations）预计 ~2h。

---
