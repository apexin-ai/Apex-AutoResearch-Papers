# diagnose eval xvla random k05 object seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_xvla_random_k05_object_seed42_20260521T043736_result.json`
- **Structured JSON:** [`91ed00056696fef854a7.json`](../../sessions/91/91ed00056696fef854a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：实验实际上**成功完成**，是误报

### 证据

日志最后清楚地显示实验正常结束：

```
2026-05-21 12:26:22 [INFO] SUITE: libero_object | MODEL: xvla | keep_ratio: 0.50
2026-05-21 12:26:22 [INFO] Overall SR: 353/500 (70.6%)
2026-05-21 12:26:22 [INFO] 95% Wilson CI: [66.5%, 74.4%]
2026-05-21 12:26:22 [INFO] Results saved to eval_results/xvla_prune_k0.5_libero_object.json
2026-05-21 12:26:22 [INFO] Elapsed: 76.0 min
```

### 各 Task 成绩

| Task | 描述 | SR |
|------|------|-----|
| 0 | alphabet soup | 96% (48/50) |
| 1 | cream cheese | 46% (23/50) |
| 2 | salad dressing | 98% (49/50) |
| 3 | bbq sauce | 80% (40/50) |
| 4 | ketchup | **100%** (50/50) |
| 5 | tomato sauce | 76% (38/50) |
| 6 | butter | 2% (1/50) |
| 7 | milk | 82% (41/50) |
| 8 | chocolate pudding | 26% (13/50) |
| 9 | orange juice | **100%** (50/50) |

### 为什么被标记为失败

监控系统检测到 "process dead 5× with no sentinel/W&B"——进程死了是因为它**正常退出**了，而该 eval 脚本没有写 sentinel 文件或上报 W&B，所以监控误判为失败。

### 当前服务器状态

- PID 715930 已退出（正常完成）
- GPU 2 已释放（1 MiB 占用）
- 结果已保存到 `eval_results/xvla_prune_k0.5_libero_object.json`

**无需重试，结果完整。** 监控系统的 sentinel/W&B 检测逻辑对 eval 脚本不适用，建议后续 eval 脚本结束时写一个 sentinel 文件以避免误报。

---
