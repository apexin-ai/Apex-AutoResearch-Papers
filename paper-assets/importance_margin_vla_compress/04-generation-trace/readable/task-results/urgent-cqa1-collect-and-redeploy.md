# urgent cqa1 collect and redeploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_cqa1-collect-and-redeploy_20260525T224038_result.json`
- **Structured JSON:** [`dc71723b0eb57596177b.json`](../../sessions/dc/dc71723b0eb57596177b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

**cqa1-33015 全部 4 GPU 满载，无法立即重部署。**

### 各实验状态

| GPU | 实验 | 当前进度 | 预计完成 |
|-----|------|----------|----------|
| 0 | π0.5 zeromask_random k=0.9 Object v2 | T4/10, 前3任务全100%, T4=93% | **~40min** |
| 1 | π0.5 L2norm k=0.75 Long v2 | T2/10, T0=96%, T1=94% | ~2.5h |
| 2 | π0.5 Random k=0.75 Long | T1/10, T0=84% | ~3h |
| 3 | OpenVLA Attn k=0.9 Goal seed43 | T2/10, **0% success** (异常) | 多小时 |

### 已完成操作
- 确认 `eval_pi05_l2norm_k0925_long_seed42_v2` 已 DONE (83.2%)，不需要重跑
- 标记 `eval_pi05_l2norm_k075_long_seed42_v3` 为 DONE/failed（日志卡死，实际 v2 在跑）

### 注意事项
1. **GPU0 最快释放**（~40min）→ 届时部署 `eval_pi05_attention_k075_long_seed42`
2. **GPU3 OpenVLA Attn Goal seed43 全 0%** — 79分钟内两个任务零成功，可能是 bug（模型路径/unnorm_key 问题）或 Attention pruning 在 Goal 上确实极差。需要后续确认
3. GPU1 的 L2norm k=0.75 早期数据 (T0=96%, T1=94%) 显示这个压缩率下性能仍然很高，cliff 可能在更低的 k 值

**下一步：约 40 分钟后回来收 GPU0 的 zeromask_random 结果并部署 Attn k=0.75。**

---
