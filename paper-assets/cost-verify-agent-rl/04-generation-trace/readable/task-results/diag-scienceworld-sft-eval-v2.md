# diag scienceworld sft eval v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_scienceworld_sft_eval_v2_20260520T000103_result.json`
- **Structured JSON:** [`15be7d0999ea09ad9e89.json`](../../sessions/15/15be7d0999ea09ad9e89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/scienceworld_sft_eval_v2/report/diag_eval_v2.md`。

**诊断结论**：

- **根因**：原始脚本（`.bak`，325行）无 per-episode timeout、无 resume、无 error recovery。ScienceWorld Py4J gateway deadlock 时，Python 阻塞在 socket read 上无限 hang，不是 crash 而是 hang，所以日志无错误信息。
- **修复已到位**：当前脚本（421行）已加入 `signal.alarm(300)` timeout + `--resume` + gateway kill/rebuild 机制，进程稳定运行中（PID 195853，episode 465/1796）。
- **数据可用**：465 条 JSONL 记录全部有效（0 error，0 timeout，0 重复），35.9% success rate，无需从头跑。
- **剩余风险**：env 重建 (`ScienceWorldEnv("")`) 本身不在 alarm 保护范围内，如果 init 也 deadlock 会再次 hang。预计还需 ~18h 完成全部 1796 episodes。

---
