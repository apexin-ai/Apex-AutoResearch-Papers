# ssh gpu check deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_check_deploy_20260524T171704_result.json`
- **Structured JSON:** [`c6b32ff25ec34dc5e8ed.json`](../../sessions/c6/c6b32ff25ec34dc5e8ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇报

---

### westd-38929（4× RTX PRO 6000 Blackwell, 98GB each）

| GPU | 显存占用 | 利用率 | 状态 | 运行进程 |
|-----|---------|--------|------|----------|
| **GPU0** | 14050/97887 MiB (14%) | 42% | 忙碌 | PID 568641: `pi05 l2norm k=0.3 seed42` (10190 MiB) + 两个 MetaWorld sweep 进程模型加载溢出 |
| **GPU1** | 1921/97887 MiB (2%) | **17%** | 忙碌 | PID 613259: `smolvla random_prune k=0.5` MetaWorld sweep (1912 MiB) |
| **GPU2** | 10772/97887 MiB (11%) | 57% | 忙碌 | PID 612461: `pi05 l2norm k=0.95 seed43` (10753 MiB) |
| **GPU3** | 12587/97887 MiB (13%) | 50% | 忙碌 | PID 612707: `pi05 l2norm k=0.5 seed43` (10651 MiB) + PID 614407: `smolvla l2norm_prune k=0.5` (1912 MiB) |

**MetaWorld Sweep 状态：**
- PID 613253 (RANDOM_SWEEP): **存活** — 当前跑 k=0.5 on GPU1
- PID 614338 (L2NORM_SWEEP): **存活** — 当前跑 k=0.5 on GPU3

**GPU1 问题更新：** Director 之前报告 GPU1 利用率 0%，当前已恢复到 17%。random_prune sweep 正在 GPU1 上活跃执行 k=0.5。可能之前查看时恰好处于任务切换间隙。

---

### westd-41074（4× RTX PRO 6000 Blackwell, 98GB each）

| GPU | 显存占用 | 利用率 | 状态 | 运行进程 |
|-----|---------|--------|------|----------|
| **GPU0** | 1/97887 MiB | 0% | **空闲** | 无进程 |
| **GPU1** | 10506/97887 MiB (11%) | 18% | 忙碌 | PID 474471: `pi05 l2norm k=0.85 seed43` (10487 MiB) |
| **GPU2** | 1/97887 MiB | 0% | **空闲** | 无进程 |
| **GPU3** | 10464/97887 MiB (11%) | 50% | 忙碌 | PID 467274: `pi05 l2norm k=0.7 seed43` (10445 MiB) |

**进程存活检查：**
- PID 466673 (K09): **已结束** ✓ — GPU0 已释放
- PID 466931 (K085): **已结束** — 被 PID 474471 替代（同为 k=0.85 seed43，新 PID）
- PID 467274 (K07): **存活** — GPU3 上运行中

---

### 总结

| 服务器 | 空闲 GPU | 忙碌 GPU |
|--------|---------|---------|
| westd-38929 | 0 | 4（全满） |
| westd-41074 | **GPU0, GPU2** | GPU1, GPU3 |

**可用资源：westd-41074 有 2 块空闲 GPU（GPU0、GPU2）可调度新任务。**

---
