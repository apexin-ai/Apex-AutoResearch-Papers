# code rescue 14b 72b check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rescue_14b_72b_check_20260519T124546_result.json`
- **Structured JSON:** [`7479beed524b5d84c0d8.json`](../../sessions/74/7479beed524b5d84c0d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Server C (14B) — autodl-5090-c

- **状态：存活，正常训练中**
- screen session `train_14b_s42` 存活（PID 56766）
- 当前 step: **6483/41180 (15.7%)**，从上次 4934 增长了 ~1500 steps
- 最近 loss: **0.0608**，grad_norm: 0.343
- GPU 0,1 利用率 95-96%，显存各占 ~26GB/32GB
- 速度 ~2.2s/it，ETA ~21h
- checkpoint-6000 已保存
- 注意：GPU 2,3 上还有另一个 7B 训练在跑（`train_config_qwen25_7b_fewnerd_s42.yaml`，PID 72042/72043，19:28 启动）

## Server B (72B) — autodl-5090-b

- **状态：存活，正在处理 FewNERD（conll2003 已完成）**
- PID 59040 存活，4 GPU 100% 利用率，各占 ~32GB 显存
- 进度：**289848/301184 prompts (96.2%)**，正在处理 FewNERD 的 stochastic sampling
- 已完成数据集：
  - SciERC: **551 行** (samples.jsonl) ✓
  - CoNLL2003: **3453 行** (samples.jsonl) ✓
  - FewNERD: 进行中，约 96%
- 速度 ~18 it/s，剩余 ~11000 prompts，**ETA ~10-15 分钟**

两个实验都在正常运行，系统标记的 failed 是误报。

---
