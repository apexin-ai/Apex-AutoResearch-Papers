# ops d034 check ckpt7080 step90 gpus

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d034-check-ckpt7080-step90-gpus_20260514T195737_result.json`
- **Structured JSON:** [`fb4db553fdc3159179bf.json`](../../sessions/fb/fb4db553fdc3159179bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## 1. ckpt7080 eval — 双双失败

- **checkpoint-70**: OOM killed (exit -9)，仅推理到 2/62 batches (3%)
- **checkpoint-80**: 启动推理后也死了——日志停在 "Inference: 0%"，无 EXIT_CODE，无 GPU 进程，无 exit file

**根因**: eval 脚本未指定 GPU，默认用 GPU 0。ckpt-70 运行时 step-90 eval 仍在 GPU 0 上（两进程抢显存 → OOM）；ckpt-80 启动时 P0 训练已占 GPU 0（13.6 GB）→ 同样 OOM。

**修复建议**: 重跑时加 `CUDA_VISIBLE_DEVICES=1` 或 `CUDA_VISIBLE_DEVICES=3`（当前空闲）。

---

## 2. step-90 eval — 已完成 ✓

| 指标 | 值 |
|------|-----|
| F1 | 0.2108 |
| Ign-F1 | 0.2108 |
| Evi-F1 | 0.5666 |
| EDCR | 0.8584 |
| Format OK | 985/985 (100%) |
| Truncated | 22/985 |
| Predictions | 11160 |

进程 83207 已退出，metrics 写入 `/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-90/metrics.json`。

---

## 3. GPU 状态

| GPU | VRAM | Util | 进程 |
|-----|------|------|------|
| 0 | 13645/32607 MiB | 56% | PID 90085 — P0 GRPO 训练 |
| **1** | **0/32607 MiB** | **0%** | **空闲** |
| 2 | 10297/32607 MiB | 71% | PID 85997 — checkpoint-20 eval (运行 48 min) |
| **3** | **0/32607 MiB** | **0%** | **空闲** |

**GPU 1、3 空闲**，可用于 P0 补充任务或 P1。

---

## 4. P0 训练 (grpo_ced_lr5e6_r1) — 存活但有隐患

- PID 90080 存活，已运行 18 min
- 当前进度: **step 9/200** (4.5%)，~110s/step
- **⚠️ KL 爆炸**: step 5 时 KL divergence = **2,412,554,396.9**（阈值 100.0，超了 2400 万倍）。当前为 monitoring-only 未停止，但这个量级意味着 policy 已严重偏离 reference model，后续 reward 和 loss 很可能崩坏。
- 日志中尚未出现 f1_reward 数值（step 太早，还在 warmup 阶段）。

---
