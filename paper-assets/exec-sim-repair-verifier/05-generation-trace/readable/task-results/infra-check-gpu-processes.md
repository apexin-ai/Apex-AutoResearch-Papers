# infra check gpu processes

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-gpu-processes_20260516T183254_result.json`
- **Structured JSON:** [`e571be48aacb08746aa6.json`](../../sessions/e5/e571be48aacb08746aa6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进程状态汇总

| 实验 | PID | 状态 | GPU | GPU 利用率 | 显存占用 | 进度 | 预估剩余时间 |
|------|-----|------|-----|-----------|---------|------|-------------|
| **deepseek-cwm-repo** | 479953 | ALIVE | cuda:1 | 100% | 19.7/32.6 GB | 3031/4668 (65%) | ~9 min |
| **deepseek-cls-repo-v2** | 547065 | **DEAD** | cuda:0 | 0% | 0 MB | — | — |
| **deepseek-cls-repo-s123** | 542509 | ALIVE | cuda:2 | 99% | 17.6/32.6 GB | 303/6633 (5%) | ~19h |
| **deepseek-cwm-repo-s123** | 542901 | ALIVE | cuda:3 | 100% | 18.1/32.6 GB | 378/13266 (3%) | ~30h |

### 死亡进程诊断：deepseek-cls-repo-v2

启动即失败，原因：**参数错误**

```
train_unified.py: error: unrecognized arguments: --save_steps 500
EXIT_CODE=2
```

`train_unified.py` 不支持 `--save_steps` 参数。需要去掉该参数后重新启动。

### 备注
- deepseek-cwm-repo (seed=42) 即将完成，约 9 分钟后结束
- deepseek-cls-repo-s123 (seed=123) 刚启动不久，速度 ~11s/it
- deepseek-cwm-repo-s123 (seed=123) 也在早期阶段，速度 ~8.5s/it，总 steps 较多（13266）因为 cwm task 用了更大 batch 配置

---
