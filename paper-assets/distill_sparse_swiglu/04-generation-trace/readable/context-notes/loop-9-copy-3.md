# reviewer / loop_9.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`656e2f26184ba245ee52.json`](../../sessions/65/656e2f26184ba245ee52.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-17T21:48:58+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 C004: westd-34887 cuda:0/1 + westd-41718 cuda:0/1，越界即 critical
- 论文数字必须有 registry exp_id 溯源（C003）
- 训练必须用 nohup/tmux（C002）
- "TEAL vanilla" vs "predictor-TEAL" 是两个不同函数（evaluate.py L57 vs L195），不可混用。我已因此发过 critical，Agent 已修复（删除了错误的 8.76，加了 TODO）
- D050 约束：allocation 叙事只能用 "variance reduction (7.5×)"，不能 claim uniform 绝对更好

### 2. 🖥️ 基础设施快照
- 服务器: westd-34887(root) + westd-41718(root)
- 代码根: /root/distill_sparse_swiglu/
- Python: /root/miniconda3/bin/python
- 模型: /root/autodl-tmp/models/llama-3.1-8b, /root/autodl-tmp/models/qwen2.5-14b, /root/autodl-tmp/models/mistral-7b-v0.3
- HF cache: /root/autodl-tmp/.hf_cache/datasets
- W&B: disabled (WANDB_MODE=disabled)
- 论文目录(本地): /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/
- Registry: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/registry.yaml (~5800 lines, 139 experiments)

### 3. 📊 当前状态
**刚完成**:
- 全文数字核实：所有 Table 2/3/4/5/6 及 abstract/intro/conclusion 数字与 registry 精确匹配（已发 info 报告）
- 发现并报告 14B "TEAL vanilla PPL 8.76" 标注错误（critical），Agent 已修复
- AI 风格审计通过（去 -ing 短语，数值无变化）
- qwen14b_kl30_s42_eval DONE: PPL=7.6232, MMLU=63.72%, GSM8K=48.82%（极强结果）
- bce_isocompute_v3_s456 训练+eval 完成: PPL=28.35, MMLU=25.67%
- bce_isocompute_v3_s123 训练完成，eval 刚启动

**RUNNING**:
- qwen14b_bce30_s42_eval (westd-34887 cuda:0) — GSM8K ~29%时检查，预计还需2-3h
- qwen14b_teal30_eval (westd-41718 cuda:1) — GSM8K ~39%时检查，预计还需2-3h
- qwen14b_dense_baseline (westd-41718 cuda:0) — MMLU loglikelihood ~6%时检查，预计还需4-5h
- bce_isocompute_v3_s123_eval (westd-34887 cuda:1) — 刚启动，~45min

**PREPARING (stale)**:
- c4_ood_kl30_s42: PID 17632 dead, HF httpx error，registry 未更新为 FAILED
- c4_download: 同上，依赖下载失败

### 4. 📋 待办
- qwen14b_teal30_eval 完成 → 这是真正的 vanilla TEAL 14B PPL，论文 TODO 需要填入此数字，重算 advantage ratio
- qwen14b_bce30_s42_eval 完成 → 与 KL (PPL 7.62) 和 vanilla TEAL 三方对比
- qwen14b_dense_baseline 完成 → 获取 14B dense downstream (MMLU/ARC/WG/GSM8K)，计算 KL 14B 的 degradation ratio
- bce_isocompute_v3_s123_eval 完成 → 与 s42 (PPL 27.97) 和 s456 (PPL 28.35) 合并，计算 BCE 3-seed mean±std
- 三个 14B eval 全部完成 → 综合审查 14B scaling story，验证 paper 新增段落是否需要补充 downstream 数字
- 论文 limitations.tex L5 "scaling to 13B or 70B remains untested" → 14B 完成后需更新

### 5. 🎯 战略上下文
- 核心论文 story: KL distillation > BCE for contextual sparsity prediction，因为 KL gradient 通过 Jacobian 耦合所有神经元，而 BCE gradient 是 per-neuron independent
- 14B 实验是回应 reviewer R3-S4 "跨规模验证" concern (D048)
- KL 14B 结果极强: PPL ratio 1.47× 与 8B 完全一致，MMLU 63.72%（dense 约 65-66%），BCE 在 14B 完全崩溃（6.4% native sparsity）
- **易错点**: evaluate.py 中 `teal_global_masks` 用 predictor scores，`vanilla_teal_global_masks` 用 magnitude scores。training script 的 "teal_global_ppl" 字段是 predictor-based 不是 vanilla。不要把 BCE experiment 的 teal_global_ppl 当成 vanilla TEAL
- **PPL std 精度**: 论文报告 "11.92±0.07"，实际 std=0.076 (严格四舍五入应为 0.08)，极小问题已记录
- BCE 3-seed 正在收集中：s42=27.97, s456=28.35, s123 eval running


---
