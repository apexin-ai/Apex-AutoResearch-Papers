# reviewer / loop_1.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`619941f2fe163b5fb10b.json`](../../sessions/61/619941f2fe163b5fb10b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-15T10:04:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：cuda:0 + cuda:1（westd-19183 上的 2×RTX PRO 6000 Blackwell）
- 模型/数据/features 必须存放 `/root/autodl-tmp/`（数据盘），根分区只有 ~30GB
- OpenVLA checkpoint 路径：`/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b/`（与 `/root/vla-ssd/checkpoints/openvla-7b/` 是同一目录）
- shard 1 曾多次下载失败/竞争，**首次使用前必须用 `safetensors.safe_open()` 验证文件完整性**
- untrained model 使用 `from_config()` 初始化（不是 xavier_normal_），必须与 `extract_features.py` 保持一致

### 2. 🖥️ 基础设施快照
- 服务器：`westd-19183`，工作目录 `/root/vla-ssd/`
- Python：`/root/miniconda3/bin/python`，conda base 环境（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型：`/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b/`（trained，3 shards ~15GB）
- untrained 模型：**尚未初始化**（`openvla-7b-untrained/` 不存在）
- LIBERO-Long：`/root/autodl-tmp/vla-ssd/data/libero/libero_10/`（10 tasks 全部到位）
- DINO-V2：checkpoint `/root/vla-ssd/checkpoints/dinov2-large/`，features `/root/autodl-tmp/vla-ssd/features/dinov2/`
- 活跃进程：trained 特征提取 PID 27096，tmux session `openvla-trained-extract`，GPU 0，16.4GB VRAM，75% util
- GPU 1 完全空闲
- 无 wandb 配置，无 cron 任务

### 3. 📊 当前状态
**trained 特征提取正在运行**（GPU 0），task 1/10 约 15% 进度，~37 step/s。预计单卡总耗时 ~1-2h（10 tasks）。

**已完成的 baseline**：
- DINO-V2 probe：ρ = 0.833（这是 VLA 需要打败的高 bar）
- Oracle probe：ρ = 1.0

**registry**：mvp_001 状态仍为 PREPARING（Agent 未更新为 RUNNING）

**我刚报告给 Director 的 warning**：GPU 1 空闲，untrained model 未初始化，ROADMAP 计划双 GPU 并行但实际只有一路在跑。

### 4. 📋 待办（条件触发式）
- trained 特征提取完成 → 核实 features/trained/ 目录文件完整性（10 task × H5 文件，每个含 last_preaction + image_mean，shape 维度含 33 layers）
- untrained 初始化完成 → 核实 `from_config()` 方式，确认 vision encoder + projector 保留、LLM 随机初始化
- untrained 特征提取完成 → 核实 features/untrained/ 同样结构
- probe 训练完成 → **核心审查**：读 summary.json，独立执行三分支 MVP 判定：
  - best_layer ρ > 0.3？
  - Δρ(trained − untrained) > 0.1？
  - VLA ≥ DINO-V2 (ρ=0.833) 或 subtask AUC > 0.7？
  - 三者全满足 → PASS；Δρ > 0.1 但第三条不满足 → CONDITIONAL；否则 → FAIL
- Agent 声称 MVP PASS → 交叉验证 registry 数据、检查是否 cherry-picking（只报最好 layer）、确认 cross-trajectory shuffle sanity check（Control B）结果 ρ ≈ 0
- Agent 提 framing 调整 → Read `negative-framing-review.skill.md`，四维度审查

### 5. 🎯 战略上下文
- **核心假设**：VLA 预训练隐状态编码 task-progress → 可做零成本 demo 质量打分。理论基础是 iw-SFT。
- **DINO-V2 ρ=0.833 是关键 bar**：如果 VLA 打不过 DINO-V2（一个冻结的通用视觉模型），novelty 论述很弱。我已向 Director 分析过三种场景的论文策略。
- **RoPE 不是混淆因素**：OpenVLA 对每个 timestep 做独立 forward pass，RoPE 编码 sequence 内 token position 而非 trajectory timestep。这个已解决，不需要 RoPE 控制实验。
- **易错点 1**：不要把 "temporal distance probing ρ 高" 等同于 "quality scoring 能力强"——ρ 测的是 progress tracking，不是 demo 质量区分度。VLA 可能在 probing 上输给 DINO-V2 但在下游打分上赢（因为 VLA 有 action semantics）。
- **易错点 2**：mvp_001 registry 状态一直是 PREPARING，Agent 从未更新过——不要因为 registry 状态就认为实验没在跑，实际进程在 tmux session 里。
- **易错点 3**：之前的 context summary 说 "all 3 shards present"，实际 shard 1 多次下载失败直到本轮才成功——对 Agent 声称的"已完成"要独立 SSH 验证。
- **CoRL 2026**：abstract May 26, paper May 29。GPU-hours 充足，不构成 deadline 风险。


---
