# ops gpu audit all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-audit-all-servers_20260521T103101_result.json`
- **Structured JSON:** [`09bf92f1e81199ed69eb.json`](../../sessions/09/09bf92f1e81199ed69eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已注册为 RUNNING。以下是完整的 4 服务器 GPU 审计结果：

---

## 4 服务器 GPU 状态表

### westd-27271 (2× RTX PRO 6000 Blackwell 98GB)

| GPU | PID | 实验 | VRAM | GPU-Util | 状态 |
|-----|-----|------|------|----------|------|
| 0 | 193983 | OpenVLA L2norm k=0.3 eval (seed42) | 16.1GB | 67% | ✅ 运行中 (2h37m) |
| 1 | 921279 | OpenVLA SC M32 train (resume) | 42.2GB | 97% | ✅ 运行中 (23h44m), step 54200/100000 |

**M32 未崩溃**，训练进度 54.2%，loss ~2.4-2.7，正常。

### cqa1-33015 (4× RTX 4090D 24GB)

| GPU | PID | 实验 | VRAM | GPU-Util | 状态 |
|-----|-----|------|------|----------|------|
| 0 | 944993 | X-VLA L2norm k=0.3 seed43 | 4.5GB | 1% | ✅ 运行中 (39m) |
| 1 | 946702 | X-VLA random k=0.3 seed43 | 4.5GB | 1% | ✅ 运行中 (38m) |
| 2 | **66544** | **X-VLA random k=0.7 seed44** ← 新部署 | ~4.5GB | - | ✅ 刚启动 |
| 3 | 947883 | X-VLA L2norm k=0.7 seed43 | 4.0GB | 0% | ✅ 运行中 (37m) |

**已完成**: X-VLA L2norm k=0.3 seed42 — **SR=22.2%** [95% CI: 18.8%-26.0%]
- Per-task: 26%, 0%, 32%, 40%, 18%, 46%, 0%, 24%, 0%, 36%

GPU2 空闲卡已用 X-VLA random k=0.7 seed44 填充。

### westd-41074 (4× RTX PRO 6000 Blackwell 98GB)

| GPU | PID | 实验 | VRAM | GPU-Util | 状态 |
|-----|-----|------|------|----------|------|
| 0 | 68573 | π0.5 L2norm k=0.7 | 10.5GB | 31% | ✅ 运行中 |
| 1 | 95490 | π0.5 random k=0.5 seed43 | 10.5GB | 21% | ✅ 运行中 |
| 2 | 68539 | M96 train | 28.5GB | 0% | ✅ 运行中 |
| 3 | 51513+59671 | π0.5 random k=0.7 + M64v6 | 38.0GB | 45% | ✅ 运行中 |

全部满载，PID 全部匹配。

### westd-38929 (4× RTX PRO 6000 Blackwell 98GB)

| GPU | PID | 实验 | VRAM | GPU-Util | 状态 |
|-----|-----|------|------|----------|------|
| 0 | 1945 | OpenVLA L2norm k=0.7 | 16.0GB | 84% | ✅ 运行中 |
| 1 | 2478 | OpenVLA random k=0.3 | 16.1GB | 67% | ✅ 运行中 |
| 2 | 3110 | OpenVLA random k=0.7 | 16.0GB | 70% | ✅ 运行中 |
| 3 | 3825 | OpenVLA L2norm k=0.5 | 16.0GB | 69% | ✅ 运行中 |

全部满载，PID 全部匹配。

---

**总结**: 14 GPU 全部在用，0 空闲卡，0 崩溃。唯一的空闲卡 (cqa1-33015 GPU2) 已部署 X-VLA random k=0.7 seed44 (PID 66544)。M32 train 未崩溃，54.2% 进度正常推进。

---
