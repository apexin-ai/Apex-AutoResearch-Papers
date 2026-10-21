# ops piqa metric deep check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_piqa_metric_deep_check_20260520T220631_result.json`
- **Structured JSON:** [`c80c7868ae9145cfabe6.json`](../../sessions/c8/c80c7868ae9145cfabe6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

contamination_rate_sweep 没有 PIQA（benchmark 不同），但确认了 ARC-C 也用 acc_norm。数据全部收集完毕。

## PIQA 指标核查结果

### base_model_eval.json
- PIQA acc = **0.7579**
- PIQA acc_norm = **0.7612**
- 差值 = 0.0033

### `scores` 字典的指标选择（所有文件一致）

**关键发现：`scores` 字典对不同 benchmark 混用了不同指标。**

| Benchmark | scores 用的指标 |
|-----------|----------------|
| PIQA | **acc**（raw） |
| ARC-C | **acc_norm** |
| HellaSwag | **acc_norm** |
| Winogrande | acc（仅有 acc） |
| TruthfulQA MC2 | acc（仅有 acc） |

### 所有文件的 PIQA acc vs acc_norm

| 文件 | PIQA acc | PIQA acc_norm | 差值 |
|------|----------|---------------|------|
| base_model_eval | 0.7579 | 0.7612 | +0.0033 |
| no_filter_seed0 | 0.7519 | 0.7541 | +0.0022 |
| no_filter_seed1 | 0.7508 | 0.7497 | -0.0011 |
| no_filter_seed2 | 0.7497 | 0.7519 | +0.0022 |
| binary_ours_seed0 | 0.7530 | 0.7465 | -0.0065 |
| binary_ours_seed1 | 0.7524 | 0.7497 | -0.0027 |
| binary_ours_seed2 | 0.7530 | 0.7476 | -0.0054 |
| graduated_seed0 | 0.7514 | 0.7530 | +0.0016 |
| graduated_seed1 | 0.7508 | 0.7503 | -0.0005 |
| graduated_seed2 | 0.7492 | 0.7497 | +0.0005 |

### ARC-C 确认

| 文件 | ARC-C acc | ARC-C acc_norm |
|------|-----------|----------------|
| base_model_eval | 0.4915 | 0.5486 |
| no_filter_seed0 | 0.4693 | 0.5128 |
| no_filter_seed1 | 0.4744 | 0.5213 |
| no_filter_seed2 | 0.4676 | 0.5239 |
| binary_ours_seed0 | 0.4787 | 0.5196 |
| binary_ours_seed1 | 0.4735 | 0.5188 |
| binary_ours_seed2 | 0.4744 | 0.5128 |
| graduated_seed0 | 0.4693 | 0.5128 |
| graduated_seed1 | 0.4744 | 0.5230 |
| graduated_seed2 | 0.4684 | 0.5213 |

### 结论

- **0.7579** 对应的是：**acc**（raw accuracy）
- **0.7612** 对应的是：**acc_norm**（length-normalized accuracy）
- `scores` 字典内部不一致：PIQA 取 acc，ARC-C/HellaSwag 取 acc_norm
- Open LLM Leaderboard 惯例：PIQA、ARC-C、HellaSwag 均用 **acc_norm**
- **论文应统一使用：PIQA=acc_norm, ARC-C=acc_norm**（与 leaderboard 一致）
- **需要修正的值**：所有引用 `scores.piqa` 的地方需改为 `full.piqa.acc_norm,none`。base_model 的 PIQA 应报 **0.7612**，而非 0.7579

### contamination_rate_sweep 补充
该实验集不含 PIQA，benchmark 为 MMLU/HellaSwag/ARC-C。其中 ARC-C 和 HellaSwag 均已用 acc_norm，与标准一致。

---
