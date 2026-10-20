# ops exp004 tmpdir audit gpu4 verify

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp004_tmpdir_audit_gpu4_verify_20260515T180307_result.json`
- **Structured JSON:** [`cfb82e75b6b6d027131c.json`](../../sessions/cf/cfb82e75b6b6d027131c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是结果：

---

## 任务 1: exp_004 v6 tmpdir

### 状态：v6 已完成，但大量 seed 失败

v6 已跑完（0.5h），12 条件中 8 条产出结果（部分 seed 失败），4 条缺失。

### 根因：不是系统清理脚本，是 Python multiprocessing 竞态

- `systemd-tmpfiles-clean` 只清理 `/tmp`（10d）和 `/var/tmp`（30d），**不影响 `/home/ubuntu/tmp_cmdstan/`**
- 无 crontab 清理脚本（只有一个 PID 411032 watchdog）
- **真正根因**：`--parallel 2` 同时跑两个条件，Python multiprocessing 在 TMPDIR 下创建共享的 `pymp-*` 目录。一个 worker pool 结束时，finalizer 调用 `rmtree(pymp-dclv6cfs)` 清理临时目录，导致其他仍在运行的 CmdStan 进程找不到文件
- 日志证据：`FileNotFoundError: [Errno 2] No such file or directory: '/home/ubuntu/tmp_cmdstan/pymp-dclv6cfs'`
- 失败 seed 全部显示 `FAIL [Errno 2] No such file or directory` 且耗时仅 0.1s（正常应数百秒）

### v5 失败也是同一根因

v5 和 v6 用同一 TMPDIR + 同一并行配置，问题一致。

### 修复方案

不需要换 TMPDIR 路径，需要**隔离每个并行 worker 的临时目录**：

```python
# 在 run_sweep.py 的 worker 函数开头：
import tempfile, os
worker_tmpdir = tempfile.mkdtemp(prefix=f"stan_cond{condition_id}_", dir="/home/ubuntu/tmp_cmdstan")
os.environ["TMPDIR"] = worker_tmpdir
```

或者更简单——降低并行度 `--parallel 1` 消除竞态（但速度减半）。

### 已有结果可用

8 条件有数据，coverage 80%-100%，bias 低。如果 4 条缺失的可以用 `--resume --parallel 1` 补跑。

---

## 任务 2: GPU 4 VRAM

### PID 590509 (zombie)：已确认死亡

### GPU 4 当前状态：有两个进程，几乎满载

| PID | VRAM | 运行时间 | 进程 |
|-----|------|----------|------|
| 597179 | 13868 MiB | 1h12m | d000_v3 SFT（预期）|
| **605267** | **8204 MiB** | **4m12s** | **compute_signals.py 3B_d005_s42（未预期）**|
| 合计 | 22072 / 24564 MiB | | **仅剩 ~2.5GB 余量** |

### C001/C002 违规

PID 605267 是 `compute_signals.py --model-path Qwen2.5-3B --adapter-path 3B_d005_s42`，在 d000_v3 SFT 仍运行时被提交到 GPU 4。这违反了 C001（GPU 查重）和 C002（确认空闲）。

当前两个进程恰好能塞下（22GB/24.5GB），但余量极小，任一进程 batch 峰值即可触发 OOM。

### 建议

1. **GPU 4**：如果 d000_v3 SFT 快完成（已跑 1h12m，预估 8-12h 总时长），605267 大概率会先 OOM 或两者共存到 SFT 结束。需要决定是 kill 605267 等 SFT 完再跑 signals，还是承受 OOM 风险。
2. **v6 重跑**：用 `--parallel 1 --resume` 补齐失败的 seed，或修 run_sweep.py 隔离 worker TMPDIR 后用 `--parallel 2 --resume`。

---
