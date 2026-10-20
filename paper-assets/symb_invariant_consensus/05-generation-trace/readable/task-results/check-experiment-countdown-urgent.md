# check experiment countdown urgent

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_experiment-countdown-urgent_20260523T051009_result.json`
- **Structured JSON:** [`e56ba7df883fed9305f4.json`](../../sessions/e5/e56ba7df883fed9305f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

qwen25_pw_seed456 确认无进程运行。现在汇总结果。

## 实验倒计时表 (UTC: 2026-05-23 05:12)

### 活跃实验 (westd-16639, 4×GPU 97%)

| 实验 | GPU | Port | 进度 | 速率 | 剩余 | 预计完成 (UTC) |
|------|-----|------|------|------|------|----------------|
| Qwen2.5 PW seed123 | cuda:3 | 8005 | 474/600 (79%) | 0.87/min | 146 min | 05-23 07:38 |
| LLaMA-8B PW seed123 | cuda:1 | 8006 | 430/600 (72%) | 0.79/min | 216 min | 05-23 08:49 |
| Qwen2.5 PW seed789 (v2) | cuda:2 | 8007 | 53/600 (9%) | 0.85/min | 641 min | 05-23 15:54 |
| LLaMA-8B PW seed789 | cuda:0 | 8009 | 12/600 (2%) | 0.70/min | 838 min | 05-23 19:11 |

> LLaMA seed789 仅 12 样本，速率估计可能偏低，后续会稳定到 ~0.8/min。

### 已停止

| 实验 | 进度 | 状态 |
|------|------|------|
| **Qwen2.5 PW seed456** | **478/600** | **已停止 19min，无活跃进程** |
| LLaMA-8B PW seed42 | 223/600 | 已停止 (12h+) |

### 已完成

| 实验 | 进度 | 状态 |
|------|------|------|
| Mistral PW seed42/123/456/789 | 600/600 ×4 | DONE |
| 全部 FOLIO (3模型×3种子=9组) | 204/204 ×9 | DONE (FOLIO 数据集=204条) |

### Qwen seed456 恢复计划

- **当前状态**: 478/600 截断，无活跃进程，文件 19min 前最后更新
- **恢复方案**: 当前 4 GPU 全部占用，需等待一个实验完成后释放 GPU。最快释放的是 **Qwen seed123 (cuda:3)**，预计 07:38 UTC 完成。届时可用同一 vLLM (port 8005) 以 `--resume` 或从 478 继续跑剩余 122 条
- **预计恢复完成时间**: 07:38 + 122/0.85 ≈ 07:38 + 144min ≈ **05-23 10:02 UTC**

### westd-14391

该服务器不在当前项目配置中，未检查。如需检查请确认服务器名称。

---
