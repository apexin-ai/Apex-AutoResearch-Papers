# diagnose eval xvla random k05 spatial seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_xvla_random_k05_spatial_seed43_20260523T234137_result.json`
- **Structured JSON:** [`1fe2e5d1363c304dbbf1.json`](../../sessions/1f/1fe2e5d1363c304dbbf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### `eval_xvla_random_k05_spatial_seed43`: **误报，实验已正常完成**

日志和输出文件均确认实验成功运行完毕：
- **Overall SR: 72.6% (363/500)**，95% Wilson CI: [68.5%, 76.3%]
- 结果已保存至 `eval_results/eval_xvla_random_k05_spatial_seed43.json`
- 耗时 64.3 分钟，于 2026-05-24 07:29:23 正常退出

**Root cause**: cron 监控系统的 **false positive**。进程正常完成后退出（PID 155546 不再存在），监控系统检测到"process dead"但没有 sentinel/W&B 来确认成功，误判为失败。

### westd-38929 上当前运行实验状态: **健康**

| 实验 | GPU | 显存 | GPU利用率 | PID | 状态 |
|------|-----|------|-----------|-----|------|
| `eval_xvla_l2norm_k05_spatial_seed43` | GPU 0 | 4920MiB / 98GB | 49% | 330589 | 正常运行 |
| `eval_xvla_l2norm_k05_long_seed43` | GPU 1 | 5061MiB / 98GB | 38% | 432791 | 正常运行 |

GPU 2、3 空闲，磁盘 52GB 可用（80%），无异常。

### 其他 2 个失败实验

`eval_pi05_random_k03_goal_seed42` 和 `eval_pi05_attention_k05_object_seed42` 可能也是同样的 false positive 模式——需要分别检查它们的日志和输出文件确认。

### 建议

监控系统应增加检查实验输出文件是否存在（如 `eval_results/*.json`）作为成功判定条件，而不仅依赖进程存活和 sentinel/W&B。

---
