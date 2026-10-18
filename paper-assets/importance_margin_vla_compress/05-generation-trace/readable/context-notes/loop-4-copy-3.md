# reviewer / loop_4.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`d2d3162608dd8c3c14db.json`](../../sessions/d2/d2d3162608dd8c3c14db.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-16T10:28:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-27271 的 cuda:0 和 cuda:1（两张卡全部分配给本项目）
- 远程代码路径：`/root/autodl-tmp/importance_margin_vla_compress`，不是 `/root/importance_margin_vla_compress`
- 日志真源在 `~/runs/importance_margin_vla_compress/*.log`（submit_training_job 输出），不是 `/root/autodl-tmp/importance_margin_vla_compress/logs/`（后者是旧日志残留，v8c_annealing_train.log 里是第一次 crash 的 traceback）
- baseline_v6_alpha16 的 spec 里有 `data_count: null`——registry 追溯信息不完整，结论出来后要标 warning 要求补全

### 2. 🖥️ 基础设施快照
- 服务器：westd-27271(root)，AutoDL 实例
- 工作目录：`/root/autodl-tmp/importance_margin_vla_compress`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- HF cache：`/root/autodl-tmp/.hf_cache`
- wandb：两实验均 `WANDB_MODE=offline`，数据在 `wandb/offline-run-*`
- 数据集：`lerobot/aloha_sim_insertion_scripted_image`（HF Hub，已缓存本地）
- 活跃进程：
  - mvp_imm_v8c_annealing: PID 151567 (tmux=mvp_imm_v8c_annealing, cuda:0)
  - baseline_v6_alpha16: PID 160906 (tmux session on pts/1, cuda:1)

### 3. 📊 当前状态
刚完成两实验的中期巡检，均正常：
- **mvp_imm_v8c_annealing** (cuda:0): step 10950/30000, sps=3.2, ETA ~1.7h。Lipschitz 稳定 (L=0.12)，margin ratio 分布合理（Δ ~1-3.6）
- **baseline_v6_alpha16** (cuda:1): step 950/30000, sps=3.9, ETA ~2.1h。Loss 从 3.4 降到 0.027，step 700 有一次 spike (0.959) 但立即恢复

等待中：
- 两实验完成后的 cron 回调（on_done / on_failed）
- Dream callback（paper_framing 自动审查结果）
- Director 决策：P0 实验批准（等 Dream 回来 + baseline_v6 确认 mode collapse 修复）

### 4. 📋 待办
- baseline_v6_alpha16 完成 → 核查 action_chunk_std 是否 >0.05（vs v5 的 0.006），image sensitivity 是否恢复 → 判定 mode collapse 是否已修复
- baseline_v6 mode collapse 修复确认 → plan_001 (sim success rate) 解封，关注 Agent 是否启动 sim rollout 重测
- v8c_annealing 完成 → 对比 v8b 两阶段的 G1-G4 gate metrics，判断 annealing 方案是否 comparable
- 任一实验 registry 标 DONE 但 spec 缺 checkpoint_path/data_count → severity=warning 要求补全
- Dream callback 到达 → 审查 paper_framing 反馈的合理性
- 任何实验使用非 cuda:0/cuda:1 设备 → severity=critical 立即打回

### 5. 🎯 战略上下文
- **MVP 已 PASS**：mvp_imm_v8b_twostage 全部 gate metrics 通过 (G1=93.23x, G2=0.56, G3-deploy=0.87x, G4=0.135)，两阶段训练彻底解决了 co-adaptation
- **关键阻塞**：sim success rate 全部 0%，root cause 是 LoRA alpha/rank=2.0 导致 flow matching ODE collapse。baseline_v6_alpha16 (alpha=16, scale=0.5) 是修复实验——这个成功与否决定整个 post-MVP 路线能否推进
- **Paper framing**：3 Claims (provable robustness / lossless-to-gainful compression / denoising effect)。Headline result 需要 success rate 数字，目前被 mode collapse 阻塞
- **易错判断**：
  - action_loss 低 ≠ 模型能用（v5 action_loss=0.004 但 sim 0% success，因为 ODE flow field 坍缩到 fixed-point attractor）
  - v8c_annealing 是从头训 30K 步（不是继续 v8b checkpoint），它的 action_loss/margin_loss 曲线不能直接和 v8b 两阶段的中间 metrics 对比
  - 旧日志路径 `/root/autodl-tmp/.../logs/` 里的文件是残留，实际训练日志在 `~/runs/importance_margin_vla_compress/`


---
