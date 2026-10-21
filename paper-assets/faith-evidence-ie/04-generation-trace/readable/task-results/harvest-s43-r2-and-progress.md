# harvest s43 r2 and progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_s43_r2_and_progress_20260519T055844_result.json`
- **Structured JSON:** [`e80081c00a7dd0fbd846.json`](../../sessions/e8/e80081c00a7dd0fbd846.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总报告：

---

## 实验状态汇总

### 1. plan019_1_7b_rsft_s43_r2 — 已完成
- **Final loss**: 0.5526 @ step 567/567
- Loss 趋势: 520→0.5352, 530→0.5519, 540→0.5683, 550→0.5482, 560→0.5526
- checkpoint-567 完整（adapter_model.safetensors 278MB + 全部文件）
- Registry metrics 已更新

### 2. 三个 running 实验进度

| 实验 | GPU | 进度 | 最新 loss | 剩余 steps |
|------|-----|------|-----------|------------|
| d112_rsft_s44_train | cuda:0 (29.6/32.6 GB) | **350/567** (62%) | 0.6624 | 217 |
| plan019_1_7b_rsft_s44_r2 | cuda:3 (27.5/32.6 GB) | **300/567** (53%) | 0.5459 | 267 |
| plan017_14b_sft | cuda:1+2 (16.1+25.2/32.6 GB) | **48/144** (33%) | 0.6035 | 96 |

### 3. GPU 显存

| GPU | 显存占用 | 利用率 | 进程 PID |
|-----|----------|--------|----------|
| cuda:0 | 29.6 / 32.6 GB | 19% | 613083 |
| cuda:1 | 16.1 / 32.6 GB | 84% | 611578 |
| cuda:2 | 25.2 / 32.6 GB | 82% | 611579 |
| cuda:3 | 27.5 / 32.6 GB | 99% | 618028 |

四卡全部在用，无空闲 GPU。所有 PID 与 registry 记录的略有偏差（d112 registry PID 613075 vs 实际 613083，plan019_s44 registry 618021 vs 实际 618028），可能是子进程。三个实验都在正常推进。

---
