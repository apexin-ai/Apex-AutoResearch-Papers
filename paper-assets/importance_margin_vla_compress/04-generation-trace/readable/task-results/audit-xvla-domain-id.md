# audit xvla domain id

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_xvla-domain-id_20260524T083837_result.json`
- **Structured JSON:** [`b5f55e015bb412893382.json`](../../sessions/b5/b5f55e015bb412893382.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复已生效。以下是完整审计报告。

---

## 审计结果

### 1. GPU 3 状态
**空闲**（1MiB / 97GB，P8 节能，0% util）。无 X-VLA 进程。

GPUs 0/1/2 运行的是 **Pi0.5** 实验（`eval_pi05_pruning_libero.py`），不涉及 X-VLA domain_id 问题。

### 2. 重要修正：X-VLA domain_id 含义

脚本 docstring 第 10 行明确写：**`domain_id=3 for LIBERO`**。X-VLA 的 domain_id 是模型级域条件信号，所有 LIBERO suites 统一用 3。`--suite` 参数才控制加载哪个 benchmark。

因此任务描述中的 domain_id=1/2/3/4 对应 object/spatial/goal/long 的映射**不适用于 X-VLA**。

### 3. 磁盘结果文件 `xvla_prune_k0.3_libero_goal.json`

**确认无效**：domain_id=1（应为 3），SR=0.2%（正常应 ~30-50%）。需用 domain_id=3 重跑。

### 4. 全面 domain_id 审计表

**L2-norm / Random 剪枝（20 个文件）：**

| 文件 | suite | domain_id | 正确? | SR | mode |
|------|-------|-----------|-------|-----|------|
| k1.0_object | object | 3 | ✅ | 99.2% | l2_norm |
| k0.95_object | object | 3 | ✅ | 99.0% | l2_norm |
| k0.9_object | object | 3 | ✅ | 97.6% | l2_norm |
| k0.85_object | object | 3 | ✅ | 65.0% | random |
| k0.7_object | object | 3 | ✅ | 56.2% | l2_norm |
| k0.5_object | object | 3 | ✅ | 43.0% | l2_norm |
| k0.3_object | object | 3 | ✅ | 23.0% | l2_norm |
| k0.2_object | object | 3 | ✅ | 5.2% | l2_norm |
| k0.1_object | object | 3 | ✅ | 0.0% | l2_norm |
| k0.5_goal | goal | 3 | ✅ | 59.0% | l2_norm |
| k0.7_goal | goal | 3 | ✅ | 51.8% | l2_norm |
| k0.85_goal | goal | 3 | ✅ | 60.4% | random |
| **k0.3_goal** | **goal** | **1** | **❌ 无效** | **0.2%** | **l2_norm** |
| k0.5_spatial | spatial | 3 | ✅ | 58.8% | l2_norm |
| k0.3_spatial | spatial | 3 | ✅ | 31.2% | l2_norm |
| k0.7_spatial | spatial | 3 | ✅ | 72.8% | l2_norm |
| k0.85_spatial | spatial | 3 | ✅ | 68.2% | random |
| k0.5_10 | libero_10 | 3 | ✅ | 44.6% | l2_norm |
| k0.7_10 | libero_10 | 3 | ✅ | 49.4% | l2_norm |
| k0.85_10 | libero_10 | 3 | ✅ | 35.0% | random |

**Attention-based 剪枝（16 个文件）：全部 domain_id=3 ✅**

| 文件 | suite | domain_id | SR | mode |
|------|-------|-----------|-----|------|
| attn_last_k0.5_object | object | 3 | 99.2% | attention_last |
| attn_mean_k0.5_object | object | 3 | 98.4% | attention_mean |
| attn_last_k0.5_goal | goal | 3 | 98.2% | attention_last |
| attn_mean_k0.3_goal | goal | 3 | 97.6% | attention_mean |
| attn_rollout_k0.5_object | object | 3 | 97.4% | attention_rollout |
| attn_mean_k0.5_goal | goal | 3 | 97.4% | attention_mean |
| attn_rollout_k0.5_goal | goal | 3 | 96.8% | attention_rollout |
| attn_mean_k0.3_object | object | 3 | 96.0% | attention_mean |
| attn_mean_k0.5_10 | libero_10 | 3 | 94.6% | attention_mean |
| attn_rollout_k0.5_10 | libero_10 | 3 | 94.8% | attention_rollout |
| attn_last_k0.3_goal | goal | 3 | 93.0% | attention_last |
| attn_rollout_k0.7_spatial | spatial | 3 | 93.0% | attention_rollout |
| attn_rollout_k0.3_object | object | 3 | 92.0% | attention_rollout |
| attn_mean_k0.3_spatial | spatial | 3 | 90.4% | attention_mean |
| attn_last_k0.5_10 | libero_10 | 3 | 90.4% | attention_last |
| attn_last_k0.3_spatial | spatial | 3 | 85.6% | attention_last |

### 5. M087 修复状态

**修改前：** `eval_results/xvla_prune_k{args.keep_ratio}_{args.suite}.json`
**修改后：** `eval_results/xvla_prune_k{args.keep_ratio}_{args.suite}_seed{args.seed}.json`

已在服务器 `eval_xvla_pruning_libero.py:302-303` 生效。

### 结论
- **36 个结果文件中仅 1 个无效**：`xvla_prune_k0.3_libero_goal.json`（domain_id=1）
- 该文件需用 `--domain_id 3` 重跑
- 其余 35 个文件的 domain_id 全部正确（=3）

---
