# reviewer / loop_8.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`bcd7ea31e7ac8768849d.json`](../../sessions/bc/bcd7ea31e7ac8768849d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-17T17:10:15+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 (C004): westd-34887 cuda:0/cuda:1 + westd-41718 cuda:0/cuda:1。其他 GPU 一律 CRITICAL。
- 论文 allocation 叙事已锁定 (D050): **只能说 variance reduction (7.5×)**，禁止说 mean improvement / "+15.3pp" / "uniform recovers accuracy"。3-seed 数据证明 mean 差异不显著。
- qwen14b_bce30_s42 的 `constraint_satisfied` 必须为 false（训练只达到 6.4% sparsity）。TEAL forced 30% 是 inference 行为，不等于训练约束满足。
- 公平比较 14B KL vs BCE 必须用 TEAL 30% PPL（KL 7.62 vs BCE 8.76），不能用 hard_mask PPL（sparsity 不等）。

### 2. 🖥️ 基础设施快照
- **westd-34887** (root): `/root/distill_sparse_swiglu/`，Python `/root/miniconda3/bin/python`
  - 模型: `/root/autodl-tmp/models/llama-3.1-8b/`, `/root/autodl-tmp/models/qwen2.5-14b/`
  - HF cache: `/root/autodl-tmp/.hf_cache/datasets`，HF_HUB_OFFLINE=1
  - 活跃: PID 52229 (tmux pane %2, cuda:1) = qwen14b_kl30_s42_eval; PID 59127 (tmux pane %5, cuda:0) = qwen14b_bce30_s42_eval
- **westd-41718** (root): `/root/distill_sparse_swiglu/`，同 Python/cache 配置
  - 活跃: PID 6896 (cuda:1) = qwen14b_teal30_eval
- WANDB_MODE=disabled（全项目）
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/`

### 3. 📊 当前状态
**刚完成的审查**:
- D050 paper rewrite 验证通过（3-seed variance framing 正确）
- qwen14b_bce30_s42 + v2: BCE Lagrangian 约束在 14B 完全失效（lambda 5000/50000 均只达 6.4%），已报 Director
- downstream_dense_baseline 完成: hellaswag 82.3%, piqa 80.7%, boolq 82.9%
- downstream_ext_kl30_s42 完成: hellaswag 72.7%, piqa 76.0%, boolq 76.9%（30% global degradation 合理）

**RUNNING 实验**:
- `qwen14b_kl30_s42_eval` (westd-34887 cuda:1): 14B KL downstream，GSM8K generate 阶段 ~15%，预计还需 2-3h
- `qwen14b_bce30_s42_eval` (westd-34887 cuda:0): 14B BCE downstream（via TEAL 30%），刚启动
- `qwen14b_teal30_eval` (westd-41718 cuda:1): 14B TEAL vanilla baseline，loglikelihood ~13%，预计 3-4h

### 4. 📋 待办（条件触发式）
- qwen14b_kl30_s42_eval 完成 → 读 results.json，验证 MMLU/ARC/WG/GSM8K；对比 training PPL ratio 1.31× 是否在 downstream 得到验证
- qwen14b_teal30_eval 完成 → 三方对比: KL vs BCE vs TEAL at 14B 30%。验证论文 "KL >> TEAL" claim 在 14B 是否成立
- qwen14b_bce30_s42_eval 完成 → 确认 BCE TEAL PPL 8.76 对应的 downstream 数字，验证 "KL > BCE at 14B"
- 三个 14B eval 全部完成 → 审查 Agent 是否在论文中添加 14B section，验证 claims 与数据一致
- paper git 有新 commit 涉及 14B → 审查是否正确标注 "preliminary (single seed)" 或有无 overclaim

### 5. 🎯 战略上下文
- **核心决策链**: D050 = allocation 叙事从 mean improvement 转为 variance reduction only。这是 3-seed 数据驱动的硬结论，不可回退。
- **14B scaling story**: KL training PPL 1.31× (vs TEAL 1.47×) 表明方法 generalize。但 downstream 未验证（正在跑）。论文当前 limitations 说 "scaling untested"——如果 14B 下 KL downstream 不如 TEAL，需要非常谨慎处理 claim。
- **易错点**: 
  1. BCE 的 `ppl_ratio_hard_mask=1.075` 是 6.4% sparsity 下的（近 dense），绝对不能用于与 KL 的 `ppl_ratio=1.31`（28% sparsity）对比
  2. Worker completion ≠ experiment completion。Worker 通知只说 Claude session 结束，tmux 里的 eval 可能还在跑
  3. 30% global MMLU 单 seed 数据不可信（s42=25.27%, s456=43.82%），必须引用 3-seed mean±std


---
