# diagnose eval openvla l2norm k09 long seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_openvla_l2norm_k09_long_seed42_v3_20260525T142007_result.json`
- **Structured JSON:** [`cb79e146c926275c3b1e.json`](../../sessions/cb/cb79e146c926275c3b1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 结论：实验已成功完成，无需重新提交

**根因**：实验实际上**正常运行并完成**了，但监控系统误判为失败。监控在检查时可能遇到了日志文件的读取时序问题（实验运行了 557 分钟 ≈ 9.3 小时，监控轮询时可能恰好在日志刷新间隙或进程检测窗口中未捕获到信号）。

**证据**：
1. **日志完整**：`eval_openvla_l2norm_k09_long_seed42_v3.log` (5826 bytes) 包含从模型加载到全部 10 个 task × 50 episodes 的完整输出
2. **结果已保存**：`eval_results/openvla_l2norm_prune_k09_10.json` 存在且完整，时间戳 `2026-05-25 22:06:40`
3. **Overall SR = 0.436** (218/500)，10 个 task 均有完整的 50 episode 评估
4. GPU 当前空闲（0MiB 占用），进程已正常退出
5. 磁盘空间充足（数据盘 29% used）

### 各 task 成功率

| Task | SR |
|------|-----|
| alphabet soup + tomato sauce → basket | 72% |
| cream cheese + butter → basket | 68% |
| stove + moka pot | 52% |
| black bowl → drawer | 34% |
| two mugs → plates | 24% |
| book → caddy | 78% |
| mug + pudding → plate | 24% |
| alphabet soup + cream cheese → basket | 48% |
| two moka pots → stove | 20% |
| mug → microwave | 16% |

### 行动建议
- **不需要重新提交**。数据已齐全，直接使用 `openvla_l2norm_prune_k09_10.json` 即可
- 监控系统中该实验的状态需要手动标记为成功
- 注意 JSON 中 `k_ratio` 字段为 `null`（可能是脚本写结果时的小 bug），但日志明确显示 `k=0.9`，`256 -> 230 vision tokens`，数据本身没问题

---
