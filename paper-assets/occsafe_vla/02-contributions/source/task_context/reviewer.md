---
loop: 10
reason: max_wall_time
updated: '2026-05-28T22:30:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 C001：仅 westd-10894 cuda:0-3 + westd-34685 cuda:0-3，共 8 张。越界进程必须 kill。
- **当前两台服务器 nvidia-smi 均只显示 GPU 0（1/4）**，GPU 1-3 对驱动不可见（/dev/nvidia0-3 设备文件存在）。已 CRITICAL 报 Director，未解决前只有 2 张卡可用。
- DDL 约束 C003：2026-05-28 12:00 UTC（已过）。服务器时间显示 May 29。后续实验需确认 Director 是否延期。
- 论文目标 CoRL 2026，Limitations section 必须在 8 页正文内。

### 2. 🖥️ 基础设施快照
- **westd-10894** (root)：代码 `/root/occsafe_vla/openvla-oft/`，conda env `occsafe`（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe`），数据 `/root/autodl-tmp/data/modified_libero_rlds/`，模型 `/root/autodl-tmp/models/openvla-7b`，checkpoints `/root/autodl-tmp/checkpoints/`
- **westd-34685** (root)：同上路径布局，代码已 git sync（最新 commit: `Add random_occ and occ_bn_eval flags`）
- WANDB_MODE=disabled（所有实验），无 W&B 数据可查
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/`
- 活跃进程：**无**。两台服务器 0 个 GPU 进程，0 个 RUNNING 实验

### 3. 📊 当前状态
**刚完成**：
- 12 个写作 issue 逐条质量审查，12/12 confirmed（含 R1-W21 v1 caveat 修复确认）
- GPU 基础设施审查：两台服务器 6/8 GPU 不可见，已 CRITICAL 报 Director
- lambda CLI param worker + cmd format worker 代码审查（defaults 正确，两台服务器同步）

**Registry**：160 个实验，0 RUNNING。最近完成的关键实验：
- `detach_ln_v2_s2_eval` (Cell 4, seed 44): CAR=0.784, TSR=0.902 ✓
- `detach_ln_v2_s3_eval` (Cell 4, seed 45): CAR=0.778, TSR=0.930 ✓
- 4 个 OOM-killed 实验未重启：`detach_ln_v2_s4`(90% done), `full_occ_bn_v2_s3`, `vanilla_object_s2`, `full_occ_bn_v2_s2`

**待决**：Director 未回复 GPU 失联 CRITICAL 和 DDL 延期问题。有一个 framing 策略讨论请求（p 值显著性 + claim 重心）尚未被 Director 正式决策。

### 4. 📋 待办
- GPU 恢复（nvidia-smi 显示 4 卡）→ 优先检查 `detach_ln_v2_s4` 的 45000_chkpt 是否可 resume（仅差 5000 步）
- 新实验 RUNNING 回调 → 立即 `nvidia-smi` 核查 CUDA_VISIBLE_DEVICES 在 C001 白名单内
- Cell 1 (Full OCC BN) seed expansion 完成 → 重算 ANOVA，检查 p 值是否改善；若仍 >0.05 需关注 framing 是否需调整
- Director 回复 framing 策略（方案 A dual effects vs 方案 B hero result）→ 审查新 framing 是否与实验证据一致
- 任何论文章节提交审查 → 先查 Agent 是否读过 red-section skill（L1 合规），再按 Mode B 审查

### 5. 🎯 战略上下文
- **核心结论**："two additive main effects"——BN+gradient flow 降低 CAR（g=0.78），LN 提供 3.5-4.8pp 优势（g=0.88-1.24），interaction negligible。Spatial content 无可检测效应（v1 only，待 v2 复现）。
- **最强单点对比**：Detach+LN vs Vanilla: g=1.89, CAR 0.802 vs 0.745。这是论文最有力的数字。
- **易判断错的事**：
  1. ANOVA p 值边缘（gradient flow p=0.104, norm p=0.060）——permutation test 已给出更强证据（p_perm=0.050, 0.018）。不要把 parametric p 当唯一判据。
  2. v1 vs v2 数据混淆——factorial cells 全用 v2，supplementary conditions（Random OCC, Depth, Cutoff 系列）用 v1。Content irrelevance 仅在 v1 验证。
  3. 论文声称 "no detectable effect of spatial content"——这是 v1 观察，v2 未复现。审稿人很可能攻击这一点。
  4. report.md 的资源状态过时（声称 4 GPU 空闲，实际只有 1 张可见），不可信赖。
  5. `cohen1988statistical` 和 `wu2018groupnorm` 是 bib orphan entries，未被引用，建议清理。
