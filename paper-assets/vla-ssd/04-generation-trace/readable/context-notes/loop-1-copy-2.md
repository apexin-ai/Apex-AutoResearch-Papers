# agent / loop_1.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`929916ef60eaf9a17779.json`](../../sessions/92/929916ef60eaf9a17779.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-15T11:46:37+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-19183 的 cuda:0 和 cuda:1（gpu_ids 白名单）
- AutoDL 每次 SSH 必须 `source /etc/network_turbo` + SSL 证书环境变量，否则网络/下载全挂
- 严禁多进程同时下载同一文件（本 session 已因此浪费 2+ 小时，带宽从 2.5MiB/s 跌到 680KiB/s）
- conda 环境，不是 venv：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 特征/checkpoint/数据全部在数据盘 `/root/autodl-tmp/vla-ssd/`，根分区仅 ~30GB，写根分区=磁盘满
- init_untrained.py 当前运行的 checkpoint 未用固定 seed（已补 seed=42 供将来用），不要重新生成 checkpoint 导致与已提取特征不一致

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183（AutoDL），2×RTX PRO 6000
- 工作目录：`/root/vla-ssd/`（脚本在 `scripts/`）
- Python：`/root/miniconda3/bin/python`，conda base 环境
- OpenVLA trained：`/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b/`（15GB, 3 shards 已验证）
- OpenVLA untrained：`/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained/`（14.3GB, 4 shards, LLM random + Vision preserved）
- DINO-V2：`/root/autodl-tmp/vla-ssd/checkpoints/dinov2-large/`（304.4M params）
- LIBERO 数据：`/root/autodl-tmp/vla-ssd/data/libero/libero_10/`（10 HDF5, 50 demos each, ~250 ts/demo）
- DINO-V2 特征：`/root/autodl-tmp/vla-ssd/features/dinov2/`（503MB, 已完成）
- Trained 特征：`/root/autodl-tmp/vla-ssd/features/trained/`（提取中，4/10 tasks = ~24GB）
- Untrained 特征：`/root/autodl-tmp/vla-ssd/features/untrained/`（提取中，4/10 tasks 同步）
- 活跃 tmux：`openvla-trained-extract` (cuda:0), `openvla-untrained-extract` (cuda:1)
- transformers 版本：4.57.6（模型期望 4.40.1，已记录，对比有效）

### 3. 📊 当前状态
**刚做完**：D001 判定标准校准（ρ 下限 0.3→0.5, bootstrap CI, subtask gate 双条件）。analyze_results.py 已更新。DINO-V2 baseline 已补录 registry (dinov2_baseline, DONE, ρ=0.833)。

**正在做**：
- `worker_code_fix-bootstrap-ci` 正在运行 — 修正 bootstrap CI 采样单元（层→task），同时给 train_probes.py 补 per-task ρ 输出，加 permutation test 备选。**这个 Worker 的回调必须处理**。

**Registry 状态**：
| exp_id | status | 说明 |
|--------|--------|------|
| mvp_001 | RUNNING | 总实验（Phase 2 特征提取中） |
| openvla-trained-extract | RUNNING | cuda:0, ~4/10 tasks |
| openvla-untrained-extract | RUNNING | cuda:1, ~4/10 tasks |
| dinov2_baseline | DONE | ρ=0.833, R²=0.687 |

### 4. 📋 待办（条件触发式）
- `fix-bootstrap-ci` Worker 回调 → 验证 per-task ρ 输出 + permutation test，向 Director 汇报
- 特征提取 cron 回调（trained/untrained 完成）→ 立即双卡并行跑 probe：(1) trained temporal_distance 33 layers, (2) untrained temporal_distance 33 layers, (3) Control B cross-traj shuffle on trained。所有脚本已就绪。
- Probe 结果出来后 → 跑 analyze_results.py 做三分支判定（PASS/CONDITIONAL/FAIL）
- 如果 VLA_ρ < DINO_ρ → 需要 subtask AUC，但 LIBERO HDF5 无 predicate 标注，需 simulator 回放提取。Director 待决策。
- DINO-V2 subtask AUC baseline → 提取完成后优先做（Director 要求，用于校准 subtask gate 阈值）

### 5. 🎯 战略上下文
- **项目核心问题**：OpenVLA 7B 隐状态是否编码 task-progress 信息，信号来自 content 还是 positional shortcut
- **RoPE 已排除**：每个 timestep 独立 forward pass，RoPE 编码 token position 不是 trajectory position，不构成 confound
- **DINO-V2 ρ=0.833 是高 bar**：纯视觉特征已很强（邻近帧相似），VLA 需要展示超越视觉相似性的 task-semantic 编码
- **D001 决策**：PASS 标准已校准，ρ 下限提高到 0.5，bootstrap CI 必须 task-level（不是 layer-level），这是 Reviewer Critical
- **易错点 1**：submit_training_job 的 gpu_ids 是物理卡号，但脚本内 `--gpu 0` 因为 CUDA_VISIBLE_DEVICES 映射。untrained 用 gpu_ids=[1] 但脚本参数是 --gpu 0
- **易错点 2**：特征大小 ~58GB/model，数据盘 220GB 够但别忘了 untrained checkpoint 也占 14GB
- **易错点 3**：extract_features.py 的 untrained 日志显示 mode=trained（默认值），功能正确但审计易混淆，已在 registry notes 记录
- **目标会议**：CoRL 2026，abstract deadline May 26，paper May 29


---
