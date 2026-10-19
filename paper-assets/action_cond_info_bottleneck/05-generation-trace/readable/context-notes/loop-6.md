# reviewer / loop_6.md

**action cond info bottleneck** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`fec6997b3faf7301f77b.json`](../../sessions/fe/fec6997b3faf7301f77b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-17T17:20:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：只能用 cuda:0 和 cuda:1（`execution.gpu_ids=[0,1]`）
- 服务器：westb-13953，账号 root
- 远程代码根目录：`/root/acib`，checkpoint 存储：`/root/autodl-tmp/`
- baseline 模型路径：`lerobot/smolvla_libero`（HF hub），本地 copy `/root/autodl-tmp/models/smolvla_libero/model.safetensors` 与 HF cache 版本**不同**（max_diff=6.3e-3），训练用的是 HF cache 版本
- eval 基线数据：spatial=66.0%, object=67.8%, goal=76.4%, libero_10=54.2%, avg=66.1%

### 2. 🖥️ 基础设施快照
- 服务器：westb-13953(root)，工作目录 `/root/acib`
- Python：`/root/miniconda3/bin/python3`（直接调用，无 conda activate）
- 模型：`lerobot/smolvla_libero`（0.45B SmolVLA，64 visual tokens）
- Checkpoint v7.2：`/root/autodl-tmp/acib_v7.2_connector_scorer`
- Eval 输出：`/root/autodl-tmp/v72_eval/alpha_{0.0,1.0}_seed1/`
- 活跃进程：
  - PID 40598: v7.2 α=0.0 4-suite eval (GPU 0)
  - PID 44022: v7.2 α=1.0 4-suite eval (GPU 1)
  - 两者 libero_spatial + libero_object 已完成，正在跑 libero_goal 或 libero_10
- tmux session: `v72_seed1`
- W&B：项目未配 W&B（不检查）

### 3. 📊 当前状态
**刚完成**：
- v7.3 LoRA 代码审查 → PASS（228K params，α=0.0 精确恢复 baseline）
- Paper framing 审查 → CRITICAL（story claims "without corrupting policy" 但 v7.2 α=0.0=-6.6pp）
- Related work survey 审查 → WARNING（4 个新竞争者未纳入 framing：VLA-ADP, Compressor-VLA, VLA-Pruner, DeepVision-VLA）
- Eval 脚本兼容性修复审查 → PASS（connector_lora eval 静默丢弃 LoRA 权重 bug 已修复）
- v7.3 lambda_drift=0.0 修复确认

**Registry RUNNING**：
- `acib_v72_eval_alpha00` — 4-suite eval，spatial 59.4% 已出，object 完成，goal/10 进行中
- `acib_v72_eval_alpha10` — 4-suite eval，spatial 61.0% 已出，object 完成，goal/10 进行中

**等待中**：
- v7.2 full eval 完成（预计 ~2-3h），需收集 4-suite pc_success
- v7.3 LoRA 训练待 GPU 释放后启动（eval 占满两卡）
- connector-only ablation 待 GPU 释放后启动

### 4. 📋 待办
- v7.2 eval 完成（grep "pc_success" 出 4 条/log）→ 收集 4-suite 数据，验证 MVP gate（α=1.0 avg ≥ 64%），更新 registry metrics
- v7.3 训练启动 → 审查 GPU 使用、确认 lambda_drift=0.0 生效、确认 LoRA params 在 optimizer 中
- v7.3 训练完成 → 跑 cross_task_probe 验证 Probe A cos < 0.8，跑 eval（α=0.0 应精确=baseline，α=1.0 是新 MVP gate）
- Director 若决定调整 paper framing → 按 negative-framing-review skill 审查新方案
- connector-only ablation 完成 → 验证是否 connector 本身 unfine-tunable（C8 claim 数据）

### 5. 🎯 战略上下文
**核心发现**：SmolVLA action expert 对 connector output 分布极度敏感（0.4% weight shift → -6.6pp）。v7.2 connector+scorer 实现了 spatial conditioning（Probe A PASS）但 MVP gate FAIL（spatial -5pp）。v7.3 LoRA 是当前唯一希望——rank-8 约束 + α=0.0 精确恢复 baseline。

**决策链**：v7 joint training FAIL → v7.1 scorer-only FAIL（无 spatial conditioning）→ v7.2 connector+scorer PARTIAL（conditioning YES，performance NO）→ v7.3 LoRA（pending）

**易错点**：
1. 不要信 registry 中 `libero_spatial_sr: 0.76` — 那是错误的单 task 数据，实际 suite-level 是 59.4%/61.0%
2. 本地 `/root/autodl-tmp/models/smolvla_libero/model.safetensors` 不是训练时加载的权重，对比 connector drift 时用 v7.1 scorer_only checkpoint 的 connector（因为 scorer_only 冻结 connector）
3. paper_framing.md 已过时——基于 v7.2 是"成功方法"的假设写的，但 v7.2 MVP gate 已 FAIL，如果 v7.3 成功则需重写 framing
4. 文献竞争比 framing 显示的更激烈——VLA-ADP / DeepVision-VLA 都做 action-conditioned token selection，ACIB 差异化在于 IB framework + soft gating + robustness goal（非 efficiency）


---
