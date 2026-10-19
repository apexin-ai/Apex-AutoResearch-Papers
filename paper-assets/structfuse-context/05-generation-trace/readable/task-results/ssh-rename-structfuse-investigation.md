# ssh rename structfuse investigation

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rename_structfuse_investigation_20260513T222818_result.json`
- **Structured JSON:** [`d52b0cce32f2ac2a7727.json`](../../sessions/d5/d52b0cce32f2ac2a7727.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。报告写入 `artifacts/rename_safety_report.md`。

核心发现：**重命名已经执行完毕**，当前 `/root/structfuse` 是指向 `/root/structfuse-context` 的符号链接，两个训练进程 cwd 均已指向新目录，训练不受影响。

需注意：
- 2 个 shell 脚本 + 10 个 Python 文件中仍有旧路径 `/root/structfuse/` 的硬编码引用，目前靠符号链接兜底
- **符号链接不能现在删除** — 两个脚本的 loop 每轮 run 都会重新解析这些绝对路径
- 训练结束后应批量 sed 替换这些路径，然后删除符号链接

---
