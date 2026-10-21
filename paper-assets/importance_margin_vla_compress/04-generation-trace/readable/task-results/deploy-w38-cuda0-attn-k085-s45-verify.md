# deploy w38 cuda0 attn k085 s45 verify

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_w38_cuda0_attn_k085_s45_verify_20260528T005910_result.json`
- **Structured JSON:** [`0b1d84c7379123c9cc9a.json`](../../sessions/0b/0b1d84c7379123c9cc9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### w38 (westd-38929) GPU 全景

| GPU | 显存 | 利用率 | 进程 | 实验 |
|-----|------|--------|------|------|
| cuda:0 | 1→加载中 | 0%→启动中 | PID 899580 (新部署) | **Attn k=0.85 s45** — 模型加载中 |
| cuda:1 | 10894 MiB | 51% | PID 893108 | **Attn k=0.9 s45** — 运行中 ✓ |
| cuda:2 | 10686 MiB | 32% | PID 773760 | L2Norm k=0.85 s44 |
| cuda:3 | 10904 MiB | 19% | PID 774388 | Attn k=0.5 s44 |

### w41 (westd-41074) GPU 全景

| GPU | 显存 | 利用率 | 进程 | 实验 |
|-----|------|--------|------|------|
| cuda:0 | 10762 MiB | 52% | PID 453203 | OpenVLA random k=0.5 object s42 |
| cuda:1 | 11056 MiB | 21% | PID 374814 | Attn k=0.7 s44 |
| cuda:2 | 1 MiB | 0% | — | 空闲 |
| cuda:3 | 10888 MiB | 48% | PID 459974 | **Attn k=0.75 s45** — 运行中 ✓ |

### 结论

1. **w38:cuda:0 部署完成** — Attn k=0.85 s45, PID 899580, 模型正在加载
2. **w38:cuda:1 Attn k=0.9 s45** — 运行中（PID 893108 是 893099 的 python 子进程，GPU 51% 利用率）
3. **w41:cuda:3 Attn k=0.75 s45** — 运行中（PID 459974 是 459963 的 python 子进程，GPU 48% 利用率）

Reviewer 报告的"空闲"是误判，两个实验都在正常跑。

---
