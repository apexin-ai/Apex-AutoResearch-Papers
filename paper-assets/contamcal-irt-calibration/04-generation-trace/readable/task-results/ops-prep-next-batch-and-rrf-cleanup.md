# ops prep next batch and rrf cleanup

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep_next_batch_and_rrf_cleanup_20260516T115430_result.json`
- **Structured JSON:** [`5f60ec18c0dec4b31efe.json`](../../sessions/5f/5f60ec18c0dec4b31efe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务完成。

---

**任务 1：RRF exposure_scores.json 去重**
- 删除 `Qwen2.5-3B_d000_s42_a32` 和 `Qwen2.5-3B_d005_s42_a32`（统一保留 `_a32_s42` 格式）
- 清理后 23 条目 ✓
- 原文件备份为 `exposure_scores.json.bak`

**任务 2：3B d000_s123 checkpoint 验证 & signals 脚本**
- Checkpoint 存在：`/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter/`
- `lora_alpha = 32` ✓（C006 合规）
- signals 输出目录 `Qwen2.5-3B_d000_s123_a32` 尚不存在（需创建，脚本已包含 `mkdir -p`）
- 脚本就绪：`/root/contamcal-irt-calibration/exp002/run_3B_d000_s123_signals.sh`
  - 用法：`bash run_3B_d000_s123_signals.sh &lt;GPU_ID>`（如 `0` 或 `3`）
  - 3 benchmarks × 3 signals = 9 tasks，支持断点续跑（已有输出自动 skip）
  - 语法验证通过

---
