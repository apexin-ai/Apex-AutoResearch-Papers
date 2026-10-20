# prism_collapse_mixing — Research Dashboard

> 最后更新: 2026-05-15 16:56 UTC | 更新原因: Reviewer 审查后量化 pass/fail 阈值、增加 2-seed 要求、明确实验细节

## 核心方向
PRISM: 用多分辨率 collapse 信号（output entropy、spectral effective rank、generation diversity）增强 online data mixing（AIOLI/ODM），使混合比在迭代合成训练中能感知 collapse 而非仅追踪 loss。核心科学问题：collapse 信号是否包含 loss 无法捕获的退化信息？

## 当前进展
- **阶段**: MVP 验证
- **服务器**: rtx6000-diagprobe (2× RTX 6000, cuda:0/1)
- **实验**: 无（Agent 正在搭建环境 + 写代码）
- **目标会议**: EMNLP 2026 ARR (DDL 5/25) → ICLR 2027 (~9月)
- **立项评审**: clarity 4.5, feasibility 4, novelty 4, impact 3.5; 出口共识 33%

## MVP 方案

**核心假设**: 在迭代合成训练中，collapse 信号与 loss 脱钩——loss 稳定/改善而 entropy/spectral rank/diversity 下降。

**实验设计**:
- 模型: Pythia-410M-deduped (`EleutherAI/pythia-410m-deduped`)
- 数据: FineWeb (real) + 当代模型自生成 (synthetic)，固定 50/50 混合比
- 迭代: 3 代，每代 ~200M tokens
- Seeds: 2 个独立 seed (42, 137)，分别跑完整 3 代链
- Probe set: FineWeb validation split 中 5000 条 × 256 tokens，与训练集无交集
- 信号计算层: 最后一层 hidden states（与 SIGMA 一致）
- 合成数据: 每代模型自生成（标准 model collapse 设定）

**Pass/Fail 标准（预注册）**:
- ✅ Pass（需同时满足）:
  1. ≥1 个 collapse 信号在 Gen 3 与 loss 的 |Spearman ρ| < 0.5，且 Gen 0-1 时 |ρ| > 0.7
  2. 该信号从 Gen 0 到 Gen 3 单调退化（每代下降），且末代相对首代下降 ≥15%
  3. 以上 pattern 在 2 个 seed 中均观测到
- ❌ Fail: 不满足上述条件 → 前提不成立，项目 pivot 或 kill
- ⚠️ 弱 pass（1 seed 满足另一不满足）→ 追加第 3 seed 确认

**时间估计**: 2× RTX 6000 上 ~2-3 天（含环境搭建、2 seeds × 3 代训练、信号计算）

## 近期任务
- [ ] Agent 搭建服务器环境 + 安装依赖
- [ ] 准备 FineWeb 子集 + probe set（确保与训练集无交集）
- [ ] 实现 collapse 信号计算 pipeline（entropy/spectral rank/distinct-n）
- [ ] Seed 42: Gen 0→1→2→3 训练 + 信号追踪
- [ ] Seed 137: Gen 0→1→2→3 训练 + 信号追踪
- [ ] 跨 seed 分析 loss-signal 相关性，判断 pass/fail

## GPU 预算
- 本地: 2× RTX 6000 (rtx6000-diagprobe, cuda:0/1)
- MVP 预估: ~24-40 GPU 小时（2 seeds）
- 总项目预算: ≤200 H100-hours（需申请云 GPU 进入 research 阶段）

## 立项评审关键担忧（需在 research 阶段回应）
1. Novelty ceiling: "显而易见的工程组合" → 需 Collapse Staging 框架 + Optimality Gap 分析
2. Circularity: PRISM 内部 diversity 信号 vs 评估指标 → 用 embedding-space coverage
3. 理论声明过强 → 降为 "directionally aligned"
4. 实验计划过饱和 → 优先级排序
5. Generation depth 3→5，1B 升级为 full replication

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D009 | 2026-05-16 | MVP-v2 verdict: FAIL（预判）。Gen2 Δρ=+0.0007 触发 D006 负 | mvp_collapse_decoupling_v2 |
| D008 | 2026-05-16 | Gen2 决策门结果：Δρ=+0.001 远低于 D006 的 0.02 门槛，Gen5 扩展不启动 | mvp_collapse_decoupling_v2 |
| D007 | 2026-05-16 | D006 修正：证据框架改为 bootstrap CI + effect size 为主、统计检验为 | mvp_collapse_decoupling_v2 |
| D006 | 2026-05-16 | MVP-v3 预设计：从 Gen3 续跑到 Gen5，pass 标准改为统计检验框架（斜率显著性+b | mvp_collapse_decoupling_v2 |
| D005 | 2026-05-15 | 预判 3 代 MVP 大概率 fail，准备 5 代扩展 contingency，预注册标准不变 | mvp_collapse_decoupling_v2 |
| D004 | 2026-05-15 | D004: 裁定 Condition 2 语义——检查 signal mean 退化，非 |ρ| 退 | — |
| D003 | 2026-05-15 | 维持预注册标准不变，entropy 为 per-example ρ pass/fail 主信号，sp | mvp_collapse_decoupling |
| D002 | 2026-05-15 | MVP 方案细化: 量化 pass/fail 阈值（ρ<0.5 vs >0.7, 退化≥15%），增 | — |
| D001 | 2026-05-15 | MVP 方案确定: Pythia-410M 3代迭代训练，固定50/50混合比，追踪4类信号与los | — |

