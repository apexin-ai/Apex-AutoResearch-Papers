# debug exp 002 signals 3B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_exp_002_signals_3B_20260515T154911_result.json`
- **Structured JSON:** [`c12ff4db637a6eadf892.json`](../../sessions/c1/c12ff4db637a6eadf892.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 GPU 都在使用中。现在有足够的信息写诊断报告了。

---

## 诊断报告：exp_002_signals_3B

### 失败原因

**代码被中途更新，导致参数接口不兼容。**

证据链：

1. **日志记录的 signals 格式与当前代码不一致**：日志显示 `signals: ['embedding', 'minkpp', 'selfcritique']`（3 个具名信号），但当前 `run_batch.py:102` 传的是 `"--signal", "all"`，`task["signals"]` 也是 `"all"`。说明运行时的代码是旧版本。

2. **两个文件都在实验结束后被修改**：
   - `run_batch.py` — 修改于 23:31（实验 23:23 结束）
   - `compute_signals.py` — 修改于 23:50

3. **Task 1 运行了 37 分钟（22:46→23:23），到 self-critique 83% 时被 SIGTERM 杀死（rc=-15）**。这意味着旧版 compute_signals.py 接受了旧格式参数并正常执行。

4. **Tasks 2-12 全部瞬间失败（rc=2）**，报错 `compute_signals.py: error: the following arguments are required: --signal`。原因：旧版 `run_batch.py`（已在内存中）构建的命令使用旧参数格式（可能是 `--signals` 复数形式），但磁盘上的 `compute_signals.py` 已被更新为要求 `--signal` 单数形式。subprocess.run 每次启动子进程都从磁盘读取新文件，所以 task 2+ 读到了新版 compute_signals.py，但收到的却是旧格式参数。

5. **exp002/ 目录未被 git 跟踪**，无法查看旧版本差异。

### Task 1 部分产出

`/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_s42/` 下有：
- `signal_embedding_mmlu.json` — S1 完成
- `signal_minkpp_mmlu.json` — S2 完成
- selfcritique（S4）在 83%（365/439）时被杀，未保存
- 无 `signals_merged_mmlu.json`

### 修复状态

当前代码已修复（run_batch.py 和 compute_signals.py 参数一致，都用 `--signal all`）。此外新版还增加了 S3（ConStat），旧版只跑 3 个信号（S1/S2/S4）。

### 是否可以立即重试

**不能**。6 块 GPU 全部被占用（GPU 0-1 ~5.8GB, GPU 2-5 ~9GB）。3B 模型推理约需 6-8GB + signal 计算开销，需要等一块 GPU 空闲。

重试时注意：
1. d000_s42 的部分产出（embedding/minkpp 两个文件）无 merged 文件，`--skip-completed` 不会跳过，会重算（这是正确行为）
2. 新版代码会跑 4 个信号（含 S3 ConStat），与 0.5B/1.5B 的 3 信号结果不一致——确认这是否是预期变更
3. 按约束 C001/C002，提交前必须 `nvidia-smi` 确认目标 GPU 空闲且无同类进程

---
