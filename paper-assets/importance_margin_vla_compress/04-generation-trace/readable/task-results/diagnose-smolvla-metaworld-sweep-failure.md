# diagnose smolvla metaworld sweep failure

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_smolvla_metaworld_sweep_failure_20260524T181755_result.json`
- **Structured JSON:** [`ebd3ebd575f207d9954c.json`](../../sessions/eb/ebd3ebd575f207d9954c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 诊断结论

**根因：监控系统误报，实验实际已全部成功完成。**

监控报 "process dead 5× with no sentinel/W&B — auto-resolved as failed" 是因为 cron entry 中没有配置 `log_path`，自动发现也未找到位于 `/tmp/` 的日志文件。脚本本身无 bug，两个 sweep 均正常跑完并输出了 `ALL_RANDOM_DONE` / `ALL_L2NORM_DONE` sentinel。

### 完整结果 (50 ep/task × 5 tasks, Overall SR)

| Method | k=0.5 | k=0.85 | k=0.9 | k=0.95 | Baseline |
|--------|-------|--------|-------|--------|----------|
| Random | 9.6% | 4.4% | 5.6% | 6.4% | 26.4% |
| L2Norm | 0.8% | 2.4% | **10.0%** | 7.2% | 26.4% |

### 关键观察
- Token pruning 对 SmolVLA + MetaWorld 伤害极大，最佳点 L2Norm k=0.9 (10.0%) 仅为 baseline 的 38%
- Random pruning 结果非单调（k=0.5 反而比 k=0.95 好），噪声较大
- drawer-open 最鲁棒（L2Norm k=0.95: 30%），其余 tasks 基本归零
- 结果文件路径：`/root/autodl-tmp/importance_margin_vla_compress/results/{random,l2norm}_k{0.5,0.85,0.9,0.95}.json`

### 修复建议
提交 sweep 任务时配置 `log_path` 指向持久化路径（非 /tmp），或让脚本输出 W&B sentinel，使监控系统能正确追踪。

---
