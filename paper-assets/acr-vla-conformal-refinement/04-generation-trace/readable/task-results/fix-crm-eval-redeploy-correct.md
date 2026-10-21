# fix crm eval redeploy correct

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_crm-eval-redeploy-correct_20260522T232804_result.json`
- **Structured JSON:** [`5edf09ba6810ef92efd9.json`](../../sessions/5e/5edf09ba6810ef92efd9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。总结：

**已完成：**
- 确认 `--input_mode obs_only` 是 evaluate.py 不接受的参数，导致 CRM eval 静默失败
- 从 bjb2-28827 正在运行的 object CRM eval 提取了正确命令模板
- Kill 了 bjb1-32546 上 3 个错误的 goal eval sessions
- 在 bjb1-32546 部署了 5 个正确的 CRM eval（3 spatial + 2 goal），全部使用 PIPESTATUS 防护
- 所有 5 个进程已验证正常启动，日志无 argparse 错误

**待处理：**
- Goal seed44 CRM eval 暂无 GPU — 等 bjb2-28827 cuda:3/4/5 的 VLA-only spatial 跑完后可部署
- bjb2-28827 cuda:3,4,5 的 VLA-only spatial baseline 让其继续跑完（数据可用）

---
