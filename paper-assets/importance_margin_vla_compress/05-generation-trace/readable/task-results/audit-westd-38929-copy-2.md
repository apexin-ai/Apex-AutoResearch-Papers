# audit westd 38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd-38929_20260523T110748_result.json`
- **Structured JSON:** [`97496d3bf25b528ca760.json`](../../sessions/97/97496d3bf25b528ca760.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

**服务器: westd-38929**

**GPU 状态:** 全部空闲（利用率 0-46%，显存 ~5GB/98GB，无活跃实验进程）

**已完成实验（全部 exit code 0）:**

| 实验 | Mode | Suite | k | SR | Episodes | 耗时 |
|------|------|-------|---|-----|----------|------|
| eval_e5_xvla_attn_last_obj_k05 | attention_last | Object | 0.5 | **99.2%** | 500 | 32min |
| eval_e5_xvla_attn_mean_obj_k05 | attention_mean | Object | 0.5 | **98.4%** | 500 | 33min |
| eval_e5_xvla_attn_rollout_obj_k05 | attention_rollout | Object | 0.5 | **97.4%** | 500 | 34min |
| eval_e5_xvla_attn_last_long_k05 | attention_last | Long (libero_10) | 0.5 | **90.2%** | 500 | 59min |

**注意：实际运行 suite 与预期不符。** 预期部署的是 3×Goal + 1×attention_mean Long，实际运行的是 3×Object + 1×attention_last Long。**Goal suite 的 xvla_attn 实验从未运行。** attention_mean Long 也未运行。

**空闲 GPU:** 0, 1, 2, 3（全部空闲，可部署新实验）

**与已有 E5 结果对比（Object k=0.5）:**
- attention_last: 99.2% ← 已知结果重复确认
- attention_mean: 98.4% ← **新结果**
- attention_rollout: 97.4% ← **新结果**

三种 attention 模式在 Object suite 上差距极小（97.4%–99.2%），都接近饱和。

---
