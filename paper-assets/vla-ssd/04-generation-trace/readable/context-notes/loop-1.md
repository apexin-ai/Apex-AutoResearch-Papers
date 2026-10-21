# director / loop_1.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`a5dca34b5e17ee89f2f4.json`](../../sessions/a5/a5dca34b5e17ee89f2f4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-15T10:04:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0, cuda:1（westd-19183 分配的 2×RTX PRO 6000）
- OpenVLA 模型路径：`/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b/`，不要碰根分区
- features/ 是 symlink → `/root/autodl-tmp/vla-ssd/features/`，不要删 symlink 重建真实目录
- MVP PASS 判据已更新：Δρ 对照组是 **untrained model**（不是 timestep baseline），三分支判定（PASS/CONDITIONAL/FAIL）
- OpenVLA 下载反复出问题（xet 超时），hf-mirror.com + `HF_ENDPOINT` 才有效，`HF_HUB_DISABLE_XET=1` 对此 repo 无效
- 不要同时开多个进程下载同一文件（之前 4+ 进程竞争导致文件损坏 + 速度暴跌）

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183, `ssh -p 19183 root@connect.westd.seetacloud.com`
- 工作目录：`/root/vla-ssd/`（代码），数据盘 `/root/autodl-tmp/vla-ssd/`（模型/数据/features）
- Python：aml-train 镜像，conda base 环境，`/root/miniconda3/bin/python`
- 模型：OpenVLA 7B `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b/`（3/3 shards 已验证）；DINO-V2 已就绪；untrained checkpoint **尚未生成**（`openvla-7b-untrained/` 不存在）
- 数据：LIBERO-10 全 10 task HDF5 就绪；LIBERO-90 部分下载中
- HF cache：`/root/autodl-tmp/.hf_cache`
- 活跃进程：cuda:0 trained 特征提取（tmux session `openvla-trained-extract`，~15% 进度，~37.8 step/s）；cuda:1 空闲
- DINO-V2 features 已提取完成：`/root/autodl-tmp/vla-ssd/features/dinov2/`，503MB

### 3. 📊 当前状态
- **cuda:0**: OpenVLA trained 特征提取正在跑（task 1/10，15%），预计 4-6h 完成全部 10 task
- **cuda:1**: 空闲 — 我刚发了指令让 Agent 执行 init_untrained.py → untrained 特征提取，但 Agent 还在处理队列，尚未确认启动
- Registry: mvp_001 (PREPARING)
- DINO-V2 probe 已完成：temporal distance ρ=0.833, Oracle ρ=1.0
- 代码全部就绪：extract_features.py, train_probes.py, analyze_results.py, init_untrained.py, extract_dinov2.py
- Reviewer 代码审查的 2 个 bug 已修复（CONDITIONAL 分支 + untrained init 统一为 from_config）
- 等待：Agent 回调确认 untrained 提取启动；trained 提取完成回调

### 4. 📋 待办
- Agent 回调确认 untrained 启动 → 确保 cuda:1 利用率 > 0%；如果 init_untrained 失败 → 诊断并重试
- trained + untrained 特征提取均完成 → 派 Worker 跑 probe 训练（trained/untrained/cross-traj Control B）+ analyze_results.py
- MVP probe 结果出来 → 按三分支判定：
  - PASS（ρ>0.3, Δρ>0.1, VLA≥DINO 或 AUC>0.7）→ complete_mvp() 进入 research
  - CONDITIONAL（Δρ>0.1 但 VLA&lt;DINO 且 AUC<0.7）→ pivot DINO-V2 pipeline + negative finding
  - FAIL（ρ≤0.3 或 Δρ≤0.1）→ 终止
- 如 VLA ≈ DINO-V2（Δρ<0.05）→ 检查 sub-task predicate AUC 是否 >0.7 作为替代 PASS 路径

### 5. 🎯 战略上下文
- 核心假设：VLA 预训练表征编码了 task-progress 信息，可自我打分 demo 质量
- **RoPE 不是混淆因素**（每 timestep 独立 forward pass，RoPE 只编码 sequence 内 token position）→ 这简化了控制实验，也是论文 positive point
- DINO-V2 ρ=0.833 设了高 bar — VLA 必须显著超越纯视觉 baseline。Reviewer 分析了三种场景：远超/微超/不如，只有场景 1（远超）对 CoRL 有力
- Reviewer 提醒：temporal distance probing ≠ quality scoring，VLA 可能在 Stage 2-3 downstream 有优势即使 probing 不如 DINO-V2
- CoRL DDL：abstract May 26, paper May 29。时间紧但 GPU-hours 充足
- 易踩的坑：(1) AutoDL 上 HF 下载必须 `source /etc/network_turbo` + SSL 证书 + `HF_ENDPOINT=hf-mirror.com`；(2) 不要多进程下载同一文件；(3) untrained checkpoint 还没生成，是当前 cuda:1 空闲的原因


---
