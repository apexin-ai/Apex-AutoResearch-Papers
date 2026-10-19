# analysis bootstrap result check v2

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-result-check-v2_20260515T153952_result.json`
- **Structured JSON:** [`8e307c043d458a0859db.json`](../../sessions/8e/8e307c043d458a0859db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果文件 `bootstrap_s43_paired.json` 不存在于 results 目录。总结：

## Bootstrap 脚本状态

**3 次运行，全部失败，无结果产出。**

| 运行 | 日志 | 状态 |
|------|------|------|
| s43.log (22:46) | 30KB | Model 2 加载崩溃：`assert not result.missing_keys` — 旧代码对 adapter-only checkpoint 使用了 strict 断言 |
| s43_v2.log (22:51) | 577B | Model 1 pool encoding 阶段日志中断，疑似 SSH 超时 |
| s43_v3.log (23:38) | 1.2KB | **修复后版本**：Model 1 OK (R@1=0.5449)，Model 2 加载成功（434 missing keys 已改为 warning），但在 Model 2 query encoding 阶段进程消失 |

**v3 的问题**：脚本已修复了 assert 问题（改用 `strict=False` + warning），Model 2 成功加载，但进程在 encoding queries 时中断。没有 OOM 记录、没有 nohup.out。最可能原因是 **SSH 会话超时** 导致进程被杀——脚本需要 ~35 分钟完成（Model 1 encoding ~34 min + Model 2 encoding ~34 min + bootstrap），但没有用 nohup 正确后台化。

**下一步**：需要用 `nohup ... > /tmp/bootstrap_s43_v3.log 2>&1 &` 重跑脚本，确保 SSH 断连不会杀死进程。

---
