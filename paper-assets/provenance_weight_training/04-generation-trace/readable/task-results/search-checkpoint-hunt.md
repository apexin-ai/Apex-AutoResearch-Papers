# search checkpoint hunt

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_search_checkpoint_hunt_20260517T145139_result.json`
- **Structured JSON:** [`3c9f7a784cc405a5f19a.json`](../../sessions/3c/3c9f7a784cc405a5f19a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== 搜索结果 ===
uniform_seed42 (Qwen3-0.6B):     NOT FOUND（两台服务器均无）
adaptive_fix_seed42 (Qwen3-0.6B): NOT FOUND（两台服务器均无）

=== 所有 final 目录列表 ===
westd-30476: 无（4个训练中/未完成的 Qwen3-0.6B 实验，均无 final）
westd-41312:
  /root/autodl-tmp/.../llama3b_uniform_seed42/final     ✓ 完整
  /root/autodl-tmp/.../llama3b_adaptive_seed42/final    ✓ 完整
  /root/autodl-tmp/.../hybrid_rho04_seed42/final
  /root/autodl-tmp/.../hybrid_rho06_seed42/final
  /root/autodl-tmp/.../grid_b0_2_seed42/final
  /root/autodl-tmp/.../batchsize16_nmin8_seed42/final
```

**关键发现：**

| 目标 | 状态 | 说明 |
|------|------|------|
| `uniform_seed42` (Qwen3-0.6B) | **NOT FOUND** | westd-41312 有 `llama3b_uniform_seed42`，但基座是 **Llama-3.2-3B**，不是 Qwen3-0.6B |
| `adaptive_fix_seed42` (Qwen3-0.6B) | **NOT FOUND** | 两台服务器均无任何包含 "adaptive_fix" 的目录。westd-41312 有 `llama3b_adaptive_seed42`（Llama-3.2-3B, weighting=adaptive, tau=0.8），也非 fix 版 |

**westd-30476 上的 Qwen3-0.6B 实验（均无 final，仍在训练或未完成）：**
- `bs8_auto_nmin_seed42` — adaptive, bs=8, n_min=4（checkpoint 到 1800）
- `batch_adaptive_tau_rho06_seed42` — adaptive, adaptive_tau=true, rho=0.6（checkpoint 到 1800）
- `rho02_adaptive_tau09_seed42` — adaptive, tau=0.9, rho=0.2（checkpoint 到 1600）
- `random_reweight_seed123` — random, seed=123（checkpoint 到 3000）

这两个 Qwen3-0.6B checkpoint 从未在这两台服务器上生成过，或已被删除。

---
