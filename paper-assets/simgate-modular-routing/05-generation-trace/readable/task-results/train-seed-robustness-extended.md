# train seed robustness extended

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_seed-robustness-extended_20260515T190619_result.json`
- **Structured JSON:** [`26faa83fb89dd8795860.json`](../../sessions/26/26faa83fb89dd8795860.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常进行，loss 下降曲线合理：

| Epoch | GPU0 (seed 46) loss | GPU1 (seed 48) loss |
|-------|--------------------|--------------------|
| 0.18  | 5.56               | 5.40               |
| 0.37  | 5.01               | 4.85               |
| 0.55  | 3.30               | 3.17               |
| 0.74  | 1.72               | 1.77               |
| 0.92  | 1.00               | 1.00               |

初始 loss ~5.5 → epoch 1 结束 ~1.0，符合预期。

**汇总：**
- **GPU0** (cuda:0): seed 46 → seed 47, PID 890486, ~36% done
- **GPU1** (cuda:1): seed 48 → seed 49, PID 890629, ~36% done
- 每个 seed 165 steps × ~1s/step ≈ 3 min 训练 + eval，每张卡跑 2 个 seed 串行
- **预计总时长：~10-12 min**（含 eval 和模型加载）
- Registry `seed-robustness-ext` 已更新为 RUNNING，spec 完整

---
