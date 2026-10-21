# audit cqa1 full

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_cqa1_full_20260522T200552_result.json`
- **Structured JSON:** [`977d6e422a22712f5d57.json`](../../sessions/97/977d6e422a22712f5d57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the full report.

---

## 审计报告 — westd-27271 (2 GPUs)

### GPU 状态

| GPU | VRAM | Util | 进程 |
|-----|------|------|------|
| 0 | 4856 MiB | 85% | X-VLA random k=0.9 Goal (task 0, ep 18/50) |
| 1 | 4938 MiB | 1%* | X-VLA random k=0.9 Spatial (task 0, ep 19/50) |

*GPU 1 util 低是瞬时读数，进程活跃。

两张卡均被 X-VLA random 链占满，链结构：k=0.95(done) → k=0.9(running) → k=0.7(queued)。

### 收割结果

| exp_id | SR | 状态 |
|--------|-----|------|
| `eval_xvla_random_k095_goal_seed42` | **54.0%** (baseline 98.4%, -44pp) | → DONE |
| `eval_xvla_random_k095_spatial_seed42` | **70.2%** (baseline 93.0%, -23pp) | → DONE |

X-VLA 对 random pruning 极度敏感：仅 5% random 移除即造成 Goal 44pp、Spatial 23pp 暴跌。

### 失败实验（本服务器日志）

| exp_id | 错误 | 时间 |
|--------|------|------|
| `eval_pi05_l2norm_k095_goal_seed42` | Network unreachable (tokenizer download) | May 22 17:52 |
| `eval_pi05_l2norm_k0925_object_seed43_v2` | Network unreachable (tokenizer download) | May 22 17:43 |

原因：`TRANSFORMERS_OFFLINE=1` 未完全阻止 tokenizer 网络请求。这两个 registry 仍为 RUNNING，未标 FAILED（可能已在其他服务器重新部署）。

### 新部署

**0 张空闲卡。** 优先队列中的 4 个 π0.5 实验无法部署。

预计释放时间：k=0.9 各剩 ~60min（task 0/10），之后 k=0.7 各 ~70min，总计约 **2–2.5h** 后两张卡同时空闲。

---
