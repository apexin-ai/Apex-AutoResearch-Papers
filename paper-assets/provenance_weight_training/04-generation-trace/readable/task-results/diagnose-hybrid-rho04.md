# diagnose hybrid rho04

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_hybrid_rho04_20260517T001804_result.json`
- **Structured JSON:** [`1f7daabf3bd7123f4e2d.json`](../../sessions/1f/1f7daabf3bd7123f4e2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有需要删除的 cron。

## 总结

**hybrid_rho04_seed42 诊断完成：**
- 训练成功完成 6103/6103 steps（耗时 ~12h49m）
- Eval 结果：**Loss=2.863, PPL=17.514**
- Registry 已更新为 DONE/success

**对比：**
| 实验 | PPL |
|------|-----|
| detect_remove | 17.29 |
| **hybrid_rho04** | **17.51** |
| adaptive ρ=0.4 | 17.65 |

Hybrid 比 pure adaptive 好（17.51 vs 17.65），但不如 pure detect_remove（17.29）。硬过滤移除最差样本的效果优于混合策略。

**环境状态：**
- tmux 已可用 (3.2a)
- cuda:2 现已空闲，可提交 batchsize16_nmin8_seed42

---
