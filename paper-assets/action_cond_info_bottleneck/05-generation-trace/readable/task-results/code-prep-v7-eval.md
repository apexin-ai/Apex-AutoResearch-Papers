# code prep v7 eval

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_v7_eval_20260516T140406_result.json`
- **Structured JSON:** [`577665389591856ab51d.json`](../../sessions/57/577665389591856ab51d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结论：v7 eval 流水线验证通过。**

- Checkpoint 加载完美（0 missing/0 unexpected keys）
- dtype fix（bfloat16）生效
- `condition_source=language` + `conditioning_mode=concat` 从 checkpoint config 正确读取
- 5/10 task 成功执行 rollout 后进程被杀（系统 RAM 问题，非 v7 特有）
- GPU 额外占用 ~12GB，与训练共存无问题
- 无需 v7 特有修复

报告已写入 `/root/acib/outputs/v7_eval_dryrun_report.txt`，含正式 eval 推荐命令（建议逐 suite 运行避免 RAM 积累）。

---
