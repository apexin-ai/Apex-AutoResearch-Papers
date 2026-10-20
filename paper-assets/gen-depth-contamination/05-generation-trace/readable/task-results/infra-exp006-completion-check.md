# infra exp006 completion check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp006-completion-check_20260515T073823_result.json`
- **Structured JSON:** [`6dbad000f4b34a982124.json`](../../sessions/6d/6dbad000f4b34a982124.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-006 进度报告

**48/51 runs 完成**

### 当前状态
- tmux session `exp_006_graduated_filtering` 仍在运行
- 正在执行：`dsir_s456` 评估阶段（loglikelihood requests ~21%, 20250/96336）
- 待完成：`dsir_s789`, `dsir_s1024`（训练+评估）

### 已完成的 dsir 结果（2/5 seeds）

| Run | MMLU | HellaSwag (acc_norm) |
|-----|------|---------------------|
| dsir_s42 | 0.5868 | 0.6641 |
| dsir_s123 | 0.5865 | 0.6633 |

### 时间估算
- `dsir_s123` eval 完成于 14:56 CST，`dsir_s456` eval 开始于 15:33 CST（含训练约 37 分钟/run）
- `dsir_s456` eval 已跑约 5 分钟，剩余约 10 分钟
- 还需 2 个完整 run（训练+评估），每个约 40-45 分钟
- **预计全部完成时间：约 17:10-17:30 CST（09:10-09:30 UTC）**

---
