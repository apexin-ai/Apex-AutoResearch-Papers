# SVS Project Memory

## 🔴 D010 根因诊断（2026-05-14，CRITICAL）
- **IC SAT 分支（61% chains）= formalization rate**：`z3_checker.py:120-122` 中 SAT 时 `ic_score = len(formalized) / total_claims`，Z3 是 no-op
- **PCV 未实现**：premises 完全不参与 Z3 验证，solver 只收到 chain claims，不引入题目前提。D006 pivot 设计的 PCV 框架在代码层从未落地
- **fc_score ≡ formalization_rate（r=1.0）**：fc_score 不是 factual consistency，是 formalization rate 的别名
- **Z3 做的是 SAT check（claims 互相矛盾？）而非 validity check（claims 从 premises 可推导？）**
- **80-90% all-SAT 是 trivially SAT**：独立 ground atoms 在 uninterpreted functions 下几乎不可能 UNSAT
- **结论：hypothesis 从未被公平测试，这是实现 bug 不是假设失败**
- Cohen's d = -0.04 的根因是 IC 衡量"LLM 能否输出可解析 FOL"而非"推理是否逻辑一致"

## ✅ D012 Phase 2 集成审查（2026-05-14，代码已就绪）
- **Entailment check 已集成到主管线**，无需额外代码修改即可跑正式实验
- 调用链：`run_mvp.py → scorer.select_answer() → z3_checker.check_entailment() → sandbox.check_entailment()`
- `score_chain()` 已用 `ic_entail`（非旧 ic_score）：`ic_weight * ic_entail + fc_weight * fc_score`
- `evaluate_and_judge()` P2 判定已用 `cv.ic_entail` 做 Cohen's d
- `run_mvp.py` 已对 premises 做 formalization 并传递 `premises_fol`
- **v3 vs 主管线差异**：v3 用 `entailed/total_claims` 合并分母，主管线用 `entailed/formalized` + 独立 `fc_score=formalized/total`（更干净的分离）
- **冗余代码**：旧 `check_internal_consistency()` 仍被调用但结果不参与评分，保留用于 ablation 对比
- **CCLC 仍用 SAT 逻辑**：语义正确（跨链一致性 ≠ entailment），无需修改
- 设计文档：`artifacts/d012_phase2_integration_design.md`
- **feat/entailment-pipeline 分支**（6文件改动，5个dry-run测试全部通过）：z3_checker.py（6元组返回+consistency check）、scoring.py（移除冗余IC调用）、types.py（新增ic_consist字段）、run_mvp.py（P2用ic_entail）、autoformalize.py（处理R1-Distill think标签）、test_entailment_dryrun.py

## ✅ VeriCoT 深度调研（2026-05-14，新颖性风险大幅降低）
- **VeriCoT 确认不做 chain selection**——仅单链验证+串行self-reflection，binary pass/fail
- **Pass rate 极低**：ProofWriter 45%, BioASQ 25%, SARA 15%（vs SVS 85% formalization rate）
- **SVS "Graded IC for chain selection" 是独特贡献**：2023-2026 全景扫描，无人将 formal verification 连续分数用于 inference-time chain ranking
  - VeriCoT/LINC/LOGIC-LM → binary verify
  - PRoSFI/LogicReward → graded reward for training only
  - PC-CoT → binary filter + SC
- **推荐 reframe**（如 entail_001 d>0.15）："Graded Formal Verification as Test-Time Chain Selection"
- **必须做的 ablation**：(1) graded IC vs binary filter+SC (2) graded IC vs SC alone (3) PCV vs LLM-gen premises
- **Reviewer 预期攻击面**：graded vs binary 的信息增益、autoformalization faithfulness、单数据集
- 详细报告：`artifacts/vericot_deep_dive.md`

## 服务器确认（2026-05-14）
- autodl-5090 和 gpu-5090-4x-4 是**同一台机器**（同 hostname、machine-id、IP），SSH config 两个别名
- 后续统一用 autodl-5090 称呼

## Z3 Crash 经验（D008）
- [2026-05-14] Z3 C++ 层对畸形 FOL 表达式可触发 `abort()` → SIGABRT，Python try/except 无法捕获
- threading.Lock 只解决并发安全，不防 SIGABRT——mvp_002 用 Lock 方案仍然 crash
- 解决方案：`z3_sandbox.py` persistent subprocess worker（forkserver context）。所有 Z3 eval() 在子进程执行
- 子进程 crash → 父进程收到 exitcode≠0 → 自动重启 worker → pipeline 继续
- crash test 验证：os.abort() in worker → parent survived → worker restarted → 后续 validation 正常

## 量词 Bug 实证数据
- [2026-05-14] 旧 MVP（mvp_001, killed）日志归档于 `/root/mvp_run_killed_20260514.log`
- V3.2 formalization 系统性 ForAll→Exists 错误：Exists 736 vs ForAll 718
- 这是 IC 全 SAT 的根因之一——Exists(x, Implies(P(x), Q(x))) trivially SAT
- 量词修复后（CRITICAL RULES prompt）：ForAll 93% vs Exists 7%
- 论文 ablation 可用修复前后数据对比
- **⚠️ 量词修复对 Qwen 链无效**：cross-model dryrun 中 pw_563 四条 Qwen 链 IC 全 1.0（all-SAT），说明 CRITICAL RULES prompt 只对 DeepSeek formalization 生效。如果 Qwen 做 formalization（43.26% rate），量词问题会复现。**正式 cross-model 实验必须保持 DeepSeek V3.2 做 formalization。**

## ⚠️ Vacuous Quantification 实证（2026-05-14 Reviewer 发现）
- [2026-05-14] mvp_003 日志中发现：ground fact "the cat eats the bald eagle" → `ForAll([x], Implies(And(Red(x), Round(x)), Eat(cat, bald_eagle)))`
- 简单事实被包装成带条件的全称量化，前件不可满足时 vacuously SAT
- 效果类似量词 bug：人为抬高 IC score，削弱区分力
- 当前 IC 分布有方差 [0.333–0.750]，说明不是全部 claim 都 vacuously SAT
- **mvp_003 完成后必须抽查 10 claim formalization，统计 vacuous quantification 比例，>30% 需加 caveat**

## ⚠️ CRITICAL: IC Label-Dependent Bias（2026-05-14 Reviewer CRITICAL 审查）
- [2026-05-14] mvp_003 中期数据 (n=19): SVS 52.6% vs SC 63.2%，SC 领先 10.5pp
- **机制性偏差**：IC scoring 系统性偏好有明确结论（True/False）的链条。Unknown 链因推理模糊、claim 难形式化而被低估
- **具体表现**：SVS 在 gold=Unknown 时倾向错选 "True"（问题 #9,10,12,16）
- **根因假设**：Unknown 链 formalization rate 可能系统性偏低 → IC 虚低 → SVS 选择了更容易 formalize 的 True/False 链
- **这不是 hypothesis 失败，是 scoring function 可修复的偏差**

## ⚠️ Cross-Model Dryrun 配置错误（2026-05-14 Reviewer 核实）
- [2026-05-14] cross_model_dry_run.json 结果 **INVALID**：Qwen 被用于全部模块（chain gen + formalization），408 次调用全走 Qwen
- 之前汇报"Qwen chain gen + DeepSeek formalization"与实际不符
- Qwen formalization rate 仅 43.26%（P1 FAIL），该 dryrun 不能用于论证跨模型泛化性
- **正式 cross-model 实验修正**：config 中 `formalizer_model` 指向 DeepSeek V3.2 API，`chain_generator` 指向 Qwen vLLM

## Qwen2.5-14B Formalization 能力限制
- [2026-05-14] Dry-run 结果：claim formalization rate 43.26%（目标 50%），premise formalization 100%
- 原因：Qwen 14B formalization 能力弱于 DeepSeek V3.2
- **结论**：正式实验 cross-model 验证时，Qwen 只做 chain generation，formalization 仍走 DeepSeek V3.2 API
- vLLM 部署：cuda:2+3, port 8002, PID 41276, TP=2, max-model-len 4096

## 文献定位策略（2026-05-14 两份调研 + VeriCoT 深度调研综合）
- **最近竞品**：VeriCoT (ICLR 2026, binary Z3 验证, 不做chain selection), VERGE (2026.01, MCS error localization), SSV (IJCAI 2025, Z3 concrete instantiation)
- **SVS 核心差异化（经 VeriCoT 深度调研确认成立）**：(1) IC = graded verifier for chain selection (2) PCV 框架 (3) 实用性（85% vs 15-45%）
- **全景定位**：Binary verify (VeriCoT/LINC/LOGIC-LM/SatLM) → Graded for training (PRoSFI/LogicReward) → Binary filter+SC (PC-CoT) → **Graded for inference-time selection (SVS, 独此一家)**
- **VeriCoT 确认 ICLR 2026 Poster**（arXiv 2511.04662），引用时用 ICLR 2026
- **论文定位**：不说"首次用 FV 检查 CoT"，说"首次将形式一致性检查转化为 graded chain selection 机制 + PCV"
- **与 VERGE 区分**：VERGE 的 MCS 用于 error localization + iterative refinement，SVS 的 IC(MCS) 用于 graded scoring + selection
- **与 SSV 区分**：SSV 验证"formalization 是否正确"，SVS 用 verification score 做"chain selection"
- **autoformalization 风险**：arXiv:2604.19459 发现 axiom fabrication + premise mistranslation 两类系统性 unfaithfulness，对 formalization confidence 设计有启示
- **P0 baselines**：SC, FoVer binary filter+SC, Self-Certainty, ORM for Logical Reasoning
- **必须做的 ablation**：graded IC vs binary filter+SC（VeriCoT风格）、graded IC vs SC alone、PCV vs LLM-gen premises

## Reviewer Novelty 风险点（2026-05-14 文献调研审查，已部分缓解）
- [2026-05-14] **D014 新颖性风险大幅降低**：VeriCoT 深度调研确认其不做 chain selection，SVS graded IC for selection 是 2023-2026 文献中唯一
- [2026-05-14] **VERGE trivial extension 风险**：VERGE 已用 MCS 做 error localization，SVS 将 MCS 转为 graded score 可能被审稿人视为 trivial extension。Post-MVP 需要强化 IC 在 chain selection 场景的独特价值（selection vs refinement 是本质区别）
- [2026-05-14] **PCV vs VeriCoT 区分**：VeriCoT 做 binary Z3 验证，PCV 做 premise-conditioned graded verification。需要实验证明 graded IC 优于 binary filter——**post-MVP 必须有 binary filter vs graded IC ablation**
- [2026-05-14] **影响 experiment plan**：post-MVP 阶段必须设计 ablation 对比 binary filter（FoVer 风格）vs graded IC（SVS），这是回应 reviewer 最可能的攻击面

## ORM Baseline 审查备注（2026-05-14 Director 审查通过）
- [2026-05-14] 推荐方案：LogicReward-Qwen3-8B (⭐⭐⭐) + FoVer-PRM (⭐⭐) + GenRM prompt-based (⭐⭐)，2-3 天完成
- **LogicReward 实际是 LoRA adapter (83MB)**，需基座 Qwen3-8B (~16GB)，已下载到 autodl-5090:/root/autodl-tmp/models/LogicReward-Qwen3-8B/
- **FoVer 两篇论文区分**：FoVer 验证 (TACL 2025) vs FoVer-PRM (ACL 2026 Findings, `ryokamoi/fover`)，引用审计时需区分
- **⚠️ LogicReward 信息泄漏风险**：如果 LogicReward 训练数据包含 ProofWriter/FOLIO，则对比实验存在数据泄漏。实现时必须检查训练集构成
- **论文 positioning**：LogicReward 本质是 SVS 形式验证信号的 learned 版本——需区分 training-free (SVS) vs training-based (LogicReward) 的方法论差异

## 进度核实规范（2026-05-14 Director 三次纠正后确立）
- **硬规则**：更新 mvp_003 进度时，必须直接 `grep -c "gold_label" /root/outputs/results_partial.json` 取数，不引用任何人的口头数字
- 原因：多次进度数据不一致（6→28→10→11→19），各来源在不同时间点取的快照
- 此规则适用于所有未来实验的进度核实

## D012 Entailment Rescoring 中间结果（2026-05-14）
- [2026-05-14] **PID 54002 运行中**，16 问题，~160 min 预计完成
- **4 问题 checkpoint (n=32 chains, 18 correct / 14 wrong)**：
  - ic_score_old Cohen's d = -0.644（wrong > correct，方向错误）
  - ic_entail Cohen's d = **-0.410**（比 old IC 好 36%，但仍为负）
  - ic_consist Cohen's d = -0.558
  - 95% CI 均过零，全部不显著
- **根因**：ProofWriter depth-5 标签分布 61% Unknown，IC 系统性惩罚 Unknown 正确链
- **Entailment 机制验证**：79.6% formalized claims 被 Z3 确认 entailed，非平凡结果
- **发现 formalization 语义错误**：e.g. "chase" → Eat() predicate mismatch
- **关键下一步**：按 gold label 分层分析（True-only / False-only / Unknown-only），验证在 True/False 问题上 hypothesis 是否成立
- **⚠️ 并发实例冲突**：发现并杀掉了第二个实例（PID 60443），它曾覆盖 checkpoint 文件为空

## Post-MVP 待办
- ~~LogiQA/FOLIO 主入口分发~~ → 已修复，`load_problems(dataset=...)` 支持多数据集（下次部署生效）
- [2026-05-14 Reviewer 中期审查] **pw_4572 scoring 问题**：当前 group scoring 中单条高 IC 链可击败多链一致的正确答案组。Research 阶段需在 scoring.py 加 chain count 加权或 min_chains 阈值。mvp_003 不动。
- [2026-05-14 Reviewer 中期审查] **LogiQA 适配**：run_mvp_v6.py 部署前必须修 chain_sampler + metrics.py 支持 A/B/C/D 标签，否则 LogiQA 实验 0% 准确率。config_logiqa.yaml 的 num_problems 改为 651。
- [2026-05-14 Director] **LogiQA 兼容性硬阻塞**：chain_sampler 硬编码 True/False/Unknown 答案格式，LogiQA 是 A/B/C/D 多选格式，完全不兼容。必须先适配 chain_sampler 才能跑 LogiQA 实验。

## 架构决策
- [2026-05-14] 混合推理：chain gen → 本地 14B vLLM (cuda:0+1 TP=2) / formalization → DeepSeek V3.2 API
- [2026-05-14] PCV pivot（D006）：IC 从 internal coherence 升级为 Premise-Conditioned Verification
- [2026-05-14] 量词修复后 IC 本身可能恢复区分力，MVP 结果将同时包含 IC 和 PCV-IC 对比
- [2026-05-14] **Cross-model 架构确认**：Qwen chain gen + DeepSeek formalization，隔离 chain generator 变量
