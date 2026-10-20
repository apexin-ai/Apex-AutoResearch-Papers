# analysis task complexity routing

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_task_complexity_routing_20260518T211156_result.json`
- **Structured JSON:** [`2a9f0bdd39d230845833.json`](../../sessions/2a/2a9f0bdd39d230845833.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 分组表格（按 |ΔR²| 降序）

| Task | |ΔR²| | Group |
|------|-------|-------|
| wine on rack | 0.2346 | complex |
| bowl on cabinet | 0.2006 | complex |
| bowl on stove | 0.1598 | complex |
| cream cheese in bowl | 0.1594 | **simple** |
| bowl on plate | 0.0986 | complex |
| open top drawer + bowl | 0.0754 | complex |
| wine on cabinet | 0.0740 | complex |
| turn on stove | 0.0359 | simple |
| open middle drawer | 0.0240 | simple |
| push plate to stove | 0.0067 | simple |

### 统计结果

| Metric | Complex (n=6) | Simple (n=4) |
|--------|--------------|--------------|
| Mean |ΔR²| | 0.1405 | 0.0565 |
| Median |ΔR²| | 0.1292 | 0.0299 |

- **Mann-Whitney U = 21.0, p = 0.033** (单侧)
- **Effect ratio = 2.49x**

### 结论

Instruction-discriminative tasks 的 L1 ablation effect 显著大于 visually unambiguous tasks (p < 0.05)，均值差 2.49 倍。

注意 outlier："cream cheese in bowl" 被分为 simple 但 |ΔR²| = 0.159，可能因为 bowl 作为目标容器出现在多个其他任务中，使其也隐含了 instruction dependence。排除此 outlier 后 simple 均值降至 0.022，effect ratio 升至 6.3x。

### 产出文件

- JSON: `/root/autodl-tmp/vla-ssd/results/task_complexity_routing.json`
- Figure: `/root/autodl-tmp/vla-ssd/results/figures/fig_task_complexity_routing.{pdf,png}`
- Registry: `task_complexity_routing` → DONE (success)

---
