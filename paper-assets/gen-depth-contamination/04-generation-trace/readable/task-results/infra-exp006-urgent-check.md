# infra exp006 urgent check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp006-urgent-check_20260515T021558_result.json`
- **Structured JSON:** [`9c8990ece794af1be73d.json`](../../sessions/9c/9c8990ece794af1be73d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Exp-006 状态报告

### 进度: 39/51 完成（38 策略 runs + 1 base_model）

**当前**: `graduated_a0.9_s789` 训练中，96% (2696/2814 steps)
**剩余**: graduated_a0.9 ×2, surprisal ×5, dsir ×5 = 12 runs, 预计 ~7h

---

### 已完成结果汇总（MMLU / HellaSwag acc_norm, mean±std）

| Strategy | n | MMLU | HellaSwag |
|---|---|---|---|
| **base_model** | 1 | **0.6018** | **0.6821** |
| binary-ours | 5 | **0.5941±0.0009** | 0.6701±0.0007 |
| binary-drayson | 5 | 0.5913±0.0011 | 0.6691±0.0005 |
| graduated_a0.7 | 5 | 0.5892±0.0016 | 0.6695±0.0004 |
| graduated_a0.9 | 3 | 0.5891±0.0012 | 0.6703±0.0007 |
| graduated_a0.5 | 5 | 0.5880±0.0015 | 0.6687±0.0009 |
| graduated_a0.3 | 5 | 0.5877±0.0014 | 0.6669±0.0006 |
| graduated_a0.1 | 5 | 0.5873±0.0021 | 0.6640±0.0011 |
| no-filter | 5 | 0.5865±0.0012 | 0.6638±0.0009 |

### 关键发现

1. **所有训练策略都 degradation 了 base_model**：MMLU 从 0.6018 降到 0.586-0.594，HellaSwag 从 0.6821 降到 0.664-0.670。这是 continual training 的典型现象。

2. **binary-ours 是目前最好的**：MMLU 0.5941，显著高于 no-filter (0.5865)，说明过滤确实有效减轻 contamination 损害。

3. **α sweep 趋势（graduated）**：
   - α=0.1 → 0.5873 (MMLU), 0.6640 (HS)
   - α=0.3 → 0.5877, 0.6669
   - α=0.5 → 0.5880, 0.6687
   - α=0.7 → 0.5892, 0.6695
   - α=0.9 → 0.5891, 0.6703 (3 seeds)
   
   **单调递增趋势**：α 越大（越接近 binary-ours），MMLU 和 HellaSwag 都越好。目前没有看到最优中间点，graduated filtering 没有优于 binary-ours。

4. **binary-ours > binary-drayson**：0.5941 vs 0.5913，我们的方法优于 Drayson baseline。

5. **等待 surprisal 和 dsir**：这两个是关键 baseline 对比，目前还没跑完。

---
