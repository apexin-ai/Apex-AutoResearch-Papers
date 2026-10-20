# svs_formal_verification — Research Dashboard

> 最后更新: 2026-05-14 15:39 UTC | 更新原因: 修正过时信息：mvp_003=DONE, v3 rescorer 运行状态, GPU 实际状态, 决策树更新

## 核心方向
用 Z3 形式验证作为 graded verifier 替代 self-consistency 多数投票，进行 LLM 逻辑推理的 test-time chain selection。

**核心 pivot（D006→D012）**: IC 从 SAT consistency check 升级为 **claim-level entailment check**（premises ∧ prior_claims ⊢ claim）。原 PCV 设计从未在代码层实现（D010-D012 确认）。

**🔴 D014 新颖性风险**：VeriCoT (ICLR 2026) 已做 autoformalize CoT→FOL→Z3（含 entailment+consistency），在 ProofWriter 上测试。残余差异化：graded scoring + chain selection。等 entailment IC 结果后决定 reframe 方向。

## 当前进展
- **阶段**: MVP 验证——entailment IC 最终测试
- **entail_001 (v3 rescorer)**: RUNNING，PID 76901，5/50 题完成，平均 4.6 min/题，**ETA UTC+8 02:45**
  - V3.2 远程 API formalization（100% 成功率），方法论经 Reviewer 确认正确
  - 这是 entailment-based IC 的首次有效测试（之前 v1/v2/v3 均未产出数据）
- **mvp_003**: DONE (NEGATIVE)，d=-0.37。P1 PASS (84.9%)，P2 FAIL。根因已确认为实现 bug（IC=formalization rate，PCV 未实现），非假设失败。
- **Phase 2 代码预改**: scoring.py 已改为 ic_entail 驱动评分，z3_checker.py entailment 逻辑待集成到主管线
- **基础设施**: autodl-5090 4×RTX 5090 32G
  - cuda:0+1: vLLM server（空转，为 Phase 2 mvp_004 保留）
  - cuda:2+3: 空闲
  - v3 rescorer 用远程 API，不占本地 GPU

## MVP Pass 标准
- P1: formalization 成功率 > 50% ✅ (84.9%)
- P2: entailment IC correct-chain > wrong-chain, Cohen's d > 0.15, 95% CI excludes 0 ⏳

## 决策树（entail_001 完成后）
- **d > 0.15** → Phase 2：修改主管线重跑 50 题 mvp_004。同时走方向 (B) reframe（claim-level entailment + graded selection）
- **0 < d ≤ 0.15** → 按 gold label 分层分析，True/False 子集可能有信号。评估是否换数据集（ProofWriter depth-5 的 61% Unknown 可能是 confound）
- **d ≤ 0 或不显著** → 假设失败。评估方向 (A) 方法论比较研究 或 (C) autoformalization faithfulness pivot

## 近期任务
- [ ] **entail_001 运行中**（ETA UTC+8 02:45）
- [ ] Phase 2 主管线代码预改（feat/entailment-pipeline）
- [ ] v3 进度监控（每 30min）
- [ ] VeriCoT 深入调研（具体实验配置、局限、chain selection 是否涉及）——为 reframe 做准备
- [x] 10q test 残留进程清理
- [x] entail_001 registry 补注册
- [x] mvp_003 完成（NEGATIVE，d=-0.37）
- [x] D010-D012 根因诊断：IC=formalization rate, PCV 未实现

## Post-MVP 待处理
- VeriCoT 发表状态确认（ICLR 2026 已确认）+ 深入对比
- LogiQA 兼容性适配（chain_sampler 硬编码 True/False/Unknown）
- Faithfulness validation 实验设计
- ORM/GenRM baseline 实现
- LogicReward 训练集信息泄漏检查
- Cross-model validation（Qwen chain gen + DeepSeek formalization）
- Vocab 污染修复（constants 中的噪声词）

## GPU 预算
autodl-5090 (= bjb2-35890): 4×RTX 5090 32G
- cuda:0+1: vLLM server 空转（为 mvp_004 保留）
- cuda:2+3: 空闲
- v3 rescorer: 远程 V3.2 API，零 GPU 开销

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D014 | 2026-05-14 | 新颖性自查：VeriCoT (ICLR 2026) 高度重叠，SVS 当前 framing 新颖性不 | mvp_003, D012 |
| D013 | 2026-05-14 | mvp_003 完成 NEGATIVE (d=-0.37, P2 FAIL)。结果符合预期(IC=f | mvp_003 |
| D012 | 2026-05-14 | PCV 未实现确认（premises 未进 Z3）。采用方向 3：claim-level entai | mvp_003, D010, D011 |
| D011 | 2026-05-14 | D010 根因确认：IC=formalization rate(SAT) + noise drown | mvp_003, D010 |
| D010 | 2026-05-14 | CRITICAL: n=24 诊断确认 IC 无区分力(d=-0.04)，启动根因诊断判断是实现问题 | mvp_003 |
| D009 | 2026-05-14 | 文献调研完成：SVS novelty 中等偏上，识别 autoformalization unfai | — |
| D008 | 2026-05-14 | Z3 validate_z3_syntax 需 subprocess 隔离——LLM 畸形 FOL  | mvp_002 |
| D007 | 2026-05-14 | 发现并修复 V3.2 formalization 量词系统性错误（ForAll→Exists），可能 | — |
| D006 | 2026-05-14 | Reviewer 深度审查后确认 IC 全 SAT 退化风险，采纳方向 (b) PCV 作为主方向  | — |
| D005 | 2026-05-14 | 预下载 Qwen2.5-14B-Instruct 作为正式实验第二模型（cross-model va | — |


