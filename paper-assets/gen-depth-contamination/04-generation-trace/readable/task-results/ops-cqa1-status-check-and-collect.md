# ops cqa1 status check and collect

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-status-check-and-collect_20260518T212956_result.json`
- **Structured JSON:** [`6a01af72439c4758314f.json`](../../sessions/6a/6a01af72439c4758314f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

OLMo 僵尸已清理（PID 78990 已杀）。结果文件已写入。

---

## 实验状态汇总

### 1. exp_qwen_retrain_chain (cuda:0, PID 86210)
**状态：运行中** — bootstrap CI 阶段，4 对中已完成 2 对

| Pair | 5-fold CV AUC | Bootstrap AUC | 95% CI |
|------|--------------|---------------|--------|
| 0v1  | 0.9838       | 0.9942        | [0.9933, 0.9950] |
| 1v2  | 0.8969       | 0.9611        | [0.9580, 0.9640] |
| 2v3  | 0.8100       | *running*     | — |
| 3v4  | 0.7624       | *pending*     | — |

- **K\* = 4**（已确认）
- **JSD**: 0v1=0.226, 1v2=0.105, 2v3=0.075, 3v4=0.065（单调递减）
- 每对 bootstrap 约 30-34 分钟，预计 **~06:10 UTC** 全部完成（约 40 分钟后）
- GPU 0: 3394MiB / 24564MiB, 0% util（CPU 密集型 bootstrap 阶段）

### 2. exp_code_llama8b (cuda:2, PID 96340)
**状态：运行中** — depth 1 生成阶段，506/1375 batches (37%)

- 模型: LLaMA-3.1-8B, scorer: Qwen2.5-1.5B
- 参数: 5000 samples, max_depth=5, batch_size=4, continuation mode
- 当前速度: ~5.9 s/batch
- **预估剩余时间**:
  - depth 1 剩余: ~85 min
  - depth 2-5: 每个 ~2.25 h, 共 ~9 h
  - 加上 scoring + features + analysis: **总计 ~10-11 小时**（约 15:30-16:30 UTC）
- GPU 2: 16052MiB / 24564MiB, 95% util

### 3. OLMo 僵尸
**已清理** — PID 78990 (tmux session `olmo_download`) 已杀。下载曾因网络超时失败（FileNotFoundError）。其余 PID（78429, 78613, 78940, 78997）此前已不存在。

### GPU 分配
| GPU | 占用 | 利用率 | 用途 |
|-----|------|--------|------|
| 0   | 3.4G/24.6G | 0% | qwen_retrain (bootstrap CPU phase) |
| 1   | 空闲 | 0% | — |
| 2   | 16.1G/24.6G | 95% | code_llama8b |
| 3   | 空闲 | 0% | — |

### 磁盘
`/root/autodl-tmp`: 74G/250G used (30%)

### 产出文件
- `artifacts/exp_qwen_retrain_chain/final_results.json` — 已写入当前可用数据（AUC、JSD、已完成的 bootstrap CI），标记 bootstrap 未完成部分为 pending

---
