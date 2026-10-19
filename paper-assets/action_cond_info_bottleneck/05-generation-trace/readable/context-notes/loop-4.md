# director / loop_4.md

**action cond info bottleneck** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`62519bfc8629092b98c8.json`](../../sessions/62/62519bfc8629092b98c8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-16T17:28:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westb-13953 的 cuda:0 和 cuda:1，不可用其他 GPU
- 所有训练/eval 输出必须写 `/root/autodl-tmp/`（根分区曾因满崩溃）
- v7 训练使用 `--conditioning_mode concat`（不是 FiLM）——config.py 默认值曾被改为 "film"，必须显式传 concat
- eval_acib.py 必须有 dtype fix（scorer.to(dtype=target_dtype)）+ select_action 中 `_compute_lang_condition` 调用（本轮发现的 critical bug，已修复）
- Constraint C002: cron failed 报告不可直接信任——必须先 ssh_read_only 验证进程存活再行动（已 5 次误报）
- Constraint C003: 启动任何训练前必须 nvidia-smi 确认目标 GPU 无占用

### 2. 🖥️ 基础设施快照
- 服务器：westb-13953 (connect.westb.seetacloud.com), account=root, 2x RTX PRO 6000 Blackwell 96GB
- 工作目录：/root/acib（代码），/root/autodl-tmp/（训练输出+checkpoint+eval 输出）
- Python：/root/miniconda3/bin/python（conda base 环境）
- 数据：/root/autodl-tmp/libero_dataset (273K frames)
- 模型：lerobot/smolvla_libero + lerobot/smolvla_libero_plus (HF cache)
- 活跃进程（handoff 时刻）：
  - PID 46186: buggy/unconditioned seed1 eval, cuda:0, 4 suites 串行（作为 "unconditioned scoring" ablation 数据）
  - PID 104743: **FIXED seed1 eval**, cuda:1, 4 suites 串行（**MVP 判定数据**）
- 预备脚本：/root/acib/scripts/run_acib_on_plus.sh（ACIB-on-plus，dry-run 验证过）
- Checkpoints：/root/autodl-tmp/acib_v7_contrastive/checkpoint-{5000,10000,15000,20000}, /root/autodl-tmp/acib_v7_seed2/checkpoint-{5000,10000,15000,20000}

### 3. 📊 当前状态
v7 双 seed 训练已完成（20000 步，cos≈0.58-0.60）。发现 eval 时 select_action 未调用 _compute_lang_condition 的 critical bug，已修复代码。现在两张卡都在跑 eval：
- cuda:0: buggy eval（unconditioned ablation 数据，让它跑完）
- cuda:1: fixed eval（MVP 判定，刚启动 libero_spatial）

每 suite ~3-4h，4 suites 串行 ≈ 12-14h。首个 MVP 信号（fixed seed1 spatial SR）预计 ~3-4h 后。

Registry 状态不准（acib_v7_contrastive 显示 DONE/failed，实际训练成功且 eval 在跑）。acib_v7_seed2 条目为 RUNNING。

### 4. 📋 待办
- fixed seed1 spatial 结果出来 → 对比 baseline_std spatial=66.0%，如果 > 70% 是强信号
- fixed seed1 全 4-suite 完成 → 计算 avg SR，与 baseline_std avg=66.1% 对比
- SR ≥ 64% + perturbation > baseline+5pp → complete_mvp() 进入 research 阶段
- SR < 64% → MVP fail，需分析原因（是方法问题还是超参问题）
- buggy eval 完成 → 保存结果作为 "unconditioned scoring" ablation 数据点
- fixed seed1 eval 完成后 → 在 cuda:1 启动 fixed seed2 eval（去掉 debug print 后启动）
- MVP pass 后 → 立即启动 ACIB-on-plus (run_acib_on_plus.sh) + contrastive-only ablation (alpha=0, beta=0, lambda_ctr=0.1)
- debug print `[EVAL] Using language conditioning` 需从 acib_policy.py 移除（84K prints/suite 拖慢 eval）

### 5. 🎯 战略上下文
**决策链**：D029（probe 证实 position prior）→ D030（实现 bug）→ D032（v6 conditioning 退化）→ D033（cosine 零梯度）→ D034（log-barrier 有效）→ D035（cron 误报防护约束）

**核心结论**：concat+MLP 架构能产生 condition-dependent output，关键是 loss 设计——log-barrier contrastive 解决了 cosine 在 cos=1 处零梯度问题。FiLM 不需要。

**Reviewer 论文预审结论**：
- Path B（ACIB 提升泛化）为主 claim，Path A（诊断）为 methodology，Path C（互补 data-aug）最强但需 ACIB-on-plus 实验
- 论文生死取决于 eval SR：>71% 有竞争力，64-68% 偏弱，<64% 失败
- 审稿人必问"去掉 IB 只保留 contrastive 行不行？"——contrastive-only ablation 是 must-have
- CoRL abstract DDL: 5/26 (10天), paper DDL: 5/29 (13天)

**易错点**：
1. Registry 状态不可靠（wrapper PID 死亡导致误报），永远 ssh 验证
2. acib_policy.py 的 select_action bug 已修复，但 eval 进程加载的是启动时的��码——修改文件不影响已运行进程
3. 不要在 eval 结果出来前启动 P1-P7 实验（40min 等待 < 错误方向的 GPU 成本）
4. buggy eval 数据仍有价值（unconditioned scoring ablation），不要删
5. 如果有人提 FiLM，当前证据不支持需要它（D034 已确认）


---
