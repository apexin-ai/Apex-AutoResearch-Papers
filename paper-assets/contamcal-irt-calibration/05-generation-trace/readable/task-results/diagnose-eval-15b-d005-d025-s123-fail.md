# diagnose eval 15B d005 d025 s123 fail

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_15B_d005_d025_s123_fail_20260515T134549_result.json`
- **Structured JSON:** [`2af98a2f0a1d38e32d66.json`](../../sessions/2a/2af98a2f0a1d38e32d66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 根因：SIGHUP（信号断连），非 OOM/代码问题

**证据链：**

1. **退出记录**：两个实验在完全相同的秒数退出 — `129|2026-05-15T13:42:57Z`。同一秒双杀 = 系统级事件，不是代码 bug。

2. **EXIT_CODE=129 = SIGHUP**：进程收到 HUP 信号（通常由终端/session 断连触发）。wrapper 脚本中有明确的 `trap 'exit 129' HUP`。

3. **排除 OOM**：系统内存 1TB 总量仅用 56GB，GPU 显存每个实验仅占 ~5.8GB/24.5GB，远未满载。

4. **排除代码/adapter 问题**：两个实验使用不同的 adapter（d005 vs d025），同时以相同方式死亡 → 不可能是代码逻辑或数据问题。

5. **父进程**：两个 wrapper 的 PPID 都是 208932（一个 tmux session，5月14日创建，至今存活）。最可能的场景是 tmux 中的某个窗口被关闭、或 SSH attach 断连导致 HUP 传播到该窗口的子进程。

### 当前状态：实验已自动重试且正常运行

| 实验 | 当前 PID | GPU | 进度 | 状态 |
|------|---------|-----|------|------|
| d005_s123 | 566219→566224 | cuda:0, 5848MiB | MMLU ~88% (12359/14042) | 正常运行 |
| d025_s123 | 566306→566311 | cuda:1, 5848MiB | MMLU ~88% (12382/14042) | 正常运行 |

评估输出目录（`Qwen2.5-1.5B_d005_s123_aligned/` 和 `Qwen2.5-1.5B_d025_s123_aligned/`）目前为空，说明之前那次失败时没产出结果文件，当前这次还在跑 MMLU 尚未写入。MMLU 完成后还有 gsm8k、arc_challenge、humaneval 三个 benchmark。

### 结论

- **Transient failure**，无需修复代码或环境
- 实验已被自动重提交，正在正常推进
- 注意 bitsandbytes 的 `libnvJitLink.so.13` 加载失败是 warning 级别，不影响评估功能
- 唯一需要注意的：exit 文件 (`/tmp/agent-ml-exit/`) 里还残留着旧的 `129` 记录，当前运行结束后会被正确覆盖

---
