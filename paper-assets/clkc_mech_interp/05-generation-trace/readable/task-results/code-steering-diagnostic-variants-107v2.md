# code steering diagnostic variants 107v2

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_steering-diagnostic-variants-107v2_20260522T112822_result.json`
- **Structured JSON:** [`eb35612cf6c136047cc9.json`](../../sessions/eb/eb35612cf6c136047cc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**脚本修改**（6 处）：
1. 添加 `--output_suffix` 参数
2. `run_steering_experiment` 新增 `position` 参数
3. Steering `SteeringHook` 传入 `position`
4. Control `SteeringHook` 传入 `position`
5. `main()` 调用时传递 `args.position`
6. 输出文件名使用 `steering_results{suffix}.json`

（`--peak_layer` 和 `--position` 已有，且 `load_steering_direction` 已经在指定层重新训练 probe，逻辑正确）

**两个诊断变体已启动**：

| 变体 | exp_id | GPU | PID | 层 | 位置 |
|------|--------|-----|-----|---|------|
| V1: L13/last | `steering_107_L13` | cuda:1 | 479381 | 13 | last |
| V2: L18/last | `steering_107_L18` | cuda:2 | 479644 | 18 | last |

**预计运行时间**：Steering v1 (L28) 在 136 samples × 10 alphas 约 1-2 小时，这两个变体配置相同应类似。变体 3 (L28/all-position) 等 cuda 释放后再跑。

---
