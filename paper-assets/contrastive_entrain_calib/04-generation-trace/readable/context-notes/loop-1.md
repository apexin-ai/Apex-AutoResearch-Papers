# director / loop_1.md

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`befe1e99266b0d7f1448.json`](../../sessions/be/befe1e99266b0d7f1448.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-19T08:32:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：westd-29046 GPU 0,1（2×96GB）；westd-28034 GPU 0,1,2,3（4×32GB）
- `output/directions.pt` 已重命名为 `directions_STALE_DO_NOT_USE.pt`（M013）——任何诊断脚本只能引用 `results/exp001/directions.pt`
- exp-002v2-recalib **不再 kill**（已第 3 次重启），让它跑完与 exp-003 对比
- 用户尚未回复 EMNLP venue 决策（May 25 vs ARR August），不要替用户做这个决定
- eval pipeline 必须传 `enable_thinking=False`（Qwen3 thinking token 污染 bug 已修复）

### 2. 🖥️ 基础设施快照
- **westd-29046**（2×L40S 96GB）：`/root/contrastive_entrain_calib/`
  - GPU 0: exp002v2-recalib (PID 172838, tmux=exp002v2-recalib)
  - GPU 1: exp-003 (PID 70649)
- **westd-28034**（4×A6000 32GB）：`/root/contrastive_entrain_calib/`
  - GPU 0: exp-004 (PID 18204) — ETA ~20:40 UTC 今晚
  - GPU 1+2: exp-008v3 (DeepSpeed ZeRO-2, tmux=exp-008v3)
  - GPU 3: vanilla baseline eval Worker（进行中）
- 模型：Qwen3-8B（HF cache 本地，HF_HUB_OFFLINE=1）
- W&B：无（实验未配 W&B，靠日志和 cron 监控）
- eval pipeline：`/root/contrastive_entrain_calib/evaluation/eval_pipeline.py`（已修复 thinking token）
- dcgrpo_trainer.py：已有 `r1_scale_factor` 参数支持 + `recalibrate_direction()` sanity logging

### 3. 📊 当前状态
刚完成 R1 信号弱根因分析（D025）+ exp-002v3 代码设计（D026）+ paper_framing.md 双线 narrative 更新。

**RUNNING**：
- exp002v2-recalib: step ~741/8000, R1≈0（信号弱确认，跑完做对比）, ETA May 21-22
- exp-003: step ~1894/8000, R3-only baseline, 正常, ETA May 21
- exp-004: step ~6390/8000, ACT baseline, SFT loss=0（过拟合）, ETA 今晚 ~20:40
- exp-008v3: step ~291/8000, Binary Probe GRPO, R1=0.375-1.0（信号极强）, ETA May 21-22

**PREPARING**：
- exp-002v3: 代码 ready（scale_factor=5, r1=0.4, r3=0.6, lora_alpha=64, 无 resume），需 DeepSpeed ZeRO-2 config for 28034 GPU 0+3，等 exp-004 完成后部署
- exp-003-s2: 代码 ready（seed=43），等 GPU

**等待中**：
- vanilla baseline eval Worker 结果（~10-20 min）
- exp-004 完成 cron 回调（今晚）
- 用户 venue 决策

### 4. 📋 待办（条件触发式）
- vanilla eval Worker 完成 → 汇报 NoF/WRR 数据 → 立即启动 exp-014 checkpoint eval（GPU 3）
- exp-004 cron 回调 → 完整 eval（GPU 0+3）→ eval 完成后审批 exp-002v3 启动（GPU 0+3 ZeRO-2）
- exp-008v3 step 500 → 确认 probe retrain 正常触发 → 监控 R1 趋势
- exp002v2-recalib step 1000 → 检查 recalibration 日志（cosine + AUROC）→ 确认 R1 仍弱（预期）
- exp-003 完成 → GPU 1 (29046) 释放 → 可部署 exp-003-s2 或其他
- 用户回复 venue → 调整时间线 + 决定是否启动 Paper Agent

### 5. 🎯 战略上下文
**核心决策链**：D020(cosine fix) → D021(gate removal) → D023(kill exp-014) → D024(recalib restart, 基于错误数据) → D025(74° drift 是误报 M013, R1 弱是真问题) → D026(exp-002v3 scaled cosine 设计)

**项目存亡级问题**：Claim 2（DC-GRPO effectiveness）需要 direction-informed reward > R3-only。当前 exp-002v2 的 R1 贡献仅 8%，实质等同 R3-only。两条活路：
- **Story A**：exp-002v3 (scaled cosine R1) 有效 → continuous direction reward
- **Story B**：exp-008v3 (binary probe R1) 有效 → binarized direction reward
- 两条都支撑 "direction information matters"，最终看 eval 谁赢

**最容易判断错的事**：
1. 不要再相信 `output/directions.pt`（已重命名但可能有残留引用）——所有方向文件只用 `results/exp001/directions.pt`
2. exp-002v3 需要 ZeRO-2 双卡（28034 GPU 0+3），不能放单张 32GB 卡
3. exp-004 SFT loss=0（过拟合），eval 结果可能差——但作为 "ACT doesn't work" baseline 仍有论文价值
4. 禁止建议用户降级到更低级别会议——时间紧就加并行，不降目标


---
