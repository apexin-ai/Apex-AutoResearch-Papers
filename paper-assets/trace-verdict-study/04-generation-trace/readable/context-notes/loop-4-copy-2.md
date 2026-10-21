# agent / loop_4.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`78955a8edbc801890ed2.json`](../../sessions/78/78955a8edbc801890ed2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-15T09:32:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**只能用 westd-11235:cuda:0 和 cuda:1**，无其他可用 GPU
- 所有训练必须加 `--gradient_checkpointing`：RTX PRO 6000 98GB 对 7B full fine-tune 不够，已两次 OOM（plan_002 首次、plan_003 exception_only 首次）
- `--gpu 0` = cuda:0，`--gpu 1` = cuda:1，不要搞反（之前撞卡过）
- ae_only 数据有 88% fallback 污染（`[fallback: full locals]`），论文中使用该结果必须披露；plan_001（减法）才是验证 ae 贡献的可靠证据
- eval 数字以 bootstrap_compare.json 为准，不要用 checkpoint 目录下残留的旧 eval_results.json
- 投稿目标 **EMNLP 2026 ARR, deadline May 25**（距今 10 天）

### 2. 🖥️ 基础设施快照
- **服务器**：westd-11235，2× RTX PRO 6000 Blackwell 98GB，CUDA 12.8
- **工作目录**：`/root/trace-verdict-study`
- **Python**：`/root/miniconda3/bin/python`，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型**：Qwen2.5-Coder-7B-Instruct（via ModelScope CDN，HF 太慢）
- **数据**：`/root/autodl-tmp/trace-verdict-study-data/{condition}_{train,test}.jsonl`，每条件 train=4720 / test=1190
- **Checkpoints**：`/root/autodl-tmp/trace-verdict-study-checkpoints/{condition}/final/`
- **HF_HOME**：`/root/autodl-tmp/.hf_cache`
- **W&B project**：`trace-verdict-study`
- **活跃进程**：
  - vota_exception_only_seed42_v2: PID 79633, cuda:1, tmux session（RUNNING）
  - vota_loop_only_seed42: PID 82362, cuda:0, tmux session（PREPARING→应已在跑）
- **Cron**：reconcile 返回 0，上述两个实验的 cron 可能需要确认是否正常注册

### 3. 📊 当前状态
**刚完成的关键工作**：
- plan_001（去 actual/expected ablation）：99.4% → D008 确认 ae 冗余，Claim 1 走 full positive framing
- plan_002（label-only loss）：86.2% → D009 确认 gradient dilution 贡献 ~4.5pp，information overload 贡献 ~13pp
- no_trace v5 补跑：75.1%，三条件统一 v5 代码版本

**Registry 状态**：
| exp_id | status | accuracy | 说明 |
|--------|--------|----------|------|
| vota_exception_only_seed42_v2 | RUNNING | — | plan_003 sub-b, cuda:1, gradient_checkpointing 重跑 |
| vota_loop_only_seed42 | PREPARING | — | plan_003 sub-c, cuda:0, 已 submit_training_job |
| vota_ae_only_seed42 | PREPARING | — | plan_003 sub-a, 88% fallback 污染，优先级低 |

**已完成关键实验摘要**：
- no_trace v5: 75.1% | full_trace v5: 81.8% | VOTA v5: 99.2% | VOTA no_ae: 99.4% | full_trace label_only: 86.2%

**等待中**：
- vota_exception_only_seed42_v2 cron 回调（cuda:1）
- vota_loop_only_seed42 cron 回调（cuda:0）
- 无 pending Director 决策

### 4. 📋 待办（条件触发式）
- vota_exception_only_seed42_v2 完成 → 分析 accuracy，与 VOTA 99.2% 对比，更新 registry + report.md，汇报 Director
- vota_loop_only_seed42 完成 → 同上，对比 exception_only 结果，三 sub-condition 完成后综合分析 component 贡献
- plan_003 三个 sub 全部完成 → 综合写 component ablation 结论，更新 paper_framing.md Claim 3，决定是否需要 ae_only clean 版（大概率不需要）
- plan_003 完成后 → 启动 plan_004（DeepSeek-Coder 复现，6h）或 plan_005（第二 verdict task），取决于 Director 优先级
- 任一 GPU 空闲 → 立即铺下一个实验（plan_004/005/006/007/008 按优先级）
- 10 天 deadline 逼近 → 实验与论文写作需并行推进，空闲 Worker 应开始准备 paper structure

### 5. 🎯 战略上下文
**核心结论链**：
- D003: MVP PASS（VOTA 95.6%→v5 99.2%）
- D006: full_trace collapse 是 chat template bug，不是 genuine negative
- D008: actual/expected 冗余，VOTA 效果来自行为模式理解（排除 trivial string matching）
- D009: gradient dilution real but minor（4.5pp），information overload 才是主因（13pp）

**Paper story arc**：verdict task 需要 decision-relevant state snapshots（VOTA），不需要完整执行模拟。三层证据：(1) VOTA 99.2% vs full_trace 81.8%（压缩 > 完整），(2) 去 ae 不降（行为模式 > 值匹配），(3) label-only loss 仅修复 4.5pp（训练目标优化不够，要信息压缩）。

**易错点**：
- plan_003 的 cron 状态要确认——reconcile 返回 0 可能意味着 cron 未注册或已完成，新 session 应 SSH 检查 tmux 进程存活
- vota_ae_only_seed42 还在 PREPARING 但有 88% fallback 污染——不要急着提交，等 exception_only 和 loop_only 结果再决定是否值得跑
- 不要把 exception_only/loop_only/ae_only 结果简单加总期望等于 VOTA 99.2%——component 之间有交互效应
- full_trace_seed42_v2 的 28.4% 是 bug 不是 negative result——论文中不要引用这个数字
- "pass"/"fail" 在 Qwen2.5-Coder tokenizer 中均为单 token (6385/18403)——这是 label-only loss 能工作的前提


---
