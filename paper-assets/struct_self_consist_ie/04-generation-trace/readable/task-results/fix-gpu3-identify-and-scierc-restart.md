# fix gpu3 identify and scierc restart

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gpu3_identify_and_scierc_restart_20260515T192333_result.json`
- **Structured JSON:** [`0ecb7bb957b52e4307e4.json`](../../sessions/0e/0ecb7bb957b52e4307e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行。汇总：

### Part 1: GPU 3 进程
- PID 223820 已不存在，GPU 3 已自动释放
- GPU 2 上新出现 `run_freeform_inference.py`（8B SciERC seed789，PID 226169），是合法实验，未动

### Part 2: v2 标记
- `exp_qwen3_4b_scierc_finetune_v2`: status=DONE, conclusion=failed, notes 已更新

### Part 3: SciERC 4B finetune 重启
- v3 提交到 cuda:2 时因 freeform inference 占满 GPU 导致 OOM，已标记失败
- **v4 (`exp_qwen3_4b_scierc_finetune_v4`)** 成功启动在 **cuda:0**
  - PID: **227123** (实际 GPU 进程 227128)
  - 显存占用: 20.4GB / 32GB
  - 585 steps, ~2.0s/step → 预计 **~20 分钟**完成
  - Log: `~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune_v4.log`

### 当前 GPU 布局
| GPU | 占用 | 进程 |
|-----|------|------|
| 0 | 20.4GB, 86% | SciERC 4B finetune v4 |
| 1 | 18.8GB, 41% | CoNLL 4B resume |
| 2 | 30.4GB, 100% | freeform inference seed789 |
| 3 | 空闲 | — |

---
