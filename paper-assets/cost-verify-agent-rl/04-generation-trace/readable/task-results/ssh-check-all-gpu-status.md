# ssh check all gpu status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_all_gpu_status_20260523T031312_result.json`
- **Structured JSON:** [`a0b522e06e6d95f93751.json`](../../sessions/a0/a0b522e06e6d95f93751.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告

### westd-47453（4× RTX PRO 6000 96GB）

| GPU | 显存使用 | 利用率 |
|-----|---------|--------|
| 0 | 0 / 97887 MiB | 0% |
| 1 | 0 / 97887 MiB | 0% |
| 2 | 0 / 97887 MiB | 0% |
| 3 | 0 / 97887 MiB | **100%** |

- **无 GPU 进程**（nvidia-smi 未报告 compute apps）
- GPU 3 利用率 100% 但显存 0，可能是短暂状态或驱动误报
- 仅有系统服务进程：jupyter-lab、tensorboard
- 无 tmux session

### bjb1-17606（2× GPU 96GB）

| GPU | 显存使用 | 利用率 |
|-----|---------|--------|
| 0 | 0 / 97887 MiB | 0% |
| 1 | 0 / 97887 MiB | 0% |

- **无 GPU 进程**
- **有残留进程**：
  - 5 个 `ray::TaskRunner` 进程（PID 433097/444677/447671/449672/453685），占用大量 CPU 内存（最大 ~6.4GB），但未占用 GPU 显存
  - 1 个 `python -m http.server 18923`（expert_sft 相关）
  - 系统服务：jupyter-lab、tensorboard
- 无 tmux session

**结论**：两台服务器 GPU 显存均空闲。bjb1-17606 上有 5 个 ray::TaskRunner 残留进程占用 CPU 内存，如不再需要建议清理。

---
