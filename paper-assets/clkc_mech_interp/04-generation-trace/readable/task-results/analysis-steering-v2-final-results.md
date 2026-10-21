# analysis steering v2 final results

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_steering-v2-final-results_20260522T132532_result.json`
- **Structured JSON:** [`49bb2510a0bfdba3cb1b.json`](../../sessions/49/49bb2510a0bfdba3cb1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均正常完成，无报错。以下是完整汇报：

---

## L13 Steering 完整结果 (v2a)

Probe accuracy: 0.761 | Baseline: p=32, c=41, both=35, neither=28

| α | Steering flips | Control flips | p→c | c→p | Fisher p | 
|---|---|---|---|---|---|
| **-20** | 49/136 (36.0%) | 24/136 (17.6%) | 1 | 5 | **0.0009** |
| -10 | 31/136 (22.8%) | 25/136 (18.4%) | 2 | 1 | 0.454 |
| -5 | 22/136 (16.2%) | 17/136 (12.5%) | 2 | 1 | 0.489 |
| -2 | 16/136 (11.8%) | 9/136 (6.6%) | 0 | 1 | 0.207 |
| -1 | 7/136 (5.2%) | 6/136 (4.4%) | 0 | 0 | 1.0 |
| +1 | 11/136 (8.1%) | 6/136 (4.4%) | 1 | 0 | 0.317 |
| +2 | 16/136 (11.8%) | 7/136 (5.2%) | 3 | 0 | 0.079 |
| **+5** | 27/136 (19.9%) | 9/136 (6.6%) | 4 | 0 | **0.0020** |
| +10 | 31/136 (22.8%) | 20/136 (14.7%) | 2 | 0 | 0.120 |
| +20 | 28/136 (20.6%) | 43/136 (31.6%) | 2 | 2 | 0.053 |

**方向性清晰**：负α → c2p（5 flips at α=-20），正α → p2c（4 flips at α=+5）。最显著点在 α=-20 (p=0.0009) 和 α=+5 (p=0.002)。α=+10/+20 效果下降，可能因过大 perturbation 导致 degradation（α=+20 时 control flips 反超 steering flips）。

## L18 Steering 完整结果 (v2b)

Probe accuracy: 0.739 | Baseline: 同上

| α | Steering flips | Control flips | p→c | c→p | Fisher p |
|---|---|---|---|---|---|
| -20 | 28/136 (20.6%) | 25/136 (18.4%) | 0 | 4 | 0.760 |
| -10 | 18/136 (13.2%) | 17/136 (12.5%) | 0 | 1 | 1.0 |
| -5 | 7/136 (5.2%) | 9/136 (6.6%) | 0 | 0 | 0.798 |
| -2 | 3/136 (2.2%) | 5/136 (3.7%) | 0 | 0 | 0.722 |
| -1 | 3/136 (2.2%) | 5/136 (3.7%) | 0 | 0 | 0.722 |
| +1 | 4/136 (2.9%) | 3/136 (2.2%) | 1 | 0 | 1.0 |
| +2 | 5/136 (3.7%) | 2/136 (1.5%) | 1 | 0 | 0.447 |
| +5 | 9/136 (6.6%) | 7/136 (5.2%) | 1 | 0 | 0.798 |
| +10 | 14/136 (10.3%) | 12/136 (8.8%) | 1 | 0 | 0.837 |
| +20 | 24/136 (17.6%) | 26/136 (19.1%) | 1 | 1 | 0.876 |

**无显著效果**。所有 alpha 的 Fisher p 均 > 0.44，steering flips 与 control flips 无显著差异。L18 方向不可 steer。

## GPU 状态

| GPU | VRAM used | VRAM total | Util |
|-----|-----------|------------|------|
| 0 | 16,379 MiB | 97,887 MiB | 6% |
| 1-3 | 3 MiB | 97,887 MiB | 0% |

GPU 0 有约 16GB 占用（可能是某个进程残留或模型缓存），GPU 1-3 空闲。

## 其他任务状态

| 任务 | 状态 |
|------|------|
| DE translate | **完成** — test: 272 行, train: 1096 行 |
| Llama bootstrap n=2000 | **文件不存在** — 未开始或未产出 |
| Qwen bootstrap n=2000 | **文件存在** (22KB, 21:08 更新) — 需进一步检查内容 |
| Gemma bootstrap n=2000 | **文件不存在** — 未开始 |
| C3 MLP bootstrap | **无 bootstrap 文件** — 仅有 `mlp_probe_results.json`（非 bootstrap 版） |

## 异常

- 日志文件名是 `steering_llama_L13_last.log` 而非 `steering_L13_last.log`（路径修正后读取正常）
- Llama bootstrap n=2000 文件缺失，需确认是否已启动
- GPU 0 有 16GB 占用但利用率仅 6%，可能是进程已退出但显存未释放

---
