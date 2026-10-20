# director / loop_3.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`b6ecfc06ef35a11d3909.json`](../../sessions/b6/b6ecfc06ef35a11d3909.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-14T05:31:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-22162 的 cuda:0-3（4× RTX 6000 Pro 96G）
- **Qwen 速度正常（~50s/problem）**——之前 37-75min/problem 的诊断是误诊（D018），不要再启动任何"Qwen speed fix"工作
- 服务器代码已被 bf16-nan-fix Worker 改为 bf16，当前服务器上的 run_profiling.py 用的是 bfloat16
- 不要杀正在运行的实验来给新实验腾位——本 session 已发生两次误杀（Qwen 被杀给 v6_random、v6_random_s030 被杀给 bf16 verify）

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162 (connect.westd.seetacloud.com)，用户 root
- 工作目录：/root/autodl-tmp/pacs
- Python：需探测（可能 venv 或 conda，上任未记录具体路径）
- 模型：DeepSeek-R1-Distill-Qwen-7B（默认），Qwen2.5-7B-Instruct 在 /root/autodl-tmp/models/Qwen2.5-7B-Instruct
- 活跃进程（3h 前状态，需重新确认）：
  - v6_random_s015 cuda:0 PID 72073
  - v6_random_s020 cuda:1 PID 71488
  - v6_random_s025 cuda:3 PID 73459
  - v6_random_s030 cuda:2 可能在跑（PID 未确认，4/50 进度）
- GPU 预算：~250h，已用 ~11h

### 3. 📊 当前状态
- **v6_random 4 组**（fp16）：s015/s020/s025 在跑（约 40-50min 总时长），s030 可能在跑或被杀需确认
- **NaN overlap check**（P0 阻塞项）：Worker diag:nan-overlap-check 已派出，检查 v6_importance 4 条件的 NaN 位置是否完全重合。结果决定是否需要 bf16 全量重跑 v6_importance。**3h 前派的，应该已经完成，优先读取结果**
- **bf16 代码修复**：已完成并验证通过（bf16 + NaN 过滤），服务器代码已更新
- **论文写作**：3 个 Worker 已派（Method / Experimental Setup / Related Work），可能已有产出
- **Qwen 4 组**：全部 QUEUED/PENDING（s015/s020/s025/s030），等 v6_random 完成 + NaN 决策后提交
- 等待：NaN overlap 结果 → Director 决策 bf16 vs filter → 排满 GPU

### 4. 📋 待办
- NaN overlap 结果已出 → 立即汇报 Director，等决策（overlap 一致 = fp16+filter 够用，不一致 = bf16 全量重跑）
- v6_random 4 组完成 → GPU 释放 → 立即提交 Qwen importance 4 组（bf16，~1h 完成）
- Qwen importance 完成 → 提交 Qwen random 4 组（对照实验）
- 写作 Worker 完成 → 收集产出，Results 骨架可写但数字留空
- 所有实验完成 → problem-level permutation test（importance vs random）

### 5. 🎯 战略上下文
- **核心发现**：importance-based eviction 的 compound interaction gradient 在 low-sparsity phase 达 12-75×，random ~1×（phase-modulated severity）
- **统计确认**：bootstrap CI (B=10000) 全部 p=0.0000，但 n_paired 仅 16-22/50（因 fp16 Layer 27 NaN）
- **决策链**：D010(MVP FAIL→pivot) → D014(新发现 phase-modulated) → D015(GO) → D017(bootstrap 确认) → D018(Qwen 速度误诊纠正)
- **目标**：EMNLP 2026 ARR，截稿 2026-05-25（距今 11 天）
- **最易判断错的事**：NaN overlap 结果出来后的决策——如果 overlap 一致，不需要重跑 v6_importance（fp16+filter 即可），省大量时间；如果不一致才需要 bf16 重跑全部。不要默认"bf16 已改就全部重跑"
- **易踩的坑**：服务器代码已是 bf16，如果决策是 fp16+filter 方案，跑新实验前需确认 torch_dtype 设置是否需要改回


---
