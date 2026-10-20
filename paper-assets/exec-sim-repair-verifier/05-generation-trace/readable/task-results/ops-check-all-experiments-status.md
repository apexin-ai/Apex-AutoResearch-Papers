# ops check all experiments status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-all-experiments-status_20260516T013749_result.json`
- **Structured JSON:** [`aec62ffc0d695101d0b8.json`](../../sessions/ae/aec62ffc0d695101d0b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

**4 个实验全部存活，无异常。**

| 实验 | GPU | 进度 | Accuracy | ETA |
|------|-----|------|----------|-----|
| cwm8b-ckpt400-test-eval-v3 | cuda:3 | 5712/9784 (58%) | 62.8% | ~8h (~17:45 UTC) |
| cwm8b-ckpt400-test-eval-shard2 | cuda:1 | 7784/9784 (80%) | 69.2% | ~3.8h (~13:25 UTC) |
| cls8b-seed123-ckpt3000-mutation | cuda:0 | 7330/9784 (75%) | 85.4% | **~5 min** |
| cls8b-s42-resume-ckpt3600-test-v2 | cuda:2 | 8630/9784 (88%) | 84.3% | **~2.5 min** |

**Registry 操作**：`cls8b-s42-resume-ckpt3600-test-v2` 从 ALLOCATED → RUNNING（PID 446868 确认存活）。

两个 CLS eval 即将完成，两个 CWM eval 还需数小时（生成 1024 tokens vs 分类 8 tokens，速度差 ~50x）。

---
