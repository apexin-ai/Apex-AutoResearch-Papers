# ops check exp020 progress

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-exp020-progress_20260523T125939_result.json`
- **Structured JSON:** [`0d5350b1ebb3f9a300c1.json`](../../sessions/0d/0d5350b1ebb3f9a300c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_020 状态报告

### 1. 运行状态
**正在运行。** 日志最后修改时间 2026-05-23 21:00:14，实验从 17:46 启动。

### 2. 当前进度
**Gen 1 fine-tuning 中**，step 4500 / ~6250（72%）。Gen 0 已完成评估。

### 3. Gen 0 Metrics（GPT-2-medium pretrained baseline）

| Metric | GPT-2-medium (355M) | Pythia-410M (对比) |
|--------|---------------------|-------------------|
| eff_rank | **23.09** | 417.55 |
| PPL | **15.45** | 9.55 |
| distinct-4 | **0.9127** | 0.7414 |

GPT-2-medium 的 eff_rank 远低于 Pythia（23 vs 418），说明其 pretrained representation 已经高度集中在低维子空间。PPL 更高（15.45 vs 9.55）符合预期（GPT-2-medium 比 Pythia-410M 弱一些）。distinct-4 更高说明生成更多样。

### 4. 预估完成时间
- 配置：10 generations，batch_size=8，50000 samples/gen，1 epoch/gen
- 已耗时 ~3.25h 完成 Gen 0 eval + Gen 1 的 72% training
- 预估每 gen ~2.5-3h（generation + training + eval）
- **剩余 ~9 gen，预计还需 22-27 小时**，即约 **5月24日 19:00-24:00 完成**

### 5. SLV 轨迹数据
目前只有 Gen 0 数据，尚无多代 SLV 轨迹。Gen 1 完成后会写入第一个 post-training 数据点。

**注意**：eff_rank=23.09 的 baseline 值得关注——如果 GPT-2-medium 的表征本身就高度低秩，collapse 的演化轨迹可能与 Pythia 有本质差异（decompression peak 可能不明显或完全缺失）。

---
