# analyze cutoff s1

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_cutoff_s1_20260523T005329_result.json`
- **Structured JSON:** [`4333a7b78fa1d8146adf.json`](../../sessions/43/4333a7b78fa1d8146adf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**cutoff_s1 训练报告：**

1. **训练完成** — 50005 步，EXIT_CODE=0，耗时 ~17.4 GPU 小时
2. **最终 loss** — action_loss=0.0547, occ_loss=0.0129
3. **Cutoff 效果** — occ_loss 在 cutoff (35k步) 前稳定在 ~0.010，cutoff 后略升至 0.013-0.015（梯度停止但 loss 仍计算，符合预期）；action_loss 持续收敛
4. **Checkpoint 完整** — 4 个 model shard + action_head + occ_head + proprio_projector + tokenizer 均存在
5. **Registry 已更新** — conclusion=success, status=DONE, metrics 已记录

---
