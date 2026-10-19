# code deploy verify precompute v5

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_deploy-verify-precompute-v5_20260514T075426_result.json`
- **Structured JSON:** [`a348cec99523aed94980.json`](../../sessions/a3/a348cec99523aed94980.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

1. **修复验证通过** — C1（ee_states 含 gripper_states，8D）和 W3（alpha=0.5）均已到位
2. **旧缓存已清除** — `/root/autodl-tmp/crm_cache/spatial` 和 `object` 已删除
3. **3 个 precompute shard 已启动**：
   - `precompute-v5-shard0` → cuda:0 (PID 178134)
   - `precompute-v5-shard1` → cuda:1 (PID 178213)
   - `precompute-v5-shard2` → cuda:3 (PID 178359)

日志文件在 `~/runs/acr-vla-conformal-refinement/precompute-v5-shard{0,1,2}.log`。

---
