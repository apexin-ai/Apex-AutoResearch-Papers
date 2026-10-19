# deploy bjb1 32546 force fill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-32546-force-fill_20260528T084657_result.json`
- **Structured JSON:** [`5a8e6b8c44471319c713.json`](../../sessions/5a/5a8e6b8c44471319c713.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 张卡全部填满，6 个 tmux session 运行中。GPU 4 和 5 还在加载模型阶段（显存正在上涨）。

### 部署汇总

| GPU | exp_id | PID |
|-----|--------|-----|
| cuda:0 | smolvla-tau045-spatial-s42 | 627129 |
| cuda:1 | smolvla-crm-norm005-spatial-s42-d149 | 627406 |
| cuda:2 | eval-obs-only-object-norm003-seed65 | 628011 |
| cuda:3 | eval-obs-only-object-norm005-seed64 | 629839 |
| cuda:4 | eval-obs-only-object-norm01-seed74 | 630922 |
| cuda:5 | eval-obs-only-object-norm003-seed73 | 632374 |

**跳过**：无，候选 #1-#6 全部一次成功。

**nvidia-smi 确认**：GPU 0-3 已分配 5.7-6.3GB 显存运行中，GPU 4-5 正在加载（1.8GB / 4MB，模型加载中）。

---
