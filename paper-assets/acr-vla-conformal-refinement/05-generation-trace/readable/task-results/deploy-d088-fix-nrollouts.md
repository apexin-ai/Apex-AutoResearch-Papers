# deploy d088 fix nrollouts

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_d088-fix-nrollouts_20260520T171807_result.json`
- **Structured JSON:** [`0a17b60fcf23c336473a.json`](../../sessions/0a/0a17b60fcf23c336473a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：

| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| eval-adaptive-unc-head-object-seed42 | cuda:0 | 741948 | 运行中，10 tasks loaded |
| eval-adaptive-unc-head-object-seed43 | cuda:1 | 742213 | 运行中，10 tasks loaded |
| eval-obs-only-object-norm003-seed43 | cuda:4 | 742545 | 运行中，10 tasks loaded |
| eval-adaptive-unc-head-object-seed44 (保留) | cuda:5 | 728278 | 运行中 (21:51 elapsed) |

- 3 个错误进程 (n_rollouts=100) 已 kill
- 无异常 exit files
- 3 个新进程全部正常启动，UncHead/CRM 模型加载成功，10 tasks loaded
- seed44 (cuda:5) 未受影响

---
