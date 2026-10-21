# director / loop_2.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`e3392e549323604bb4a8.json`](../../sessions/e3/e3392e549323604bb4a8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-15T21:01:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只有 westd-27271 的 2 张 RTX PRO 6000 96GB（cuda:0, cuda:1），无 gpu_ids 白名单但两卡均归本项目
- G4 gate 已改为绝对阈值（D015）：IMM LED median < 1.0，不再与 baseline 做 relative comparison
- D014 数据准确性规则：所有 metrics 报告必须直接引用 JSON 文件值（文件名 + condition key），禁止手动抄数
- evaluate.py 的 compute_empirical_lipschitz() 必须保存/恢复 training mode（D014 教训，v7.1 因此被 kill）
- baseline eval 使用 random importance scores（torch.rand + deterministic seed）作为 null-hypothesis 对照

### 2. 🖥️ 基础设施快照
- 服务器：westd-27271 (connect.westd.seetacloud.com)，用户 root
- 工作目录：/root/autodl-tmp/importance_margin_vla_compress
- Python 环境：需 SSH 探查确认（aml-train 镜像，大概率 conda base）
- v7 checkpoint：checkpoints/imm_anchor/step_029999（final，30K steps）
- baseline checkpoint：需确认路径（mvp_baseline_v5，已 success）
- v7 eval 结果：eval_results/eval_imm_v7_final.json（500 batches, seed=42）
- v7.2 训练：cuda:0，PID 54978，~15K/30K steps（约 50% 完成，~90min 剩余，可能已完成）

### 3. 📊 当前状态
v7 训练完成（30K steps），D014 Phase 1（v7 final eval 500 batches）已完成。Reviewer 确认 G4 全 PASS（LED 0.134-0.692）。

**未完成的关键任务**：D014 Phase 2-3 baseline eval 未执行（Agent idle 180min 触发 reset）：
- baseline final eval：500 batches（未开始）
- baseline mid-checkpoint eval：step_005000 + step_010000，各 50 batches（未开始）
- analyze_gate.py 最终 gate 报告（依赖上述 baseline 数据）

Registry 状态：
- mvp_imm_anchor_v7：ANALYZING（需更新 conclusion/metrics/gpu_hours）
- mvp_imm_anchor_v7_2：RUNNING cuda:0（eval mode fix + lambda=0.2，SN 稳定）
- mvp_baseline_v5：DONE (success)

### 4. 📋 待办
- Agent reset 完成 → 立即派 Agent 在 cuda:1 跑 D014 Phase 2-3（baseline final 500 batches + mid-checkpoint step_005000/step_010000 各 50 batches）+ 运行 analyze_gate.py 生成 gate 报告
- Gate 报告出来 → 4 个 gate 全 PASS → complete_mvp() 进入 research 阶段；任一 FAIL → 评估是否调参/换策略
- v7.2 训练完成回调 → 与 v7 对比（lambda=0.2 vs 0.5），决定哪个配置用于 research 阶段
- Reviewer LED 右偏 warning → 论文 framing 需声明 certified bound 覆盖率（~50% at eps0.05），不能暗示全局保证

### 5. 🎯 战略上下文
核心假设：IMM 训练增大 importance margin Δ_k，使 token compression 在扰动下保持 top-k 稳定性。

v7 数据信号积极：margin_median=0.574（vs baseline random ~0.005），preservation=91.2%@eps0.01，LED 全 < 1.0。**但 G1/G2/G3 需要 baseline eval 才能正式判定**——这是当前唯一阻塞项。

易错点：
- eps0.05 preservation 仅 60.7%，baseline random 理论值 ~50%，G2 (+10pp) 在该条件下可能刚好踩线或不过——不要提前宣布 PASS
- LED 分布严重右偏（mean 远大于 median），用 median 是 D012/D015 决策，但论文不能回避 mean 的问题
- 决策链：D007(gate#3 放宽≤1.10) → D012(LED 用 median) → D013(v7 Lipschitz spike 不 kill) → D014(eval mode fix + gate 评估协议) → D015(G4 绝对阈值)


---
