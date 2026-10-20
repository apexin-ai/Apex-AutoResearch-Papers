# ssh check gpu status 20260513

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_gpu_status_20260513_20260513T213318_result.json`
- **Structured JSON:** [`b5d59287e7274aa96adc.json`](../../sessions/b5/b5d59287e7274aa96adc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| | cuda:0 | cuda:1 |
|---|---|---|
| **显存** | 68,433 / 97,887 MiB (70%) | 21,687 / 97,887 MiB (22%) |
| **GPU 利用率** | 39% | 0% (训练间隙) |
| **当前任务** | **medium_rgds** (gpt2-medium, rgds, seed=42) | **ext_seed456** (gpt2, external_only, seed=456) |
| **进度** | **Gen 0/7** — 刚启动 (~8 min) | **Gen 7/7** — step [3/5] Training student，接近完成 |
| **Chain 脚本** | chain_cuda0 运行中 | chain_cuda1 运行中，等待 seed456_methods 完成 |

**已完成任务：**
- **medium_uncurated** (gpt2-medium, seed=42)：已跑完全部 8 代 (gen_0–gen_7)，chain_cuda0 于 05:25 自动切换到 medium_rgds
- ext_seed456 的 gen_0–gen_6 均已完成，gen_7 正在训练中

**Chain 调度：**
- chain_cuda0：medium_uncurated ✅ → **medium_rgds** (进行中) → 后续任务待定
- chain_cuda1：正在 `sleep 60` 轮询等待 seed456_methods 组（uncurated_seed456 → ext_seed456 → rgds_seed456）完成，ext_seed456 是该组的第二个，完成后自动启动 rgds_seed456

---
