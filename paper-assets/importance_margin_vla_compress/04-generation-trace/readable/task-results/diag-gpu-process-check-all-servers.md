# diag gpu process check all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu_process_check_all_servers_20260524T021222_result.json`
- **Structured JSON:** [`a8b74895fb93153a6f9c.json`](../../sessions/a8/a8b74895fb93153a6f9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/report_gpu_status.md`。

**关键发现：**

1. **cqa1-33015**: `eval_pi05_random_k095_object_seed42_v2` 已于今天 09:58 完成，SR=74.0%，**fig_method_gap 阻塞已解除**。`eval_pi05_l2norm_k085_goal_seed43` 在 GPU 3 运行中 (Task 8/10)。3 个 GPU 空闲。

2. **westd-27271**: 两个 OpenVLA eval 都确认运行中 — l2norm_k05 在 GPU 0 (Task 5/10)，random_k05 在 GPU 1 (Task 4/10)。满载。

3. **westd-41074**: 4 GPU 满载运行 4 个 pi05 seed43 实验。**`eval_pi05_random_k085_spatial_seed42_postfix` 已终止**（EXIT_CODE=129，被 kill），需要重新调度。

4. **westd-38929**: X-VLA random_k085_goal (cuda:2) 和 spatial (cuda:3) 运行中。`xvla_l2norm_k05_goal_seed43` 已完成。GPU 0、1 空闲。

**总计 9/14 GPU 活跃，5 个 GPU 可用**（cqa1 ×3, westd-38929 ×2）。

---
