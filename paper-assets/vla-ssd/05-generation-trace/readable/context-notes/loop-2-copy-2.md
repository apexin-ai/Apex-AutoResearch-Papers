# agent / loop_2.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`165369bac5c56e5c1fc8.json`](../../sessions/16/165369bac5c56e5c1fc8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-15T15:57:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：只能用 westd-19183 的 cuda:0 和 cuda:1，不可用其他设备
- `openvla-trained-extract` 在 cuda:0 上仍在跑（PID 27091），**不要 kill**
- untrained checkpoint 路径 `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained/` 是唯一副本，不可删除
- 所有 ρ 比较使用 **per-task mean**（D002 决策），pooled ρ 仅作参考，不用于 gate 判定
- DINO-V2 baseline 阈值是 0.554（per-task mean），不是 0.833（pooled）——D004 勘误

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183（2×RTX PRO 6000），工作目录 `/root/vla-ssd`
- Python：conda base `/root/miniconda3/bin/python`（aml-train 镜像，不用 venv）
- 模型：trained `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b/`，untrained `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained/`
- 数据：`/root/autodl-tmp/vla-ssd/data/libero/libero_10/`（10 tasks × 50 demos × ~250 timesteps）
- 特征：trained → `/root/autodl-tmp/vla-ssd/features/trained/`，untrained → `/root/autodl-tmp/vla-ssd/features/untrained/`（8/10 已完成），dinov2 → `/root/autodl-tmp/vla-ssd/features/dinov2/`（完成，503MB）
- 活跃进程：`openvla-trained-extract` PID 27091 tmux session cuda:0，cron 监控中
- HF cache：`/root/autodl-tmp/.hf_cache`
- transformers 版本 4.57.6（模型期望 4.40.1，trained/untrained 同版本，对比有效）

### 3. 📊 当前状态
**刚做完**：处理 `openvla-untrained-extract` 失败回调。确认 EXIT_CODE=130 是 Worker `fix-extraction-restart` 主动 kill 以修复 I/O 瓶颈（264 次 `.cpu()` → 2 次/batch），非意外失败。已更新 registry notes，已汇报 Director。

**Registry**：
- `openvla-trained-extract` RUNNING cuda:0 — trained 特征提取，cron 确认存活
- `mvp_001` RUNNING — 父实验，追踪整个 MVP 验证
- `dinov2_baseline` DONE/success — per-task mean ρ=0.554, subtask AUC=0.9717
- `openvla-untrained-extract` DONE/failed — Worker 正在修复重启

**等待中的回调**：
- Worker `code:fix-extraction-restart`（turn 15）— 修复 extract_features.py 后重启 untrained 提取剩余 2 tasks（LIVING_ROOM_SCENE6, STUDY_SCENE1），完成后会回调
- Worker `code:control-b-label-permutation` — 编写 Control B cross-trajectory shuffle 代码
- `openvla-trained-extract` cron — trained 提取完成回调

### 4. 📋 待办
- `fix-extraction-restart` Worker 回调 → 确认修复生效 → 用 `submit_training_job` 重新提交 untrained 提取（只跑剩余 2 tasks）→ 新 exp_id 注册到 registry
- `openvla-trained-extract` cron 回调（完成）→ 记录 checkpoint_path/log_path → 状态推进
- trained + untrained 特征全部就绪 → spawn Worker 跑 `train_probes.py`（temporal distance probe 全 33 层）+ Control B shuffle + bootstrap CI → 这是 MVP 判定的最后一步
- Control B Worker 回调 → 验证 shuffle 代码 → 与 probe 训练合并执行
- Probe 结果出来 → 用 `analyze_results.py` 做三分支判定：best_layer per-task mean ρ>0.5 AND Δρ(trained−untrained)>0.1 AND VLA≥0.554
- 判定 PASS → 汇报 Director，推进 Phase 3（hierarchical quality scoring）
- 判定 CONDITIONAL/FAIL → 按 red-section skill 产 Framing 调整提案，禁止自行跑下一步

### 5. 🎯 战略上下文
- **核心假设**：OpenVLA 隐状态编码 task-progress 信息，信号来自训练习得的 task-semantic content 而非 positional shortcut。RoPE 不编码 trajectory timestep（每 timestep 独立 forward pass），所以 positional shortcut 已排除。
- **决策链**：D001（MVP 三分支标准）→ D002（全面切 per-task mean ρ）→ D003（移除 subtask gate）→ D004（DINO 阈值勘误 0.833→0.554）
- **目标会议**：CoRL 2026（abstract May 26, paper May 29）——时间极紧
- **易错点**：
  - 不要混淆 pooled ρ 和 per-task mean ρ——前者被 cross-task variance 膨胀，所有判定用后者
  - `analyze_mvp.py` 已废弃，只用 `analyze_results.py`
  - untrained 提取已有 8/10 完成的 .pt 文件，Worker 修复后只需跑剩余 2 tasks，不要全量重跑
  - trained extraction 日志路径和 mvp_001 日志路径相同（`~/runs/vla-ssd/openvla-trained-extract.log`），这是正常的


---
