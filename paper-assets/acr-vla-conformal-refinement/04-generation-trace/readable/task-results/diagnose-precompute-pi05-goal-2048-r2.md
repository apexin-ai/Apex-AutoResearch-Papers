# diagnose precompute pi05 goal 2048 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_precompute-pi05-goal-2048-r2_20260524T061726_result.json`
- **Structured JSON:** [`1492bbe4cc01d9245709.json`](../../sessions/14/1492bbe4cc01d9245709.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 结果

| 项目 | 状态 |
|------|------|
| **goal** (pid=114159) | **正常完成**。Cache 完整：manifest.json (n=61728, K=10, obs_dim=2048) + obs_features.pt (483M) + k_samples.pt (71M) + expert_actions.pt (7.1M) |
| **object** (pid=113456) | 仍在运行，已跑 1 天 9 小时，manifest 尚未生成 |
| **long** (pid=114507) | 仍在运行，已跑 1 天 9 小时，manifest 尚未生成 |
| **磁盘** | /root/autodl-tmp 剩余 **54GB** (79% used) |
| **Registry** | `precompute-pi05-goal-2048-r2` 已创建并标记 DONE/success |

**注意**：目录名 `crm_cache_pi05_2048` 中的 "2048" 指 obs_dim（π0.5 特征维度），实际采样 K=10。三个 precompute 命令均为 `--K 10`。object 和 long 完成后需同样注册 registry。

---
