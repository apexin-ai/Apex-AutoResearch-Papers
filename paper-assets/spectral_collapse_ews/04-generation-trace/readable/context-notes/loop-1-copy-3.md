# reviewer / loop_1.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`3ca85a8537cbb1f04ddc.json`](../../sessions/3c/3ca85a8537cbb1f04ddc.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-16T12:07:15+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1 only（rtx6000-diagprobe）。越界 → severity: critical
- Phase 0 用 cuda:0，HellaSwag eval 用 cuda:1。不可反过来（Phase 0 进程已绑定 cuda:0）
- Controller 参数与论文不一致（论文 k=2.0/r_min=0.10/r_max=0.90 vs 代码 k=1.0/r_min=0.20/r_max=0.80）——Phase 1 启动前必须统一，以 Director 决策为准
- Gen 0→1 effective rank 上升是已知现象（D004），decline rate 基线从 Gen 1 算，不是 Gen 0

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe（2× RTX PRO 6000 Blackwell, 98GB each）
- 工作目录：/root/spectral_collapse_ews
- Python：/root/miniconda3/bin/python（conda base env，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型：/root/spectral_collapse_ews/models/models--EleutherAI--pythia-410m-deduped/（safetensors 格式）
- 数据：/root/spectral_collapse_ews/data/（train_real_50k.pt / eval_5k.pt / spectral_1k.pt）
- 论文：/root/spectral_collapse_ews/paper/（abstract.tex / introduction.tex / method.tex / related_work.tex / experiments.tex / references.bib）
- 活跃：exp_001 Phase 0（PID 7396, tmux, cuda:0）——registry 标 PREPARING 但实际 RUNNING
- HellaSwag 数据：/root/.cache/huggingface/hellaswag_manual/（parquet 格式）
- lm_eval：/root/miniconda3/lib/python3.12/site-packages/lm_eval/

### 3. 📊 当前状态
Phase 0 正在运行（Gen 1 已完成，Gen 2+ 训练中）。早期数据：
- Gen 0: eff_rank=417.5, ppl=9.55, distinct4=0.7414
- Gen 1: eff_rank=491.8（上升！已知 anisotropy 效应）, ppl=11.38, distinct4=0.6256

论文 5 个章节初稿完成（abstract/intro/method/related_work/experiments），references.bib 已修正（16/16 真实作者）。

未完成审查：controller 参数不一致（paper vs code）需 Director 决策。
Registry status 应为 RUNNING 但仍标 PREPARING——提醒过 Director 但未见更新。

### 4. 📋 待办
- Phase 0 完成（10 代全部跑完）→ 检查 go/no-go 三条件：(1) eff_rank Gen 1-10 单调下降（允许 ≤1 波动）, (2) 加速比 decline_rate(gen6-10)/decline_rate(gen1-5) ≥ 1.5x, (3) ppl ≥ 20% 上升。任一不满足 → 项目 kill
- Gen 2-3 数据出来 → 确认 eff_rank 从 Gen 1 开始是否下降。如果继续上升 → 立即报 Director 启动 contingency（加 log-det metric / 切信号）
- Phase 0 pass → 审查 Phase 1 controller 参数最终值（τ, k 从 Phase 0 校准）+ pipeline.py 实际使用的参数
- Phase 1 结果出来 → 核心假设检验：adaptive vs fixed ≥ 3 ppl (paired t-test p<0.1)
- 论文最终版 → 对照 registry 数字逐条验证每个 quantitative claim

### 5. 🎯 战略上下文
决策链：D001(MVP方案) → D002(3 seeds + 量化 go/no-go) → D003(保持 May 25 DDL) → D004(Gen 1 作为 decline 基线)

核心风险：**如果 effective rank 在 Gen 1-10 不单调下降，项目必须 kill 或 pivot 到 log-det 信号**。这是 Phase 0 go/no-go 的核心判断。

易错点：
1. 不要把 Gen 0→1 的上升当作 Phase 0 fail——D004 已决定排除 Gen 0，只看 Gen 1 起的趋势
2. 论文 controller 参数和代码不一致——审查 Phase 1 结果时必须确认实际跑的参数是哪组
3. Registry exp_001 spec 被 submit_training_job 覆盖了原始 hyperparams——原始 spec 在 decisions.yaml D001 中有记录
4. 投稿 DDL 是 May 25 ARR（9 天），所有审查应优先不阻塞实验流水线


---
