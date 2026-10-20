# ops verify null seeds running

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_null_seeds_running_20260521T063444_result.json`
- **Structured JSON:** [`437e571719397e0b072f.json`](../../sessions/43/437e571719397e0b072f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### s45 (westd-17855, GPU 2) — 正常运行

- GPU: 14260MiB, **95% util**
- 进度: **gen_2 训练中**, step 3725/5000 (74%), ~7.70 it/s
- gen_0, gen_1 已完成
- loss@3700: 3.21, lr: 1.446e-05
- 预计 gen_2 完成还需 ~2:45，整体 10 gen 预计还需数小时

### s46 (westd-19828, GPU 1) — 刚启动，需观察

- GPU: 12445MiB, **0% util**（模型已加载）
- 进度: **gen_0 baseline 刚保存完**, 日志仅 9 行，gen_0 目录只有 `synthetic_data`，训练尚未开始
- 可能原因: 快照时恰好在 baseline 保存和训练启动之间，GPU util 0% 是瞬时状态
- config 确认: seed=46, synthetic_ratio=0.0, 10 gen, 5000 steps, pythia-410m — 参数正确

s46 目前看起来刚刚启动，尚未进入训练循环。建议几分钟后再检查一次确认 GPU util 升上来、gen_0/trainer 目录出现。如果仍然 0% util 则需要排查。

---
