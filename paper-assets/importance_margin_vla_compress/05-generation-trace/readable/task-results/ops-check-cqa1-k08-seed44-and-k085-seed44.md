# ops check cqa1 k08 seed44 and k085 seed44

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-cqa1-k08-seed44-and-k085-seed44_20260520T224824_result.json`
- **Structured JSON:** [`3289b3553aaf457214d7.json`](../../sessions/32/3289b3553aaf457214d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated for k08_seed44. Now the summary:

## 结果汇总

### GPU 状态 (cqa1-33015)
| GPU | Util | VRAM |
|-----|------|------|
| 0 | 0% | 空闲 |
| 1 | 0% | 空闲 |
| 2 | 63% | 4.5/24GB — running k085_seed44 |
| 3 | 0% | 空闲 |

### k=0.8 (keep 40/50 tokens) — 全部完成 ✓

| Seed | SR | Successes | Wilson CI 95% |
|------|----|-----------|---------------|
| 42 | 88.8% | 444/500 | [85.7%, 91.3%] |
| 43 | 88.4% | 442/500 | [85.3%, 90.9%] |
| 44 | 89.8% | 449/500 | [86.8%, 92.2%] |
| **Mean** | **89.0%** | | |

JSON 文件问题：seed43 和 seed44 的 JSON 文件缺失（日志数据完整），seed42 的 JSON 正常。可能是并发写入或 cron 调度问题。

### k=0.85 (keep 42/50 tokens) — seed44 仍在运行

| Seed | SR | Successes | Wilson CI 95% |
|------|----|-----------|---------------|
| 42 | 68.0% | 340/500 | [63.8%, 71.9%] |
| 43 | 67.6% | 338/500 | [63.4%, 71.6%] |
| 44 | **运行中** (~6/10 tasks done) | 228/300 so far | — |
| **Mean (2-seed)** | **67.8%** | | |

k085_seed44 已完成 task 0-5，当前在 task 6 (butter, 预期 0%)。预计还需 ~30-40 分钟完成 task 6-9。

### Cliff 定位结论

**Cliff 位于 keep_ratio 0.80 → 0.85 之间**：
- k=0.80: 3-seed mean = **89.0%** (方差极小，σ≈0.6pp)
- k=0.85: 2-seed mean = **67.8%** (方差极小，σ≈0.2pp)
- **Drop: ~21 个百分点**，仅移除 2 个额外 token (40→42 kept)

k=0.85 的崩溃主要来自 task 6 (butter: 0%) 和 task 4 (ketchup: ~27%)，而 k=0.80 这些任务仍有 56-82% 的成功率。

### 待完成
- k085_seed44 运行完成后需更新 registry（预计 ~30min 后）

---
