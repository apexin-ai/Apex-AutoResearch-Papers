# deploy pi05 object eval 3seeds

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_pi05-object-eval-3seeds_20260522T010324_result.json`
- **Structured JSON:** [`8b87c317f76d8456e988.json`](../../sessions/8b/8b87c317f76d8456e988.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个进程全部在运行。

**部署结果：**

| 实验 | GPU | PID | tmux session |
|------|-----|-----|-------------|
| eval-pi05-crm-object-seed42 | cuda:0 | 218131 | eval-pi05-crm-object-seed42 |
| eval-pi05-crm-object-seed43 | cuda:1 | 218420 | eval-pi05-crm-object-seed43 |
| eval-pi05-crm-object-seed44 | cuda:2 | 218700 | eval-pi05-crm-object-seed44 |

- Checkpoint 已确认在 bjb1-32546（2.4M）
- 无残留 eval 进程
- 3 个 registry 条目已创建（PREPARING → RUNNING），hypothesis 和 parent 已设置
- 日志路径：`/root/runs/acr-vla-conformal-refinement/eval-pi05-crm-object-seed{42,43,44}.log`

---
