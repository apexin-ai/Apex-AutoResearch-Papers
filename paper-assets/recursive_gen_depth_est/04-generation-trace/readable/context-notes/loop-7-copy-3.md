# reviewer / loop_7.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`0ccf6b2e872fe86adeb5.json`](../../sessions/0c/0ccf6b2e872fe86adeb5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-15T19:24:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：gpu-6000pro-2 上只能用 cuda:0 / cuda:1（`execution.gpu_ids`）。feature_ablation_9cell.py 是 CPU-only（RF），不涉及 GPU，但任何新训练实验必须检查
- 编译源是 `docs/paper/`（有 main.tex），**不是** `artifacts/_project/paper/`（旧版残留，仍含 D028 overclaim）。审查论文内容必须读 `docs/paper/` 目录
- feat_ablation_v1 的 registry spec 说 `n_estimators=100` + `python scripts/feature_ablation.py`，实际代码是 `n_estimators=200` + `python3 src/feature_ablation_9cell.py`——spec 不可信，以代码为准

### 2. 🖥️ 基础设施快照
- 服务器：gpu-6000pro-2，代码根目录 `/root/autodl-tmp/recursive_gen_depth_est`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/`
- 活跃进程：PID 473989（`python3 src/feature_ablation_9cell.py`，CPU-only，etime ≈2h，n_jobs=-1 占 ~16 核）
- 结果目录：`/root/autodl-tmp/recursive_gen_depth_est/results/feature_ablation/`（OLD 文件 topk_ablation.json 01:25 + v2 文件 top_k_ablation.json 03:07）
- SHAP 结果：`/root/autodl-tmp/recursive_gen_depth_est/results/shap_analysis/`（9/9 cells 完整）
- 无 wandb 配置（CPU 实验，不检查 wandb）

### 3. 📊 当前状态
**刚完成**：
- SHAP 文件验证 worker 审查（PASS）
- 论文目录澄清：确认 `docs/paper/` 是编译源且已含 D028 修正，撤回了对 `artifacts/_project/paper/` 的旧 WARNING
- Feature ablation v2 中间审查（5/9 cells），发现 forward selection vs permutation importance 方法分歧（WARNING 已提交）

**RUNNING**：feat_ablation_v1（PID 473989）。v2 输出文件停在 5/9 cells（pythia×3 + olmo_nucleus + olmo_temp09），缺 gpt2xl×3 + olmo_topk50。有命名不一致问题：脚本 CELLS dict 用 `_nucleus095` 但 v2 输出文件用 `_nucleus`（无 095），且脚本 output filenames 是 `topk_ablation.json` 而 v2 实际文件名是 `top_k_ablation.json`——**可能存在第二个已退出的进程生成了 v2 文件，PID 473989 可能是生成 OLD 文件的进程仍在运行 forward selection**

**等待**：无活跃 worker 回调。Director 已收到我的所有报告。

### 4. 📋 待办
- feat_ablation_v1 v2 文件更新（forward_selection.json 新增 cells）→ 检查 gpt2xl cells 是否出现；若出现则做全 9-cell 交叉验证并发最终审查报告
- PID 473989 退出 → 检查是否生成 summary.json；确认 OLD vs v2 文件哪套是最终版
- 新 worker_done 通知 → 按 audit-checklist 审查
- abstract.tex L5 的 "40%" 零射基线数字（应为 500-sample 36.2%）→ 等 Paper Agent 修正后验证
- Table 2 / Table 6 等 XX.X% placeholder 被填充 → 验证数字与 registry 一致

### 5. 🎯 战略上下文
- **项目阶段**：Phase 2 论文写作，DDL 2026-05-25 ARR May cycle（~10 天）
- **D028 是关键决策**：z-score 从"不可挽救的结构性偏移"修正为"scale + structural 双组份"。`docs/paper/` 已修正，但 `artifacts/_project/paper/` 未修正——下一个"你"不要被旧目录误导
- **Feature importance 叙事精度**：var_surprisal 和 p90_ppl 交替领先，排名因模型和方法而异。abstract 用 "9/9 and 8/9" 是准确的（SHAP 下 gpt2xl_topk50 var_surprisal 是 #3 不是 #2）。不要笼统说"var_surprisal 是最重要特征"
- **易踩坑**：(1) `artifacts/_project/paper/` ≠ 编译源，读错目录会误判论文内容；(2) OLD vs v2 feature ablation 文件命名不同（topk vs top_k，有/无 095），不要混淆引用；(3) ssh_read_only 不支持管道符 `|`，需拆分 grep 命令


---
