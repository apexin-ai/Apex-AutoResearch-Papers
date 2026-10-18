# deploy pi05 random k095 seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_pi05-random-k095-seed42-v2_20260521T200916_result.json`
- **Structured JSON:** [`3df11cc23fd55b1ab53a.json`](../../sessions/3d/3df11cc23fd55b1ab53a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成，总结：

- **根因**：`from_pretrained("google/paligemma-3b-pt-224")` 在离线环境下尝试网络验证失败
- **修复**：设 `HF_HUB_OFFLINE=1`，强制使用 `/root/autodl-tmp/.hf_cache/` 中的本地缓存
- **状态**：GPU0 占用 10.5GB，eval 已开始（random prune 243/256 tokens，10 tasks × 50 episodes）
- **Registry**：`eval_pi05_random_k095_object_seed42_v2` → RUNNING，parent 链接到 k=0.9 v2
- **预计耗时**：~2 小时（参考同系列实验）

---
