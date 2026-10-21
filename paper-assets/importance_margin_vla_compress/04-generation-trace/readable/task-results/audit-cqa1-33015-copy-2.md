# audit cqa1 33015

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_cqa1-33015_20260523T110812_result.json`
- **Structured JSON:** [`1ec2f32044007703deb3.json`](../../sessions/1e/1ec2f32044007703deb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the complete picture. Here's the audit report:

---

## cqa1-33015 服务器审计报告

### GPU 状态
| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| 0 | 0% | 9671/24564 MiB | 空闲 |
| 1 | 61% | 10307/24564 MiB | 运行中 |
| 2 | 24% | 10156/24564 MiB | 运行中 |
| 3 | 49% | 10307/24564 MiB | 运行中 |

### 已完成实验（今天新产出的 seed43 复现）

| 实验 | SR | 对比 seed42 | 结果文件 |
|------|-----|------------|----------|
| π0.5 Random k=0.7 Object s43 | **78.6%** | 78.6% (一致) | `pi05_random_k0.70_libero_object_seed43.json` |
| π0.5 Random k=0.5 Object s43 | **66.2%** | ~66% (一致) | `pi05_random_k0.50_libero_object_seed43.json` |
| π0.5 L2norm k=0.7 Object s43 | **56.8%** | 56.8% (一致) | `pi05_l2norm_k0.70_libero_object_seed43.json` |
| π0.5 L2norm k=0.5 Object s43 | **32.0%** | ~32% (一致) | `pi05_l2norm_k0.50_libero_object_seed43.json` |

seed43 与 seed42 结果高度一致，复现性良好。

### 正在运行的实验（4 个 tmux session）

| 实验 | 进度 | 当前 SR | 预计完成 |
|------|------|---------|----------|
| L2norm k=0.85 Object s43 | T8/10 完成 | **98.9%** | ~20 min |
| Random k=0.85 Object s43 | T4/10 | **3.5%** | ~1.5 hr |
| L2norm k=0.3 Object s43 | T0/10 刚开始 | 40% (10ep) | ~2.5 hr |
| Random k=0.3 Object s43 | T0/10 刚开始 | 50% (10ep) | ~2.5 hr |

### 异常标记

**Random k=0.85 结果异常**：当前 3.5% SR（7/200），对于保留 85% token 的 random pruning 来说极不合理。对比 Random k=0.7 的 78.6%，k=0.85 应该更高才对。配置确认正确（keep 217/256），但结果暗示可能存在 bug 或 seed-specific 问题。建议实验完成后复查。

**L2norm k=0.85 表现优异**：98.9% 接近 baseline（98.2%），说明 L2norm 在高 keep ratio 下几乎无损。

### 之前的 k=0.3/k=0.85 旧 run（May 22）
全部停在 T3-T4 且所有 task 均 0%，已被杀掉并重新启动（今天 17:48-19:03）。新 run 的 k=0.3 实验 T0 已显示非零 SR，说明旧 run 的问题已修复。

---
