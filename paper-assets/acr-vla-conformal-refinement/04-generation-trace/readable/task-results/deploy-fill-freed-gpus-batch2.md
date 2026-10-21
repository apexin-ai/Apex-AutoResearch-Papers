# deploy fill freed gpus batch2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_fill-freed-gpus-batch2_20260519T184938_result.json`
- **Structured JSON:** [`6c1ee148c0fe89f31dfb.json`](../../sessions/6c/6c1ee148c0fe89f31dfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部正常启动，环境加载成功。

**部署汇总 (bjb1-32546):**

| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| `eval-vla-only-spatial-seed46` | cuda:0 | 47637 | RUNNING - spatial 10 tasks loaded |
| `eval-vla-only-spatial-seed47` | cuda:2 | 47706 | RUNNING - spatial 10 tasks loaded |
| `eval-vla-only-long-seed47` | cuda:3 | 47968 | RUNNING - long 10 tasks loaded |

注意：因为没有 `submit_training_job` 工具，用 tmux + ssh_execute 手动启动，没有自动注册 cron 监控。需要手动检查完成状态。

---
