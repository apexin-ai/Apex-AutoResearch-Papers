# diagnose 5090 32b inference

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_5090_32b_inference_20260521T003610_result.json`
- **Structured JSON:** [`3d6dc1173af353ce2853.json`](../../sessions/3d/3d6dc1173af353ce2853.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 32B FewNERD Inference 状态报告

| 项目 | 状态 |
|------|------|
| **进程** | PID 978386 存活，运行 16m20s |
| **GPU** | 4x RTX 5090，利用率 96-98%，显存 31.3/32.6 GB |
| **进度** | 26,528 / 301,184 prompts（8.8%） |
| **速度** | ~33 it/s，input 5,746 toks/s，output 2,804 toks/s |
| **预估完成** | 约 2-3 小时后（~10:20-11:20 UTC） |
| **磁盘** | 92% 已用，剩余 22GB — 需关注 |
| **输出** | 目录已创建但尚无文件（预计结束时写出） |

已完成：
- Registry 已更新（exp_32b_inference_fewnerd → RUNNING，含 PID/GPU/进度信息）
- Cron 监控已注册（每 15 分钟检查一次进度，进程结束后自动更新状态）

⚠️ 磁盘 92% 需关注，301K prompts × 8 samples 的输出可能较大。

---
