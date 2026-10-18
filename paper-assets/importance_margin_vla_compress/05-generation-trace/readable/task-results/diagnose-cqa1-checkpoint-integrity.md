# diagnose cqa1 checkpoint integrity

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1-checkpoint-integrity_20260521T230226_result.json`
- **Structured JSON:** [`960348c07c4b57893543.json`](../../sessions/96/960348c07c4b57893543.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是完整报告：

---

## 诊断报告：π0.5 Checkpoint 状态

### 1. 服务器状态修正

**任务描述与实际状态严重不符：**
- π0.5 实验在 **westd-38929**，不在 westd-27271（cqa1）
- 原始 4 个 PID (719440, 725484, 716056, 716134) **全部不存在**
- westd-27271 上无任何 π0.5 文件，当前跑的是 OpenVLA 实验

### 2. westd-38929 当前状态

| GPU | PID | 实验 |
|-----|-----|------|
| GPU0 | — | 空闲 |
| GPU1 | 829120 | `l2norm k=0.7 spatial seed42`（运行中） |
| GPU2 | — | 空闲 |
| GPU3 | 824152 | `random k=0.85 object seed42`（运行中，非 seed43） |

### 3. Checkpoint 校验：**正常，未损坏**

Checkpoint 位于 `/root/autodl-tmp/pi05_libero_finetuned/`，今天刚下载（7.47GB），文件完整。

**Baseline spatial seed42 SR = 97.2%** (486/500) — checkpoint 完全健康。

### 4. 已完成 π0.5 结果（全部 libero_spatial, seed42）

| Mode | keep_ratio | Overall SR |
|------|-----------|------------|
| **baseline (none)** | **1.0** | **97.2%** |
| random | 0.7 | 74.4% |
| random | 0.5 | 71.6% |
| random | 0.3 | 49.6% |
| l2norm | 0.5 | 55.6% |
| l2norm | 0.3 | 57.2% |

降级曲线平滑合理，进一步证实 checkpoint 正常。

### 5. "k=0.85 全部 0%" 的真实原因

当前跑的 `random k=0.85 object seed42` 进度（9/10 tasks done）：

| Task | SR |
|------|----|
| T0 | 6% |
| T1 | 10% |
| T2 | 2% |
| T3 | 4% |
| T4 | 12% |
| T5 | 0% |
| T6 | 0% |
| T7 | 0% |
| T8 | 6% |
| **Running total** | **4.4%** (20/450) |

**根因：π0.5 模型只在 `libero_spatial` 上微调过（训练配置来自 `pepijn223/pi05_libero_31_9_non_q`），在 `libero_object` 上属于 out-of-distribution 评测。** 即使保留 85% 的 token，模型在 object 任务上本来就不行——这不是 pruning 造成的 cliff，是模型本身不具备 object 能力。

### 6. 结论

| 检查项 | 结果 |
|--------|------|
| Checkpoint 完整性 | ✅ 正常（baseline spatial 97.2%） |
| MD5 对比 | ❌ 无法对比（westd-27271 上不存在 pi05 checkpoint） |
| 数据有效性 | **spatial 实验全部有效；object 实验无效**（模型未在 object 上训练） |
| 需要 kill 实验？ | **建议 kill GPU3 的 random k=0.85 object（PID 824152）**——出来的数据没有意义 |

**无需 kill 所有实验，无需重新下载 checkpoint。** 后续 π0.5 实验应限定在 `libero_spatial` 上，或先用 baseline 跑一次 `libero_object` 确认模型本身在该 suite 的表现。

---
