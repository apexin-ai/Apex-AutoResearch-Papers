# code pi05 zeromask support and deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pi05-zeromask-support-and-deploy_20260525T195657_result.json`
- **Structured JSON:** [`5f5abd680ba39c682638.json`](../../sessions/5f/5f5abd680ba39c682638.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

仍在加载模型，正常。π0.5 模型 ~3B 参数加载需要时间。

完成汇总：

1. **脚本修改**：`eval_pi05_pruning_libero.py` 新增 `zero_mask_random` 和 `zero_mask_l2norm` 两种 prune_mode
   - 添加了 `zero_mask_tokens_random()` 和 `zero_mask_tokens_l2norm()` 两个函数
   - 复用 random/l2norm 的 scoring 逻辑，但不移除 token，而是将 low-importance token 值置 0（`img_emb * mask`）
   - 输出 tensor shape 不变，token 数量保持原样

2. **实验部署**：
   - `eval_pi05_zeromask_random_k09_object_seed42` — GPU0，已在跑（ZEROMASK-DIAG 确认 230/256 keep）
   - `eval_pi05_zeromask_l2norm_k09_object_seed42` — GPU2（CUDA_VISIBLE_DEVICES=2），加载模型中

3. **修复问题**：发现 `DEVICE = "cuda:0"` 硬编码，第二个实验需要 `CUDA_VISIBLE_DEVICES=2` 才能使用 GPU2，已重启修复。

---
