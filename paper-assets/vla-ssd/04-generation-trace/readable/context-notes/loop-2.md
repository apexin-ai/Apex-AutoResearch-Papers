# director / loop_2.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`eb45d1ea8d91acee1a3c.json`](../../sessions/eb/eb45d1ea8d91acee1a3c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-15T14:08:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 `cuda:0` 和 `cuda:1`（westd-19183），配置白名单 `execution.gpu_ids: [cuda:0, cuda:1]`
- 服务器只有 `westd-19183`，SSH host 未在 list_ssh_hosts 中注册（通过 connect.westd.seetacloud.com 连接）
- 根分区仅 ~30GB，所有大文件必须放 `/root/autodl-tmp/vla-ssd/`
- 严格单进程下载（多 Worker 同时下载抢带宽的教训）
- AutoDL 网络：必须 `source /etc/network_turbo` + `HF_HUB_DISABLE_XET=1` + SSL 证书环境变量

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183（connect.westd.seetacloud.com），2×RTX PRO 6000
- 工作目录：`/root/vla-ssd`
- Python/conda：未明确记录，需首次连接探测（可能是 aml-train 镜像的 conda base）
- 模型：OpenVLA 7B（trained + untrained via init_untrained.py，SigLIP ViT-SO400M preserved）
- 数据：LIBERO tabletop，HDF5 格式（含 7-DoF action labels），每 task 特征 ~5.8GB
- W&B：未配置
- 活跃进程：mvp_controlb_untrained + mvp_controlb_trained 在 cuda:0 / cuda:1 上 RUNNING
- Agent 当前正在处理 worker_done 回调（action-prediction-probe-prep worker 完成）

### 3. 📊 当前状态
**阶段**：MVP → 方向探索（原始假设 FAIL，正在寻找新 probing task）

**Registry**：
- `mvp_controlb_untrained` — RUNNING（Control B: shuffled labels, 预期 ρ≈0）
- `mvp_controlb_trained` — RUNNING（Control B: shuffled labels, 预期 ρ≈0）
- 其余 6 个实验全部 DONE（4 success, 2 negative）

**关键结论**：MVP Gate 2 FAIL（Δρ=0.043 << 0.1）。Temporal distance 信号来自 SigLIP vision encoder 而非 VLA 训练。Subtask predicate pivot 也终止（DINO AUC=0.9717，视觉可辨）。

**Agent 正在处理**：action-prediction-probe-prep worker 刚完成（HDF5 action 格式探查），另有文献调研 worker 可能也在进行中。

### 4. 📋 待办（条件触发式）
- Control B 两个实验完成 → 确认 ρ≈0（probe validity null control），关闭 MVP 实验系列
- Action prediction probe 两个 Worker（文献调研 + HDF5 技术设计）都完成 → 评估 action probe 可行性 + story 强度 → 做方向决策
- 方向决策通过 → 设计 MVP-2 实验（action probe: trained vs untrained vs DINO）
- **CoRL go/no-go 决策点**：~May 17-18（abstract DDL May 26，paper May 29，仅剩 11 天）
- 如 action probe 也 FAIL → 需要更根本的 pivot 或考虑 practical pipeline story（VLA ρ=0.95 已足够强做 self-scoring，不管信号来源）

### 5. 🎯 战略上下文
**核心问题**：VLA 预训练表征是否编码了"视觉不可达"的 task-progress 信息？前两个候选（temporal distance、subtask predicate）都因 vision encoder 太强而 FAIL。Action prediction 是第三个候选——预测 next action 需策略知识，vision encoder 天然不擅长。

**决策链**：D001-D004 校准 MVP 判定标准 → D005-D006 DINO baseline 从 0.554 修正为 0.901（采样伪影） → D007 Gate 2 FAIL 确认 → D008 设 48h 决策窗口 → D009 subtask predicate 终止，转 action prediction probe

**最容易判断错的事**：
1. 不要低估 vision encoder 的能力——前两轮 pivot 都栽在"以为 vision 做不到，结果 vision 做得很好"
2. Action probe story 需要精心设计：不是"VLA 能预测 action"（trivial），而是"action knowledge 如何编码在表征中"（层级分布、跨任务泛化、与 vision 的解耦）
3. CoRL DDL 极紧（11 天），如果 action probe 也不 work，要快速决策是走 practical pipeline story 还是放弃 CoRL
4. `paper_framing.md` 和 `experiment_plan.yaml` 尚未创建——仍在 MVP 阶段，不要过早启动 post-MVP kickoff


---
