# code threecond multiseed r2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_threecond_multiseed_r2_20260518T064603_result.json`
- **Structured JSON:** [`18dfbe229475a6c83e24.json`](../../sessions/18/18dfbe229475a6c83e24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

正常运行中。每层 ~25s × 3 seeds，33 layers × 3 conditions ≈ 82 min。实验已在跑，registry 已更新为 RUNNING。

总结：
- 脚本 `/root/vla-ssd/scripts/threecond_multiseed_probe.py` 已部署
- tmux session `threecond_multiseed` 运行中，GPU cuda:0
- 3 条件 × 33 层 × 3 seeds = 297 个 probe 训练
- 预计 ~80 min 完成
- 日志: `/root/autodl-tmp/vla-ssd/results/threecond_multiseed.log`
- 输出 JSON: `/root/autodl-tmp/vla-ssd/results/threecond_multiseed.json`
- 输出图: `/root/autodl-tmp/vla-ssd/results/figures/fig_threecond_multiseed.{pdf,png}`

---
