# ops urgent check expanded eval

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_check_expanded_eval_20260520T191844_result.json`
- **Structured JSON:** [`6ab7cd55c805be843478.json`](../../sessions/6a/6ab7cd55c805be843478.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 **仍在运行**，约完成 60%（6/10 evals done）。当前正在训练 graduated_seed1。GSM8K 所有结果均为 null。

## 当前状态

- **GPU 0**: 活跃运行（64% util, 327W, 11GB），PID 334631
- **进度**: base + seed0×3 + seed1×2 = 6 evals 完成，剩余 graduated_seed1_eval + seed2×3 = 4 evals
- **预估剩余时间**: ~80 min（每轮 ~20 min）
- **GSM8K**: 所有结果为 null，可能评估失败

## 已有结果（seed0 + seed1，部分数据）

| Benchmark | Base | no_filter (2s) | binary (2s) | graduated (1s) | binary-nf delta |
|-----------|------|----------------|-------------|----------------|-----------------|
| PIQA | 0.7579 | 0.7514 | 0.7527 | 0.7514 | +0.13pp |
| TruthfulQA | 0.4659 | 0.4230 | 0.4408 | 0.4225 | +1.78pp |
| WinoGrande | 0.6456 | 0.6488 | 0.6405 | 0.6488 | -0.83pp |
| ARC-C | 0.5486 | 0.5171 | 0.5192 | 0.5128 | +0.21pp |
| GSM8K | null | null | null | null | - |

初步趋势：binary 在 TruthfulQA 上有较明显优势（+1.78pp），其他 benchmark 差异很小。所有策略相比 base model 均有退化（尤其 TruthfulQA、ARC-C），说明 contaminated data 训练损害了通用能力。

## 建议

实验仍在运行，不更新 registry。GSM8K 全部为 null 需要排查——等实验完成后再统一处理结果收集和 registry 更新。

---
