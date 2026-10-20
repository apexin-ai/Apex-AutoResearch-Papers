# ops gpu status check all

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_all_20260520T142451_result.json`
- **Structured JSON:** [`e23683c97705e5cb03dc.json`](../../sessions/e2/e23683c97705e5cb03dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总

### westd-21461

| GPU | 任务 | 进程 | 利用率 | 显存 | 进度 | 预估剩余 |
|-----|------|------|--------|------|------|----------|
| GPU0 | d065 Qwen DocRED greedy con rerun | PID 194615 | 83% | 18.9 GB | **823/998** (log), jsonl 726行 | ~50 min |
| GPU1 | d066 LLaMA SciERC beam2 unc | PID 213209 | 87% | 18.4 GB | **242/551** (44%) | 运行中，无时间戳估算 |

- d065: 从上次 714 推进到 823，约 12% 的 FAIL（超时 ~77s），OK 样本 ~15s 均值。175 个剩余样本估算 ~50 min。

### westd-16980

| GPU | 任务 | 进程 | 利用率 | 显存 | 进度 | 预估剩余 |
|-----|------|------|--------|------|------|----------|
| GPU0 | d066 LLaMA DocRED beam4 s1 (constrained) | PID 763083 | 81% | 21.5 GB | **95/200** (47.5%) | ~8 min |
| GPU1 | 空闲 | 无 | 0% | 0 MB | — | — |

- beam4 unc 阶段已完成（200/200，22:18 结束），constrained 阶段 22:18 起跑，7 分钟完成 95 个样本，约 4.4s/样本，剩余 ~105 个 → **~8 min 完成**。
- westd-16980 已完成的 d066 beam sweep 文件：beam2 unc/s1, beam8 unc/s1, beam4 unc 均已跑完（都是 200 行），当前是最后一个 beam4 s1。

---
