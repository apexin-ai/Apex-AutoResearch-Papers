# harvest s43 r2 and submit s44 r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_s43_r2_and_submit_s44_r2_20260519T054059_result.json`
- **Structured JSON:** [`82f46a534aec0e721a20.json`](../../sessions/82/82f46a534aec0e721a20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

s44_r2 启动成功，cuda:3 占用 27439 MiB，训练已开始 (7/567 steps)。

## 汇总

### Part 1: s43_r2
- **结论**: success，567/567 steps 完成
- **Checkpoint**: `/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43/`
- Registry 已更新 conclusion=success

### Part 2: s44_r2
- 首次提交因 `CUDA_VISIBLE_DEVICES=0` 覆盖导致 OOM（撞上 D112 在 cuda:0），已修正为 `CUDA_VISIBLE_DEVICES=3` 重新提交
- **PID**: 618021, cuda:3, 27439/32607 MiB
- 训练进行中 7/567 steps，~3s/it，预计 ~28min

### Part 3: D112 step 3
- PID 613075 仍在运行（子进程 613076，已运行 1h08m）
- 训练进度 **240/567 steps** (~42%)，~7s/it，剩余约 38min
- 尚未完成，step 4 暂不提交

### GPU 状态
| GPU | 显存占用 | 利用率 | 任务 |
|-----|---------|--------|------|
| 0 | 29639/32607 MiB | 99% | D112 step 3 |
| 1 | 16183/32607 MiB | 100% | 其他任务 |
| 2 | 25209/32607 MiB | 100% | 其他任务 |
| 3 | 27439/32607 MiB | 95% | s44_r2 训练中 |

---
