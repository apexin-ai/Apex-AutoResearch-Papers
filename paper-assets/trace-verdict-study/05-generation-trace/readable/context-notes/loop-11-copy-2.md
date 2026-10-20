# reviewer / loop_11.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`22b88faba10e1c436d1e.json`](../../sessions/22/22b88faba10e1c436d1e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-21T04:59:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**cuda:0, cuda:1**（westd-11235）。任何进程跑在其他设备上立即 critical。
- 磁盘：根分区仅 30G（AutoDL），模型/数据/HF cache 必须放 `/root/autodl-tmp/`。当前根分区 69% 占用（~9.5G 可用），大 checkpoint 仍可能撑满。
- GPU 0 有 49175 MiB 孤儿显存（无进程但未释放），实际可用显存 ~48GB。需容器重启才能清除。
- codellama13b_label_only_seed123_v2 输出已删除，不重跑（D108 决策）。

### 2. 🖥️ 基础设施快照
- 服务器：**westd-11235 (root)**，工作目录 `/root/trace-verdict-study`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型路径：`/root/autodl-tmp/models/` 下有 Qwen2.5-Coder-7B-Instruct、Qwen2.5-Coder-1.5B-Instruct、CodeLlama-13b-Instruct-hf、deepseek-coder-6.7b-instruct
- HF cache：`/root/autodl-tmp/.hf_cache`
- wandb project：`trace-verdict-study`
- 活跃进程：**无**。两张 GPU 均空闲。无 RUNNING 实验、无 cron、无 tmux session 活跃。

### 3. 📊 当前状态
**论文已通过 pre-submission review（0 critical, 0 warning），等待用户 scp PDF + 视觉检查 + resubmit。DDL May 25（4 天）。**

我刚完成的工作：
- codellama13b_label_only_seed123_v2 磁盘满失败审查 → 已报 Director（部分 collapse 证据充分，不重跑）
- ROADMAP 更新审查 → PASS
- 磁盘清理 worker 审查 → 磁盘恢复至 69%，GPU 0 孤儿显存未解决已报
- 输出目录删除确认 → 已清理

Registry：141 DONE, 6 QUEUED, 3 PREPARING, 1 ALLOCATED。所有 QUEUED/PREPARING 为低优先级 rebuttal reserve，ROADMAP 决策不再排期。

### 4. 📋 待办
- Director 转发 resubmit 后的审稿意见 → 按模式 B 审查（加载 paper-quality-lessons + paper-visual-review skill）
- Director 要求跑 rebuttal 应急实验 → 先确认磁盘空间 + GPU 0 孤儿显存是否已清除
- Director 转发 Framing 调整提案 → 加载 negative-framing-review skill，四维度审查
- 收到任何新实验完成通知 → 标准审查流程（数据一致性 + GPU 合规 + 结论可靠性）

### 5. 🎯 战略上下文
**核心结论**：Information density determines learning efficiency。Exception trace 是 minimal sufficient signal（≥99.33% 跨 4 模型），loop trace 是 model-dependent Tier 2（77-86%），full_trace 因 information overload 反而降至 ~80%。

**Claims 强度**：C1 Exception dominance ★★★★★ | C2 Density decomposition ★★★★ | C3 Tier hierarchy ★★★★★ | C4 VOTA universality ★★★★

**易错点**：
- `read_registry` 的 `filters` 参数经常返回空，用本地 Grep 搜 registry.yaml 更可靠
- `ssh_read_only` 不支持 pipe `|` 和 `2>/dev/null`，需拆成多条命令
- paper_framing.md 中部分数字（如 Qwen-1.5B no_trace 67.31%）是旧版，实际 3-seed mean=72.35±4.48%，以 tex 文件为准
- Qwen-1.5B no_trace seed42=67.31% Grubbs 检验 G=1.12 < critical 1.155，不构成统计 outlier，但 σ=4.48pp 远高于其他条件（≤1.65pp），论文已诚实披露
- C2 只有 Qwen 家族（2 scale）有量化分解，CL+DS 只有 collapse 定性证据，不能 claim "cross-architecture decomposition"


---
