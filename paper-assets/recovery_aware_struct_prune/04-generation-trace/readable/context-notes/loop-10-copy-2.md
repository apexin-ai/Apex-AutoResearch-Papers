# agent / loop_10.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`4a8978a02f065be52126.json`](../../sessions/4a/4a8978a02f065be52126.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: idle_timeout
updated: '2026-05-15T21:41:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb cuda:0/1, westd cuda:0/1（约束 C001）。其他设备号一律 push back Director
- RASP GRPO 已连续 3 次 collapse（v2/v5/v8），**不要再用相同参数重跑 RASP GRPO**
- westb 磁盘 250G/250G 已满——Standard v8 checkpoint 保存受威胁，提交任何新任务到 westb 前必须先清理磁盘
- Unpruned baseline GRPO 实验设计无效（D041：缺 SFT 步骤，不构成公平对照），不可引用其结果做因果推断
- GRPO collapse 因果结论暂不引用（D042），等 Standard v8 完成后三者对比才能定论
- 投稿目标 EMNLP 2026 ARR May 25（距今 10 天），不可建议降级 venue（L1 红线 #6）

### 2. 🖥️ 基础设施快照
- **westb-23072**（root）：工作目录 `/root/recovery_aware_struct_prune`，Python `/root/miniconda3/bin/python`（conda base），2× ~98GB GPU
  - cuda:0 空闲（RASP v8 已结束）
  - cuda:1 运行 `grpo_stage2_standard_20_v8`（PID 534667, cron 活跃）
  - 磁盘 100% 满，HF cache 已迁移到数据盘但仍需清理旧 checkpoint
- **westd-11672**（root）：同路径同 Python，2× ~95GB GPU
  - cuda:0/1 运行 full eval（`eval_sft_rasp_full_westd` PID 62565, `eval_sft_standard_full_westd` PID 62463）——**无 cron 注册**，由 Worker 直接管理
- W&B: grpo_stage2_standard_20_v8 run ID `q34vz8j2`
- 模型路径: `/root/recovery_aware_struct_prune/` 下各 checkpoint 子目录
- eval 脚本: westd 必须从 westb 同步（含 `apply_chat_template`），旧版在 `/root/autodl-tmp/`

### 3. 📊 当前状态
**刚完成**：RASP GRPO v8 collapse（negative）+ Unpruned baseline collapse（failed/invalid）→ narrative pivot 讨论（D035-D042）。三方 post-SFT 对比确认：Standard 64% > RASP 57% > GraSP 41%。文献搜索完成，确认 pruning+RL stability 无直接先例。

**正在运行**：
| exp_id | 服务器 | GPU | 说明 |
|--------|--------|-----|------|
| grpo_stage2_standard_20_v8 | westb | cuda:1 | **唯一核心实验**，PID 534667，cron 活跃，ETA ~5/16 11:30 UTC |
| eval_sft_rasp_full_westd | westd | cuda:0 | N=1319 full eval，无 cron，Worker 管理中 |
| eval_sft_standard_full_westd | westd | cuda:1 | N=1319 full eval，无 cron，Worker 管理中 |

**活跃 Worker**：
- `worker_ops_westd-full-eval-collect_20260515T213655` — 收集 westd full eval 结果
- `worker_ops_alpha-sweep-monitor-v3_20260515T213943` — 监控 α ablation sweep

**等待中**：多个 PREPARING 实验（alpha_ablation_sweep, eval_sft_grasp_20, grpo_standard_20_v8 等）blocked on GPU 或前序完成。

### 4. 📋 待办（条件触发式）
- **grpo_stage2_standard_20_v8 cron 回调到达** → 这是全项目最关键事件。按 ROADMAP contingency 表判定：
  - Standard GRPO 也 collapse → 三者全 collapse，GRPO 配置本身有问题，narrative 必须大 pivot（不再是 pruning vs recovery，而是 pruning 对 RL stability 的影响）
  - Standard GRPO 不 collapse 且 accuracy >15% → **核心发现：Standard pruning 保留 RL plasticity 而 RASP/Unpruned 不行**，Narrative A "Pruning for Plasticity" 成立
  - Standard GRPO 不 collapse 但 accuracy <15% → 弱信号，需要 multi-seed 验证
- **westd full eval Worker 回调** → 比较 N=1319 结果与 N=100（RASP 57%/67% 偏差是否消失），更新 registry，判断 calibration sensitivity claim
- **westb cuda:0 空闲** → 磁盘满阻塞新任务，需先 spawn Worker 清理（旧 v1-v7 checkpoint、HF cache 残留），然后可铺 α ablation 或其他 eval
- **α=0.5 SFT eval 未完成** → westd eval 完成后腾出 GPU，补齐 α ablation 全表（α=0.0 64%, α=0.5 ?, α=1.0 57%, α=2.0 62%, α=4.0 62%）
- **Director 确认 narrative 方向后** → 读 framing-reaudit skill → 全文 re-audit → 开始论文写作

### 5. 🎯 战略上下文
**项目核心结论链**：
- D027: Post-prune RASP vs Standard 仅 4pp（不显著）→ pre-recovery claim 死了
- D029: Post-SFT Standard > RASP 7pp → SFT recovery 不支持 RASP 优势
- D033: α ablation SFT 差异统计不显著
- D034: GraSP 41% 是唯一稳固 finding（p=0.001）
- D035-D038: RASP GRPO 3x collapse + Unpruned also collapse → **Standard 是唯一还在学习的模型**
- **整个论文 story 悬于 Standard GRPO v8 一个实验**

**最容易判断错的事**：
1. **不要把 Unpruned collapse 当作"剪枝有益"的证据**——Unpruned 实验缺 SFT 步骤（D041），不是公平对照。需要重新设计 SFT→GRPO 的 unpruned baseline 才能做因果推断
2. **不要混淆 westb/westd 的 RASP eval 数字**——westb 57%, westd 67%（10pp gap），根因是 calibration 差异（cal=512 vs 256），full eval 结果出来前不可取 67% 作为 RASP 代表值
3. **westb 磁盘满是定时炸弹**——Standard v8 如果在 checkpoint save 时磁盘写满会 crash，优先级高于铺新实验
4. **Narrative 方向尚未定**——Director 暂定 Narrative A "Pruning for Plasticity"，但明确说等 Standard v8 + Unpruned 结果后再改 paper_framing.md。不要提前改 framing


---
