# reviewer / loop_10.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`d4176bf7678b3bf06e2e.json`](../../sessions/d4/d4176bf7678b3bf06e2e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-19T11:20:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-34887 cuda:0,1 + westd-41718 cuda:0,1（RTX PRO 6000 Blackwell 98GB）。越界立即 critical
- westd-41718 GPU 是 98GB Blackwell，**不是 A6000 48GB**（Director 之前误判过，已纠正）
- 论文 eval 有两套 protocol：per-token（evaluate.py）vs TEAL allocation（benchmark_eval.py）。Dense PPL 两者一致，sparse PPL 差异巨大。Table 2/3/4 应全部用 TEAL（benchmark_eval.py）。混用是 critical
- C1 retrain PPL 异常已修复（registry 从 per-token 7.54/7.38 更正为 TEAL 8.84/8.82），但如果看到旧值要警惕
- bce_comp_staged_s42 的 TEAL PPL=44.54（comp 网络不兼容 TEAL 路径），per-token PPL=25.44。Table 4 已删除该行

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887(root) + westd-41718(root)
- 工作目录：/root/distill_sparse_swiglu/
- Python：/root/miniconda3/bin/python
- 模型：LLaMA-3.1-8B → /root/autodl-tmp/models/llama-3.1-8b/；Mistral-7B-v0.3 → /root/autodl-tmp/models/Mistral-7B-v0.3/；Qwen2.5-14B → /root/autodl-tmp/models/qwen2.5-14b/
- HF cache：/root/autodl-tmp/.hf_cache
- WANDB：disabled（WANDB_MODE=disabled）
- 活跃进程（截至 handoff）：qwen14b_kl30_s123_eval (RUNNING, westd-34887) + qwen14b_kl30_s456_eval (RUNNING, westd-34887)

### 3. 📊 当前状态
**刚完成**：
- R12 action matrix 全面审查，已发送 Director。关键发现：Table 2 "BCE+comp" 标签欺骗（实为纯 BCE 2700 steps 无 compensation），C1 50% max Δ 错误（0.59→0.79），WINA baseline 无数据。全部已由 worker 修复并验证
- BCE data source verify worker 审查通过，所有修复确认正确
- Qwen-14B KL 30% s123/s456 训练完成审查通过（sparsity=0.277, lambda=5000, 与 s42 一致）

**RUNNING**：
- qwen14b_kl30_s123_eval — 7 tasks downstream eval（TEAL uniform 30%），关键看 MMLU reversal
- qwen14b_kl30_s456_eval — 同上

**等待中**：
- 上述两个 eval 的 cron:on_complete 回调

### 4. 📋 待办
- qwen14b_kl30_s123_eval 完成 → 核实 MMLU 是否复现 reversal（s42: KL MMLU=63.72 < TEAL=71.83）。如果 3-seed 均 reversal → W2 response 有坚实支撑；如果不一致 → severity warning 建议重新审视 14B 结论
- qwen14b_kl30_s456_eval 完成 → 同上
- 两个 eval 都完成后 → 检查 Agent 是否更新了 appendix 14B 表格数据，核对数字一致性
- 如果 Director 转发 paper 章节审查请求 → 按 §5 对抗审查模式执行，先做合规检查（red-section skill）
- Table 4 "unified benchmark protocol" 次要关注：验证 BCE+Gumbel 系列（32.22, 38.02）的 eval 是 TEAL global 还是 per-token。尚未验证

### 5. 🎯 战略上下文
- **核心 story**：KL divergence loss 通过 coupled gradients 发现比 magnitude-based 更优的 mask targets（68% 不同），C1 ablation 证明 mask quality 是 proximate driver
- **三个 sparsity regime**：budget-surplus (≤30%, KL 全面优势)，budget-constrained (35-45%)，capacity-cliff (≥50%, downstream 全崩)
- **14B MMLU reversal 是最大叙事风险**：s42 单种子显示 KL MMLU < TEAL，与 8B 相反。论文目前 framing 为 "architecture-dependent limitation"。如果 s123/s456 不复现 reversal，这个叙事就站不住
- **易错点**：
  - checkpoint 版本混淆：kl_30pct_s*（paper main table）vs kl_sparsity30_s*（旧版本，MMLU 低 3pp）
  - Table 2 "BCE (2700 steps)" 刚改名，别再叫它 "BCE+comp"
  - Mistral 是 v0.3（rope_theta=1M, vocab=32768），不是 v0.1
  - paper_provenance.yaml 严重过时，如果 Director 问起要提醒重建


---
