# agent / loop_18.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_18.md`
- **Structured JSON:** [`9dfeeaa00f7d91c11ed5.json`](../../sessions/9d/9dfeeaa00f7d91c11ed5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: idle_timeout
updated: '2026-05-21T03:25:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-16980 cuda:0,1 + westd-21461 cuda:0,1（共 4 张 RTX PRO 6000 96GB）。白名单外的 GPU 必须 push back Director
- Table 2 eval 统一用 `eval_d064.py`（决策 D068），禁止混用其他 eval 脚本，否则指标不可比
- DocRED 所有 Llama 结果必须用 westd-16980 的 w5 checkpoint（决策 D069），21461 上的 Llama greedy 仅作内部参考
- 提交截止 **May 25 EMNLP 2026 ARR**，距今 4 天

### 2. 🖥️ 基础设施快照
- **westd-16980**：工作目录 `/root/autodl-tmp/OntoCoDec/`，Python `/root/miniconda3/bin/python`，conda base
  - 模型：`/root/autodl-tmp/checkpoints/llama_lora_docred_merged`、`qwen_lora_docred_merged`、`qwen3_8b_lora_scierc_merged`
  - 输出：`/root/autodl-tmp/schema_outputs/`（d065/d066/d067 子目录）
  - 磁盘：`/usr/bin/nvidia-smi` 50% 已用（424G 可用）
- **westd-21461**：同结构，磁盘 3% 已用（817G 可用）
  - 模型路径同上
- 无 W&B 集成（inference-only 实验），cron 靠进程存活 + sentinel 文件检测

### 3. 📊 当前状态
**刚做完**：d066_sweep_16980_gpu1（Llama beam2 unc DocRED 200-doc）被 cron 误判 failed——日志确认 200/200 完成。已更正 registry conclusion=success，派了 Worker `worker_eval_d066_sweep_16980_gpu1_20260520T112330` 跑 eval 取 metrics，**尚未回调**。

**RUNNING 实验**（3 个，reconcile 确认全部存活）：
| exp_id | 服务器 | 内容 | PID |
|--------|--------|------|-----|
| d065_qwen_greedy_4096_r2 | westd-21461 GPU0 | Qwen DocRED 998-doc greedy con 4096（关键路径 appendix 数据） | 194615 |
| d066_sweep_21461_gpu1 | westd-21461 GPU1 | Qwen beam8 constrained DocRED 200-doc | 196653 |
| d066_sweep_llama_beam2_s1 | westd-16980 GPU1 | Llama beam2 constrained DocRED 200-doc（从 unc 接力） | 750801 |

**ANALYZING**：d066_beam_sweep（父实验，SciERC 8 配置全完，DocRED 子任务还在跑）

**等待中**：eval Worker 回调（d066_sweep_16980_gpu1 metrics）

### 4. 📋 待办
- eval Worker 回调到 → 将 metrics 写入 d066_beam_sweep 父实验的 DocRED 段，检查是否与 SciERC Pareto pattern 一致
- d066_sweep_llama_beam2_s1 cron 完成 → eval → 与 unc 对比 DR/CF 消除效果
- d066_sweep_21461_gpu1 cron 完成 → eval → Qwen beam8 con 入 DocRED Pareto 数据
- d065_qwen_greedy_4096_r2 cron 完成 → eval → 替换 appendix 2 行数据，**这是关键路径**
- 所有 DocRED beam sweep + d065 全部到齐 → 生成 Pareto 曲线图 → 入稿 appendix → 触发 R12 fresh 内审
- 第二个 cron 重复回调（同一 exp_id d066_sweep_16980_gpu1）已在本 session 处理过，**忽略即可**

### 5. 🎯 战略上下文
- **核心结论**：OntoCoDec 两层约束解码在 SciERC 和 DocRED 上均实现 DR→0%，LoRA+constrained 强协同（即使 k=1 也能消除 DR），beam k=2 是 Pareto optimal
- **d066 SciERC 结果已齐**（registry metrics 完整），DocRED 侧还差 3 个子任务完成 + eval
- **易错点 1**：这些 inference 实验没有 W&B，cron 会误判完成的进程为 failed——看到 "process dead with no W&B" 先查日志确认是否正常完成
- **易错点 2**：d066_beam_sweep 父实验状态是 ANALYZING 但实际 DocRED 子任务仍在跑，不要提前关闭
- **论文状态**：8 页编译通过，0 undefined refs。剩余：Pareto 图 + d067 determinism 段落 + d065 appendix 数据替换 + R12 内审 + 定稿
- **决策链关键节点**：D068（统一 eval 为 eval_d064.py）、D069（Llama 用 w5 checkpoint）、D070（Table 2 全面 re-eval）、D063（constraint-guided beam no-go）


---
