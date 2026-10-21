# reviewer / loop_2.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`0f30546c54a533ea81dd.json`](../../sessions/0f/0f30546c54a533ea81dd.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-14T04:11:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 分配：cuda:0 + cuda:1（bjb1-45299），两卡均属本项目，无其他项目共享。当前无 constraints.yaml，但需核对进程 CUDA_VISIBLE_DEVICES 与 registry spec.gpu 一致
- exp_008a/c/d 均为 fixed_dt 模式（gate_fixed_dt=2），curriculum 不生效——不要误判为"curriculum 导致崩塌"（D015 已被代码审计推翻，见 D016/D017）
- paper_framing.md 已创建但尚未经过 Reviewer 正式审查（Director 未转发审查请求）。如果 Director 转发来审，需按 Section 5 章节审查流程走，不是随手 PASS

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299(root)，工作目录 /root/autodl-tmp/event-gated-adaptive-horizon
- Python：/root/miniconda3/bin/python（conda base 环境）
- GPU：2× NVIDIA RTX PRO 6000 Blackwell (97GB each)，每个实验占 ~2.7-4.2GB
- 活跃进程（截至 handoff 时刻）：
  - exp_008a: PID ~106947 (GPU 0), tmux, fixed_dt=2 no_subsample H=15, 跑到 105K
  - exp_008d: PID ~109524 (GPU 0), tmux, fixed_dt=2 subsample_on H=8, 跑到 105K
  - exp_008c: PID ~107026 (GPU 1), tmux, fixed_dt=2 no_subsample H=8, 跑到 105K
- W&B：未配置（本项目不检查 W&B）
- BernoulliST 代码已部署到服务器（networks.py:408-456, models.py 多处集成），exp_008e 待启动

### 3. 📊 当前状态
**刚完成**：审查了 worker_code_bernoulli_st（PASS）、ROADMAP 更新（PASS）、monitor worker（PASS）、paper_framing.md 已读但未正式审查（未收到 Director 审查请求）。

**RUNNING 实验**：
- exp_008a: @55K=487.9, v/e=37.6%，**即将到达 65K 决策点**（B vs B+ 锁定）
- exp_008c: @65K=240.86, plateau 确认，诊断价值已完成
- exp_008d: @35K=146.3, v/e=41.2%（决定性证据），等 45K 确认崩塌复现

**等待**：
- 008a @65K eval → Director 做 B/B+ 最终决策
- 008d @45K eval → 确认 delusional critic 崩塌复现
- 008e dryrun（Agent 正在做 dt_embed_dim=0 验证）
- paper_framing.md 可能的正式审查请求

### 4. 📋 待办（条件触发式）
- 008a @65K ≥450 → 支持 B+（"延迟+减弱崩塌"），C3 claim 升级为 Strong
- 008a @65K <350 → 锁定纯 B，C3 降级为"delays only"
- 008a @65K 350-450 → 灰色地带，看 actor_loss 斜率 + v/e 是否突破 50%
- 008d @45K v/e >50% + eval 加速下降 → 完整复现 exp_006 崩塌模式，D021 因果链最终确认
- Director 转发 paper_framing.md 审查 → 按 Section 5 章节审查流程，特别关注 C2 claim 强度（单 seed 风险）和 R1（单环境）
- exp_008e 启动后 → 监控 BernoulliST gate 的 v/e 比率，特别注意 phase2 后 dt_embedding 训练是否触发同样的 delusional critic

### 5. 🎯 战略上下文
**核心结论链**：D020→D021 闭合了因果链：trained dt_embedding → RSSM 精确预测 dt=2 → imagination 过于乐观 → value 过估（v/e>40%）→ advantage 枯竭 → actor 停止学习 → 崩塌。008c vs 008d 是 smoking gun（同 H=8 同 dt=2，唯一差异 subsample=dt_emb 训练，v/e 19% vs 41%）。

**易错点**：
1. **不要把 008c 的低 eval（~240 vs baseline 950）误判为"失败"**——008c 不崩塌就是成功，低 eval 是 H=8 learning signal reduction 的预期结果（D019），不是 dt=2 的问题
2. **不要用人类工时直觉判断 deadline 风险**——15 天够，核心实验几小时完成，后续是写作密集型
3. **单 seed 是最大审稿风险**——所有析因实验 seed=1。MVP 通过后必须对 008c vs 008d 这个核心 pair 补 2 个 seed。我已在审查中提过，但 Agent/Director 尚未响应
4. **bernoulli_physical_horizon=30 是 no-op**——default imag_horizon=15 + max dt=2 → worst case 29 < 30，mask 永不触发。如果 008e 需要真正的 horizon masking，参数要降低


---
