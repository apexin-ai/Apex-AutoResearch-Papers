# agent / loop_10.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`b38694dd2d0fd0ec2d92.json`](../../sessions/b3/b38694dd2d0fd0ec2d92.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: idle_timeout
updated: '2026-05-16T04:27:14+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 **仅 westd-11235:cuda:0 和 cuda:1**，绝对不碰其他 GPU
- eval max_length **必须匹配训练 max_length**（DeepSeek full_trace 曾因 eval 用 16384 vs 训练 2048 导致 accuracy 从 79%→28%，详见 memory.md）
- submit_training_job 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不能假设 .venv 存在
- ae_only 数据集 4720 条（ae_only_{train,test}.jsonl），exception_only 与之不同，不要混淆
- 论文 EMNLP 8 页硬限（当前草稿 ~13 页，D042 决策已将 Discussion 移 appendix，但压缩工作未完成）
- Qwen exception_only 99.83% 的 irreducible error（id=901, 905, GeneratorExit）是已确认的 representation 上限，不要当 bug 查

### 2. 🖥️ 基础设施快照
- **服务器**: westd-11235, account=root
- **工作目录**: `/root/trace-verdict-study`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- **数据集**: `/root/autodl-tmp/trace-verdict-study-data/`
- **Checkpoints**: `/root/autodl-tmp/trace-verdict-study-checkpoints/`
- **HF cache**: `/root/autodl-tmp/.hf_cache` (HF_HOME)
- **W&B project**: `trace-verdict-study`
- **活跃进程**:
  - ae_only_seed123: RUNNING on cuda:0, cron 监控中, log=/tmp/ae_only_seed123.log
  - ae_only_seed456: RUNNING on cuda:1, cron 监控中, log=/tmp/ae_only_seed456.log
- **活跃 Worker**:
  - `worker_analysis_trace_length_ablation_fig_20260516T040942` (running, turn 34, 正在 SSH 读取数据做 trace length ablation 图)

### 3. 📊 当前状态
上一轮完成了大量收官工作：regex baseline 分析（93.61% vs SFT 99.83%, p=0.041）、DebugBench 跨任务验证（exception_only 100%）、1024tok trace length ablation、论文页面压缩（13→8 页方案）、对抗审稿 Round 4、DeepSeek paired bootstrap 统计检验、fig1/fig4 修复。

**Registry**: 44 实验总计（25 success / 7 negative / 3 failed / 多个 killed）。仅 2 个 RUNNING：ae_only_seed123 和 ae_only_seed456（ae_only 条件的 seed robustness，Reviewer P0 要求）。

**等待中**:
- ae_only_seed123/456 的 cron 完成回调（训练+eval 一体，预计数小时内完成）
- trace_length_ablation_fig Worker 回调（turn 34，仍在活跃 SSH 读取中）
- 无 Director 待决策项

### 4. 📋 待办（条件触发式）
- **ae_only_seed123 cron 回调到达** → spawn worker 分析结果 → 更新 registry(conclusion) → 若 success: 记录 accuracy/CI 到 paper_framing.md seed robustness 表 → 若两个 seed 都完成: 汇报 Director 完整 ae_only 3-seed 数据
- **ae_only_seed456 cron 回调到达** → 同上逻辑
- **两个 seed 都完成** → patch seed data 进论文草稿（Table 里加 ae_only seed 行）→ 更新 ROADMAP 近期任务清单
- **trace_length_ablation_fig Worker 完成** → 检查产出图表质量 → register_artifact → 集成到论文
- **所有 seed + 图表就绪** → 派 Paper Agent Worker 做最终 patch（regex baseline + DebugBench + ae_only seeds + ablation fig 全部整合进草稿）→ 然后启动 Reviewer 对抗轮次
- **论文初稿完成** → 3 轮 Reviewer 对抗（5/18-20）→ 定稿（5/21-23）→ 5/24 提交 ARR

### 5. 🎯 战略上下文
**核心结论**: Exception events 是 verdict prediction 最有效的 trace 组件。Qwen 99.83% ± 0.00 (3 seeds 完美一致，irreducible error 已确认)。VOTA 的真正贡献是 fault indicator isolation 而非 generic trace compression。Paper framing v3.0 已 FINALIZED（3 claims 全部 confirmed）。

**决策链关键节点**:
- D029: DeepSeek 3-seed 分析 FINALIZED（seed42/456=99.33%, seed123=91.09% LoRA outlier）
- D042: 论文 13→8 页重组方案（Discussion 移 appendix）
- D044-D047: 对抗审稿驱动的 regex baseline + DebugBench 补充实验

**易错点**:
- ae_only ≠ exception_only：ae_only 是 actual/expected output 对比（99.92%），exception_only 是异常事件摘要（99.83%）。两者都是 Tier 1 但信号不同
- DeepSeek seed123 是 LoRA initialization outlier（91.09%），不是方法问题——论文中要讨论但不能当作 limitation
- 不要把 GC4-par (Falcon parallel) 和 GC4-seq 混淆——本项目无 Falcon，但 DeepSeek VOTA 84.45% 的 gap 是 trace truncation 导致而非模型能力问题（D030 已确认）
- 论文压缩是硬需求（EMNLP 8 页），但 D042 方案已就绪，执行即可
- 当前是 9 天冲刺最后阶段，seed 实验是最后的 blocking 数据点，完成后全力转论文


---
