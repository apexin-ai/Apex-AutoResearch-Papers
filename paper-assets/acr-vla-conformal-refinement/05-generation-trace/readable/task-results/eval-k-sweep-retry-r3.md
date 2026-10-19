# eval k sweep retry r3

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_k-sweep-retry-r3_20260517T221500_result.json`
- **Structured JSON:** [`f9c02e8051a5326a0549.json`](../../sessions/f9/f9c02e8051a5326a0549.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**K=5 和 K=20 实验已经在运行中，无需重新提交。**

当前 bjb1-18228 GPU 占用情况：

| GPU | 进程 | 启动时间 | 运行时长 |
|-----|------|---------|---------|
| cuda:0 | K=5 eval (PID 713405) | 02:54 | ~3.3h |
| cuda:1 | K=1 eval / OpenVLA (PID 747644) | — | — |
| cuda:2 | K=20 eval (PID 713480) | 02:54 | ~3.3h |
| cuda:3 | perdof seed45 (PID 749547) | 05:03 | ~1.2h |

K=5 和 K=20 的命令与任务要求一致（同 checkpoint、同参数），唯一区别是输出文件名没有 `_r3` 后缀（当前写入 `eval_object_obs_only_norm02_k5_seed42.json` 和 `eval_object_obs_only_norm02_k20_seed42.json`），且未设置 `HF_HUB_OFFLINE=1` 等环境变量（但因为模型已在本地缓存，不影响离线运行）。

**服务器稳定性**: uptime 4 天 19 小时，无近期重启。dmesg 权限受限无法读取，但 uptime 确认系统稳定。

**结论**: 这两个实验已经被成功重启（第 3 次尝试），目前正常运行中。4 个 GPU 全部占满，并发 = 4（达上限）。建议等待当前运行完成，无需再次提交。

是否需要我将这两个运行中的实验注册到 registry？

---
