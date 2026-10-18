# critical domain id audit

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_critical_domain-id-audit_20260523T160853_result.json`
- **Structured JSON:** [`df73a2aa271db22fd7e8.json`](../../sessions/df/df73a2aa271db22fd7e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完毕。以下是完整结论。

---

## 排查结果

### 根因

脚本无 bug。`--domain_id` 默认值=3，对所有 LIBERO suite 都正确（X-VLA 的 domain_id 按机器人域区分，非按 suite 区分，LIBERO 统一用 3）。

**问题是 4 个实验的启动命令显式传了 `--domain_id 2`**，导致使用了错误的 action decoder，SR 全部为 0%。

### 受影响实验（4 个，全部需重跑）

| exp_id | suite | mode | k | domain_id_used | correct | SR | action |
|--------|-------|------|---|:-:|:-:|---:|--------|
| eval_e5_xvla_attn_last_goal_k05 | goal | attention_last | 0.5 | **2** | 3 | 0.0% | **RERUN** |
| eval_e5_xvla_attn_mean_goal_k05 | goal | attention_mean | 0.5 | **2** | 3 | 0.0% | **RERUN** |
| eval_e5_xvla_attn_rollout_goal_k05 | goal | attention_rollout | 0.5 | **2** | 3 | 0.0% | **RERUN** |
| eval_xvla_random_k05_goal_seed42 | goal | random | 0.5 | **2** | 3 | 0.0% | **RERUN** |

### 已验证正确的实验（全部 domain_id=3）

| 类别 | 实验 | SR |
|------|------|-----|
| **Goal baseline** | k=1.0 L2 | 98.4% |
| **Goal attn k=0.3** | last / mean | 93.0% / 97.6% |
| **Goal L2 k=0.5** | cqa1-33015 | 61.0% |
| **Goal L2 k=0.9** | cqa1-33015 | 70.2% |
| **Goal random k=0.7/0.9/0.95** | westd-27271 | 57.2% / 70.6% / 54.0% |
| **Spatial baseline** | k=1.0 | 93.0% |
| **Spatial L2 k=0.5/0.9** | cqa1-33015 | 58.8% / 79.0% |
| **Spatial attn rollout k=0.7** | westd-38929 | domain_id=3 ✓ |
| **Spatial attn k=0.3** | last / mean | domain_id=3 ✓ |
| **Long baseline** | k=1.0 | 94.0% |
| **Long attn k=0.5** | last / mean / rollout | 90.4% / 94.6% / 94.8% |
| **Object 全部** | 所有 k 值 | domain_id=3 ✓ |

### 脚本一致性

| 服务器 | eval_xvla_attention_pruning | eval_xvla_pruning | default domain_id |
|--------|:--:|:--:|:-:|
| westd-38929 | ✓ | ✓ | 3 |
| westd-27271 | ✓ | ✓ | 3 |
| westd-41074 | 不存在 | ✓ | 3 |
| cqa1-33015 | 不存在 | ✓ | 3 |

### 建议

1. **重跑 4 个实验**时不传 `--domain_id`（使用默认值 3），或显式传 `--domain_id 3`
2. 脚本层面无需修复——默认值已正确，且所有 LIBERO suite 共享同一个 domain_id
3. 注意 westd-27271 上 `xvla_prune_k0.5_libero_goal.json` 实际内容是 **random** mode（被覆写），原 L2 结果在 cqa1-33015 的 `xvla_goal_k05_seed42.json` 中

---
