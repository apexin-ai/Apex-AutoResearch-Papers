# fix k8 oom batch size

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_k8_oom_batch_size_20260516T142455_result.json`
- **Structured JSON:** [`6e142025e34677429cea.json`](../../sessions/6e/6e142025e34677429cea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程存活，正在加载模型（`torch_dtype` 警告来自 reward model 加载），无 OOM。完成：

1. **修改完成**：`run_quick_probe_k8.py` 已加入 `config.GEN_BATCH_SIZE = 8`（8×8=64 序列/batch）
2. **旧数据已清理**：`outputs_k8/` 已重建
3. **`carr_quick_probe_k8_02` 已启动**：PID 507603，tmux session 运行中，日志在 `~/runs/collapse_aware_reward_rebalancing/carr_quick_probe_k8_02.log`

---
