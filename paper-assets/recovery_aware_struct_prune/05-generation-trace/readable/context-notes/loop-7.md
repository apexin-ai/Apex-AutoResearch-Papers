# director / loop_7.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`03ee2e35f837b816b927.json`](../../sessions/03/03ee2e35f837b816b927.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-15T13:55:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 C001：westb cuda:0/1, westd cuda:0/1。严禁使用其他卡
- westd 上必须用 `CUDA_VISIBLE_DEVICES=X` + `--gpu 0`（进程只看到一张卡，device 编号用 0），否则会 OOM（已踩坑 3 次）
- `sft_recovery.py` 不支持 `--save_strategy no` CLI 参数（会 EXIT_CODE=2），需用 sed 在脚本内改 `save_total_limit=1`
- westd 数据盘 `/root/autodl-tmp/` 250GB 已满，大文件必须清理或用根分区
- D006/D014/D015 决策链已失效（基于 eval bug 的 29x advantage），不可引用

### 2. 🖥️ 基础设施快照
- **westb-23072**: `connect.westb.seetacloud.com`, 2x ~98GB GPU
  - 代码: `/root/recovery_aware_struct_prune/`
  - 模型: `/root/autodl-tmp/recovery_aware_struct_prune/` (pruned models, SFT checkpoints)
  - GRPO v6 RASP: PID 520992 cuda:0
  - GRPO v6 Standard: PID 521084 cuda:1
- **westd-11672**: `connect.westd.seetacloud.com`, 2x ~95GB GPU
  - 代码: `/root/recovery_aware_struct_prune/`
  - α pruned models: `/root/autodl-tmp/pruned_alpha_{0.0,0.5,1.0,2.0,4.0}/`
  - GraSP pruned model: `/root/autodl-tmp/pruned_grasp_20/` (或类似路径，需确认)
  - GraSP SFT: PID 38509 cuda:0
  - α=0.0 SFT: 正在 cuda:1 启动中（Agent 发现已有旧产出，在验证）

### 3. 📊 当前状态
刚完成：D028 kill v5 + 启动 v6，D029 确认 SFT recovery 阶段 Standard 优于 RASP。已重置 Reviewer。

**RUNNING:**
- `grpo_stage2_rasp_20_v6` — westb cuda:0, max_completion_length=1024, 250 steps, ~21h, ETA ~5/16 09:00 UTC
- `grpo_stage2_standard_20_v6` — westb cuda:1, 同参数，负对照
- `sft_grasp_20_westd` — westd cuda:0, GraSP pruned model SFT recovery (~35min)
- α=0.0 SFT — westd cuda:1, 验证中/启动中

**PREPARING/队列:**
- α ablation SFT 剩余: α=0.5 → α=2.0（排在 α=0.0 之后逐个跑 westd GPU 1）
- GraSP N=100 eval — 待 GraSP SFT 完成后补跑
- GraSP SFT eval — 待 SFT 完成后

**等待中:** GRPO v6 step 10 metrics 回调（~50min from v6 start，可能已过期需检查）

### 4. 📋 待办
- GRPO v6 step 10 metrics 出来 → clipped_ratio >80% 则讨论再加长 max_completion_length; <80% 则继续
- GRPO v6 完成（~5/16 09:00）→ 立即 eval 两个模型（N=100, greedy）→ 对比 |RASP - Standard|: <5pp 全面 pivot, 5-15pp 降级 claim, >15pp recovery-pathway 成立
- GraSP SFT 完成 → eval N=100 → 填入三方对比表
- α=0.0 SFT 完成 → eval → 继续 α=0.5 SFT → 直到 5 个 α 值都有 post-SFT 数据
- 所有 α SFT+eval 完成 → 完整 α vs recovery 曲线，检验非单调模式

### 5. 🎯 战略上下文
**核心危机：** 原始 "RASP 29% vs Standard 1%" 完全是 eval bug。Definitive re-eval: RASP 31% vs Standard 27% (4pp, p=0.54)。Post-SFT: Standard 64% > RASP 57%。两阶段均未支持核心假设。

**决策链：** D027 暂不 pivot 等 GRPO → D028 kill v5 切 v6 (512→1024) → D029 SFT recovery 也未支持假设

**GRPO v6 是项目翻盘唯一机会。** 如果 GRPO RASP 显著优于 Standard → story 转为 "CKA-guided pruning 创造更好的 RL recovery dynamics"（窄但有意义）。如果 GRPO 也无差异 → 需根本性 pivot。

**易错点：**
- westd 任务反复未被 Agent 执行（前 session 连续 3 次 Reviewer 报告空闲），新 session 启动后必须确认 westd 进程实际在跑
- Agent 容易 kill 进程时只改 registry 不实际 kill PID（v5 事件），必须 nvidia-smi 确认
- calibration 混淆：westb 用 cal=512, westd 用 cal=256，跨服务器对比不严格；α ablation 内部对比（全是 cal=256）是干净的
- GraSP 8% 是好数据——证明 RASP >> GraSP，可作为 baseline 对比论据，无论 pivot 与否


---
