# ops diag 15B d100 s123 and realloc cuda2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diag_15B_d100_s123_and_realloc_cuda2_20260516T131115_result.json`
- **Structured JSON:** [`d4486edd2ea4c8f409a0.json`](../../sessions/d4/d4486edd2ea4c8f409a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Part A: exp_002_signals_15B_d100_s123_cuda2
**SUCCESS** — 9/9 signals 全部完成（3 benchmarks × 3 signals），输出目录 `/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B_d100_s123/`。Registry 已更新 (conclusion=success)。Cron 不存在（已被清理）。

### Part B: cuda:2 重新分配
**1.5B s123 全部完成** — d000/d005/d025/d100 四个 dosage 均 9/9，无缺失。0.5B s123 同样全部完成。

按 C007 优先级下移，发现 **3B d000_s123_a32 仅 2/9**（s1_mmlu, s2_mmlu），是唯一未完成的 s123 信号集。

已提交：**3B d000_s123_a32 signals → cuda:2**
- 脚本: `run_3B_d000_s123_signals_v2.sh`（移除了 `$1` GPU 参数依赖，C004 compliant）
- PID: 784219 (shell) / 784230 (python, 6788 MiB on cuda:2)
- alpha=32 confirmed (C006)
- 将跳过 2 个已完成信号，计算剩余 7 个
- Registry: `exp_002_signals_3B_d000_s123_cuda2` → RUNNING

---
