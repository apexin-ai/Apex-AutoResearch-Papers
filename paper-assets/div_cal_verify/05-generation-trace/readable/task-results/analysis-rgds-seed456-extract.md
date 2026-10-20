# analysis rgds seed456 extract

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rgds_seed456_extract_20260513T232137_result.json`
- **Structured JSON:** [`90383cf8c0be7f046f35.json`](../../sessions/90/90383cf8c0be7f046f35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。汇报如下：

---

## 1. rgds_seed456 Gen7 最终指标

| 指标 | Gen7 值 |
|------|---------|
| PPL | **66.22** |
| RankMe | **286.54** |
| kNN | **0.988** |
| Rare | **0.0069** |
| Corr | **-0.0228** |
| Ratio | **0.8682** |

完成时间：2026-05-14 06:56 CST。PPL 从 Gen0 的 36.7 退化到 Gen7 的 66.22（+80%），Rare 从 0.0284 降至 0.0069，与 seed=42/123 的 RGDS 加速崩塌趋势一致。

## 2. GPU 运行状态

| GPU | PID | 实验 | 说明 |
|-----|-----|------|------|
| cuda:0 | 312677 | **medium_rgds_seed42** | gpt2-medium RGDS, 自 05:27 运行中 |
| cuda:1 | 349822 | **medium_external_seed42** | gpt2-medium external_only, 06:58 启动 |

两块 GPU 各占用 ~28.7GB 显存。

## 3. medium_external 已自动启动

确认：rgds_seed456 于 06:56 完成后，chain 脚本在 cuda:1 上自动启动了 `medium_external` 实验（gpt2-medium external_only, seed=42），日志 `/root/autodl-tmp/div_cal_verify/medium_external.log` 已有输出（07:19 更新）。该实验在 registry 中尚未注册。

---
