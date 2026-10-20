# ssh progress check 016 017

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_progress_check_016_017_20260522T073721_result.json`
- **Structured JSON:** [`77d4c9f03ea34cc0f6a4.json`](../../sessions/77/77d4c9f03ea34cc0f6a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### exp_016 — r=0.3, seed44, cuda:0
| 项目 | 状态 |
|------|------|
| 当前阶段 | **Generation 5/10 — 正在生成合成数据** (15,360/35,000 samples, 44%) |
| 已完成 | gen 0 (baseline) + gen 1–4 (results JSON 已写入 5 条) |
| 运行时长 | ~8.4h（07:16 UTC 启动） |
| 每代耗时 | ~100 min/gen |
| 剩余 | ~5.5 代 → **预计还需 ~9–10h**，约 UTC 01:00–02:00 (May 23) 完成 |

### exp_017 — r=0.2, seed43, cuda:1
| 项目 | 状态 |
|------|------|
| 当前阶段 | **Generation 1/10 — 正在生成合成数据** (29,120/40,000 samples, 73%) |
| 已完成 | gen 0 (baseline eval)，尚未产出 results JSON |
| 运行时长 | ~1.4h（14:18 UTC 启动） |
| 每代耗时 | 估计 ~90–100 min/gen（r=0.2 合成量更大: 40k vs 35k） |
| 剩余 | ~9.3 代 → **预计还需 ~14–15h**，约 UTC 05:00–06:00 (May 23) 完成 |

### 资源状态
| 资源 | 状态 |
|------|------|
| GPU 0 | 93% 利用率, 25.0/95.6 GB 显存 |
| GPU 1 | 90% 利用率, 19.0/95.6 GB 显存 |
| 磁盘 | **25G/30G (83%)** — 剩余 5.2G，偏紧，两个实验各产出 ~1.5G checkpoint/gen，需关注 |

**注意**：磁盘仅剩 5.2G，两个实验共还需写约 15 代的 checkpoint（每代 ~1.5G），如果 checkpoint 是覆盖式保存（只留最新）则无碍，否则会爆盘。

---
