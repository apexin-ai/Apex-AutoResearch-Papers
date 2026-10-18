# audit urgent full scan 7gpu idle

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_urgent_full_scan_7gpu_idle_20260523T000330_result.json`
- **Structured JSON:** [`339c07355f4298166ba9.json`](../../sessions/33/339c07355f4298166ba9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。14/14 GPU 已满载。

---

## 14 GPU 逐卡表格

| 服务器:GPU | 实验 | 状态 | PID | SR |
|------------|------|------|-----|----|
| westd-38929:0 | Random k=0.9 Long seed43 | RUNNING | 209581 | ~30.8% (进行中) |
| westd-38929:1 | **L2norm k=0.7 Long seed43** | **新部署** | loading | — |
| westd-38929:2 | **Random k=0.3 Long seed43** | **新部署** | loading | — |
| westd-38929:3 | **L2norm k=0.85 Long seed43** | **新部署** | loading | — |
| westd-41074:0 | Random k=0.85 Long seed43 | RUNNING | 185720 | — |
| westd-41074:1 | L2norm k=0.3 Long seed43 | RUNNING | 149709 | — |
| westd-41074:2 | Random k=0.5 Long seed43 v2 | RUNNING | 192839 | — |
| westd-41074:3 | M64 训练 (81300/100000) | RUNNING | 59671 | ~8.7h 完成 |
| westd-27271:0 | L2norm k=0.3 Long seed42 | RUNNING | 912230 | — |
| westd-27271:1 | L2norm k=0.5 Long seed43 | RUNNING | 912303 | — |
| cqa1-33015:0 | L2norm k=0.7 Goal seed43 | RUNNING | 66871 | — |
| cqa1-33015:1 | Random k=0.95 Goal seed43 | RUNNING | 67046 | — |
| cqa1-33015:2 | Random k=0.3 Goal seed43 | RUNNING | 946063 | — |
| cqa1-33015:3 | L2norm k=0.85 Long seed42 | RUNNING | 114091 | — |

## 新收割结果 (3 experiments → DONE)

| exp_id | SR | 备注 |
|--------|-----|------|
| eval_pi05_random_k03_long_seed42 | **29.0%** | Long 极端压缩 floor |
| eval_pi05_l2norm_k05_long_seed42 | **50.2%** | L2norm = Random 在 k=0.5 |
| eval_xvla_random_k095_object_seed42_v2 | **98.8%** | Random ≈ L2norm(97.6%), 确认 method-independence |

## 额外发现的已完成结果 (Goal suite, cqa1)

| 实验 | SR |
|------|-----|
| Random k=0.95 Goal seed42 | 84.0% |
| L2norm k=0.95 Goal seed42 | 89.4% |
| L2norm k=0.7 Goal seed42 | 71.8% |
| Random k=0.3 Goal seed42 | 51.8% |
| Random k=0.85 Goal seed42 | 52.4% |
| Random k=0.9 Goal seed42 | 62.6% |

## 部署计划 (已执行)

| GPU | 新部署实验 | tmux session |
|-----|-----------|-------------|
| westd-38929:1 | L2norm k=0.7 Long seed43 | eval_l2norm_k07_long_s43 |
| westd-38929:2 | Random k=0.3 Long seed43 | eval_random_k03_long_s43 |
| westd-38929:3 | L2norm k=0.85 Long seed43 | eval_l2norm_k085_long_s43 |

利用率从 11/14 (78.6%) 恢复到 **14/14 (100%)**。

---
