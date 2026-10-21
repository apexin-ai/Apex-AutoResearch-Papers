# monitor rep44 rep45 status

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_rep44_rep45_status_20260514T145801_result.json`
- **Structured JSON:** [`5ea0cfd7e1c793e948dd.json`](../../sessions/5e/5ea0cfd7e1c793e948dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态

### rep44: **RUNNING — Gen 4/10 (featurize/generation 阶段)**
- **已完成**: Gen 0-3，3轮训练已完成
- **当前**: Gen 4 文本生成中（right-padding warnings 表明正在 model.generate()）
- **指标趋势** (分布坍缩明显):
  | Gen | ppl | entropy | eff_rank | mauve |
  |-----|-----|---------|----------|-------|
  | 0 | 26.95 | 3.2342 | 46.6 | - |
  | 1 | 56.37 | 1.8894 | 78.6 | 0.0319 |
  | 2 | 161.76 | 1.5357 | 74.5 | 0.0325 |
  | 3 | 281.75 | 1.3493 | 83.5 | 0.0340 |
- **预估剩余**: ~3-3.5 小时 (Gen 4 featurize 剩余 + Gen 5-9 × ~35min/gen)

### rep45: **RUNNING — Gen 3/10 (training 20%)**
- **已完成**: Gen 0-2，2轮训练已完成
- **当前**: Gen 3 训练中，step 992/5000 (20%), epoch 0.72, loss=0.82
- **指标趋势**:
  | Gen | ppl | entropy | eff_rank | mauve |
  |-----|-----|---------|----------|-------|
  | 0 | 26.95 | 3.2342 | 46.6 | - |
  | 1 | 56.15 | 1.9000 | 78.9 | 0.0308 |
  | 2 | 169.33 | 1.5541 | 74.4 | 0.0313 |
- **预估剩余**: ~4 小时 (Gen 3 剩余 + Gen 4-9 × ~35min/gen)

### GPU 状态
- cuda:0 — 93% 利用率, 14391 MiB (rep44)
- cuda:1 — 48% 利用率, 14391 MiB (rep45)

两个实验均正常运行，指标一致显示分布坍缩：ppl 指数上升、entropy 持续下降。两个 rep 的轨迹高度一致（Gen 1-2 的 ppl/entropy 差异 <5%）。

---
