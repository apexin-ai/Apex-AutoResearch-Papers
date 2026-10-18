# eval official smolvla baseline v4

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_official_smolvla_baseline_v4_20260518T130236_result.json`
- **Structured JSON:** [`e81c933f211a85ffb4f9.json`](../../sessions/e8/e81c933f211a85ffb4f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

正常运行中，Task 0 Ep 3 已经 SUCCESS。模型加载和 normalization 正确。全 10 tasks * 50 episodes 预计需要 2-3 小时。

总结已完成的工作：
1. **清理崩溃进程** — 已完成，GPU 空闲
2. **修复 transformers 兼容性** — 不再需要，`SmolVLAPolicy.from_pretrained` 在 transformers 5.8.1 上正常加载
3. **修复 normalization** — 根因确认：`eval_official_libero.py` 缺少 state 归一化和 action 反归一化。已添加：
   - `load_norm_stats()`: 从 checkpoint safetensors 文件加载 mean/std
   - `normalize_state()`: 对 `observation.state` 做 `(x - mean) / (std + eps)` 
   - `unnormalize_actions()`: 对模型输出做 `x * std + mean`
4. **提交完整 baseline eval** — `eval_official_smolvla_baseline`，10 tasks × 50 episodes，LIBERO-Object，seed=42，已在 westd-27271 cuda:0 运行

---
