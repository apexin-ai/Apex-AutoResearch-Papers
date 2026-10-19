# check bjb2 40593 gpu status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb2-40593-gpu-status_20260525T034428_result.json`
- **Structured JSON:** [`450a76169044a6d0b5fa.json`](../../sessions/45/450a76169044a6d0b5fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb2-40593 状态汇报

**GPU**
- 1× RTX 4090D 24GB，利用率 0%，显存占用 0 MiB，**完全空闲**

**遗留进程**
- 系统服务（supervisord/sshd/jupyter/tensorboard/proxy）
- 两个 http.server：PID 308490（端口 19876，serving CRM checkpoint 目录）、PID 643113（端口 18888）
- 无遗留训练/Python 计算进程
- tmux 不可用（read-only 模式禁用，需要时改 ssh_execute 检查）

**磁盘**
- `/` (root): 30G 总, 9.7G 可用 (68% used) — 紧张
- `/root/autodl-tmp` (数据盘): 250G 总, 72G 可用 (72% used)

**环境就绪**
- ✅ CRM checkpoint: `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt` (1.3MB, May 24)
- ✅ evaluate.py 存在

**结论**：GPU 完全空闲可立即使用；checkpoint 与评估脚本齐备；根分区偏紧，新增产物务必写入 autodl-tmp。

---
