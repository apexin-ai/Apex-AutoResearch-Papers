# ops westb 1p5b progress check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_1p5b_progress_check_20260519T014121_result.json`
- **Structured JSON:** [`94a4d06dcedb1bac7e6f.json`](../../sessions/94/94a4d06dcedb1bac7e6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| Eval | 进度 | Interim Acc | EOS Rate |
|------|------|-------------|----------|
| **Standard 1.5B SFT** (cuda:1, PID 842784) | **~708/1319 (54%)** | **0.2386** (@ 700) | 91.57% |
| **RASP 1.5B SFT** (cuda:0, PID 845212) | **~854/1319 (65%)** | **0.2800** (@ 850) | 93.88% |

GPU 状态：cuda:0 68% util / 6.6GB, cuda:1 71% util / 6.5GB — 都在正常跑。

结果文件尚未写出（eval 脚本应在全部完成后才写 JSON）。按当前速度估算，RASP 约还需 ~1h，Standard 约还需 ~1.5-2h。

RASP interim acc (28.0%) > Standard interim acc (23.9%)，差距约 4.1pp。

---
