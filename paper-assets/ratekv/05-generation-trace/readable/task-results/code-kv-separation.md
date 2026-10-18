# code kv separation

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_kv_separation_20260514T060217_result.json`
- **Structured JSON:** [`1154131e0608d6415bc0.json`](../../sessions/11/1154131e0608d6415bc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动，运行状态正常。

**Summary:**
- `run_kv_separation.py` 已部署到 `/root/ratekv/`
- 任务在 westd-37397 cuda:1 运行，tmux session `kv_separation`
- **Phase 1**: K/V 分离 profiling（672 passes，ETA ~2h）
  - 每个 KV head 分别测量 K-only 和 V-only 在 {2,4,8} bit 下的 PPL delta
  - L0H0 K 结果: 2bit=+6.24, 4bit=+0.36, 8bit=0.0 (与 joint K+V 的 L0H0 profile 6.76 对比，说明 K 贡献了大部分 distortion)
  - 带 checkpoint 自动恢复
- **Phase 2**: MCKP solver（224 items vs 112 items）
- **Phase 3**: WikiText-2 PPL eval（baseline / K/V sep / joint K=V / uniform 4-bit）
- Registry: `kv_separation` → RUNNING
- 日志: `/root/ratekv/kv_separation.log`
- 结果输出: `/root/ratekv/kv_separation_results.json`

---
