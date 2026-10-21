# ssh check fewshot bcs v2 status

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_fewshot_bcs_v2_status_20260517T134249_result.json`
- **Structured JSON:** [`9a99272383bef8a625e8.json`](../../sessions/9a/9a99272383bef8a625e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

| 项目 | 状态 |
|------|------|
| **PID 480497** | Running (bash wrapper) |
| **相关进程** | PID 480496 (tmux session), PID 480501 (timeout wrapper), PID 480502 (python3 主进程), PID 480593 (extract 子进程) |
| **GPU** | NVIDIA RTX PRO 6000 Black, 89357/97887 MiB 占用 (vLLM engine), GPU-Util 15% |
| **tmux session** | `exp_fewshot_bcs_v2` (created 21:39:04) |

### 实验进度

- **当前位置**: [32/150] — 已完成 31 个 inference task，正在处理第 32 个
- **当前阶段**: 0-shot inference，正在跑 `high_6_shot0` (BCS=0.7934, 8 types, 96 samples)
- **已用时间**: ~4 分钟 (21:39 开始，当前 21:43)
- **速度**: 每个 task 约 4 秒
- **预计剩余**: 还有 ~118 个 task × 4s ≈ **~8 分钟完成 0-shot 阶段**

注意：`--n_shots 0 1 5` 意味着还有 1-shot 和 5-shot 阶段。如果每阶段都是 150 个 task，总计需要 ~450 个 task，还剩 ~420 个，预计 **~28 分钟** 完成全部 inference。另外还有一个 `--stage extract` 子进程 (PID 480593) 已在并行运行 bootstrap CI 计算。

无错误输出。

---
