# ops fix cron exit129 logic

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-cron-exit129-logic_20260528T070507_result.json`
- **Structured JSON:** [`74cb15aac73a1d940139.json`](../../sessions/74/74cb15aac73a1d940139.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本都已读取完毕。分析如下：

**westd-34685 `poll_eval_detach_ln_v2_s2.sh`** 和 **westd-10894 `poll_eval_vanilla_object_s1.sh`** 的逻辑都是：
1. 轮询检测 `50000_chkpt` 目录 + `adapter_config.json` 存在
2. 等待 60s 确保写入完成
3. `kill` 训练进程（不依赖其退出码）
4. 启动 eval
5. `break` 退出循环

两个脚本都**不使用训练进程的退出码做任何判断**。`$?` 只在日志中记录的是 eval 的退出码，不是训练的。脚本最终通过 `break` 退出 while 循环，自身退出码为 0（最后执行的 `echo` 成功）。

**结论：脚本本身无问题，问题在 cron 监控层。**

cron 监控系统独立追踪训练进程的 PID，当训练进程被轮询脚本 kill 后以 exit 129 (128 + SIGHUP) 退出时，cron 系统将其判定为 `conclusion=failed`。这是 cron 监控系统的退出码判定逻辑问题——它没有区分"被外部 kill 导致的非零退出"和"训练本身失败导致的非零退出"。

按要求，不修改 cron 监控代码。

---
