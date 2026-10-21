# ops mmlu merge and cuda4 submit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mmlu-merge-and-cuda4-submit_20260516T061927_result.json`
- **Structured JSON:** [`dfcecb2220b7a2dbda97.json`](../../sessions/df/dfcecb2220b7a2dbda97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成：

**Part 1 — signals merge**
- `signals_merged_mmlu.json` 已生成：14042 items，keys = `[item_id, benchmark, s1_embedding, s2_minkpp, s4_selfcritique]`，格式与 gsm8k/arc_challenge merged 文件一致。

**Part 2 — cuda:4 eval 提交**
- 已提交 `exp_001_eval_3B_d000_s42_a32_para_aligned`
- Checkpoint: `Qwen2.5-3B_d000_a32_s42`（lora_alpha=32 已验证）
- cuda:4, PID 716470, 6306 MiB 已分配，模型加载中
- Registry 已更新为 RUNNING
- 每 8 分钟自动监控已注册

---
