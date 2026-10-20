---
loop: 1
reason: max_messages
updated: '2026-05-14T10:32:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 autodl-5090 的 cuda:0-3（项目配置白名单），gpu-5090-4x-4 尚未实际使用过
- formalization API: http://47.94.22.126/v1 (DeepSeek V3.2)，API key 在 config_local.yaml 明文（Reviewer 已 flag，非 git repo 暂可接受）
- 代码部署路径是 `/root/svs_pipeline/`（不是 `/root/autodl-tmp/svs_formal_verification/svs_pipeline/`，后者是旧残留）
- premise_formalizer.py 和 autoformalize.py 的 prompt 必须都包含 CRITICAL RULES for quantifiers（6 条规则），缺一个就会量词退化导致 IC 全 SAT
- Z3 eval 必须走 z3_sandbox.py subprocess 隔离，绝不能 in-process eval（SIGABRT 会杀死整个 pipeline）

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090 (connect.bjb2.seetacloud.com:35890, root, SSH key ~/.ssh/id_ed25519)
- 工作目录：`/root/svs_pipeline/`（v5 部署，含 z3_sandbox.py）
- vLLM：PID 12250, cuda:0+1 TP=2, DeepSeek-R1-Distill-Qwen-14B（chain gen 用）
- Qwen2.5-14B-Instruct：`/root/autodl-tmp/models/Qwen/Qwen2.5-14B-Instruct/`（28GB, 完整，post-MVP cross-model 用）
- 旧日志归档：`/root/mvp_run_killed_20260514.log`（量词 bug 实证，论文 ablation 可能用到）
- 活跃：mvp_003 (PID 37622, cron 180s interval)，6/50 完成时 ~6 problems/hr
- 本地 artifacts：`projects/svs_formal_verification/artifacts/svs_pipeline/`

### 3. 📊 当前状态
mvp_003 RUNNING（PID 37622, 50×8=400 chains, ProofWriter depth-5）。handoff 时 6/50 完成，预估总运行 ~8h。Z3 sandbox 稳定无 crash 重启。Formalization rate dry-run 84.95%，ForAll 93%。

Registry: mvp_003 RUNNING；mvp_001 DONE(killed)；mvp_002 DONE(failed, Z3 segfault)。

等待中：mvp_003 cron 回调（完成或失败）；Reviewer PCV SAT 退化风险分析（已 post_to_reviewer，未回）。

### 4. 📋 待办
- mvp_003 cron 回调"完成" → 分析 P1 (formalization rate) + P2 (correct-chain IC vs wrong-chain IC, Cohen's d, CI) → pass 则 complete_mvp() 进入 Research
- mvp_003 cron 回调"失败" → 检查日志，若 Z3 crash 则检查 sandbox 是否正常重启，若其他原因则诊断修复
- P2 PASS → post-MVP kickoff: paper_framing.md → experiment_plan.yaml → dream_simulate("full") → update_roadmap
- P2 FAIL (IC 无区分力) → 检查 entailment checking (z3_checker.check_entailment 已实现但未接入 scoring.py) → 若 entailment 也无效 → analysis pivot 或 kill
- Reviewer PCV 分析回来 → 根据分析调整 MVP 评估策略或补充 ablation 设计
- Research 阶段启动后 → cuda:2+3 部署 Qwen2.5-14B vLLM 跑 cross-model 验证

### 5. 🎯 战略上下文
- 决策链：D001(MVP设计) → D002(50×8) → D003(本地GPU) → D004(API formalization) → D005(Qwen下载) → D006(PCV pivot) → D007(量词修复) → D008(Z3 subprocess隔离)
- 核心 insight：原始 IC（internal consistency）只检查 validity，现代推理模型的错误链往往内部自洽，所以 IC 全 SAT 退化。PCV 加入 premises 检查 soundness 是关键 pivot。
- 易错点1：formalization rate 数字有不一致历史（69.3% vs 77.53% vs 84.95%），不同版本 dry-run 结果，不要混用。mvp_003 的正式数据以最终 report 为准
- 易错点2：`run_mvp.py` 硬编码 `load_proofwriter` 已在本地修复但 mvp_003 部署的是旧版（v5），不影响当前 ProofWriter 运行，但 post-MVP 跑 FOLIO/LogiQA 前需要重新部署
- 易错点3：chain-level 并发本地已改为 4 但 mvp_003 服务器上仍是 2，这是 ETA 比预估长的原因
- 投稿目标：EMNLP 2026 ARR，DDL 5月25日（距今 11 天）
