# ops audit westd41074 harvest

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit_westd41074_harvest_20260522T150648_result.json`
- **Structured JSON:** [`dcea0771750f55a7a42c.json`](../../sessions/dc/dcea0771750f55a7a42c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。下面是完整汇报。

---

## westd-41074 GPU 全状态

| GPU | Util | VRAM | Session | 实验 | 进度 |
|-----|------|------|---------|------|------|
| **cuda:0** | 4% | 11.4/97.9 GB | `pi05_k0925_s43` | π0.5 L2norm k=0.925 Object seed43 | T4/10 (ep30, ~93%) |
| **cuda:1** | 0% | 4.4/97.9 GB | `xvla_long` | X-VLA Long L2norm k=0.9 | T4/10 进行中 |
| **cuda:2** | 43% | 10.7/97.9 GB | `pi05_attention` | π0.5 Attention k=0.95 Object s42 | T5/10 (ep40, ~98%) |
| **cuda:3** | 0%* | 27.5/97.9 GB | `train_m64v6` | OpenVLA M64 训练 | step 62250/100000 (62%) |

> *cuda:3 的 0% util 是 nvidia-smi 瞬时快照，**M64 未 stuck**。最后日志 23:07:19，间隔 ~84s/50步，sps=0.6 稳定。

额外：`smolvla_spatial` session 已完成，进程退出，GPU 已释放。

---

## 已完成实验结果

### X-VLA Long (新结果，尚未注册)
| 配置 | SR | 备注 |
|------|-----|------|
| **Baseline (k=1.0)** | **92.5%** (185/200) | 新基线 |
| **L2norm k=0.95** | **47.0%** (94/200) | 仅去5%就崩 -45.5pp！ |

X-VLA Long k=0.95 崩得很惨：T0=5%, T7=10%, T9=0%。X-VLA 对 Long 任务的 vision token 极度敏感。k=0.9 正在跑。

### π0.5 L2norm k=0.85 Goal (已收割)
- SR = **86.8%** (434/500)，baseline=96.4%，下降~10pp
- T9(wine_bottle_rack)=46% 严重拖后腿，其余 T0-T8 在 80-100%
- **Registry 已更新为 DONE/success**

### SmolVLA Spatial Baseline (新结果)
- SR = **55.0%** (110/200), 20 eps/task

---

## 活跃实验详情

**pi05_k0925_s43 (cuda:0)**:
- T0=100%, T1=100%, T2=98%, T3=94%, T4=93% (ep30)
- 跑完 ~40 min

**pi05_attention (cuda:2)** — 首个 attention 剪枝实验:
- k=0.95: T0=100%, T1=100%, T2=100%, T3=98%, T4=96%, T5=~98% (ep40)
- 累计 247/250=98.8% (T0-T4)
- k=0.95 完成后自动链 k=0.9→0.85→0.7

**xvla_long (cuda:1)**:
- 已完成: baseline(92.5%), k=0.95(47.0%)
- 正在跑: k=0.9, Task 3=95%, Task 4 进行中

**M64 训练 (cuda:3)**:
- 62250/100000, loss ~2.5-2.8, ETA ~17.5h

---

## 崩溃的实验

**Goal Random k=0.85 和 k=0.7** — `IndexError: index 50 is out of bounds for axis 0 with size 50`
- 原因：`n_episodes=500` bug，init_states 只有 50 条
- k=0.85 T0 部分跑到 86% 后在 T1 开始时崩溃
- k=0.7 同样 bug，启动即崩
- **Registry 已标记 DONE/failed**
- 需用 `--n_episodes 50` 重跑

---

## 重部署建议

**当前所有 4 GPU 占满，无法立即重部署。**

- **cuda:0 最先空闲** (~40min): pi05_k0925_s43 完成后 → 部署 Goal Random (k=0.85, 0.7, 0.5) 用 `--n_episodes 50`
- **cuda:1 次之** (~1-2h): xvla_long k=0.9 完成后 → 部署 π0.5 Long Random k=0.95, 0.9, 0.85
- cuda:2 和 cuda:3 长时间占用（attention 链 + M64 训练）

---
