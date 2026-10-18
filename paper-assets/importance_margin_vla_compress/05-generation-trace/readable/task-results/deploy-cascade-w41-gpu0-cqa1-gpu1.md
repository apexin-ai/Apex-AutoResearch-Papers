# deploy cascade w41 gpu0 cqa1 gpu1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cascade_w41_gpu0_cqa1_gpu1_20260527T122228_result.json`
- **Structured JSON:** [`c0e3bfc4c3e65ded9de3.json`](../../sessions/c0/c0e3bfc4c3e65ded9de3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 部署汇报

### 任务 1：westd-41074 GPU0 → π0.5 Attn k=0.75 strict ✅

| 项目 | 值 |
|------|-----|
| 服务器 | westd-41074 GPU0 |
| tmux | `pi05_attn_k075` |
| 日志 | `eval_pi05_attn_k075_long_seed42_strict_w41.log` |
| 状态 | 模型加载中，tmux + 日志正常 |
| Artifact | `art_20260527_44a041` |

### 任务 2：cqa1-33015 GPU1 → ❌ 不可用

GPU1 仍在运行 **Random k=0.5 strict**（PID 118731, 9994 MiB），当前进度 Task 0 ep=40/50，刚起步。全部 4 张 GPU 均被占用：

| GPU | 占用 |
|-----|------|
| 0 | Random k=0.7 (10211 MiB) |
| 1 | Random k=0.5 strict (9994 MiB) |
| 2 | L2norm k=0.85 strict (10463 MiB) |
| 3 | L2norm k=0.7 strict (10533 MiB) |

**Attn k=0.7 strict** 需要等 cqa1 某个 GPU 空出后再部署。

---
