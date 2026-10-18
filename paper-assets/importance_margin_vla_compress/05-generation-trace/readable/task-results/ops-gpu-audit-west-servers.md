# ops gpu audit west servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-audit-west-servers_20260520T165607_result.json`
- **Structured JSON:** [`a43c777c7de4ba064c74.json`](../../sessions/a4/a43c777c7de4ba064c74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 审计报告

---

### 1. westd-27271（2 GPU）

| GPU | 利用率 | 显存 | PID | 脚本 |
|-----|--------|------|-----|------|
| 0 | **70%** | 16.0/95.6 GB | 17634 | `eval_openvla_libero.py` random_prune **k=0.7** seed=43 |
| 1 | **62%** | 56.8/95.6 GB | 43505 | `eval_openvla_l2norm_libero.py` l2norm_prune **k=0.5** seed=42 |
| 1 | — | (共享) | 921279 | `train_openvla_smart_compress.py` **M32** (resume) |

**与预期对比**：
- ✅ M32 VTC-only 训练 (pid=921279, cuda:1) — 仍在跑
- ✅ D108 L2 norm k=0.7 — **已完成**（无对应进程）
- ⚠️ GPU 0 新增了 OpenVLA random prune k=0.7 eval (pid=17634)
- ⚠️ GPU 1 新增了 OpenVLA L2 norm k=0.5 eval (pid=43505)，与 M32 训练共用 GPU 1

**空闲 GPU：0**

---

### 2. westd-38929（4 GPU）

| GPU | 利用率 | 显存 | PID | 脚本 |
|-----|--------|------|-----|------|
| 0 | **70%** | 16.0/95.6 GB | 787425 | `eval_openvla_l2norm_libero.py` l2norm **k=0.5** seed=42 |
| 1 | **58%** | 15.7/95.6 GB | 788043 | `eval_openvla_l2norm_libero.py` l2norm **k=0.3** seed=42 |
| 2 | **82%** | 16.0/95.6 GB | 796062 | `eval_openvla_l2norm_libero.py` l2norm **k=0.9** seed=42 |
| 3 | **69%** | 16.0/95.6 GB | 796839 | `eval_openvla_l2norm_libero.py` l2norm **k=0.95** seed=42 |

**与预期对比**：
- ✅ D108 L2 norm k=0.9 (pid=796062) 和 k=0.95 (pid=796839) — 仍在跑
- ❌ D108 L2 norm k=0.5 (pid=787425) 和 k=0.3 (pid=788043) — **未完成，仍在跑**

**空闲 GPU：0**

---

### 3. westd-41074（4 GPU）

| GPU | 利用率 | 显存 | PID | 脚本 |
|-----|--------|------|-----|------|
| 0 | **88%** | 16.0/95.6 GB | 468330 | `eval_openvla_libero.py` random_prune **k=0.7** seed=43 v2 |
| 1 | **66%** | 16.0/95.6 GB | 468864 | `eval_openvla_libero.py` random_prune **k=0.5** seed=43 v2 |
| 2 | **0%** | 27.9/95.6 GB | 68539 | `train_openvla_smart_compress.py` **M96** |
| 3 | **0%** | 26.9/95.6 GB | 68852 | `train_openvla_smart_compress.py` **M64** |

**与预期对比**：
- ✅ OpenVLA random k=0.7 v2 (cuda:0) 和 k=0.5 v2 (cuda:1) — 仍在跑
- ⚠️ M96 训练 v3 (cuda:2, pid=68539) — 进程在，但 **GPU 利用率 0%**，显存 28GB 已占用，可能卡住或在做 checkpoint/data loading
- ⚠️ M64 训练 v3 (cuda:3, pid=68852) — 同上，**GPU 利用率 0%**，显存 27GB 已占用

**空闲 GPU：0**（但 GPU 2/3 疑似挂起）

---

### 汇总

| 服务器 | 总 GPU | 活跃（>0% util） | 疑似挂起（0% util 但有进程） | 真正空闲 |
|--------|--------|------------------|---------------------------|---------|
| westd-27271 | 2 | 2 | 0 | 0 |
| westd-38929 | 4 | 4 | 0 | 0 |
| westd-41074 | 4 | 2 | **2**（GPU 2, GPU 3） | 0 |
| **合计** | **10** | **8** | **2** | **0** |

**需要关注**：
1. **westd-41074 GPU 2/3**：M96 和 M64 训练进程 0% GPU 利用率但占用 27-28GB 显存，建议检查训练日志确认是否卡住
2. **westd-38929**：k=0.5 和 k=0.3 的 eval 并未完成，4 卡全满
3. **westd-27271 GPU 0/1**：出现了新的 eval 进程（random k=0.7 和 l2norm k=0.5），GPU 1 上 eval 与 M32 训练共享显存

---
