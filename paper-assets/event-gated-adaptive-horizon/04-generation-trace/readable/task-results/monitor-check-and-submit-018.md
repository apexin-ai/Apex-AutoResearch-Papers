# monitor check and submit 018

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_check-and-submit-018_20260516T025531_result.json`
- **Structured JSON:** [`a59bf20a1aced101ac0d.json`](../../sessions/a5/a59bf20a1aced101ac0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### 009d — Walker Baseline (cuda:0, PID 149708)
- **状态**: 运行中，已运行 14h31m
- **进度**: step 344,000 / 500,000 (68.8%)
- **最新 eval_return**: 933.17 @ step 338K（峰值 949.46 @ step 328K）
- **train_return**: ~841–949 @ step 344K
- **FPS 估算**: ~9.6K steps/hr → 预计还需 ~16h 完成

### 010a — Cheetah Baseline (cuda:1, PID 536890)
- **状态**: 运行中，已运行 4h08m
- **进度**: step 165,000 / 512,000 (32.2%)
- **最新 eval_return**: 582.95 @ step 165K（峰值 592.59 @ step 155K）
- **FPS**: 11.0 steps/s → 预计还需 ~8.8h 完成

### GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 16% | 4,165 / 97,887 MiB |
| 1 | 38% | 4,690 / 97,887 MiB |

### 结论
**009d 未完成**，还在跑，预计约明天凌晨结束。010a 进度约 1/3。两个实验都在正常运行，无需干预。018 提交需等 009d 跑完。

---
