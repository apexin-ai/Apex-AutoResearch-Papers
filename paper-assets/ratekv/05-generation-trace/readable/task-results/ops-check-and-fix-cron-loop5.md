# ops check and fix cron loop5

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_and_fix_cron_loop5_20260514T151716_result.json`
- **Structured JSON:** [`235a6d04c23b9df52142.json`](../../sessions/23/235a6d04c23b9df52142.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Gemma2 (gemma2_9b_full_pipeline)
- **状态**: ✅ 已完成 (21:58 CST)，注册表已更新为 DONE
- **结果**: Verdict PASS
  - Baseline PPL: 711.38
  - MCKP PPL: 514.62 vs Uniform 4-bit: 579.91 (改善 +65.29)
  - Best k=16, PPL=377.87
  - Top-5 concentration: 1.64, L0 dominance: 5.34x
  - 总耗时 0.3h
- **GPU**: cuda:0 已释放 (0% / 0 MiB)

### Yi15 (yi15_9b_full_pipeline)
- **状态**: 模型下载中 (2/4 shards 完成，model-00001 54%, model-00003 60%, ~400KB/s)
- **问题**: v1 wait 脚本 bug — 只检查 safetensors 文件数稳定性但不要求 4 个全到齐，1 个 shard 完成后就过早启动 pipeline → FileNotFoundError 崩溃
- **修复**: 已部署 v2 脚本 (`wait_and_run_yi15_v2.sh`)，显式检查 4/4 shards + 文件大小稳定性。PID 233153 运行中，当前正确等待 (2/4)
- **ETA**: 下载完成 ~1-1.5h，之后 pipeline 自动启动
- **GPU**: cuda:1 待用 (0% / 0 MiB)

### Cron 监控
- 已注册 job `378c4382`，每 23 分钟检查 yi15 进度，完成后自动更新注册表并汇报

---
