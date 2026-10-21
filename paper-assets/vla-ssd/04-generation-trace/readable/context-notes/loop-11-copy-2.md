# agent / loop_11.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_11.md`
- **Structured JSON:** [`4858ddbb8fc0242be6a1.json`](../../sessions/48/4858ddbb8fc0242be6a1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: idle_timeout
updated: '2026-05-22T22:58:46+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-19183 的 cuda:0 和 cuda:1（gpu_ids=[0,1]），其他 GPU 不在白名单
- NORA 只有 Goal+Spatial checkpoint，Object/Long 无 checkpoint（D089），不要尝试跑 NORA Object/Long
- DDL：Abstract 2026-05-26（4天），Paper 2026-05-29（7天），全速推进不留 buffer
- 实验是 probing/分析类（非训练），checkpoint_path 标记为 "N/A (probing experiment)"
- openvla-7b 不是 raw LLM——它有 970K+ OXE action trajectories 预训练，汇报 untrained 时必须说明这点

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183，工作目录 /root/autodl-tmp/vla-ssd/
- Python：/root/miniconda3/bin/python（conda base 环境，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型路径：trained=openvla-7b-finetuned-libero-goal / untrained=openvla-7b（HF cache 在 /root/autodl-tmp/.hf_cache）
- 数据：/root/autodl-tmp/vla-ssd/data/libero/libero_goal/（10 tasks × 10 demos × 50 timesteps）
- 实验输出：/root/autodl-tmp/vla-ssd/results/ 下
- 日志：~/runs/vla-ssd/ 下
- 活跃进程：openvla_spatial_standardized_v1 (PID 594575, cuda:0, tmux session)
- cuda:1 空闲（openvla_goal_standardized_v1 刚跑完）

### 3. 📊 当前状态
**刚做完**：收到 openvla_goal_standardized_v1 的 cron 完成回调，已派 Worker (`worker_analysis_openvla_goal_standardized_v1_20260522T041113`) 去 SSH 分析结果，Worker 尚未回调。

**Registry 状态**：
- `openvla_goal_standardized_v1` — ANALYZING：OpenVLA Goal 标准化 5-phase pipeline（R²/L1/cross-inst/RSA/CF），trained+untrained。Worker 正在分析
- `openvla_spatial_standardized_v1` — RUNNING (PID 594575, cuda:0)：OpenVLA Spatial 标准化 5-phase pipeline，同样 trained+untrained
- `cf_batch_missing_v1` — ANALYZING：batch counterfactual 补跑（untrained CF cells），状态未处理
- `tracvla_spatial_full_v2` — ALLOCATED 但未提交，等 GPU

**等待中**：
- Worker `worker_analysis_openvla_goal_standardized_v1_20260522T041113` 回调
- `openvla_spatial_standardized_v1` cron 完成回调（预计 ~3-4h）
- `cf_batch_missing_v1` 也在 ANALYZING，需要分析处理

### 4. 📋 待办（条件触发式）
- Worker 分析回调到达 → 读分析报告 → update_registry(conclusion=success/negative, metrics) → 更新 report.md → 汇报 Director（带 [资源] 行）→ 标记 3×4 矩阵 OpenVLA Goal 格完成
- openvla_spatial_standardized_v1 cron 回调 → 派 Worker 分析 → 同上流程 → 矩阵 OpenVLA Goal+Spatial 全部完成
- 矩阵 OpenVLA Goal+Spatial 都完成 → 汇报 Director 矩阵接近完整（剩 NORA Spatial untrained CF），激活 Paper Agent
- cuda:1 空闲 → 可以跑 NORA Spatial untrained CF 补跑（~15min）或 tracvla_spatial_full_v2
- cf_batch_missing_v1 需要分析处理（也在 ANALYZING 状态）
- 矩阵全完成 → Paper Agent 按 D095 跨架构 framing 更新论文

### 5. 🎯 战略上下文
- **核心结论**：VLA 微调在三个架构（OpenVLA/Llama-2, TracVLA/Phi-3, NORA/Qwen2.5-VL）上产生一致的 instruction routing 重组——R² exit collapse（architecture-independent）+ L1 attention head specialization（base-model-dependent）
- **D095 framing 升级**：paper_framing.md 已更新为跨架构版本，C2 从单架构观察升级为 3 arch × 4 suite
- **D094 三层级梯度**：VLM base → OXE-pretrained VLA → task-finetuned VLA，openvla-7b 已有强 routing 是关键发现
- **D090 区分**：R² collapse + CF = training-induced（跨架构一致）；L1 heads = base-model-dependent（不同架构不同 pattern）
- **矩阵状态**：9/10 cells 已确认，OpenVLA Goal+Spatial 是最后两个 standardized 补跑
- **易错点**：OpenVLA untrained (openvla-7b) 不是空白模型，OXE 预训练已给它强 routing pattern，分析时要区分 "OXE-pretrained baseline" vs "no training at all"
- **Reviewer RESET 循环问题**：33h+ 未解决，已 escalate 3x Manager 无回音，可能需要绕过


---
