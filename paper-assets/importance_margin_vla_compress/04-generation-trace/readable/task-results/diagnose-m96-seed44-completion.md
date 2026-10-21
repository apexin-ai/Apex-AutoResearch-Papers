# diagnose m96 seed44 completion

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_m96_seed44_completion_20260519T080216_result.json`
- **Structured JSON:** [`ceb42670ce0752664ac1.json`](../../sessions/ce/ceb42670ce0752664ac1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 中只有 `train_smart_compress_m96`（无 seed44 后缀），状态已是 DONE。seed44 变体未注册。Cron 已成功删除。

## 汇总

### train_smart_compress_m96_seed44
- **状态：正常完成**
- 日志：`/root/autodl-tmp/importance_margin_vla_compress/logs/smart_compress_m96_seed44.log`
- 最终 step：99999/100000，输出 "Training complete."（16:01:22 UTC）
- Checkpoint：`/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m96_seed44/checkpoint.pt`（1.49 GB）
- 最终指标：eval/action_loss=0.0526, train/action_loss=0.0467
- Cron 已删除
- Registry 中无此 exp_id（只有 `train_smart_compress_m96` 为 DONE）

### smart_compress_m32_seed44
- **仍在运行**，GPU 0
- 进度：step 97650/100000（97.6%）
- 速度 4.0 sps → 预计 **~10 min** 完成

### train_smart_compress_m64_seed44
- **仍在运行**，GPU 1
- 进度：step 97400/100000（97.4%）
- 速度 4.0 sps → 预计 **~11 min** 完成

两个 seed44 实验都将在 ~10 分钟内完成。是否需要我为 m32/m64 设置完成监控？

---
