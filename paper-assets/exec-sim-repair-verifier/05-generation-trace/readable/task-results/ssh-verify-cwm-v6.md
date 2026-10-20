# ssh verify cwm v6

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-cwm-v6_20260512T194444_result.json`
- **Structured JSON:** [`9770f6b6d7032ce33e85.json`](../../sessions/97/9770f6b6d7032ce33e85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cwm-v6 正在正常训练，不是僵尸进程。**

核心指标：
- PID 84887 存活，状态 `Sl`，运行 27 分钟
- GPU cuda:2 利用率 **94%**，显存 22.3/32.6 GB
- 当前 step ~65/6633 (1%)，速度 ~8s/step，预计还需 ~14.5 小时
- Step 50 输出 loss=28.168, grad_norm=17.59

两个需关注的点：
1. **checkpoint 目录为空** — `/root/autodl-tmp/checkpoints_repo_cwm_v6/` 下无文件，已过 step 50。需确认训练脚本的 save_steps 配置是否正确，否则训练中断会丢失全部进度。
2. **初始 loss 偏高 (28.168)** — 训练刚开始，暂不告警，但建议下次检查时确认 loss 在下降。

报告已写入 `artifacts/cwm_v6_health_check.md`。

---
