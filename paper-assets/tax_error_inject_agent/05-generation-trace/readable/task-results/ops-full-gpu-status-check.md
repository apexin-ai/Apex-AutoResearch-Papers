# ops full gpu status check

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-gpu-status-check_20260516T102350_result.json`
- **Structured JSON:** [`d4a166bd2b3c38fb128b.json`](../../sessions/d4/d4a166bd2b3c38fb128b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全面状态报告

### GPU 分配

| GPU | 状态 | 进程 | 显存 |
|-----|------|------|------|
| cuda:0 | **忙** | llama31-vanilla-s0 训练 | 30.8/32.6 GB |
| cuda:1 | **忙** | llama31-taxei-s0 训练 | 24.5/32.6 GB |
| cuda:2 | **忙** | llama31-random-s0 训练 | 26.0/32.6 GB |
| cuda:3 | **空闲** | — | 0/32.6 GB |

**Director 说的"4 GPU 全空闲"不准确——实际只有 GPU 3 空闲。**

---

### LLaMA s0 三组训练进度

| 训练 | GPU | 进度 | 预计剩余 |
|------|-----|------|----------|
| llama31-vanilla-s0 | cuda:0 | **1440/1635 (88%)** epoch 2.6/3 | ~8 min |
| llama31-taxei-s0 | cuda:1 | **刚启动** (v1, 18:18 开始) | ~2h+ |
| llama31-random-s0 | cuda:2 | **1811/3387 (53%)** epoch 1.6/3 | ~62 min |

Checkpoints 已保存：
- vanilla-s0: checkpoint-545 (epoch 1), checkpoint-1090 (epoch 2) ✓
- taxei-s0: checkpoint-1129 (epoch 1, v0 版) — v1 刚重新开始
- random-s0: checkpoint-1129 (epoch 1) ✓

**注意**: taxei-s0 有两个版本目录（v0 失败后 v1 重启），v1 当前无 checkpoint。

---

### Eval 完成状态

**v4-taxei-rp 系列 (injected eval)**:
| Seed | Recovery Rate | 状态 |
|------|--------------|------|
| s0 | 46.8% | ✅ 完成 |
| s1 | — | ✅ 有文件 |
| s7 | 59.6% | ✅ 完成 |
| s42 | — | ✅ 有文件 |
| s123 | — | ✅ 有文件 |

**v4 Recovery eval 已完成**:
- taxei: s0, s1, s123, r2 ✅
- taxei-rp: s7 ✅
- vanilla: s0, s1, s7, s123 ✅
- **random: 全部缺失** ❌

**Random recovery eval 缺失但 checkpoints 存在**（s0/s1/s7/s123 均有）。

---

### 还有一个活跃 eval session

`eval-rp-s0` tmux session 正在用 GPU 1 跑 v4-taxei-rp-s0 的 injected eval（但该结果文件已存在——可能是重跑或进程残留）。**这解释了 taxei-s0 训练被挤到 v1 重启**。

---

### Scale-up

trajectories_scaleup_p1: 仅 2 个 jsonl 文件，无活跃生成进程。

---

### GPU 分配建议

| 优先级 | 任务 | 建议 GPU |
|--------|------|----------|
| 1 | 等 vanilla-s0 完成 (~8min) | cuda:0 释放后可用 |
| 2 | 等 random-s0 完成 (~1h) | cuda:2 释放后可用 |
| 3 | GPU 3 空闲 | 可立即跑 random recovery eval 或其他 eval |
| 4 | eval-rp-s0 可能已完成但进程残留 | 确认后释放 cuda:1 给 taxei-s0 |

**关键行动项**: eval-rp-s0 session 结果已存在（`v4_taxei_rp_s0_injected.json`），但 tmux session 仍在——需要确认是否残留进程占 GPU，如果是则 kill 释放给 taxei-s0 训练。

---
