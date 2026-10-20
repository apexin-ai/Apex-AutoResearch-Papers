# ssh repo level cwm v6 submit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_repo-level-cwm-v6-submit_20260512T185917_result.json`
- **Structured JSON:** [`6d9f12269f7789252b8f.json`](../../sessions/6d/6d9f12269f7789252b8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 总结

**repo-level-cwm-v6 训练已成功提交并稳定运行。**

| 项目 | 值 |
|------|-----|
| PID | 83684 |
| GPU | cuda:0（物理 GPU 0） |
| GPU 占用 | 22,349 MiB / 32,607 MiB（69%） |
| batch_size | 1（v5 为 2，OOM） |
| grad_accumulation | 32（保持有效 batch size = 32） |
| 总步数 | 6633 |
| 速度 | ~8 s/step |
| 预估时长 | ~14.7 小时 |
| 预计完成 | ~2026-05-13 18:00 UTC |
| save_steps | 500 |
| Checkpoint 路径 | `/root/autodl-tmp/checkpoints_repo_cwm_v6/` |
| 日志路径 | `~/runs/exec-sim-repair-verifier/repo-level-cwm-v6.log` |

**修复措施**：发现服务器上有 8+ 个残留 python 训练进程导致 GPU 0 OOM。全部 kill 后将 batch_size 从 2 降到 1，GPU 占用从 26.5GB 降到 22.3GB，留出 10GB headroom。

---
