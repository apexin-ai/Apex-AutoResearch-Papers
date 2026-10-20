# ops cleanup orphan gpu

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-orphan-gpu_20260514T123135_result.json`
- **Structured JSON:** [`7cbe98403ee63d820ef2.json`](../../sessions/7c/7cbe98403ee63d820ef2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告：GPU 残留进程

**3 个 GRPO 实验的子进程仍在运行，`kill_job` 只杀了父进程，子 worker 未被终止。**

| GPU | PID | 显存 | 运行时间 | 进程 | 状态 |
|-----|-----|------|---------|------|------|
| **0** | **50534** | 13052 MiB | 22min | `grpo_trainer ... grpo_ced_r4` | **残留** (父 PID 50529 已死) |
| **0** | 53071 | 98 MiB | 32s | `grpo_trainer ... grpo_ced_r5` | **新实验**，刚启动 |
| 1 | 45531 | 5326 MiB | 44min | `freige.eval.inference ... sft` | 预期 (SFT eval) |
| 1 | 47298 | 5326 MiB | 43min | `freige.eval.inference ... sft` | 预期 (SFT eval) |
| **2** | **50675** | 13054 MiB | 22min | `grpo_trainer ... grpo_extract_r2` | **残留** (父 PID 50670 已死) |
| **3** | **50946** | 13052 MiB | 22min | `grpo_trainer ... grpo_flatnli_r2` | **残留** (父 PID 50941 已死) |

**需要清理的残留进程**: PID 50534 (GPU 0), 50675 (GPU 2), 50946 (GPU 3) — 共占 ~39GB 显存。

**注意**: GPU 0 上还有一个新启动的 `grpo_ced_r5` (PID 53071)，仅 32 秒前启动，不确定是否是你有意发起的。

---
