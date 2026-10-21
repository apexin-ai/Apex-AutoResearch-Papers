# diagnose cron false failure root cause

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cron-false-failure-root-cause_20260522T023419_result.json`
- **Structured JSON:** [`2bbc463fc2c346b0eec4.json`](../../sessions/2b/2bbc463fc2c346b0eec4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

根因完全清晰了。以下是完整诊断。

---

## 诊断结果

### 两个实验的具体根因

#### 1. test_eval_4b_rsft_s42_v2

**第一次提交**（通过 `submit_training_job`，pid=146146）：
- 命令含 `--rsft_adapter` 参数，但 `test_inference.py` 不识别该参数
- argparse 打印 usage 并返回 exit code 2
- EXIT trap 正确记录 `EXIT_CODE=2` 到 sentinel
- **这次失败是合理的**

**第二次提交**（on_failed hook 自动重试，pid=146485）：
- 修正了命令，实验成功完成，产出了正确结果
- **但重试不是通过 `submit_training_job` 提交的**（通过 `ssh_execute` 直接运行）
- 没有 tmux wrapper → 没有 `rm -f` 清除旧 sentinel → 没有 EXIT trap 写新 sentinel
- 旧 sentinel（EXIT_CODE=2）仍然存在
- cron 在 01:14 检测到进程死亡 → 读到旧 sentinel → `EXIT_CODE=2` → 再次标记 failed

**证据**：sentinel 文件 mtime 是 00:01 UTC（第一次失败时间），而实验结果 mtime 是 01:12 UTC（第二次完成时间）。log 文件仍然是第一次的 argparse 错误输出，未被第二次覆盖。

#### 2. test_eval_1_7b_sft_s42

- **没有通过 `submit_training_job` 提交**（cron entry 的 `log_path: null` 证实）
- 没有 tmux wrapper → 没有 sentinel 文件
- 没有 W&B（eval 实验不用）
- 进程在 02:13 UTC 正常完成
- cron 从 02:14 开始检测到 process dead，连续 5 次 "no signal" → 02:23 auto-resolved as failed

**证据**：`/tmp/agent-ml-exit/test_eval_1_7b_sft_s42.exit` 不存在；cron poll log 显示 5 次 `escalate_no_signal` → `auto_resolve_no_signal`。

---

### 系统性根因（3 个）

| # | 问题 | 影响 |
|---|------|------|
| **S1** | **实验通过 `ssh_execute` 提交时没有 sentinel 文件**。只有 `submit_training_job` 的 tmux wrapper 才有 EXIT trap 写 sentinel。直接 ssh_execute 运行的实验，cron 无法判断完成状态。 | eval 实验（无 W&B）在正常完成后被误判为 failed |
| **S2** | **on_failed hook 重试时不使用 `submit_training_job`**。重试走 ssh_execute → 没有新 sentinel → 旧 sentinel 被复用（或完全无 sentinel）。 | 重试的实验即使成功也仍被标记 failed |
| **S3** | **cron 不验证 sentinel 时间戳的有效性**。`check_status()` 读到 sentinel 后直接信任其 exit code，不检查 sentinel 时间是否在 cron entry 创建时间之后。旧 sentinel 会被当作当前实验的状态。 | 重试实验继承前次 sentinel 的失败状态 |

---

### 建议修复（按优先级）

1. **[高] 确保所有实验提交统一走 `submit_training_job`**——包括 on_failed hook 的重试路径。这从源头解决 S1 和 S2。

2. **[高] `check_status()` 增加 sentinel 时间戳验证**（`cron.py` ~line 754）：
   - 对比 sentinel 的 `finished_at` 与 cron entry 的 `created_at`
   - 如果 sentinel 时间早于 cron 创建时间，忽略该 sentinel，fall through 到 no-signal 路径
   - 这修复 S3，防止旧 sentinel 被复用

3. **[中] 为 eval 实验增加输出文件检测作为补充信号**：
   - 在 "no signal" 路径中，检查 output_dir 是否存在 `test_summary.json`
   - 如果存在且非空，视为成功（→ ANALYZING），而非 auto-fail
   - 这为 eval 实验提供了 W&B 的替代信号

4. **[低] 强制所有 cron entry 必须有 `log_path`**，使 `_extract_failure_reason` 能从日志中提取有用信息。

---
