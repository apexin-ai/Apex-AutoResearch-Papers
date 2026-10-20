# ops cuda3 oom triage

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda3-oom-triage_20260515T202010_result.json`
- **Structured JSON:** [`d7d762aedcbfe4e85bfd.json`](../../sessions/d7/d7d762aedcbfe4e85bfd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 任务 1：cuda:3 OOM 风险 — 紧急但暂未爆

**当前状态**（04:22:35）：

| PID | 进程 | 显存 | 状态 |
|-----|------|------|------|
| 627614 | 1.5B s123 eval | 5,880 MiB | GSM8K paraphrased 57/228, ~28 min 剩余 |
| 628112 | signals（身份不明） | 7,946 MiB | 仍在运行 |
| 630891 | **v6 s4 selfcritique mmlu** | 6,788 MiB | **刚启动**，7/7021 batches，ETA ~5 小时 |

**总占用 20,633 / 24,564 MiB，剩余 3,931 MiB（16%）**

关键变化：
- PID 629264 已不存在（中间进程，已退出）
- PID 630007（v6 s2 minkpp mmlu）已完成并释放
- **新进程 PID 630891 是 s4 selfcritique mmlu**（batch_size=2，14042 items），这正是你说的内存峰值最高环节
- selfcritique 还在 warm-up 阶段（6,788 MiB），长序列生成时峰值可能 +1~3 GB
- 如果峰值达到 ~9.5 GB，总显存 ~23.3 GB，**仍有 ~1.2 GB 余量但非常危险**
- 如果峰值超过 ~10.7 GB → **OOM**

**判断：大概率能存活但处于危险边缘。** selfcritique 3B 模型 batch_size=2 的峰值通常在 7-9 GB 范围内，但 MMLU 长文本可能导致更高峰值。PID 628112 身份不明是隐患——如果它也是 selfcritique 且出现峰值，两个同时 spike 就会 OOM。

**建议**：kill PID 628112（未知 signals 进程，7,946 MiB），立刻释放 ~8 GB。这样 cuda:3 只剩 eval + selfcritique ≈ 12.7 GB，留出 ~12 GB 安全余量。等你确认是否执行。

---

### 任务 2：GPU 0 — 正常

| 指标 | 值 |
|------|-----|
| PID 594494 | 17,966 MiB, GPU-Util **71%** |
| SFT 进度 | **step 3182/4159 (76%)**，epoch 0.76，ETA ~1h07m |
| Loss | 1.05-1.25 范围，正常下降 |
| Token accuracy | ~0.72-0.74 |

Reviewer 报告的 "compute 0%" 是暂态（可能 checkpoint save 瞬间或 data loading gap）。**进程完全正常，无需干预。**

---

### 任务 3：stale 文件清理

`/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_s42/`：

- **总大小：21 MB**
- **13 个文件**：embedding/minkpp/selfcritique signals for mmlu/arc_challenge/gsm8k + merged 文件
- 最新修改时间：2026-05-16 03:08
- 缺少 mmlu 的 selfcritique 和 merged 文件（未完成的旧跑）

21 MB 不大，但该目录确属旧 alpha=16 的 d000_s42 产物，已被 D075 废弃。等你指令决定是否删除。

---
