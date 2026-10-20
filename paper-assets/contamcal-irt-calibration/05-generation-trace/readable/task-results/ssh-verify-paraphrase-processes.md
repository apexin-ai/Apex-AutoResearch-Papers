# ssh verify paraphrase processes

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-paraphrase-processes_20260513T192928_result.json`
- **Structured JSON:** [`1c5fa390c97592e30692.json`](../../sessions/1c/1c5fa390c97592e30692.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认完毕。

```
进程状态：
- GPU 0 MMLU: ALIVE  PID=204758 (VLLM::EngineCore), 启动 03:15:27, 运行约 15 分钟
                      父进程 200967 已退出（正常，vLLM fork 后父进程退出）
- GPU 1 GSM8K: ALIVE  PID=189375 (python3), State=R (running), 启动 02:49:23, 运行约 41 分钟
- GPU 2 ARC:   ALIVE  PID=190717 (python3), State=R (running), 启动 02:50:43, 运行约 40 分钟

Hook 影响: 无破坏性操作。未发现任何 cleanup/restart/recover 进程。

输出目录: /root/autodl-tmp/exp001/paraphrases/
  - humaneval_paraphrases.json — 500KB, 已完成（03:10 写入）
  - mmlu/gsm8k/arc 尚未写出文件（进程仍在生成中）

日志 (phase1_paraphrase_v2.log):
  - MMLU vLLM 生成进度: 15/439 batches (3%), 预计剩余约 1 小时

GPU 状态:
GPU 0: 100% util, 22541/24564 MiB → VLLM::EngineCore (PID 204758)
GPU 1:  96% util, 15133/24564 MiB → python3 (PID 189375)
GPU 2:  95% util, 15201/24564 MiB → python3 (PID 190717)
GPU 3:   0% util,     0 MiB → idle
GPU 4:   0% util,     0 MiB → idle
GPU 5:   0% util,     0 MiB → idle
```

**结论：3 个进程全部安全运行，on_failed hook 未造成任何破坏。** 注意实际输出路径是 `/root/autodl-tmp/exp001/paraphrases/`（命令行 `--output-dir` 指定），不是 `artifacts/` 下。

---
