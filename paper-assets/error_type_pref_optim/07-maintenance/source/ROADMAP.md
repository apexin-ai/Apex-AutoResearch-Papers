# error_type_pref_optim — Research Dashboard

> 最后更新: 2026-05-14 09:40 UTC | 更新原因: 根据 Reviewer 首次审查修正：GPU 规格 96GB Blackwell、Phase B 加多 seed + grid search、Phase A 补充操作定义

## 核心方向
ETADN：根据 agent 错误类型（action/verification/planning）的修正跨度自适应调整 DPO 时间折扣因子 γ，结合渐进式课程训练和类型一致拒绝采样。目标 EMNLP 2026 Findings（ARR DDL: 2026-05-25，剩 11 天）。

## ⚠️ 立项风险
- KILL_triage 评审（19%），novelty 弱 3/3 一致（AP2O+DMPO+AgentDebug 组合推广）
- 拥挤赛道：12+ step-level credit assignment 方法
- 即使 MVP pass，novelty 攻击面仍在 → research 阶段需找 empirical surprise

## 当前进展
- 阶段：MVP 验证（Phase A 进行中）
- 实验：0
- GPU：gpu-6000pro-2, 2 × RTX PRO 6000 Blackwell Server Edition 96GB（cuda:0, cuda:1）
- Agent 状态：执行 Phase A 环境搭建 + 数据收集

## MVP 验证方案

### Phase A — 环境搭建 + 数据收集 + 修正跨度验证（Day 1-2）
- [ ] 克隆 ETO codebase，搭建 ALFWorld 环境
- [ ] 下载 Qwen3-8B，生成 ~200 条 ALFWorld 轨迹
- [ ] 零样本 LLM error classification（action/verification/planning）
- [ ] 测量每类错误的经验修正跨度
- **操作定义**：
  - step 粒度 = agent turn（一次 action + environment response）
  - 对每个 failure step 生成 N=10 correction continuations
  - correction horizon = failure step 到 recovery 的最小 agent turns（across 10 attempts）
  - 多类型重叠 → 按 root cause 归类（planning error 导致的错误 action 归 planning）
- **Pass**: 三类修正跨度 pairwise p<0.05（Mann-Whitney U）

### Phase B — ETADN 信号测试（Day 3-5）
- [ ] 类型一致拒绝采样生成 ~300 DPO pairs
- [ ] 训练 3 个变体 × 3 seeds：(1) ETO trajectory DPO (2) step-level DPO best single-γ (3) ETADN
- [ ] single-γ baseline 必须做 grid search：γ ∈ {0.85, 0.90, 0.95, 0.97}，取最优
- [ ] ALFWorld 134 episodes × 3 seeds，报告 mean ± std + bootstrap 95% CI
- **Pass**: ETADN mean ≥ +3% absolute over best single-γ mean，且 bootstrap CI 不重叠

### Research 阶段入口条件
- MVP Phase A + B 均 pass
- 明确 novelty 增强策略（需发现 empirical surprise，非纯工程组合）

## GPU 预算
- 本地：gpu-6000pro-2 × 2 GPUs（RTX PRO 6000 Blackwell 96GB）
- 96GB VRAM 支持 Qwen3-8B 全参数 DPO，无需 QLoRA
- 云 GPU：暂未申请

## 近期任务
- [ ] Agent 完成 Phase A 环境搭建
- [ ] 完成 ALFWorld 轨迹生成 + 错误分类 + 修正跨度测量
- [ ] Phase A 结果评估后决定是否进入 Phase B

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D001 | 2026-05-14 | MVP 方案：两阶段验证——先验证修正跨度分离，再验证 ETADN 信号 | — |


