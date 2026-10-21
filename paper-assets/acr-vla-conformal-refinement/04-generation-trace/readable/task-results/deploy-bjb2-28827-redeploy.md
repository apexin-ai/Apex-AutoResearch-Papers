# deploy bjb2 28827 redeploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-redeploy_20260523T041001_result.json`
- **Structured JSON:** [`1dd84ed31eab0cf638cb.json`](../../sessions/1d/1dd84ed31eab0cf638cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 个实验全部启动正常，10 tasks loaded。

## 部署报告

### 1. Object VLA-only wrapper 3 seed JSON 检查
- **seed42**: JSON 存在但 n_rollouts=1（旧测试数据），无效。日志显示跑到 task 9/10 被杀
- **seed43**: 无 JSON。日志显示跑到 task 8/10 被杀
- **seed44**: 无 JSON。日志显示跑到 task 8/10 被杀
- **结论**: 3 个 seed 均无完整输出，evaluate.py 不支持 `--skip_completed`，全部重跑

### 2. 实验提交结果（6/6 成功）

| 实验 | exp_id | GPU | PID |
|------|--------|-----|-----|
| Object VLA-only s42 | eval-object-vla-only-wrapper-s42-r2 | cuda:3 | 519749 |
| Object VLA-only s43 | eval-object-vla-only-wrapper-s43-r2 | cuda:4 | 520493 |
| Object VLA-only s44 | eval-object-vla-only-wrapper-s44-r2 | cuda:5 | 521785 |
| Object Adaptive CRM s42 | eval-supp-obj-adapt-s42-r2 | cuda:0 | 522259 |
| Object Reconvla s42 | eval-supp-obj-reconvla-s42 | cuda:1 | 523238 |
| Goal CRM norm=0.05 s42 | eval-supp-goal-crm005-s42 | cuda:2 | 524322 |

### 3. GPU 占用
- GPU 0: 5747 MiB, 13% util (adaptive CRM)
- GPU 1: 2716 MiB, 加载中 (reconvla)
- GPU 2: 刚启动 (goal CRM)
- GPU 3-5: ~5630 MiB, 17-21% util (VLA-only x3)

### 4. 日志确认
6 个实验均已加载 10 tasks，正在运行 rollouts。

### 5. Registry
- eval-supp-obj-adapt-s42-r2 已设 parent: eval-3dir-adaptive-spatial-s42

### 6. 异常：无

---
