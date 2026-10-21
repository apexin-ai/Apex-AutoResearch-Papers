# agent / loop_1.md

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`2ace1e8206125c6f3134.json`](../../sessions/2a/2ace1e8206125c6f3134.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: idle_timeout
updated: '2026-05-21T19:35:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: westd-32570:0-3, westd-19912:0-3。不得使用任何其他 GPU
- **exp-002 扩展实验 registry 条目全是 PREPARING 状态**（21 条），还没有 GPU 分配/提交。这些是 D009 8-model expansion 的占位条目，不要 submit_on_allocated——它们没有被 allocate
- **Gemma2 不支持 float16**（vLLM 架构层面限制），所有 Gemma 推理只能 bf16/fp32
- **G_item 计算已知 bug**: `gstudy_full.py` 和 `exp001b_gstudy.py` 用了 ICC（错），正确实现在 `compute_g_coefficients.py`（Henderson I G coefficient）。方差百分比正确，只有 G_item 数值受影响。已修正并记录
- **D-study 公式方向性**: `G_ni = σ²τ / (σ²τ + σ²δ × (n_actual / ni))`，G 必须随 n_items 单调递增。所有 D-study 代码必须带 monotonicity assertion
- **Claim 1 narrative 已 pivot (D010)**: 从 "cross-benchmark gradient" → "format-conditional dichotomy"（MC vs free-form）。不要用旧的 gradient 叙事
- **submit_training_job 不支持 shell builtin**（source/conda activate）。命令需用绝对路径

### 2. 🖥️ 基础设施快照
- **westd-32570**: 4× RTX PRO 6000 96GB, 工作目录 `/root/nlp_variance_gtheory`, Python `/root/miniconda3/bin/python`（conda base）
  - 模型缓存: `/root/autodl-tmp/.hf_cache/` (Llama/Gemma 本地路径), 其余模型 HF repo ID 直接加载
  - 数据: `/root/nlp_variance_gtheory/data/` (mmlu/gsm8k/arc/hellaswag/math items JSON)
  - 结果: `/root/nlp_variance_gtheory/results/exp001_*/`, `/root/nlp_variance_gtheory/results/exp002/`
  - ROADMAP 显示 GPU 利用率 70-97%，正在跑 InternLM GSM8K(26%), DeepSeek GSM8K(13%), Gemma MATH(97%)
  - DeepSeek MATH accelerator watcher 已部署（Gemma MATH 完成后自动启动）
- **westd-19912**: 4× RTX PRO 6000 96GB, 同样目录结构
  - Yi 推理进行中: MMLU 14%, ARC 37%, HellaSwag 32%, GSM8K 1.7%, MATH 待排
  - OLMo: MMLU/ARC/HellaSwag 288K 行数据存在但需 condition_id 过滤恢复 57.6K 有效记录；GSM8K/MATH 需 Yi 完成后重跑（yi_done_then_olmo 脚本已部署）
  - GPU 利用率 80-98%
- **westd-15695**: 已释放
- **活跃 Worker**: `worker_infra_gpu_status_check_both_servers_20260521T193330` (running, GPU 状态检查)
- **活跃 Cron**: 无（本 session 0 个 cron job）
- **Paper Agent**: 已启动。writing_plan PASS, fig1/fig3 PASS, 文献 cluster 1+2 PASS。**fig2 CRITICAL 修复进行中**（记录数计算错误 + ordering 分类）

### 3. 📊 当前状态
**刚完成**: Session 刚启动初始化（read registry + reconcile crons）。前一个 session 完成了：
- exp-001 系列全部 DONE (Llama/Gemma/Mistral/Qwen 4-model MMLU, 共 ~930K records)
- exp001b_resampling DONE (3×200 item resampling, item_id% CV=2.7%, G_item CV=0.5%)
- exp002_multi_benchmark DONE (4 model × 4 benchmark, 921,600 records)
- 6 项 cross-benchmark 分析 + 9 项 defensive analyses 完成
- D010 narrative pivot 完成 (gradient → format-conditional dichotomy)
- D011 Dream #5 分析完成

**Registry 状态**:
- DONE: 10 个实验 (mvp, bf16_eager, pilot, exp001_{llama,gemma,mistral,qwen}, exp001b, exp002_multi_benchmark, exp-002[killed])
- PREPARING: 21 个实验 (D009 8-model expansion 占位条目: exp002_{olmo,yi,internlm,deepseek} × {mmlu,arc,hellaswag,gsm8k,math} + exp002_math_extension)

**进行中的推理** (非 registry 管理，直接在服务器上跑):
- westd-32570: InternLM GSM8K 26%, DeepSeek GSM8K 13%, Gemma MATH 97% (即将完成)
- westd-19912: Yi 全 5 benchmarks (1.7%-37%)
- 全局完成度: ~28/40 runs (70%)

**等待中**: 
- Worker `worker_infra_gpu_status_check_both_servers` 回调
- Paper Agent fig2 修复回调
- 无 Director 决策等待

### 4. 📋 待办（条件触发式）
- **Gemma MATH 完成 (westd-32570 GPU)** → DeepSeek MATH accelerator watcher 自动启动，无需手动干预
- **InternLM GSM8K + DeepSeek GSM8K 完成** → 检查数据完整性，更新 ROADMAP 进度
- **Yi 全部完成 (westd-19912)** → yi_done_then_olmo 脚本自动触发 OLMo GSM8K/MATH 重跑
- **OLMo MMLU/ARC/HellaSwag 288K 数据** → 需派 Worker 做 condition_id 过滤恢复 57.6K 有效记录（不需要 GPU 重跑）
- **全部 40/40 runs 完成** → 更新 21 个 PREPARING registry 条目为 DONE → 启动 exp-004 全量 8×5 cross-benchmark 分析
- **Paper Agent fig2 修复完成** → 验证图表正确性，推进论文写作
- **exp-004 分析完成** → Dream #6 (review_mode="full") + re-dream 验证 → 冲 AAAI 2027 (abstract Jul 21, paper Jul 28)

### 5. 🎯 战略上下文
**项目核心结论链**: D001(MVP pass) → D002(dual metric) → D003(framing pivot) → D004(dream#2 pass) → D005(Gemma fp16限制) → D006(dream#3 4-model数据强) → D007(审稿R1 action matrix) → D008(dream#4 format confound) → D009(8-model全覆盖) → **D010(Claim 1 从 gradient → format-conditional dichotomy)** → D011(dream#5 7/5/3)

**核心 narrative**: MC benchmarks item-dominated (42-49%), free-form benchmarks methodology-dominated (model 15%, prompt 12%)。这不是 gradient，是 dichotomy。

**审稿状态**: Round 1 评分 Borderline 3.0，目标冲 4.0+。MF1(binary data)/MF2(model count)/MF3(scope) 是三个主要弱点，分别通过 GLMM sensitivity + 8-model expansion + format-conditional pivot 处理。

**最容易判断错的事**:
1. **21 个 PREPARING 条目不是真正的实验**——它们是 D009 expansion 的 registry 占位，实际推理以 bash 脚本形式在服务器上跑，不走 submit_training_job。完成后需要手动更新为 DONE
2. **OLMo 有 288K 行数据不是全部有效**——里面混了无效 condition，需过滤到 57.6K 才能用。GSM8K/MATH 完全缺失需重跑
3. **不要把 GLMM VB 的 ρ=0.571 和 marginal logit ANOVA 的 ρ=1.0 混用**——paper 必须 report both honestly (paper_framing.md 有详细说明)
4. **AAAI 2027 deadline**: abstract Jul 21, paper Jul 28 (距今 ~9 周)。时间充裕但 8×5 全量分析 + 论文写作 + 多轮 dream 需要持续推进
5. **fig2 有 CRITICAL bug** 正在修复（记录数计算错误 + ordering 分类），不要在修复前引用 fig2 数据


---
