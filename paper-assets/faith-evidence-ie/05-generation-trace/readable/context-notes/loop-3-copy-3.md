# reviewer / loop_3.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`b8f45b09c9f1755ec077.json`](../../sessions/b8/b8f45b09c9f1755ec077.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-14T19:16:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 rtx5090-4x 4 张卡（cuda:0-3）均属本项目，无跨项目 GPU 分区限制，但仍需核对每个实验 spec 里的 CUDA_VISIBLE_DEVICES 与 registry gpu 字段一致
- eval 结果的 output_dir 有两个：`/root/autodl-tmp/eval_results/grpo_ced_kl001/`（主目录，多数 checkpoint 共用）和 `/root/autodl-tmp/eval_results/grpo_ced_kl001_step100/`（step100 单独）——比对指标时注意别读错目录
- SFT baseline 已双重确认（r2=r3 完全一致）：rel_f1=0.4057, evi_f1=0.7979, edcr=0.7118。这是 MVP-2 pass criteria 的锚点，不可动摇

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x（root），备用 bjb2-12179（root）
- 代码：`/root/autodl-tmp/freige`
- Python：`/root/miniconda3/bin/python`（conda base 环境，非 venv）
- 模型：`/root/autodl-tmp/models/Qwen3-4B`，SFT adapter：`/root/autodl-tmp/sft_output`
- GRPO checkpoint：`/root/autodl-tmp/grpo_ced_kl001/`（checkpoint-10 到 checkpoint-100，共 10 个）
- 数据：`/root/autodl-tmp/data/docred`（train 3027, dev 985）
- HF cache：`/root/autodl-tmp/.hf_cache`
- Eval 结果：`/root/autodl-tmp/eval_results/grpo_ced_kl001/`（summary.json + per-checkpoint 子目录）
- 活跃进程（截至 handoff）：PID 78850 (multi eval, cuda:2), PID 80789 (step100, cuda:0), PID 81962 (high, cuda:3), PID 83207 (step90, cuda:1)

### 3. 📊 当前状态
刚完成对 worker_analysis_eval-status-check 的审查并发布报告。核心发现：

**已出 eval 结果**：
- checkpoint-10: f1=0.003, evi_f1=0.720（34 TP，无意义）—— 灾难性遗忘
- checkpoint-50: f1=0.156, evi_f1=0.564 —— 部分恢复但远低于 SFT

**仍在运行的 eval**（6 条 registry RUNNING，实际 4 个进程）：
- mvp2_eval_ced_kl001_r4_step100 (cuda:0, ~73% done)
- mvp2_eval_ced_kl001_r4_step90 (cuda:1, ~47% done)
- mvp2_eval_ced_kl001_r4_multi (cuda:2, 7 checkpoints, 已完成 ckpt-10, 数小时)
- mvp2_eval_ced_kl001_r4_high (cuda:3, 正在 eval ckpt-60)

**幽灵条目**：ckpt90 和 ckpt10 标 RUNNING 但实际未独立运行。

**等待**：Director 对我审查报告的回应（已通过 reviewer_post_to_director 发出）。

### 4. 📋 待办
- step90/step100 eval 完成 → 读 metrics.json 核对。若 f1 < 0.25 → 确认 MVP-2 FAIL，建议 Director 立即启动下一轮实验
- step90 eval_f1 意外 ≥ 0.35（接近 SFT）→ 仔细核实是否 eval 代码/数据有变（太反常，与 ckpt-10/50 轨迹不符）
- multi eval 出完整 10→80 轨迹 → 绘制 step vs f1/evi_f1 曲线，确认 reward hacking 拐点
- Director 下达 MVP-2 FAIL 后的新实验方案 → 审查新方案的 reward 设计是否修正了根因
- flatnli_r6 (mode collapse step 25) 和 extract_r4 (mode collapse step 30) 已确认失败 → 无需继续关注

### 5. 🎯 战略上下文
**MVP-2 核心问题**：CED reward + GRPO 导致灾难性遗忘。模型在第 10 步就丧失几乎全部抽取能力（f1: 0.4057→0.003），后续 training reward 持续上升但 eval f1 远未恢复。这不是"后期过拟合"——是"训练即崩"+ reward proxy 与真实任务脱钩。

**三路对比结论**（D020 配置下）：
- CED reward（ced_kl001_r4）：训练稳定（100 steps），但 eval 灾难性退化
- Flat-NLI reward（flatnli_r6）：mode collapse at step 25
- Extraction-only reward（extract_r4）：mode collapse at step 30
→ CED 是唯一能维持 GRPO 多样性的 reward，但"训练不崩"≠"有用"

**易踩的坑**：
1. 不要被 training reward 曲线（持续上升到 1.37）误导——它与 eval 性能完全脱钩
2. evi_f1 在 TP 数极少时（如 ckpt-10 仅 34 TP）不可作为判断依据
3. Registry 有 6 条 RUNNING 但实际只有 4 个进程——核对 PID 存活状态再下结论
4. 下一轮实验方案如果只是调 kl_coef / lr 微调，可能不够——reward 函数本身可能需要重新设计（format reward 在 ckpt-10 已经 0.999，说明 GRPO 主要在优化 format 而非 extraction）


---
