# code cleanup and ht check

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cleanup-and-ht-check_20260521T065132_result.json`
- **Structured JSON:** [`5075cf244fa0662ba08f.json`](../../sessions/50/5075cf244fa0662ba08f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕，汇总如下：

---

## 1. 残留进程清理

PID 83304/84455 **已不存在**，无需清理。GPU 0 完全空闲（0 MiB）。

当前所有 GPU 进程均为活跃任务，无 stale 进程：

| GPU | 占用 | PID | 运行时间 | 进程 |
|-----|------|-----|---------|------|
| 0 | **0 MiB, 0%** | — | — | 空闲 |
| 1 | 45908 MiB, 96% | 85675 | 21min | `train.py --condition clean_s4` |
| 1 | (同上) | 88589 | 1.5min | `eval_lz.py --condition contam_15` |
| 2 | 11003 MiB, 56% | 73689 | 2h08m | `train_grpo.py` |
| 3 | 32990 MiB, 95% | 86223 | 21min | `train.py --condition clean_s5` |
| 3 | (同上) | 87524 | 11min | `eval_with_ht.py --stage sft` |

---

## 2. HT Post-RL 分析

**base 阶段已完成**，结果文件 `base_results.json`：
- Overall: accuracy=70.2%, θ_MLE=0.095, lz*=5.97, HT_param=-0.044, HT_nonparam=0.175
- Seen (n=2106): lz*=2.50, HT_param=-0.048, acc=70.0%
- Unseen (n=11936): lz*=5.43, HT_param=-0.043, acc=70.3%

**SFT 阶段正在跑** — PID 87524 (`eval_with_ht.py --stage sft`) 已运行 ~11 分钟。另外 `eval_lz.py --condition contam_15` (PID 88589) 也刚启动 1.5 分钟。

尚无 `ht_*.json` 或 `ht_comparison.json` 输出。

---

## 3. GRPO 和 Seeds 训练

| 任务 | 进度 | ETA | 关键指标 |
|------|------|-----|---------|
| **GRPO** | 55% (3866/7021) | ~1h48m | reward=0.325–0.425, entropy=1.14–1.18 |
| **Seed 4** | 64% (599/939) | ~11min | loss=1.395, token_acc=0.631 |
| **Seed 5** | 66% (619/939) | ~11min | loss=1.357, token_acc=0.642 |

另外有两个 Mistral-7B 下载进程 (PID 72490, 72614) 已跑 2h+，可能卡住了，值得关注。

---
