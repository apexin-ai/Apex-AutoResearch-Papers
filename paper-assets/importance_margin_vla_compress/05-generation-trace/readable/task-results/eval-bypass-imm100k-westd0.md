# eval bypass imm100k westd0

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_bypass_imm100k_westd0_20260517T033412_result.json`
- **Structured JSON:** [`f6542262a617c747e4b6.json`](../../sessions/f6/f6542262a617c747e4b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

总结：

**已完成：**
- **Checkpoint**: `checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt`（IMM twostage fullft, k=0.5）
- **Bypass eval 已启动**: `--mode baseline`（加载 policy 权重不经过 ACIS pruning，全 token 推理）
- **PID**: 876813, **Log**: `~/runs/importance_margin_vla_compress/eval_imm100k_bypass.log`
- **Registry**: `eval_imm100k_bypass` 状态 RUNNING

**k_ratio 语义检查结果：无 bug**
- `k = max(1, int(N_vis * self.k_ratio))` → k_ratio 是 keep ratio
- k=0.5 保留 50% visual tokens，语义正确

**eval 正在跑 libero_object 10 tasks x 50 episodes，预计需要几小时。** 结果会写入 `eval_results/eval_imm100k_bypass_object.json`。如果 SR ≈ 44% 说明 Stage2 未损伤 expert 权重；如果 SR < 20% 则 Stage2 有损伤。

---
