# infra exp006 final completion

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp006-final-completion_20260515T091423_result.json`
- **Structured JSON:** [`4100252453b4baa76bf0.json`](../../sessions/41/4100252453b4baa76bf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，汇总如下：

---

## 1. exp-006 完成状态：**51/51** ✓

## 2. 结果汇总（按 MMLU 降序）

| Strategy | MMLU (mean±std) | HellaSwag (mean±std) |
|---|---|---|
| base_model | 0.6018±0.0000 | 0.6821±0.0000 |
| binary-ours | 0.5941±0.0008 | 0.6701±0.0006 |
| binary-drayson | 0.5913±0.0009 | 0.6691±0.0004 |
| surprisal | 0.5894±0.0009 | 0.6641±0.0006 |
| graduated_a0.7 | 0.5892±0.0014 | 0.6695±0.0004 |
| graduated_a0.9 | 0.5892±0.0008 | 0.6701±0.0007 |
| graduated_a0.5 | 0.5880±0.0013 | 0.6687±0.0008 |
| graduated_a0.3 | 0.5877±0.0013 | 0.6669±0.0005 |
| graduated_a0.1 | 0.5873±0.0019 | 0.6640±0.0009 |
| dsir | 0.5869±0.0003 | 0.6631±0.0007 |
| no-filter | 0.5865±0.0010 | 0.6638±0.0008 |

注：实际为 10 个策略（no-filter, binary-ours, binary-drayson, graduated×5, surprisal, dsir）× 5 seeds + 1 base_model = 51 runs。所有策略 MMLU 都低于 base_model（0.6018），binary-ours 最接近（0.5941）。

## 3. GPU 状态
- 当前：83% 利用率，4251/24564 MiB 显存占用（exp-015 运行中）

## 4. exp-015 已启动 ✓
- tmux session `exp015` 运行中
- 正在提取 pythia-1.4b embeddings（模型 1/3），~150 it/s
- 日志：`logs/exp015_neural_probe_v3.log`

---
