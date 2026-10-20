# ssh qwen kill investigation

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_qwen-kill-investigation_20260514T051704_result.json`
- **Structured JSON:** [`69b1e66172fa8c05dac1.json`](../../sessions/69/69b1e66172fa8c05dac1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查结果：

**Kill 原因：被 v6_random 实验启动挤占，非 OOM。**

4 个 Qwen 实验在 13:07-13:08 同时被终止（日志无错误、dmesg 无 OOM），v6_random tmux session 恰好在 13:08 创建并接管了全部 4 块 GPU。`/tmp/agent-ml-exit/` 无 qwen exit code 文件，说明进程被 SIGKILL。

- **Qwen 模型完整可用**（15GB，4 分片齐全）
- **v6_random 全部健康**（s015: 18/50, s020: 20/50, s025: 13/50, s030: 4/50）
- **可安全重跑** Qwen 实验，等 v6_random 跑完释放 GPU 即可

报告已保存到 `artifacts/qwen_kill_investigation.md`。

---
