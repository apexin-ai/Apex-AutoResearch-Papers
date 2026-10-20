# director / loop_2.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`29c43522c4bdcc4c08c5.json`](../../sessions/29/29c43522c4bdcc4c08c5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-21T14:45:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: westd-34685 cuda:0/1/2/3 + westd-10894 cuda:0/1/2/3，共 8 张。严禁使用白名单外 GPU
- **永久禁止自动 checkpoint 清理**: finetune.py save 时读前序 checkpoint model shards，任何自动删除 = 崩溃 (M021-M026，4 次事故)。只能手动清理，确认不在 save 中才删
- **occ_s1 (resumed from 17500) 已排除 (D013)**: 不可纳入任何 aggregate 指标。occ_s1_fresh 正在从头训练替代
- **save_freq=2500 for occ_s1_fresh**: 必须产出 47500_chkpt。之前 Agent 用了 save_freq=5000 启动（错误），我已发 replace_agent_queue 要求 kill 重启，但 Agent 尚未执行
- **eval 脚本路径**: 必须用 `python vla-scripts/safe_eval.py` 或 `python vla-scripts/evaluate_safelibero.py`，不是 `python evaluate_safelibero.py`（反复出现的路径 bug）
- **47500 是主报告点，50K 是补充**: 50K Frankenstein 标签已撤回（真实训练动态），但 47500 更稳定，论文以 47500 为主

### 2. 🖥️ 基础设施快照
- **westd-34685**: `connect.westd.seetacloud.com:18685`, root, conda env `occsafe`, 工作目录 `/root/occsafe_vla/openvla-oft`
  - 模型: `/root/autodl-tmp/models/openvla-7b`
  - 数据: `/root/autodl-tmp/data/modified_libero_rlds/`
  - OCC 数据: `/root/occsafe_vla/occ_data`
  - Checkpoints: `/root/autodl-tmp/checkpoints/{occ_s0,occ_s1,occ_s1_fresh,occ_s2}/`
  - 磁盘: ~224GB free
  - 活跃进程: occ_s1_fresh PID 480459 (cuda:0, **需要 kill 重启 save_freq=2500**)；cuda:1/2/3 空闲
- **westd-10894**: `connect.westd.seetacloud.com:10894`, root, conda env `occsafe`, 同结构
  - Checkpoints: `/root/autodl-tmp/checkpoints/ablation_{occ_detach,random_occ}_{s0,s1}/`
  - 磁盘: ~200GB free, save_freq=10000
  - 活跃: 4 ablation 训练 (cuda:0/1/2/3, ~24% 进度, ~0.96 it/s)
  - Cron: 4 个 ablation 监控已注册
- **WANDB_MODE=disabled** 所有实验。Cron 误报 EXIT_CODE=1 (torch.distributed cleanup warning) 是已知假阳性

### 3. 📊 当前状态
**刚做完**: MVP gate 正式 FAIL (D013)，3-seed OCC 评估全部完成。发了 replace_agent_queue 综合指令（kill s1_fresh 重启 + 50r eval + 50K 验证），但 **Agent 尚未执行**——这是最紧急的事。

**Registry 状态**:
- mvp_occ_s0/s2: DONE (negative) ✅
- mvp_occ_s1: DONE (conclusion 仍为 "failed"，需改 "negative"，50K metrics 未写入)
- occ_s1_fresh: RUNNING (但 save_freq 错误，需重启)
- 4 ablation: DONE/failed (实际 RUNNING，registry 状态机不允许 DONE→RUNNING，用 notes+cron 追踪)
- mvp_vanilla_s0/s1/s2: DONE (success) ✅

**等待中**:
- Agent 处理综合指令 (kill+restart s1_fresh, 50r eval, 50K 验证, registry 修正)
- Ablation 完成 ~09:30 UTC May 22
- occ_s1_fresh 完成 ~03:00+ UTC May 22 (重启后)

### 4. 📋 待办（条件触发式）
- Agent 回复综合指令执行结果 → 确认 s1_fresh 已用 save_freq=2500 重启 + 50r eval 在跑 + 50K checkpoint 验证结果
- 50K checkpoint 验证完整 → 撤回 Frankenstein 标签，50K 数据升级为正式补充数据
- 50r eval 完成 → 收集 per-task 数据，更新分析脚本
- occ_s1_fresh ~25K 步 → 手动清理 2500-20000 checkpoints (确认不在 save 中)
- Ablation 4 组完成 (~09:30 UTC May 22) → **关键诊断决策点**:
  - detach 有效 (CAR 改善) → 梯度干扰是主因 → cutoff/detach 修复实验
  - random ≈ full → OCC 空间信号本身无用 → 更深层问题
  - 两者均 negative → 考虑 analysis-only (需满足 L1 红线: 2-3 种改进方向 + oracle)
- occ_s1_fresh 完成 → eval 47500+50K → 纯净 3-seed 数据汇总
- cutoff 实验代码已修复 (commit e36e9bd, 指数衰减+cutoff)，脚本已准备 → 等 ablation 诊断后决策是否启动

### 5. 🎯 战略上下文
**核心结论链**: D008(2-seed preliminary FAIL) → D009(gate 标准调整) → D010(tradeoff, 已撤回) → D011(tradeoff 是中间态) → D012(seed 敏感性, 有 resume 混杂) → D013(MVP 正式 FAIL, s1 排除) → D014(GPU 分配: s1_fresh + 50r eval)

**最容易判断错的事**:
1. **不要混合不同 step 的 seed 做 average** — s0/s2 正式数据是 47500，s1 (resumed) 只有 50K，s1_fresh 将有 47500+50K。混合步数平均已被 Reviewer 三次打回
2. **resume ≠ seed 敏感性** — vanilla_s2 也从 35K resume 但正常，所以 occ_s1 的问题是 OCC+resume 组合效应，不能简单说"OCC 放大 seed 敏感性"
3. **T3 CAR 跨 seed 极端方差** (s0=80%, s1=5%, s2=0% at 50K) 是论文级发现，但 20r 的 per-task CI 约 ±21pp，需要 50r 数据验证
4. **cutoff 实验优先级取决于 ablation** — 之前过早准备 cutoff 配置，实际应等 ablation 诊断后再决策。cutoff 代码已修复（weight schedule 混杂已消除），但不要提前启动
5. **Ablation registry 显示 DONE/failed 但实际在跑** — 状态机不允许 DONE→RUNNING，用 notes 和 cron 追踪。不要被 registry 状态误导以为 ablation 已结束


---
