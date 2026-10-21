# diagnose libero fullft seed1 k07

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_libero_fullft_seed1_k07_20260517T015238_result.json`
- **Structured JSON:** [`acd5b0cd7c787c5a85e1.json`](../../sessions/ac/acd5b0cd7c787c5a85e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== libero_fullft_seed1 ===
退出原因: 仍在运行中（非 failed）
最后 step: 64,600/100,000 (64.6%)
有无 completion sentinel: no
最终 checkpoint: /root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_full_ft_seed1/step_060000（最新）
Log 尾部关键行: 2026-05-17 09:52:55 step=64600 loss=0.0950 sps=4.2 — 日志持续到当前时间（09:52），无 traceback/OOM/中断迹象。进程活跃，cron 误判。

=== libero_imm_fullft_k07 ===
退出原因: 正常完成
最后 step: 20,000/20,000 (100%)
有无 completion sentinel: yes（"=== stage2 complete ===" + "Two-stage training complete."）
最终 checkpoint: /root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_imm_twostage_fullft_k07/final
Log 尾部关键行: 2026-05-17 09:43:33 "=== stage2 complete ===" → 09:43:36 "Final checkpoint saved" → "Two-stage training complete."
W&B: offline mode, run saved locally at wandb/offline-run-20260517_071820-sn57pmfw（需手动 sync）
```

**总结：**
- **libero_fullft_seed1**：仍在正常训练（step 64.6K，日志时间戳为几分钟前），cron 误判为 failed。无需干预。
- **libero_imm_fullft_k07**：已正常完成全部 20K steps（stage1 + stage2），checkpoint 已保存。cron 因 W&B 是 offline 模式没有检测到 sentinel 而误报。如需 W&B 记录，运行 `wandb sync /root/autodl-tmp/importance_margin_vla_compress/wandb/offline-run-20260517_071820-sn57pmfw`。

---
