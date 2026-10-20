# diagnose full occ ln v2 s1

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_full_occ_ln_v2_s1_20260526T182633_result.json`
- **Structured JSON:** [`81afdb38b24fc880ade2.json`](../../sessions/81/81afdb38b24fc880ade2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**失败原因**：重试机制向训练命令注入了 `--resume_from_checkpoint &lt;path>`，但 finetune.py 不接受此参数（它用的是 `--resume` + `--resume_step`），导致 argparse 报错退出（exit code 2）。

**根因**：重试逻辑检测到已有 checkpoint 后，使用了 HuggingFace 风格的 `--resume_from_checkpoint` 参数名，与 finetune.py 实际的参数接口不匹配。

**当前状态**：第4次重试已自动启动（PID 391060, cuda:2），这次命令正确（无 resume 参数），从 step 0 重新训练。当前进度 ~276/50005，速度 ~1.07 it/s，预计 ~13h 完成（约 05-27 15:30 UTC）。在 DDL（05-28 12:00 UTC）之前可以完成。

**其他实验**：GPU 0/1/3 上的 reverse_cutoff_s2_v2、full_occ_ln_v2_s0、detach_ln_v2_s0 均正常（99% 利用率），未受影响。

**建议**：修复重试机制中的 resume 参数名映射，避免后续实验再踩同样的坑。

---
