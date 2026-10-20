# director / loop_3.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`724f3840d8fd9fa909e1.json`](../../sessions/72/724f3840d8fd9fa909e1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-22T18:20:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-34685 cuda:0-3, westd-10894 cuda:0-3，共 8 张，不可用其他服务器/GPU
- Checkpoint rotation 脚本在两台服务器后台运行（westd-10894 PID 991149, westd-34685 PID 151027），KEEP=1，不要手动删 checkpoint 除非确认 rotation 脚本挂了
- **不要杀正常运行的训练进程**（M031 教训：cutoff_s0 被不必要重启 3 次浪费 ~3h GPU）——kill 前必须先检查训练指标是否正常
- **清理 checkpoint 前必须 ls 确认保留哪些**（M030 教训：误删 depth_s0/s1 的 12500_chkpt 导致从头重跑）
- Depth MVP gate 已预注册锁定（paper_framing.md），不可事后修改 pass/fail 阈值
- OCC s2 可能是异常 seed（T4 TSR=0.36, T3 CAR=0.02），Random vs OCC 排序是 preliminary（0.9pp/2-seed vs 3-seed 不对等比较）

### 2. 🖥️ 基础设施快照
- **westd-34685**: connect.westd.seetacloud.com, root, 代码 /root/occsafe_vla, checkpoints /root/autodl-tmp/checkpoints/, 磁盘 350GB total ~240GB free
- **westd-10894**: connect.westd.seetacloud.com, root, 同上路径, 磁盘 250GB total ~125GB free
- Python: /root/miniconda3/bin/python (conda base), 不用 venv
- 模型: /root/autodl-tmp/checkpoints/ 下按实验名组织, 基模型 /root/autodl-tmp/models/openvla-7b
- 训练数据: /root/occsafe_vla/data/
- Eval 脚本: `evaluate_safelibero.py`（正确版），**不要用** `eval_safelibero.py`（M027 buggy）
- Rotation 脚本: /root/checkpoint_rotation.sh（两台服务器各一个，每 300s 扫描）
- 日志: ~/runs/occsafe_vla/{exp_name}.log
- Cron: 8 个实验均有 cron 监控，注意 torchrun wrapper PID vs 实际训练 PID 可能不同（cron 误判来源）

### 3. 📊 当前状态
**8/8 GPU 全满运行**，ETA May 23 20:00-23:30 UTC：

| 实验 | 服务器/GPU | ~进度 | ETA UTC |
|------|-----------|------|---------|
| random_occ_s2 | 10894/cuda:0 | ~46% | ~20:00 |
| detach_s2 | 10894/cuda:1 | ~46% | ~20:00 |
| depth_s2 | 10894/cuda:2 | ~39% | ~20:48 |
| depth_s3 | 10894/cuda:3 | ~39% | ~20:48 |
| cutoff_s0 | 34685/cuda:0 | ~28% | ~23:30 |
| depth_s0 | 34685/cuda:1 | ~32% | ~21:47 |
| depth_s1 | 34685/cuda:2 | ~32% | ~21:48 |
| cutoff_s1 | 34685/cuda:3 | ~32% | ~21:42 |

**论文预写完成**: related_work.tex, method.tex, experiment_setup.tex（引用已修复，0 undefined citation）。Agent 正在写 discussion.tex（机制分析框架，不依赖 depth 数据）。

### 4. 📋 待办（条件触发式）
- random_occ_s2 / detach_s2 训练完成（最先，~20:00 UTC）→ 立即启动 50r SafeLIBERO eval（每个实验用 evaluate_safelibero.py），用释放的 GPU 跑 eval
- **random_s2 eval 出结果** → 锁定 Random 3-seed mean → 这是 Depth MVP gate 的锚点（必须在 depth eval 前锁定）
- **detach_s2 eval 出结果** → 重算 Detach 3-seed 统计显著性（当前 2-seed std=0.001 太小，3rd seed 关键）
- depth_s0/s1/s2/s3 全部完成 → 50r eval → 用预注册 gate 判定 Pass/Fail：bootstrap 95% CI 下界 > 0.780 且 TSR ≥ 0.870
- **Depth Pass** → Path 判定（A/B/C/D，规则在 paper_framing.md）→ 写 Results + 选标题
- **Depth Fail** → 走 Option 4 分析论文（Reviewer 已确认可行），核心贡献 = 梯度流机制分析
- cutoff_s0/s1 完成 → eval → 放入 §4.5 Temporal Dynamics
- discussion.tex Agent 回调 → review 质量

### 5. 🎯 战略上下文
**项目核心发现**（D017 确认）：辅助任务梯度流正则化是 VLA safety 改善的主导机制。Random/OCC > Vanilla > Detach。BEV 空间内容边际正贡献但不显著。

**决策链**：D008(MVP FAIL 进入诊断) → D012(seed 敏感性) → D013(排除损伤 seed) → D015(BEV 有害，已推翻) → D016(checkpoint 修正) → D017(3-seed 确认 BEV 边际正贡献)

**论文方向已定**：Option B 分析论文，3-contribution 结构（C1 梯度流机制 / C2 factorial study design / C3 practical guidelines）。Reviewer 审查通过。paper_framing.md 已更新完整 story arc 和 Results section 结构。

**最容易判断错的事**：
1. Random vs OCC 排序（0.9pp/2-seed）不是定论——random_s2 出来后可能翻转，Path A/D 取决于此
2. OCC 3-seed 中 s2(0.770) 可能是异常 seed，不要基于 OCC mean=0.797 做强 claim
3. Detach 显著性取决于 detach_s2 着陆位置——如果 >0.770 则 p>0.08 不显著，需用 per-task hard-task analysis 作为后盾
4. 磁盘是反复出问题的点（M029/M030），rotation 脚本在跑但要监控，特别是 westd-10894 余量紧
5. cron 对 torchrun 进程有假阳性问题，收到 "实验 failed" 通知先 SSH 检查 nvidia-smi + 日志再决定


---
