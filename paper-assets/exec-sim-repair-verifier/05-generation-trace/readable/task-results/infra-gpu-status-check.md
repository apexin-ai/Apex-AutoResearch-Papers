# infra gpu status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-status-check_20260516T183909_result.json`
- **Structured JSON:** [`069574b4df5a2e7c1a13.json`](../../sessions/06/069574b4df5a2e7c1a13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态

| GPU | 显存 | 利用率 | 任务 | PID | 进度 |
|-----|------|--------|------|-----|------|
| cuda:0 | **0 MiB** / 32607 MiB | **0%** | **空闲** | — | — |
| cuda:1 | 19713 / 32607 MiB | 99% | deepseek-cwm-repo (s42) | 479953 | **92% (4294/4668)** |
| cuda:2 | 17633 / 32607 MiB | 100% | deepseek-cls-repo-s123 | 542509 | **5% (338/6633)** |
| cuda:3 | 18061 / 32607 MiB | 99% | deepseek-cwm-repo-s123 | 542901 | **3% (424/13266)** |

### cuda:0 状态

**空闲。** `deepseek-cls-repo-v3` (PID 547808) 已死——日志显示启动失败：

```
train_unified.py: error: unrecognized arguments: --resume_from_checkpoint /root/autodl-tmp/checkpoints_deepseek_cls_repo/checkpoint-2211
EXIT_CODE=2
```

`train_unified.py` 不支持 `--resume_from_checkpoint` 参数，导致立即退出。

### Registry 需更新的条目

| 条目 | 记录 PID | 实际状态 |
|------|----------|----------|
| deepseek-cls-repo-v3 (cuda:0) | 547808 | **已死** — 参数错误退出 |
| deepseek-cls-repo-resume (cuda:0) | 546754 | **已死** — 早已结束 |

### 进度预估

- **cwm-repo (cuda:1)**: 92%，剩余 ~374 步，约 2 分钟/步 → **~12 分钟后完成**
- **cls-repo-s123 (cuda:2)**: 5%，~11s/step，剩余 6295 步 → **~19 小时**
- **cwm-repo-s123 (cuda:3)**: 3%，~8.3s/step，剩余 12842 步 → **~30 小时**

---
