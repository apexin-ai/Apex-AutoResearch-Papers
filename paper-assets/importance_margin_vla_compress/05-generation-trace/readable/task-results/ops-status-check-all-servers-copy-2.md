# ops status check all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status_check_all_servers_20260521T181543_result.json`
- **Structured JSON:** [`e3fa13b489feac5b9bfe.json`](../../sessions/e3/e3fa13b489feac5b9bfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完成。汇总如下：

---

## 实验状态汇总

### westd-41074 (4× RTX PRO 6000 Blackwell, 96GB)

| GPU | 实验 | PID | 存活 | 进度 | 备注 |
|-----|------|-----|------|------|------|
| 0 | π0.5 L2norm k=0.1 seed42 | 531007 | ✅ | 已跑 24min | 正常 |
| 1 | π0.5 random k=0.9 seed43 | 531274 | ✅ | 已跑 23min | 正常 |
| 2 | VTC M96 | 68539 | ✅ | **67,850/100K (67.9%)** | 运行 1d14h |
| 3 | VTC M64 v6 | 59671 | ✅ | **18,200/100K (18.2%)** | 运行 9h，已安全越过 v5 的 17050 SIGKILL 点 |

**磁盘**: `/root/autodl-tmp` → **180G used / 250G total, 71G 可用 (72%)**，空间充足。

**M64 v6 checkpoint**: 目录下仅有 `checkpoint_step10000.pt` (4.5GB)。step 18200 已过 17K 但未到 20K，下一个 checkpoint 应在 20K 保存。v5 的 SIGKILL 问题未复现，磁盘空间充足。

---

### westd-27271 (2× RTX PRO 6000 Blackwell, 96GB)

| GPU | 实验 | PID | 存活 | 进度 | 备注 |
|-----|------|-----|------|------|------|
| 0 | (空闲) | — | — | — | ✅ 确认空闲，0 MiB 显存 |
| 1 | VTC M32 | 921279 | ✅ | **69,050/100K (69.1%)** | 运行 1d7h，从 checkpoint resume |

---

### westd-38929 (4× RTX PRO 6000 Blackwell, 96GB)

| GPU | 实验 | PID | 存活 | 进度 | 备注 |
|-----|------|-----|------|------|------|
| 0 | SmolVLA baseline seed43 | — | ❌ 结束 | ✅ 完成 | 结果已保存 |
| 1 | SmolVLA random k=0.95 seed43 | — | ❌ 结束 | ✅ 完成 | 结果已保存 |
| 2 | SmolVLA random k=0.5 seed43 | — | ❌ 结束 | ✅ 完成 | 结果已保存 |
| 3 | SmolVLA L2norm k=0.95 seed43 | 425135 | ❌ 结束 | ✅ 完成 | 结果已保存 |

**全部 4 个 GPU 已空闲**，所有 SmolVLA 实验均已完成。最后完成的是 L2norm k=0.95 seed43（02:15）。

---

### cqa1-33015 (4× RTX 4090D, 24GB)

**不是空闲** — 正在跑 SmolVLA official eval sweep：

| GPU | 实验 | 状态 | 备注 |
|-----|------|------|------|
| 0 | SmolVLA official l2norm k=0.9→k=0.7 sweep | 🔄 running | 当前跑 random k=0.7，ep 49/50 接近完成 |
| 1 | SmolVLA official baseline + sweep | 🔄 running | sweep 脚本运行中 |
| 2 | SmolVLA official sweep | 🔄 running | sweep 脚本运行中 |
| 3 | (空闲) | — | 1 MiB 显存 |

---

### 关键发现

1. **M64 v6 安全越过 17K** — step 18,200，磁盘 71GB 可用，v5 的 SIGKILL 问题未复现
2. **westd-38929 全部释放** — 4 个 96GB GPU 空闲可用
3. **cqa1-33015 未空闲** — 在跑 official SmolVLA eval sweep，GPU0 上的 random k=0.7 即将完成（ep 49/50）
4. **三个 VTC 训练正常推进** — M96 67.9%, M64 18.2%, M32 69.1%

---
