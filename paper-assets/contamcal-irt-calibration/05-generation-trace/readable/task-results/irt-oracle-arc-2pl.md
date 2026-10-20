# irt oracle arc 2pl

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_irt_oracle-arc-2pl_20260515T034508_result.json`
- **Structured JSON:** [`08811b83340dd33cfc9c.json`](../../sessions/08/08811b83340dd33cfc9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。

**实验已提交：**
- **exp_id**: exp006-oracle-arc-2pl
- **tmux session**: `exp006_oracle_arc_2pl`
- **PID**: 496697
- **命令**: `python exp006/run_exp006.py --oracle-exposure --pool-scales 0.5B 1.5B --benchmark arc_challenge --model-type 2pl_gamma --chains 4 --warmup 2000 --samples 4000 --parallel-chains 1 --output-dir /root/autodl-tmp/exp006/results_pooled_05B_15B_arc_oracle_2pl --aligned-only`
- **配置**: 11 models x 1172 items, 4 chains x 6000 iterations (2000 warmup + 4000 samples)
- **日志**: `/tmp/irt_oracle_arc_2pl.log`
- **输出**: `/root/autodl-tmp/exp006/results_pooled_05B_15B_arc_oracle_2pl`
- **状态**: RUNNING，registry 已更新

ARC 4PL oracle 之前 1000 warmup + 1000 samples 耗时 ~482s，本次 2000+4000 预计 ~20-30 分钟。

---
