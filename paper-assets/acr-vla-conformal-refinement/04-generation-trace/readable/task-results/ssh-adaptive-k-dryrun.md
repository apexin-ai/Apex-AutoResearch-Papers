# ssh adaptive k dryrun

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_adaptive-k-dryrun_20260519T225112_result.json`
- **Structured JSON:** [`acf897bef9993dda5ed8.json`](../../sessions/ac/acf897bef9993dda5ed8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

可以确认每一步都记录了 `meta` 到 `step_metadata`，包含 `actual_k`, `path` (fast/full), `l2_distance` 等信息。

等全部完成后还需要等很久（剩余8个task约16分钟），不必在这里一直等。已经可以给出结论了。

## Dry-run 验证报告

### 1. 参数解析 ✓
- `--adaptive_k` 是独立 flag（非 `--mode adaptive_k`），可叠加在任何mode上
- 相关参数: `--adaptive_k`, `--adaptive_threshold`, `--k_init`(默认2), `--k_full`(默认5)
- 解析输出确认: `adaptive_k: True, adaptive_threshold: 0.074855, k_init: 2, k_full: 5`

### 2. 启动成功 ✓
- SmolVLA 加载 ✓
- CRM 加载 ✓（337,438 params from perdof/crm_best.pt）
- Adaptive K CGS map 创建 ✓（k=2 和 k=5 两个 CGS 实例）
- LIBERO 10 tasks 加载 ✓
- Rollout 正常执行（已完成 2/10 tasks，进程 PID 58491 在 GPU 5 上运行，5657 MiB 显存）

### 3. JSON 输出字段
代码确认输出 JSON 会包含 `adaptive_stats`：
- `fast_path_ratio` — fast path 占比（k_init 就够的比例）
- `avg_actual_k` — 平均实际 K
- `mean_l2_distance` — 平均 L2 距离
- `total_steps`, `fast_steps`, `full_steps`

注意：字段名与任务描述中的略有不同（`fast_path_ratio` 而非 `adaptive_trigger_rate`，`avg_actual_k` 而非 `avg_K`）。没有独立的 `per_step_K` 字段（per-step数据在内存中但未写入JSON）和 `threshold` 字段。

### 4. 无错误
全程无 crash/exception。进程仍在后台运行（PID 58491），预计 ~16 分钟后全部10 tasks完成，JSON 将写入 `logs/test_adaptive_k_dryrun.json`。

---
