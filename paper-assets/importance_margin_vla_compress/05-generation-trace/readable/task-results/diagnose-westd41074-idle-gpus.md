# diagnose westd41074 idle gpus

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd41074_idle_gpus_20260527T075123_result.json`
- **Structured JSON:** [`f58780cf63256421bc37.json`](../../sessions/f5/f58780cf63256421bc37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：westd-41074 所有 GPU 均在使用中

| GPU | PID | 实验 | 进度 | 备注 |
|-----|--------|------|------|------|
| **0** | 32184 | OV Random k=0.95 Long seed42 | Task 8/10, ep20 | 未注册。Registry 中同实验指向 westd-38929 |
| **1** | 177597 | π0.5 Random k=0.75 Long strict | Task 8/10, ep20 | 已注册 ✓ |
| **2** | 262137 | π0.5 Random k=0.95 Long strict | Task 1/10, ep10 | **未注册**，~15:31 刚启动 |
| **3** | 262473 | π0.5 L2norm k=0.95 Long strict | Task 1/10, ep30 | **未注册**，~15:31 刚启动 |

### Registry 旧实验状态

- **eval_openvla_random_k095_object_seed42**: 已 DONE/success，**SR=67.4%**。无需重跑。
- **eval_openvla_attn_k075_long_seed42**: 已 DONE/success，SR=37.4%（8/10 tasks，partial）。
- **eval_openvla_random_k095_long_seed42**: 在 westd-38929 上 RUNNING（非本机）。

### 结论

**无法部署新实验** — 4 个 GPU 全部被占用。GPU2、GPU3 被另一个 agent 在约 20 分钟前部署了 π0.5 strict 实验（random k=0.95 和 l2norm k=0.95），预计各需 ~3-4 小时完成。

关于你列出的 3 个优先级实验：
1. **OV Random k=0.95 Object** — registry 显示已完成（SR=67.4%），不需要重跑
2. **OV Attn k=0.75 Long v2** — GPU3 被占，无法部署。但 v1 已有 partial 结果 37.4%（8/10 tasks）
3. **π0.5 Random k=0.85 Long strict** — GPU0 被占，无法部署

是否需要：
- 注册 GPU2/GPU3 上的未注册实验？
- 等 GPU0 的 OV Random k=0.95 Long 完成后（预计 1-2 小时）部署优先级 2 或 3？
- 在其他服务器（westd-27271/westd-38929）上部署缺失实验？

---
