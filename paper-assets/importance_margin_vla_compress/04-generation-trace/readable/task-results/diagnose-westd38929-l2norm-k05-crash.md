# diagnose westd38929 l2norm k05 crash

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd38929_l2norm_k05_crash_20260527T122053_result.json`
- **Structured JSON:** [`95fc5ee57a9daf245bdf.json`](../../sessions/95/95fc5ee57a9daf245bdf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 结论

### 原始部署（`eval_pi05_l2norm_k05_long_seed42_strict_w38.log`）
- 启动于 20:10，GPU 0，仅完成 T0（10 episodes, 30%）后被 kill
- 日志无错误信息 — 外部 kill（进程消失，GPU 0 现在空闲 1MiB）
- **死因**：大概率是 fix worker 部署 OV Attn k=0.75 Long 时误杀，或资源冲突

### 但有一个替代实例正在运行
tmux session `pi05_l2norm_k05_strict`（创建于 20:00）在 **GPU 3** 上运行了相同实验：
- 日志：`logs/pi05_l2norm_k05_long_strict.log`
- 进度：T0 ep=40/50，57% SR，正常推进中
- `CUDA_VISIBLE_DEVICES=3`，PID 250745 + 251173

### ⚠️ 问题：GPU 3 上有两个重复实例
两个 Python 进程（PID 250745 via nohup，PID 251173 via tee）都在 GPU 3 上跑相同实验，各占 ~10.6GB VRAM。不会 OOM（GPU 3 有 96GB），但浪费算力且可能写同一日志文件导致结果混乱。**建议 kill 其中一个。**

### westd-38929 当前 GPU 状态

| GPU | 状态 | 进程 |
|-----|------|------|
| 0 | **空闲** | — |
| 1 | OV Attn k=0.75 Long | PID 266221，刚启动 |
| 2 | OV 实验（v2 tmux 09:41） | PID 968309，15.9GB |
| 3 | π0.5 L2norm k=0.5 Long ×2 | PID 250745 + 251173 |

**GPU 0 空闲可用。** 需要决定是否 kill GPU 3 上的一个重复实例。

---
