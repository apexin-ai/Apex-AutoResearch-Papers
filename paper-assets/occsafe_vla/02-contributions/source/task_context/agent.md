---
loop: 8
reason: idle_timeout
updated: '2026-05-29T10:28:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: `cuda:0, cuda:1, cuda:2, cuda:3`（device id，两台服务器各 4 卡）
- 两台服务器: **westd-10894** 和 **westd-34685**，严禁用其他服务器
- **两台服务器当前 GPU 不可用**——cgroup v2 限制只分配 1 卡，需用户去 AutoDL 控制台重启为 4 卡配置。在用户确认重启前不要尝试提交实验
- 论文已提交 SafeRL Workshop @ RSS 2025（May 28），已 revert 到 paper-final-check 版本（D076）。**不要基于旧的 n=4 数据修改论文**
- 基础模型 `/root/autodl-tmp/models/openvla-7b/model.safetensors.index.json` 曾被 checkpoint save 污染（3-shard→4-shard），**提交新实验前必须先验证/修复此文件**（至少在 westd-10894 上）
- westd-10894 曾因系统 RAM OOM 同时杀 3 个实验——同时跑 3+ 实验时注意内存，建议限制为 2 并发

### 2. 🖥️ 基础设施快照
- **westd-10894**: 4×RTX PRO 6000 98GB，工作目录 `/root/occsafe_vla`，数据盘 `/root/autodl-tmp/`
- **westd-34685**: 同上配置
- Python: `/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 模型: `/root/autodl-tmp/models/openvla-7b/`
- 数据集: `/root/autodl-tmp/libero_datasets/`
- Checkpoints: `/root/autodl-tmp/checkpoints/<exp_id>/`
- 磁盘: westd-10894 最后已知 `/root/autodl-tmp/` 45% 使用率（139G 可用）；westd-34685 未知需探查
- **活跃进程**: 无（全部实验已完成或被杀）
- **Cron**: 无活跃 cron
- **Worker**: 无运行中 worker

### 3. 📊 当前状态
本轮（Loop #8）仅完成了 session-start 初始化并向 Director 汇报。确认 registry 状态：全部 160 实验 DONE，0 RUNNING / 0 PREPARING。写作修复 12/17 完成，剩余 5 个实验类 issue 全部等 GPU。D077 已批准 4 组实验（~220 GPU·h）。

无等待中的 Worker 回调、Cron、或 Director 决策。纯阻塞状态：等用户确认 AutoDL 4 卡重启。

### 4. 📋 待办（条件触发式）
- 用户确认 AutoDL 4 卡重启完成 → SSH 探查两台服务器（GPU 状态、磁盘、model index.json 完整性）→ 修复 index.json → 准备并提交 D077 批准的 4 组实验
- 提交前 → `check_disk_before_experiment` 确认两台服务器磁盘足够
- D077 实验包括：RD2-N1 seed 扩展 n≥5/cell (~60h)、RD2-N2 Random OCC (~40h)、RD2-W4 BN eval mode 消融 (~25h)、RD3-W3 λ₀ sweep (~40h)、R1-C9 v1/v2 mixing (~25h，关联 RD2-N2)
- detach_ln_v2_s4 有 45000_chkpt 可 resume（90% 进度被杀），优先 resume 而非从头跑
- 各实验完成 → on-experiment-done 流程 → 更新论文数据/表格 → 提交第 4 轮审稿

### 5. 🎯 战略上下文
- **核心结论**: Auxiliary spatial supervision 不提升 VLA collision avoidance。两个 additive main effects: (1) BN+gradient flow 有害 (g=0.78)，(2) LN 优于 BN (g=0.88)。ANOVA 交互项为零
- **Framing**: D074 "dual main effects"——从 ordinal interaction 转为两个独立主效应 + practical threshold crossing
- **v1 vs v2 数据不一致**: v1 所有机制证据（gradient collapse, CKA drift）均为 bug 产物。论文以 v2 factorial 为权威数据，v1 不纳入主 claim
- **D076 revert**: 论文被强制 revert 到 paper-final-check 版本（Cell 4 n=3），不要假设论文里已有 n=4 数据
- **易错点**: 不要混淆 v1 和 v2 数据；不要引用已被 Reviewer 驳回的机制解释（capacity competition、BN forward-pass interference）；Cell 1 高方差 (std=0.064) 是 finding 不是 noise
- **目标会议**: 论文头部写 CoRL 2026，但实际已提交 SafeRL Workshop @ RSS 2025，当前是审稿修复阶段
