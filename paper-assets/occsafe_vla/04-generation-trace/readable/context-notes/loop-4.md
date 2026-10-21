# director / loop_4.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`96b547f6e877f432adc0.json`](../../sessions/96/96b547f6e877f432adc0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-22T23:39:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-34685 cuda:0-3, westd-10894 cuda:0-3，共 8 张，不可用其他服务器/GPU
- Checkpoint rotation 脚本在两台服务器后台运行（KEEP=1），不要手动删 checkpoint
- **不要杀正常运行的训练进程**（M031 教训：cutoff_s0 被不必要重启 3 次浪费 ~3h GPU）
- Eval 必须用 `evaluate_safelibero.py`，**不要用** `eval_safelibero.py`（M027 buggy）
- MUJOCO_EGL_DEVICE_ID 使用物理设备号（CUDA_VISIBLE_DEVICES=N → MUJOCO_EGL_DEVICE_ID=N），不是 0（M032 教训）
- Depth MVP gate 已预注册锁定（paper_framing.md），不可事后修改 pass/fail 阈值

### 2. 🖥️ 基础设施快照
- **westd-34685**: connect.westd.seetacloud.com, root, 代码 /root/occsafe_vla, checkpoints /root/autodl-tmp/checkpoints/, 磁盘 ~285GB 可用, eval 环境已验证可用（conda env `occsafe`）
- **westd-10894**: 同上路径, 磁盘 ~214GB 可用, 4 GPU 当前全空闲
- Python: /root/miniconda3/bin/python (conda base 或 conda env occsafe)
- 基模型: /root/autodl-tmp/models/openvla-7b
- 训练日志: ~/runs/occsafe_vla/{exp_name}.log
- Eval 结果: /root/occsafe_vla/artifacts/safelibero_libero_spatial_*.json
- Cron: 所有实验有 cron 监控，torchrun wrapper PID vs 实际训练 PID 可能不同（cron 假阳性来源）

### 3. 📊 当前状态
**westd-34685 4 GPU 训练中（即将完成）**：
| GPU | 实验 | 进度 | ETA UTC |
|-----|------|------|---------|
| cuda:0 | cutoff_s0 | ~92% | ~1h |
| cuda:1 | depth_s0 | ~96% | ~35min |
| cuda:2 | depth_s1 | ~95% | ~37min |
| cuda:3 | cutoff_s1 | ~96% | ~35min |

**westd-10894 4 GPU 全空闲**（ablation s2 eval + depth_s2/s3 eval 均已完成）

**已完成 eval 结果**（本轮新增）：
| 实验 | TSR | CAR | 状态 |
|------|-----|-----|------|
| random_occ_s2 | 0.848 | 0.754 | DONE |
| detach_s2 | 0.624 | 0.748 | DONE（TSR 崩溃，CAR 正常）|
| depth_s2 | 0.860 | 0.758 | DONE |
| depth_s3 | 0.848 | 0.806 | DONE |

**论文预写全部完成**：Introduction/Related Work/Method/Experiment Setup/Results 模板/Discussion/Conclusion 均已写好并经 Reviewer 审查。Results Table 3 per-task 数据已填入（除 Cutoff 和 Depth 4-seed 最终版）。D019-D021 叙事调整已全文同步。

### 4. 📋 待办（条件触发式）
- depth_s0/s1 训练完成（~35min）→ 立即在 westd-34685 上启动 50r eval（用释放的 GPU）
- cutoff_s0/s1 训练完成（~35-70min）→ 立即在 westd-34685 上启动 50r eval
- **depth 4-seed eval 全部完成** → Depth MVP Gate 判定：bootstrap 95% CI 下界 > 0.780 且 TSR ≥ 0.870
  - **Pass** → Path 判定（A/B/C/D，规则在 paper_framing.md）
  - **Fail**（2-seed 初步信号指向 Path B / Fail）→ 确认分析论文路线，Depth ≈ Vanilla = 空间内容无关
- cutoff eval 完成 → 填入 results.tex §4.4 Temporal Dynamics
- 全部数据到齐 → 更新 Table 1/3 为最终版，写 Abstract，移除所有 [PENDING]
- 论文定稿后 → submit_paper_to_review

### 5. 🎯 战略上下文
**核心发现演变（D017→D019→D020→D021）**：
- D017: 梯度流正则化是主导机制（Random > Vanilla > Detach）
- D019: Random 3-seed 降至 0.789，与 Vanilla(0.780) 差距仅 0.9pp 不显著
- D020: Detach CAR=0.746±0.002 极稳定，-3.4pp vs Vanilla 是真信号
- D021: Detach s2 TSR 崩溃(0.624) 但 CAR 正常(0.748)，纳入不排除
- **最终 framing**: "梯度流是防止辅助 head 损害的必要条件"（非"正则化收益"）

**当前 3-seed 排序（CAR）**：OCC(0.797±0.032) ≈ Random(0.789±0.031) ≈ Vanilla(0.780±0.012) >> Detach(0.746±0.002)
**Depth 2-seed 初步**：CAR=0.782±0.034 ≈ Vanilla，指向 Path B

**最容易判断错的事**：
1. Depth MVP gate 2-seed 信号指向 FAIL（TSR=0.854 < 0.870），但 s0/s1 可能改变——等 4-seed 再判
2. Table 1 的 OCC TSR 已从 0.911 修正为 0.894（D018），全文已同步，不要用旧数字
3. 论文 claim 已从"正向正则化"完全转为"防止损害"——所有章节已更新，不要回退到旧 framing
4. Detach s2 TSR=0.624 是纳入的（D021），不是排除的——论文正面披露为补充 finding
5. westd-34685 eval 环境已验证可用，训练完成后直接在原服务器跑 eval，不需要传 checkpoint


---
