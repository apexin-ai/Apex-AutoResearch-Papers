# infra deploy fix c restart imm

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_deploy-fix-c-restart-imm_20260515T172434_result.json`
- **Structured JSON:** [`11db4e241c58fd09d5cf.json`](../../sessions/11/11db4e241c58fd09d5cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

1. **Step 1-2**: `_hard_forward` 已替换为 binary mask 版本（保持 (B,N,D) 输出），`torch.gather` 已从 `_hard_forward` 中移除 ✓
2. **Step 3**: `imm_anchor.yaml` 已添加 `save_every: 2000`（`eval_every: 999999` 已存在）✓
3. **Step 4**: Dry-run PASS — train=(4,64,960), eval=(4,64,960) ✓
4. **Step 5-6**: 训练已启动并正常运行在 cuda:1，step 750+，loss 0.04-0.35，sps=3.2 ✓
5. **Step 7**: Registry 已更新为 RUNNING ✓

注意：第一次提交因缺少 `HF_HOME=/root/autodl-tmp/.hf_cache` 导致数据下载失败，第二次提交已修复。Baseline v5 在 cuda:0 上未受影响。

---
