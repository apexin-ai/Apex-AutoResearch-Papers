# code insert s123 tf reeval to postchain

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_insert_s123_tf_reeval_to_postchain_20260524T024115_result.json`
- **Structured JSON:** [`1dd6eb705c4aff810fc2.json`](../../sessions/1d/1dd6eb705c4aff810fc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。v2 脚本（PID 136974）已在后台运行，当前正在轮询等待 gpu_chain (PID 108997) 完成。

执行流程：gpu_chain 结束 → GPU 空闲检查 → **s123 TF re-eval**（GAR-ours + GAR-Dongre，覆盖 `results/d048_final_ar/tf_ss_s123_{ours,dongre}/`）→ per-head KL divergence。

- 使用的 checkpoint: `runs/d048_ss_s123/epoch_2`
- 修复的问题: `mid_turns_avg = NaN`（min_turns 截断 bug，已于 2026-05-23 修复）
- 日志: `logs/post_chain_queue_v2.log`

---
