# audit full scan 20260522c

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_full_scan_20260522c_20260522T224638_result.json`
- **Structured JSON:** [`19a3c7f5337d209e69a9.json`](../../sessions/19/19a3c7f5337d209e69a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westd-38929 cuda:3 模型正在加载，部署成功。现在输出完整扫描报告。

---

## 🖥️ westd-38929

### GPU 状态
| GPU | VRAM | 实验 | 进度 |
|-----|------|------|------|
| 0 | 10.8/97.9 GB | Random k=0.9 Long s43 | T0=6.0%, 刚开始 T1 |
| 1 | 9.9/97.9 GB | Random k=0.3 Long s42 | T7, ~20% |
| 2 | 10.3/97.9 GB | L2norm k=0.5 Long s42 | T8, overall ~49.8% |
| 3 | 加载中 | **新部署** Random k=0.5 Long s43 | 模型加载中 |

**磁盘**: / 29%, /autodl-tmp 80%

**收割**:
- ✅ Random k=0.5 Long s42 = **50.2%** → registry DONE
- ✅ Random k=0.9 Long s42 = **31.8%** (确认已有值)

---

## 🖥️ westd-41074

### GPU 状态
| GPU | VRAM | 实验 | 进度 |
|-----|------|------|------|
| 0 | 9.7/97.9 GB | **新部署** Random k=0.85 Long s43 | 已加载运行 |
| 1 | 9.9/97.9 GB | L2norm k=0.3 Long s43 | 进行中 |
| 2 | 10.4/97.9 GB | ⚠️ Random k=0.5 Long s42 **重复** | 浪费中 |
| 3 | 27.5/97.9 GB | M64 训练 v6 | **78600/100000 (78.6%), ~10h 剩余** |

**磁盘**: / 14%, /autodl-tmp 77%

**收割**:
- ✅ Random k=0.85 Long s42 = **44.4%**
- ✅ Random k=0.7 Long s42 = **64.6%**
- ✅ L2norm k=0.9 Long s42 = **81.0%**

**问题**:
- ⚠️ **cuda:2 重复任务**: Random k=0.5 Long s42 已在 westd-38929 完成 (SR=50.2%)，建议 kill 回收 GPU
- ❌ Random k=0.5 Long s43 v1 失败（缺 `TRANSFORMERS_OFFLINE`，tokenizer 网络下载失败）→ 已在 westd-38929 重试
- ❌ SmolVLA Spatial 失败（SSL handshake timeout）

---

## 🖥️ westd-27271

### GPU 状态
| GPU | VRAM | 实验 | 进度 |
|-----|------|------|------|
| 0 | 10.6/97.9 GB | L2norm k=0.3 Long s42 | T1 进行中 |
| 1 | 10.3/97.9 GB | L2norm k=0.5 Long s43 | T2, ~65.0% |

**磁盘**: / 41%, /autodl-tmp 59%

**收割 (X-VLA Random chains)**:

| k | Spatial | Goal |
|---|---------|------|
| 0.95 | **70.2%** | **54.0%** |
| 0.9 | **77.8%** | **70.6%** |
| 0.7 | **76.6%** | **57.2%** |

---

## 🖥️ cqa1-33015

### GPU 状态
| GPU | VRAM | 实验 | 进度 |
|-----|------|------|------|
| 0 | 10.3/24.6 GB | L2norm k=0.7 Goal s42 | T8, overall ~77.2% |
| 1 | 10.3/24.6 GB | Random k=0.95 Goal s42 | T9 进行中 |
| 2 | 10.1/24.6 GB | Random k=0.3 Goal s43 | T3, ~55% |
| 3 | 10.5/24.6 GB | Long chain (当前 k=0.9) | T6, 下一个 k=0.85 |

**磁盘**: / 29%, /autodl-tmp 55%

**收割**:
- ✅ Random k=0.3 Goal s42 = **51.8%**
- ✅ L2norm k=0.95 Long s42 = **86.8%**
- ✅ L2norm k=0.95 Goal s42 = **89.4%**

**问题**:
- SmolVLA Spatial: **cqa1 无 smolvla cache 也无日志**，未在此服务器执行过
- OpenVLA Spatial chain: tmux 存在但无活跃 python 进程，baseline log 停在 step 250/280，结果文件未找到

---

## 📊 合并后 π0.5 Long s42 曲线

| k | Random | L2norm |
|---|--------|--------|
| 0.95 | (已有) | **86.8%** ✨ |
| 0.9 | **31.8%** | **81.0%** |
| 0.85 | **44.4%** | 78.0% (已有) |
| 0.7 | **64.6%** | 60.0% (已有) |
| 0.5 | **50.2%** | 🏃 running |
| 0.3 | 🏃 running | 🏃 running |

**关键发现**: Random Long 曲线**严重非单调** — k=0.7 (64.6%) > k=0.5 (50.2%) > k=0.85 (44.4%) > k=0.9 (31.8%)。L2norm 则保持单调下降且全面碾压 Random。

---

## 📋 新部署汇总

| 服务器 | GPU | 实验 | 状态 |
|--------|-----|------|------|
| westd-38929 | cuda:3 | Random k=0.5 Long s43 (重试) | ✅ 已启动 |
| westd-41074 | cuda:0 | Random k=0.85 Long s43 | ✅ 已启动 |

---

## ⚠️ 待处理
1. **westd-41074 cuda:2** — 重复 Random k=0.5 Long s42 建议 kill，可回收用于 Long s43 缺口
2. **SmolVLA Spatial baseline** — westd-38929 有 May 21 的旧结果 `smolvla_baseline_spatial_seed42.json`；cqa1/westd-41074 尝试均失败（网络问题）。需确认旧结果是否可用，或需在有 cache 的服务器重试
3. **OpenVLA Spatial chain on cqa1** — 可能已静默完成但结果未保存到 eval_results/，需检查 tmux pane 输出

---
