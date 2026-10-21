# debug check random ablation results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_check_random_ablation_results_20260518T033440_result.json`
- **Structured JSON:** [`89ee44e85906e2b11975.json`](../../sessions/89/89ee44e85906e2b11975.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

| 项目 | 状态 |
|------|------|
| `results/random_subset_ablation.json` | **不存在** |
| `results/figures/fig_random_subset_ablation.pdf` | **不存在** |
| `scripts/random_subset_ablation.py` | 存在 (23KB, 今天 11:30 修改) |
| 进程 | **PID 655881 正在运行** (CPU 1705%, 已跑 ~37 分钟) |

进程详情：
```
python3.12 -u scripts/random_subset_ablation.py \
  --demos_per_task 5 --n_random 3 \
  --output /tmp/test_fixed.json \
  --fig_dir /tmp/
```

注意输出路径是 `/tmp/test_fixed.json`，不是预期的 `results/` 目录。看起来是测试运行（参数较小：`n_random=3`）。

日志只有 18 行，最后更新在 11:35（启动后 3 分钟），之后无新输出。当前处于 **Phase 1：加载模型并缓存 attention 中间结果**，已枚举 3 个 task。进程仍在高 CPU 运行，说明正在做推理计算，没有中间打印。

---
