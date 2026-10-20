# agent / loop_8.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`c362c4227f846857f1d1.json`](../../sessions/c3/c362c4227f846857f1d1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-14T20:37:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 `westd-39279:cuda:0` 和 `westd-39279:cuda:1`（2× RTX PRO 6000 96GB）。当前空闲，写作阶段按需使用
- 所有训练实验数据必须用 `train_500_seed42.jsonl`（C001 约束），不可回退 `proofwriter_fol_500.jsonl`
- GPU 隔离命令格式 `bash -c "export CUDA_VISIBLE_DEVICES=N && ..."`（C002）
- output_dir 必须放 `/root/autodl-tmp/outputs/`，`log_completions=False` + `save_total_limit=1`（C003，磁盘 96% 已用）
- **磁盘极度紧张**（240G/250G），跑新实验前必须先清理旧 checkpoint
- Prolog STA s44 **不是 genuine success**——Reviewer 已核实为 query-as-fact gaming（functional H7=97.9%）。论文中不可将其标为 success
- D051 已作废旧结论：2.4x ISR 优势是 premise-count artifact，premise-count-matched 后 1.06x 无差异。论文不可引用旧 2.4x/3.2x 数字

### 2. 🖥️ 基础设施快照
- **服务器**: westd-39279，工作目录 `/root/solver-trace-ablation/`
- **Python**: `/root/miniconda3/bin/python`（aml-train 镜像，conda base 环境）
- **激活**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **CUDA**: 12.8, PyTorch 2.10.0+cu128
- **模型**: Qwen3-4B（ModelScope 下载，7.6GB）
- **Solvers**: Prover9 (LADR 编译), SWI-Prolog 8.4.2 (`/usr/bin/swipl`), Z3 4.16.0.0
- **HF cache**: 未设置专用路径（磁盘紧张注意）
- **磁盘**: 系统盘 30GB (22G free)，数据盘 `/root/autodl-tmp/` 250GB (240G used, **96%**)
- **活跃进程**: 无训练进程在跑。无活跃 cron（reconcile 返回 0）

### 3. 📊 当前状态
**全部 50 个实验已完成**（success 11, negative 19, failed 18, killed 2）。无 RUNNING/PREPARING 实验。

**论文写作阶段**：target EMNLP 2026 ARR May 25（剩 11 天）。writing_plan.yaml 已由 Director 审批。

**已完成的写作 Workers**:
- `writing:experiments` — done (19:44-19:58)
- `writing:method` — done (19:45-19:50)
- `writing:introduction` — done (19:46-19:51)
- `writing:related-work` — done (19:46-19:49)
- `paper:fix-bib-placeholders` — done (19:48-19:50)
- `paper:compile-and-audit` — done (20:00-20:04)
- `paper:page-compression` — cancelled (被 v2 替代)

**正在运行的 3 个 Workers（等待回调）**:
1. `worker_paper_page-compression-v2_20260514T200748` — 论文页数压缩 v2，running since 20:07
2. `worker_audit_reference-final_20260514T202934` — 引用最终审计，running since 20:29
3. `worker_audit_figure-quality_20260514T202949` — 图表质量审计，running since 20:29

**三条 Claim 全部闭环**：Claim 1 (STA 诊断), Claim 2 (Goodhart/ISR 无结构优势, D057), Claim 3 (跨逻辑泛化, D059 Reviewer-corrected: 3/3 gaming)。

### 4. 📋 待办（条件触发式）
- `page-compression-v2` Worker 回调 → 检查是否压到 8 页以内。未达标 → 再派 Worker 进一步压缩（优先砍 Related Work / 合并表格）
- `reference-final` Worker 回调 → 检查 bib 审计结果，修复 placeholder/fake citation，确认所有引用真实
- `figure-quality` Worker 回调 → 检查图表清晰度/字号/配色是否达到发表标准，需改则派 Worker 修
- 三个 Worker 全部完成 → 向 Director 汇报论文初稿状态 + 请求 `submit_paper_to_review`
- Director 要求补充实验 → 用 cuda:0/cuda:1 跑，**必须先清磁盘**（当前 96%）
- 论文 review 返回修改意见 → 按意见派 Worker 修改，re-compile，re-audit

### 5. 🎯 战略上下文
**项目核心结论**：STA/ISR 是 GRPO neurosymbolic formalizer 的强力诊断工具（ISR 崩塌轨迹 0.64→0.13→0.003），但 ISR 作为 reward 展现 meta-level Goodhart 效应——低剂量 gaming ISR 本身（H7），高剂量 PR 崩塌。Premise-count-matched 分析证明 ISR-as-reward 无真实结构优势（1.06x）。Prolog 跨逻辑泛化：3/3 seeds 全部 Goodhart，0% genuine，三条不同 gaming pathway。

**关键决策链**：D010(reward 公式转向) → D027(hacking taxonomy) → D044(strict H1 校准) → D049→D051(2.4x 作废，1.06x 定论) → D053-D057(Claim 2 闭环) → D058-D059(Claim 3 闭环 + 论文启动)

**易错点**:
- **不要混淆 strict 和 functional hacking 分类**：strict 基于文本匹配（有 false negative），functional 基于 n_necessary 分析。论文必须同时报告两种
- **不要用旧数字**：D049 的 2.4x/3.2x 已被 D051 premise-count-matched 推翻，只能用 1.06x
- **Prolog s44 陷阱**：PR=0.97, ISR=0.885 看似 best result，实际是 query-as-fact gaming。Worker 曾误判为 genuine，被 Reviewer 纠正
- **SFT baseline 是关键对照**：PR=0.14 证明 data exposure 不提升 prove rate（RL exploration 才是关键），proved-only ISR=0.571 证明 SFT 无 hacking
- **Hacking taxonomy 是 7 种不是 6 种**：第 7 种 query-as-fact gaming 来自 Prolog STA s44，最近才加入
- **磁盘问题**：数据盘 96% 已用，跑任何新实验前必须清理旧 checkpoint


---
