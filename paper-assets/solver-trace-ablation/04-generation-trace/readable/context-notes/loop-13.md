# agent / loop_13.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_13.md`
- **Structured JSON:** [`91b6d29a7e39cdad2758.json`](../../sessions/91/91b6d29a7e39cdad2758.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: idle_timeout
updated: '2026-05-15T18:05:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**只能用 westd-39279 的 cuda:0 和 cuda:1**，无其他 GPU 配额
- Config 命名陷阱：ISR additive bonus 的 config 是 `grpo_additive_bonus_b01.yaml`（不是 `grpo_additive_b01.yaml`），Random 的是 `grpo_additive_random_b01.yaml`
- Random s43/s44 旧统计量已 **DEPRECATED**——paper_framing.md 中 s43 genuine=6.8%、s44 genuine=20.2% 是 PROVISIONAL 推算值，**绝对不能**写入论文，必须等重训数据重算
- D051: 2.4x 倍率作废，premise-count-matched 1.06x 是定论
- genuine = proved − H7 − H1_exact − H8（D084 标准），classify_h7.py D086 版本是 ground truth

### 2. 🖥️ 基础设施快照
- **服务器**: westd-39279，账号 root
- **工作目录**: `/root/solver-trace-ablation`
- **Python**: `/root/miniconda3/bin/python`，激活方式 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型输出**: `/root/autodl-tmp/outputs/`（各实验子目录）
- **H7 分类结果**: `/root/autodl-tmp/outputs/h7_classification/`
- **训练数据**: `data/train_500_seed42.jsonl`（500 条），评估数据 `proofwriter_fol_100.jsonl`
- **活跃进程**: plan018-additive-random-b01-s44-r2（PID 533415, tmux, cuda:1, RUNNING）
- **活跃 Cron**: plan018-additive-random-b01-s44-r2（reconcile 确认 still running）
- **预置镜像**: aml-train（conda 环境，不用 venv）

### 3. 📊 当前状态
**刚完成的**:
- plan018-additive-random-b01-s43-r3（Random β=0.1 s43 重训）训练完成 → 进入 **ANALYZING**，两个分析 Worker 正在运行：
  - `worker_analysis_plan018-additive-random-b01-s43-r3_20260515T174506`
  - `worker_analysis_plan018-s43-r3-eval-taxonomy_20260515T175131`
- plan002-additive-b01-s43-r2（ISR β=0.1 s43 重训）已 **DONE(negative)**：PR=0.61, 100% H7 tautological collapse, genuine=0%。但尚未向 Director 汇报此结果

**正在运行的**:
- plan018-additive-random-b01-s44-r2（Random β=0.1 s44）在 cuda:1 上 RUNNING（PID 533415，约 17:43 提交）

**等待中**:
- 等两个 s43-r3 分析 Worker 回调 → 完成 taxonomy 分类 + 注册 metrics
- 等 plan018-s44-r2 训练完成 → cron 回调 → 分析

**未汇报 Director 的关键结果**:
- plan002-b01-s43-r2 negative（全 H7，genuine=0%）—— 这强化了 Claim 2（ISR 无结构优势），与 s42 的 H7 13/81 模式不同，s43 是 100% H7 collapse

### 4. 📋 待办（条件触发式）
- s43-r3 分析 Worker 回调到达 → 读取 taxonomy 结果 → update_registry metrics → 刷新 report.md
- s43-r3 分析完成 + plan002-s43-r2 结果整合 → 向 Director 汇报（含 plan002-s43-r2 negative + plan018-s43-r3 taxonomy，开头带 [资源] 行）
- plan018-s44-r2 cron 回调 → spawn Worker 跑 eval_sta.py + classify_h7.py → taxonomy 分类
- **s43-r3 + s44-r2 均完成** → 重算所有 Random pooled 统计量（替换 DEPRECATED Fisher p / Wilson CI / genuine rate 聚合）→ 论文 §4 数据表最终更新
- 所有 3-seed 数据就位 → TeX 全量同步 + 编译
- Provenance 35/36 → 查缺补漏（找到缺失的那 1 个）

### 5. 🎯 战略上下文
**项目处于收尾阶段**：DDL 2026-05-25（剩 10 天），审稿进行中 + 写作阶段。3 个 Core Claims 证据链全部就位（D090）。当前只是补全 Random/ISR 3-seed 数据（替换 DEPRECATED 旧数据）。

**核心结论链**:
- D090: Exec-only 3-seed 1000步确认 Goodhart collapse 是 seed-invariant（genuine→0%），但 hacking mode 是 seed-dependent（s42=H1, s43=H7, s44=H1+H8）
- D088→D089: H7 不是 GRPO 通用终态，而是 additive reward 特有现象；exec-only 走 H1
- D079: SFT 3-seed genuine=92.2%±1.2%，零 hacking → Goodhart collapse 是 GRPO 特有
- D057: ISR 与 Random β=0.1 无显著 genuine rate 差异（p=0.637），ISR 无结构优势

**最容易判断错的事**:
- plan002-b01-s43-r2 是 **negative**（100% H7, genuine=0%），但这对论文是 **好消息**——强化了 "ISR 无结构优势" 的 Claim 2。不要当作失败处理，应该走 red-section 但 narrative 方向已经是 Goodhart 案例研究
- s42 的 ISR genuine=17.3% 是 3-seed 中的异常值（s43=0%, s44 待出），不要过度解读单 seed
- eval_sta.py 没有 --gpu 参数，必须用 CUDA_VISIBLE_DEVICES 环境变量


---
