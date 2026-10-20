# research rohingya realdata feasibility

**ec hte codex a** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_rohingya_realdata_feasibility_20260531T155858.log`
- **Structured JSON:** [`00f42ec2d0c63c89c4af.json`](../../sessions/00/00f42ec2d0c63c89c4af.json)

## Before a recorded user message

56 recorded events

### Log line

_source line 1_

Reading additional input from stdin...

---

### Runtime record

_source line 2_

```json
{
  "type": "thread.started",
  "thread_id": "019e7ecb-2773-7ac3-8186-b1cea1eec962"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "turn.started"
}
```

---

### Runtime record

_source line 4_

```json
{
  "type": "item.completed",
  "item": {
    "id": "item_0",
    "type": "agent_message",
    "text": "先读取项目 brief、roadmap 和现有 memory，确定 `C_REALDATA_FEASIBILITY` 在当前 matrix 里的口径；同时检查 artifacts/注册机制，避免把调研结果写到错误位置。"
  }
}
```

---

### Runtime record

_source line 5_

```json
{
  "type": "item.started",
  "item": {
    "id": "item_1",
    "type": "command_execution",
    "command": "/bin/bash -lc \"rg --files -g 'PROJECT_BRIEF*' -g 'ROADMAP.md' -g 'memory.md' -g 'ideas.md' -g 'report.md' -g '*matrix*' -g 'findings.md'\"",
    "aggregated_output": "",
    "exit_code": null,
    "status": "in_progress"
  }
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "item.completed",
  "item": {
    "id": "item_1",
    "type": "command_execution",
    "command": "/bin/bash -lc \"rg --files -g 'PROJECT_BRIEF*' -g 'ROADMAP.md' -g 'memory.md' -g 'ideas.md' -g 'report.md' -g '*matrix*' -g 'findings.md'\"",
    "aggregated_output": "ROADMAP.md\nexperiment_matrix.lock\nideas.md\nreport.md\nexperiment_matrix.yaml\nmemory.md\ndocs/PROJECT_BRIEF.md\nlogs/workers/worker_gpu_exp_002_prepare_pending_matrix_v2_20260531T155012.log\nlogs/workers/worker_code_exp_001_bias_bound_mvp_matrix_v2_20260531T155006.log\n",
    "exit_code": 0,
    "status": "completed"
  }
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "item.started",
  "item": {
    "id": "item_2",
    "type": "command_execution",
    "command": "/bin/bash -lc \"find . -maxdepth 3 -type f | sed 's#\"'^./##'\"' | rg -i 'brief|roadmap|memory|matrix|artifact|config|registry|findings'\"",
    "aggregated_output": "",
    "exit_code": null,
    "status": "in_progress"
  }
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "item.completed",
  "item": {
    "id": "item_2",
    "type": "command_execution",
    "command": "/bin/bash -lc \"find . -maxdepth 3 -type f | sed 's#\"'^./##'\"' | rg -i 'brief|roadmap|memory|matrix|artifact|config|registry|findings'\"",
    "aggregated_output": "docs/PROJECT_BRIEF.md\ndream_registry.lock\nlogs/workers/worker_code_exp_001_bias_bound_mvp_matrix_v2_20260531T155006.log\nlogs/workers/worker_gpu_exp_002_prepare_pending_matrix_v2_20260531T155012.log\nexperiment_matrix.yaml\nmemory.md\n.venv/bin/numpy-config\nregistry.yaml\nROADMAP.lock\nexperiment_matrix.lock\nartifacts/research/baseline_protocol_20260531.md\nartifacts/manifest.yaml\nregistry.lock\nROADMAP.md\n",
    "exit_code": 0,
    "status": "completed"
  }
}
```

---

### Runtime record

_source line 9_

```json
{
  "type": "item.started",
  "item": {
    "id": "item_3",
    "type": "mcp_tool_call",
    "server": "agent-ml-research",
    "tool": "read_project_file",
    "arguments": {
      "project": "ec_hte_codex_a",
      "file": "memory.md",
      "max_chars": 12000
    },
    "result": null,
    "error": null,
    "status": "in_progress"
  }
}
```

---

### Runtime record

_source line 10_

```json
{
  "type": "item.completed",
  "item": {
    "id": "item_3",
    "type": "mcp_tool_call",
    "server": "agent-ml-research",
    "tool": "read_project_file",
    "arguments": {
      "project": "ec_hte_codex_a",
      "file": "memory.md",
      "max_chars": 12000
    },
    "result": {
      "content": [
        {
          "type": "text",
          "text": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/ec_hte_codex_a/memory.md\", \"content\": \"# Memory\\n\\n## 项目定位\\nEC-HTE 研究目标是纠正 LLM 生成的分类 effect modifier 中的差异性误分类对 CATE/HTE 估计造成的结构性偏差。首要可证伪机制是：当 subgroup misclassification rate 与真实 subgroup CATE magnitude 正相关时，单一全局 confusion-matrix correction 会系统性 under-correct 高误差/高效应 subgroup，并 over-correct 低误差/低效应 subgroup，因此可能比 uncorrected 更差。\\n\\n## 执行约束\\n`PROJECT_BRIEF.md` 同步存在于本项目 `docs/PROJECT_BRIEF.md`。项目配置绑定 `seetacloud-38274/root/cuda:0`；2026-05-31 Director 已确认 `list_available_gpus` 可见该 GPU，型号为 NVIDIA RTX PRO 6000 Blackwell Server Edition，显存约 98GB。GPU 实验仍必须只使用白名单 `cuda:0`，并在启动前记录 server、GPU 型号、driver、命令、数据路径与 seed。\\n\\n## 领域参考\\n\\n### HTE/CATE 标准评测协议\\n\\n- Honest causal forest: Wager & Athey (JASA 2018; arXiv:1510.04342, https://arxiv.org/abs/1510.04342; DOI page https://www.tandfonline.com/doi/abs/10.1080/01621459.2017.1319839) 给出用于 CATE/HTE 的 causal forest 和推断框架；honesty/sample splitting 是其核心推断条件。EC-HTE 的 causal-forest baseline 应固定 honesty 开启，并报告 CI coverage 与 CI width，避免只报点估计误差。\\n- GRF implementation reference: `grf::causal_forest` 文档说明 causal forest 用于估计 tau(X)，并提示 accurate confidence intervals 通常需要比 prediction 更多 trees；同时把 honesty 定义为 subsample splitting。来源：https://grf-labs.github.io/grf/reference/causal_forest.html。实现时需记录 `num.trees`、`honesty`、`honesty.fraction`、seed、train/test split。\\n- CATE benchmark caution: Curth, Svensson, Weatherall & van der Schaar, \\\"Really Doing Great at Estimating CATE?\\\" NeurIPS D&B 2021（https://openreview.net/forum?id=FQLzQqGEAH；PDF https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/file/2a79ea27c279e471f4d180b08d62b00a-Paper-round2.pdf）指出常见 semi-synthetic CATE benchmark 和单一 metric 可能偏向特定算法，因此 EC-HTE 必须同时报告 pointwise、group-level 和 inference metrics，而不是只报告 PEHE。\\n- PEHE / root-PEHE: Shalit, Johansson & Sontag, ICML 2017（https://proceedings.mlr.press/v70/shalit17a.html；arXiv:1606.03976）沿用 ITE/CATE 估计误差评测；本项目定义为 `sqrt(mean_i((tau_hat_i - tau_i)^2))`，仅用于 synthetic/semi-synthetic 中 ground-truth tau_i 已知的设置。项目 brief 已列 PEHE 为主指标。\\n- GATE: Group Average Treatment Effect 是预先定义 subgroup 内的平均处理效应，DoubleML 文档定义为 `E[Y(1)-Y(0)|G=1]`（https://docs.doubleml.org/tutorial/stable/lectures/L3/heterogeneity.html）；Stata 19 CATE 文档也把 GATE/GATES 作为 IATE/CATE 的 group-level summaries（https://www.stata.com/stata19/cate/）。本项目 GATE RMSE 定义为 `sqrt(mean_g((tau_hat_g - tau_g)^2))`，用于 k 个真实 subgroup CATE 已知的 simulation。\\n- Replication / split reporting: 项目 brief 明确半合成实验使用 `R >= 200` replications、`N in {2000, 5000, 10000}`、expert budget `B in {100, 500, 1000, 2000}`、subgroup count `k in {3, 6}`、treatment assignment `T ~ Bernoulli(0.5)`。这些是首批实验的默认规模来源；任何缩小版只能标为 smoke/MVP，不写成正式结论。\\n\\n### LLM annotation debiasing 与适用边界\\n\\n- PPI: Angelopoulos, Bates, Fannjiang, Jordan & Zrnic, Science 2023 / arXiv:2301.09633（https://arxiv.org/abs/2301.09633；Science DOI https://www.science.org/doi/10.1126/science.adi6000）将少量 gold labels 与大量 ML predictions 结合，为 means、quantiles、linear/logistic regression coefficients 等 population parameters 构造有效 CI。本项目可把 PPI 作为 ATE / population regression coefficient correction baseline；不能直接声称它修正 misclassified categorical effect modifier 下的 subgroup CATE，除非把每个 subgroup estimand 单独建模并处理 subgroup membership error。\\n- DSL: Egami, Hinck, Stewart & Wei, NeurIPS 2023 / arXiv:2306.04746（https://arxiv.org/abs/2306.04746）针对 CSS 中 LLM/surrogate labels 的 downstream statistical analysis，使用 gold-standard labels 与 controlled sampling probability 来获得 asymptotic unbiasedness 和 uncertainty quantification。适合作为 downstream regression/ATE-style estimand 的 debiasing baseline；不自动解决 effect modifier 本身被错分导致的 CATE conditioning error。\\n- DSL/PPI finite-sample benchmark: Audinet de Pieuchon et al., EMNLP 2025（ACL Anthology https://aclanthology.org/2025.emnlp-main.1000/；arXiv:2506.09627）比较 DSL 与 PPI 在有限 expert labels 下的 LLM-based parameter estimate debiasing；结论范围是 population parameters / regression coefficients / causal effects 的 debiasing，不是 CATE modifier misclassification correction。可引用为为什么首批实验需要固定 expert budget curves。\\n- StratPPI: Fisch et al., NeurIPS 2024（https://proceedings.neurips.cc/paper_files/paper/2024/hash/c9fcd02e6445c7dfbad6986abee53d0d-Abstract-Conference.html；arXiv:2406.04291）通过 stratified sampling 缩窄 PPI CI，尤其当 autorater performance across conditional distributions varies。EC-HTE 可把 StratPPI 作为 ATE/population mean 的 stratified correction baseline，或作为 expert allocation 思路来源；不能把它当成 categorical modifier confusion-matrix correction，除非 correction estimand 明确改成每个 subgroup 的 gold-label estimand。\\n- Active Statistical Inference / AM-PPI: Zrnic & Candès, ICML 2024 Active Statistical Inference（https://arxiv.org/abs/2403.03208；ICML page https://icml.cc/virtual/2024/poster/34504）用 model uncertainty 主动选择 gold labels 并构造有效 CI；Brawand et al., AM-PPI arXiv:2605.08429（https://arxiv.org/abs/2605.08429）扩展为多 predictor、per-instance routing、residual uncertainty sampling。可作为 Stage 3 allocation baseline/灵感；其原始目标是 population mean monitoring/valid CI，不直接修 CATE conditioning variable 的 misclassification。\\n- Mozer difference-estimator view: Mozer, arXiv:2603.19160（https://arxiv.org/abs/2603.19160）指出 PPI mean estimator 等价于 survey sampling difference estimator，并讨论 differential prediction error for subgroup estimands such as ATE。项目中的 \\\"arm-specific rectifier\\\" baseline 应仅实现为 treatment/control arm 内各自估计 LLM-vs-expert residual/confusion correction，然后估计 ATE/GATE；它仍然是 arm-level/population-level rectification，不能代替 subgroup-specific modifier confusion correction。\\n- Ashwin real-data motivation: Ashwin, Chhabra & Rao, Sociological Methods & Research 2025, DOI 10.1177/00491241251338246（publisher page https://journals.sagepub.com/doi/10.1177/00491241251338246；Maastricht record https://cris.maastrichtuniversity.nl/en/publications/using-large-language-models-for-qualitative-analysis-can-introduc-2/）用 Rohingya/Bengali host interviews 说明 LLM coding errors are not random with respect to respondent characteristics。World Bank summary explicitly names refugee status, gender, education as non-random error correlates（https://documents1.worldbank.org/curated/en/099348304162431121/pdf/IDU1271bc2541c5e8144f51b8cc1be231f985cc6.pdf）。本项目 real-data validation 只用于验证 differential misclassification pattern，不用于声称真实 CATE accuracy。\\n\\n### Measurement error / categorical misclassification correction baselines\\n\\n- Global confusion matrix correction: 从 expert validation subset 估计单一 `P(Z_hat | Z)` 或 inverse matrix，把所有 subgroup 共用同一 misclassification mechanism。来源对应 epidemiology 中 matrix / inverse matrix correction for misclassification；见 Lyles et al. extended matrix/inverse matrix method with internal validation data（PMC https://pmc.ncbi.nlm.nih.gov/articles/PMC4382468/）。本项目必须报告当 subgroup-specific error differs 时 global correction 的 under/over-correction。\\n- Per-subgroup confusion matrix correction: 在每个 true or pilot-estimated subgroup g 内估计 `C_g = P(Z_hat | Z, g)`，再做 correction。该 baseline 是 EC-HTE 的 non-pooled comparator；高方差风险来自每组 expert labels 少。来源是同一 validation-data misclassification framework；partial pooling 是本项目新增稳定化层，不能把 independent per-subgroup correction 写成已有 EC-HTE 结果。\\n- Arm-specific correction: treatment/control arm 内分别估计 confusion/residual correction，模拟 Mozer/PPI arm-level rectifier 对 ATE 的处理。适用 ATE 或 arm-specific mean outcome/label correction；不能直接修正 \\\"which subgroup is the unit conditioned on\\\" 的 modifier misclassification，除非同时对 subgroup-specific `C_{g,t}` 做建模。\\n- SIMEX categorical approximation: Kuchenhoff, Mwalili & Lesaffre, Biometrics 2006（PubMed https://pubmed.ncbi.nlm.nih.gov/16542233/）把 SIMEX 扩展到 discrete covariate/response misclassification，通过 transition matrix Pi 增加误分类并外推到无误分类。EC-HTE 可实现为 categorical transition-matrix SIMEX + causal forest baseline；必须标记为近似 baseline，因为项目目标变量是 categorical effect modifier，而 classic SIMEX 更自然地服务 regression parameter correction。\\n- Calibration/probability modifier baseline: 用 expert validation subset 做 Platt scaling / temperature scaling 或 Dirichlet/multinomial calibration，把 LLM hard label 改成 calibrated class probabilities，再作为 soft modifier features 输入 CATE estimator。该实现只校准 predicted probabilities；如果 downstream CATE 仍按 hard subgroup 分层，它不会消除 subgroup membership error。概率校准作为一般 ML practice 可参考 Niculescu-Mizil & Caruana, ICML 2005（https://dl.acm.org/doi/10.1145/1102351.1102430），但 EC-HTE 需在 artifact 中记录 calibration loss 和 subgroup confusion recovery，而非只报 predictive accuracy。\\n\\n## 首批实验协议\\n\\n### 统一评测输出\\n\\n- 每个 experiment/config/replication 输出：seed、N、k、B、misclassification severity、CATE values、misclassification-CATE correlation direction、method、PEHE、per-subgroup CATE bias、GATE RMSE、95% CI empirical coverage、mean/median CI width、bound diagnostic product、runtime、artifact path。指标来自项目 brief；PEHE/GATE 定义见上方领域参考。\\n- 正式 simulation 默认：`R >= 200` replications、`N in {2000, 5000, 10000}`、`B in {100, 500, 1000, 2000}`、`k in {3, 6}`、`T ~ Bernoulli(0.5)`。来源：PROJECT_BRIEF.md Validation Design。\\n- Smoke/MVP 可以只跑 `N=2000`、`k=3`、少量 replications，但必须标注为 smoke/MVP，不得进入定量结论。来源：项目内部工程约束；正式规模仍以 brief 为准。\\n\\n### 实验矩阵建议\\n\\n| 实验 | 目标 | Metrics | Baselines | 最小样本规模 | 预计运行成本 |\\n|---|---|---|---|---|---|\\n| MVP / Stage 0 bias-bound mechanism | 验证 positive misclassification-CATE correlation 下 global correction 可 worse than uncorrected | per-subgroup CATE bias, GATE RMSE, bound diagnostic product; optional PEHE | uncorrected, global confusion matrix, oracle/stratified subgroup correction | 正式最小 `N=2000`, `k=3`, `R>=200`; smoke 可低于此但仅作工程检查。来源：brief `N`/`k`/`R` | CPU-only 低成本；GPU 非必要 |\\n| Stage 1 partial pooling | 验证 hierarchical/partial-pooling confusion matrices 在小 B 下优于 global 与 per-subgroup independent | confusion recovery error, PEHE, GATE RMSE, subgroup CATE bias, budget curve | global, per-subgroup independent/no pooling, hierarchical partial pooling, oracle confusion | `N in {2000,5000}` 起步，`B in {100,500,1000,2000}`, `k in {3,6}`, `R>=200`。来源：brief | CPU 中等；VI 可本地跑，MCMC 只做 appendix representative configs。来源：brief Stage 1 VI/MCMC 描述 |\\n| Stage 2 CI | 验证 Stage 1 nuisance uncertainty 未传播时 CI under-cover；比较 sandwich/boot/naive | 95% empirical coverage, CI width, GATE RMSE, PEHE | naive causal forest CI, sandwich-adjusted CI, bootstrap CI | `N in {2000,5000,10000}`, `B in {500,1000,2000}`, `R>=200`。来源：brief | CPU 中到高；bootstrap 是主要成本来源，GPU 非必要 |\\n| Stage 3 allocation | 比较 adaptive expert annotation allocation 是否优于 uniform | PEHE at fixed B, GATE RMSE, subgroup bias, confusion uncertainty, annotation allocation share | uniform, misclassification-uncertainty-only, CATE-magnitude-only, joint criterion, pilot ratios 10/20/30% | `B in {100,500,1000,2000}`, pilot ratios `10%,20%,30%`, `R>=200`。来源：brief Stage 3 ablation | CPU 中等；多 budget/pilot sweep 带来配置数成本 |\\n| Real-data misclassification validation | 在 Rohingya interview corpus 验证 differential misclassification，并测试 leave-expert-out confusion recovery | subgroup error-rate gaps, confusion recovery error, calibration loss, budget curve; 不报真实 CATE accuracy | global confusion, per-subgroup independent, partial pooling, calibration/probability modifier | expert-label subsampling budget 复用 `B in {100,500,1000,2000}`；subgroups: refugee status/gender/education。来源：brief + Ashwin et al. 2025 / World Bank summary | 数据访问/清洗成本中等；不需要 GPU；若 transcripts 不可公开，artifact 只记录 aggregate metrics |\\n\\n### Baseline 实现规范\\n\\n- 所有 correction methods 使用同一 expert label budget B、同一 validation split、同一 random seed list；PPI/DSL/StratPPI/ASI/AM-PPI 类方法只作为 ATE/population-parameter 或 allocation baselines，若用于 CATE 必须明确每个 subgroup estimand 的定义与 membership-error 处理。\\n- Global/per-subgroup/SIMEX/calibration baselines 都必须输出 estimated confusion matrix 或 transition matrix；没有 matrix recovery 输出的 run 不用于判断 EC-HTE 机制。\\n- Arm-specific rectifier 只能解释 arm-level residual correction 效果；如果它在 GATE/CATE 上失败，不写成 PPI/Mozer 失效的泛化结论，只写成 \\\"arm-level correction does not address modifier misclassification in this DGP\\\"。\\n- Real-data Rohingya validation 的结论边界：只验证 LLM coding errors 是否随 respondent characteristics 差异化、以及 partial pooling 是否更好恢复 subgroup-specific error patterns；由于缺少自然 causal ground truth，不报告 PEHE/GATE RMSE 作为真实 causal accuracy。\\n\\n## 执行事件记录\\n\\n- [2026-05-31] `worker_research_baseline_protocol_ec_hte_20260531T153440` 被系统标记为 faile\\n\\n... [截断: 省略 283 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 12283, \"truncated\": true}, \"error\": null, \"metadata\": {}}"
        }
      ],
      "structured_content": {
        "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/ec_hte_codex_a/memory.md\", \"content\": \"# Memory\\n\\n## 项目定位\\nEC-HTE 研究目标是纠正 LLM 生成的分类 effect modifier 中的差异性误分类对 CATE/HTE 估计造成的结构性偏差。首要可证伪机制是：当 subgroup misclassification rate 与真实 subgroup CATE magnitude 正相关时，单一全局 confusion-matrix correction 会系统性 under-correct 高误差/高效应 subgroup，并 over-correct 低误差/低效应 subgroup，因此可能比 uncorrected 更差。\\n\\n## 执行约束\\n`PROJECT_BRIEF.md` 同步存在于本项目 `docs/PROJECT_BRIEF.md`。项目配置绑定 `seetacloud-38274/root/cuda:0`；2026-05-31 Director 已确认 `list_available_gpus` 可见该 GPU，型号为 NVIDIA RTX PRO 6000 Blackwell Server Edition，显存约 98GB。GPU 实验仍必须只使用白名单 `cuda:0`，并在启动前记录 server、GPU 型号、driver、命令、数据路径与 seed。\\n\\n## 领域参考\\n\\n### HTE/CATE 标准评测协议\\n\\n- Honest causal forest: Wager & Athey (JASA 2018; arXiv:1510.04342, https://arxiv.org/abs/1510.04342; DOI page https://www.tandfonline.com/doi/abs/10.1080/01621459.2017.1319839) 给出用于 CATE/HTE 的 causal forest 和推断框架；honesty/sample splitting 是其核心推断条件。EC-HTE 的 causal-forest baseline 应固定 honesty 开启，并报告 CI coverage 与 CI width，避免只报点估计误差。\\n- GRF implementation reference: `grf::causal_forest` 文档说明 causal forest 用于估计 tau(X)，并提示 accurate confidence intervals 通常需要比 prediction 更多 trees；同时把 honesty 定义为 subsample splitting。来源：https://grf-labs.github.io/grf/reference/causal_forest.html。实现时需记录 `num.trees`、`honesty`、`honesty.fraction`、seed、train/test split。\\n- CATE benchmark caution: Curth, Svensson, Weatherall & van der Schaar, \\\"Really Doing Great at Estimating CATE?\\\" NeurIPS D&B 2021（https://openreview.net/forum?id=FQLzQqGEAH；PDF https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/file/2a79ea27c279e471f4d180b08d62b00a-Paper-round2.pdf）指出常见 semi-synthetic CATE benchmark 和单一 metric 可能偏向特定算法，因此 EC-HTE 必须同时报告 pointwise、group-level 和 inference metrics，而不是只报告 PEHE。\\n- PEHE / root-PEHE: Shalit, Johansson & Sontag, ICML 2017（https://proceedings.mlr.press/v70/shalit17a.html；arXiv:1606.03976）沿用 ITE/CATE 估计误差评测；本项目定义为 `sqrt(mean_i((tau_hat_i - tau_i)^2))`，仅用于 synthetic/semi-synthetic 中 ground-truth tau_i 已知的设置。项目 brief 已列 PEHE 为主指标。\\n- GATE: Group Average Treatment Effect 是预先定义 subgroup 内的平均处理效应，DoubleML 文档定义为 `E[Y(1)-Y(0)|G=1]`（https://docs.doubleml.org/tutorial/stable/lectures/L3/heterogeneity.html）；Stata 19 CATE 文档也把 GATE/GATES 作为 IATE/CATE 的 group-level summaries（https://www.stata.com/stata19/cate/）。本项目 GATE RMSE 定义为 `sqrt(mean_g((tau_hat_g - tau_g)^2))`，用于 k 个真实 subgroup CATE 已知的 simulation。\\n- Replication / split reporting: 项目 brief 明确半合成实验使用 `R >= 200` replications、`N in {2000, 5000, 10000}`、expert budget `B in {100, 500, 1000, 2000}`、subgroup count `k in {3, 6}`、treatment assignment `T ~ Bernoulli(0.5)`。这些是首批实验的默认规模来源；任何缩小版只能标为 smoke/MVP，不写成正式结论。\\n\\n### LLM annotation debiasing 与适用边界\\n\\n- PPI: Angelopoulos, Bates, Fannjiang, Jordan & Zrnic, Science 2023 / arXiv:2301.09633（https://arxiv.org/abs/2301.09633；Science DOI https://www.science.org/doi/10.1126/science.adi6000）将少量 gold labels 与大量 ML predictions 结合，为 means、quantiles、linear/logistic regression coefficients 等 population parameters 构造有效 CI。本项目可把 PPI 作为 ATE / population regression coefficient correction baseline；不能直接声称它修正 misclassified categorical effect modifier 下的 subgroup CATE，除非把每个 subgroup estimand 单独建模并处理 subgroup membership error。\\n- DSL: Egami, Hinck, Stewart & Wei, NeurIPS 2023 / arXiv:2306.04746（https://arxiv.org/abs/2306.04746）针对 CSS 中 LLM/surrogate labels 的 downstream statistical analysis，使用 gold-standard labels 与 controlled sampling probability 来获得 asymptotic unbiasedness 和 uncertainty quantification。适合作为 downstream regression/ATE-style estimand 的 debiasing baseline；不自动解决 effect modifier 本身被错分导致的 CATE conditioning error。\\n- DSL/PPI finite-sample benchmark: Audinet de Pieuchon et al., EMNLP 2025（ACL Anthology https://aclanthology.org/2025.emnlp-main.1000/；arXiv:2506.09627）比较 DSL 与 PPI 在有限 expert labels 下的 LLM-based parameter estimate debiasing；结论范围是 population parameters / regression coefficients / causal effects 的 debiasing，不是 CATE modifier misclassification correction。可引用为为什么首批实验需要固定 expert budget curves。\\n- StratPPI: Fisch et al., NeurIPS 2024（https://proceedings.neurips.cc/paper_files/paper/2024/hash/c9fcd02e6445c7dfbad6986abee53d0d-Abstract-Conference.html；arXiv:2406.04291）通过 stratified sampling 缩窄 PPI CI，尤其当 autorater performance across conditional distributions varies。EC-HTE 可把 StratPPI 作为 ATE/population mean 的 stratified correction baseline，或作为 expert allocation 思路来源；不能把它当成 categorical modifier confusion-matrix correction，除非 correction estimand 明确改成每个 subgroup 的 gold-label estimand。\\n- Active Statistical Inference / AM-PPI: Zrnic & Candès, ICML 2024 Active Statistical Inference（https://arxiv.org/abs/2403.03208；ICML page https://icml.cc/virtual/2024/poster/34504）用 model uncertainty 主动选择 gold labels 并构造有效 CI；Brawand et al., AM-PPI arXiv:2605.08429（https://arxiv.org/abs/2605.08429）扩展为多 predictor、per-instance routing、residual uncertainty sampling。可作为 Stage 3 allocation baseline/灵感；其原始目标是 population mean monitoring/valid CI，不直接修 CATE conditioning variable 的 misclassification。\\n- Mozer difference-estimator view: Mozer, arXiv:2603.19160（https://arxiv.org/abs/2603.19160）指出 PPI mean estimator 等价于 survey sampling difference estimator，并讨论 differential prediction error for subgroup estimands such as ATE。项目中的 \\\"arm-specific rectifier\\\" baseline 应仅实现为 treatment/control arm 内各自估计 LLM-vs-expert residual/confusion correction，然后估计 ATE/GATE；它仍然是 arm-level/population-level rectification，不能代替 subgroup-specific modifier confusion correction。\\n- Ashwin real-data motivation: Ashwin, Chhabra & Rao, Sociological Methods & Research 2025, DOI 10.1177/00491241251338246（publisher page https://journals.sagepub.com/doi/10.1177/00491241251338246；Maastricht record https://cris.maastrichtuniversity.nl/en/publications/using-large-language-models-for-qualitative-analysis-can-introduc-2/）用 Rohingya/Bengali host interviews 说明 LLM coding errors are not random with respect to respondent characteristics。World Bank summary explicitly names refugee status, gender, education as non-random error correlates（https://documents1.worldbank.org/curated/en/099348304162431121/pdf/IDU1271bc2541c5e8144f51b8cc1be231f985cc6.pdf）。本项目 real-data validation 只用于验证 differential misclassification pattern，不用于声称真实 CATE accuracy。\\n\\n### Measurement error / categorical misclassification correction baselines\\n\\n- Global confusion matrix correction: 从 expert validation subset 估计单一 `P(Z_hat | Z)` 或 inverse matrix，把所有 subgroup 共用同一 misclassification mechanism。来源对应 epidemiology 中 matrix / inverse matrix correction for misclassification；见 Lyles et al. extended matrix/inverse matrix method with internal validation data（PMC https://pmc.ncbi.nlm.nih.gov/articles/PMC4382468/）。本项目必须报告当 subgroup-specific error differs 时 global correction 的 under/over-correction。\\n- Per-subgroup confusion matrix correction: 在每个 true or pilot-estimated subgroup g 内估计 `C_g = P(Z_hat | Z, g)`，再做 correction。该 baseline 是 EC-HTE 的 non-pooled comparator；高方差风险来自每组 expert labels 少。来源是同一 validation-data misclassification framework；partial pooling 是本项目新增稳定化层，不能把 independent per-subgroup correction 写成已有 EC-HTE 结果。\\n- Arm-specific correction: treatment/control arm 内分别估计 confusion/residual correction，模拟 Mozer/PPI arm-level rectifier 对 ATE 的处理。适用 ATE 或 arm-specific mean outcome/label correction；不能直接修正 \\\"which subgroup is the unit conditioned on\\\" 的 modifier misclassification，除非同时对 subgroup-specific `C_{g,t}` 做建模。\\n- SIMEX categorical approximation: Kuchenhoff, Mwalili & Lesaffre, Biometrics 2006（PubMed https://pubmed.ncbi.nlm.nih.gov/16542233/）把 SIMEX 扩展到 discrete covariate/response misclassification，通过 transition matrix Pi 增加误分类并外推到无误分类。EC-HTE 可实现为 categorical transition-matrix SIMEX + causal forest baseline；必须标记为近似 baseline，因为项目目标变量是 categorical effect modifier，而 classic SIMEX 更自然地服务 regression parameter correction。\\n- Calibration/probability modifier baseline: 用 expert validation subset 做 Platt scaling / temperature scaling 或 Dirichlet/multinomial calibration，把 LLM hard label 改成 calibrated class probabilities，再作为 soft modifier features 输入 CATE estimator。该实现只校准 predicted probabilities；如果 downstream CATE 仍按 hard subgroup 分层，它不会消除 subgroup membership error。概率校准作为一般 ML practice 可参考 Niculescu-Mizil & Caruana, ICML 2005（https://dl.acm.org/doi/10.1145/1102351.1102430），但 EC-HTE 需在 artifact 中记录 calibration loss 和 subgroup confusion recovery，而非只报 predictive accuracy。\\n\\n## 首批实验协议\\n\\n### 统一评测输出\\n\\n- 每个 experiment/config/replication 输出：seed、N、k、B、misclassification severity、CATE values、misclassification-CATE correlation direction、method、PEHE、per-subgroup CATE bias、GATE RMSE、95% CI empirical coverage、mean/median CI width、bound diagnostic product、runtime、artifact path。指标来自项目 brief；PEHE/GATE 定义见上方领域参考。\\n- 正式 simulation 默认：`R >= 200` replications、`N in {2000, 5000, 10000}`、`B in {100, 500, 1000, 2000}`、`k in {3, 6}`、`T ~ Bernoulli(0.5)`。来源：PROJECT_BRIEF.md Validation Design。\\n- Smoke/MVP 可以只跑 `N=2000`、`k=3`、少量 replications，但必须标注为 smoke/MVP，不得进入定量结论。来源：项目内部工程约束；正式规模仍以 brief 为准。\\n\\n### 实验矩阵建议\\n\\n| 实验 | 目标 | Metrics | Baselines | 最小样本规模 | 预计运行成本 |\\n|---|---|---|---|---|---|\\n| MVP / Stage 0 bias-bound mechanism | 验证 positive misclassification-CATE correlation 下 global correction 可 worse than uncorrected | per-subgroup CATE bias, GATE RMSE, bound diagnostic product; optional PEHE | uncorrected, global confusion matrix, oracle/stratified subgroup correction | 正式最小 `N=2000`, `k=3`, `R>=200`; smoke 可低于此但仅作工程检查。来源：brief `N`/`k`/`R` | CPU-only 低成本；GPU 非必要 |\\n| Stage 1 partial pooling | 验证 hierarchical/partial-pooling confusion matrices 在小 B 下优于 global 与 per-subgroup independent | confusion recovery error, PEHE, GATE RMSE, subgroup CATE bias, budget curve | global, per-subgroup independent/no pooling, hierarchical partial pooling, oracle confusion | `N in {2000,5000}` 起步，`B in {100,500,1000,2000}`, `k in {3,6}`, `R>=200`。来源：brief | CPU 中等；VI 可本地跑，MCMC 只做 appendix representative configs。来源：brief Stage 1 VI/MCMC 描述 |\\n| Stage 2 CI | 验证 Stage 1 nuisance uncertainty 未传播时 CI under-cover；比较 sandwich/boot/naive | 95% empirical coverage, CI width, GATE RMSE, PEHE | naive causal forest CI, sandwich-adjusted CI, bootstrap CI | `N in {2000,5000,10000}`, `B in {500,1000,2000}`, `R>=200`。来源：brief | CPU 中到高；bootstrap 是主要成本来源，GPU 非必要 |\\n| Stage 3 allocation | 比较 adaptive expert annotation allocation 是否优于 uniform | PEHE at fixed B, GATE RMSE, subgroup bias, confusion uncertainty, annotation allocation share | uniform, misclassification-uncertainty-only, CATE-magnitude-only, joint criterion, pilot ratios 10/20/30% | `B in {100,500,1000,2000}`, pilot ratios `10%,20%,30%`, `R>=200`。来源：brief Stage 3 ablation | CPU 中等；多 budget/pilot sweep 带来配置数成本 |\\n| Real-data misclassification validation | 在 Rohingya interview corpus 验证 differential misclassification，并测试 leave-expert-out confusion recovery | subgroup error-rate gaps, confusion recovery error, calibration loss, budget curve; 不报真实 CATE accuracy | global confusion, per-subgroup independent, partial pooling, calibration/probability modifier | expert-label subsampling budget 复用 `B in {100,500,1000,2000}`；subgroups: refugee status/gender/education。来源：brief + Ashwin et al. 2025 / World Bank summary | 数据访问/清洗成本中等；不需要 GPU；若 transcripts 不可公开，artifact 只记录 aggregate metrics |\\n\\n### Baseline 实现规范\\n\\n- 所有 correction methods 使用同一 expert label budget B、同一 validation split、同一 random seed list；PPI/DSL/StratPPI/ASI/AM-PPI 类方法只作为 ATE/population-parameter 或 allocation baselines，若用于 CATE 必须明确每个 subgroup estimand 的定义与 membership-error 处理。\\n- Global/per-subgroup/SIMEX/calibration baselines 都必须输出 estimated confusion matrix 或 transition matrix；没有 matrix recovery 输出的 run 不用于判断 EC-HTE 机制。\\n- Arm-specific rectifier 只能解释 arm-level residual correction 效果；如果它在 GATE/CATE 上失败，不写成 PPI/Mozer 失效的泛化结论，只写成 \\\"arm-level correction does not address modifier misclassification in this DGP\\\"。\\n- Real-data Rohingya validation 的结论边界：只验证 LLM coding errors 是否随 respondent characteristics 差异化、以及 partial pooling 是否更好恢复 subgroup-specific error patterns；由于缺少自然 causal ground truth，不报告 PEHE/GATE RMSE 作为真实 causal accuracy。\\n\\n## 执行事件记录\\n\\n- [2026-05-31] `worker_research_baseline_protocol_ec_hte_20260531T153440` 被系统标记为 faile\\n\\n... [截断: 省略 283 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 12283, \"truncated\": true}, \"error\": null, \"metadata\": {}}"
      }
    },
    "error": null,
    "status": "completed"
  }
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "item.started",
  "item": {
    "id": "item_4",
    "type": "mcp_tool_call",
    "server": "agent-ml-research",
    "tool": "read_project_file",
    "arguments": {
      "project": "ec_hte_codex_a",
      "file": "ROADMAP.md",
      "max_chars": 12000
    },
    "result": null,
    "error": null,
    "status": "in_progress"
  }
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "item.completed",
  "item": {
    "id": "item_4",
    "type": "mcp_tool_call",
    "server": "agent-ml-research",
    "tool": "read_project_file",
    "arguments": {
      "project": "ec_hte_codex_a",
      "file": "ROADMAP.md",
      "max_chars": 12000
    },
    "result": {
      "content": [
        {
          "type": "text",
          "text": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/ec_hte_codex_a/ROADMAP.md\", \"content\": \"# ROADMAP\\n\\n> 最后更新: 2026-05-31 15:53 UTC | 更新原因: 量化 H1/exp_002 判据并新增 H2 partial-pooling claim\\n\\n## 项目目标\\n\\nEC-HTE 的内部研究目标是验证并实现一套面向 LLM 分类 effect modifier 误分类的 HTE/CATE 纠偏流程。最终产出是技术报告、可复现实验包和可部署代码，不走会议论文提交流程。\\n\\n核心问题：当 LLM 注释误分类率在 subgroup 间不同，并且误分类强度与真实 CATE/HTE 结构相关时，使用单一全局 confusion matrix 的纠偏可能放大 subgroup CATE bias，甚至比不纠偏更差。\\n\\n## 当前主线 Hypothesis\\n\\nH1: 在 misclassification rate 与真实 subgroup CATE magnitude 正相关的 DGP 中，全局 confusion-matrix correction 会 under-correct 高误差/高效应 subgroup，并 over-correct 低误差/低效应 subgroup，因此 GATE RMSE 可能高于 uncorrected。\\n\\nH2: subgroup-specific correction 能降低 H1 暴露的结构性偏差；当 expert label budget 较小时，partial pooling 会比 per-subgroup independent confusion matrix 更稳健。\\n\\nH3: naive CI 会低估 Stage 1 misclassification estimation uncertainty；sandwich 或 bootstrap variance adjustment 能改善 subgroup CATE coverage。\\n\\nH4: adaptive expert annotation allocation 应优先投向 misclassification uncertainty 与 CATE magnitude 同时较高的 subgroup，在固定预算下优于 uniform allocation。\\n\\n## Operational 判据\\n\\n`exp_001_bias_bound_mvp`：唯一 primary metric 是 GATE RMSE；mean subgroup CATE bias 与 max subgroup CATE bias 是 secondary diagnostics；最低 200 replications。\\n\\nH1 success for exp_001：在 positive-correlation high-misclassification/high-CATE-heterogeneity 设置中，`oracle_global - uncorrected` 的 GATE RMSE 差值大于 0，且 bootstrap 95% CI lower bound > 0。`estimated_global` 单独报告；`estimated_global - oracle_global` 用于量化 finite-sample confusion-estimation noise。如果 GATE RMSE 支持 H1 但 secondary bias diagnostics 方向相反，标记 mixed，先 Director 复核再推进 Stage 1。\\n\\nH1 negative for exp_001：如果 positive-correlation worst-case 中 oracle global 不劣于 uncorrected，则 H1 暂不支持；下一步先审计 DGP construction、correction algebra、metric definitions、subgroup weighting，而不是推进 Stage 1。\\n\\n`exp_002_gpu_dgp_grid`：primary metric 是 `global_worse_rate_difference_positive_minus_negative`；secondary metrics 是 `bias_bound_vs_global_worse_spearman` 与 `estimated_global_minus_oracle_global_gate_rmse`；每个 condition 最低 200 replications。\\n\\nH1 success for exp_002：positive-correlation conditions 的 oracle-global-worse rate 至少比 negative-correlation controls 高 20 percentage points，且 bootstrap 95% CI lower bound > 0；bias-bound diagnostic 对 oracle-global-worse conditions 的 Spearman rho >= 0.50，且 bootstrap 95% CI lower bound > 0。estimated-global 结果必须与 oracle-global 分开报告。\\n\\nH2 success for Stage 1：low expert-label budget 下，partial pooling 在 GATE RMSE 上优于 global correction，`partial_pooling_minus_global` bootstrap 95% CI upper bound < 0；相对 per-subgroup independent correction 满足 5% relative GATE RMSE non-inferiority。PEHE 和 mean subgroup CATE bias 是 secondary diagnostics。\\n\\n## 短期计划\\n\\n1. 完成 `exp_001_bias_bound_mvp` CPU-only 半合成 MVP simulation，验证 H1。必跑对照为 uncorrected、oracle global confusion correction、estimated global confusion correction、stratified/subgroup correction；必须拆开结构性 global-correction 偏差与 finite-sample confusion-estimation noise。\\n2. `exp_002_gpu_dgp_grid` 只能在 PENDING 审批、QUEUED、Director GPU allocation 后启动。GPU 实验必须使用项目白名单 `seetacloud-38274/root/cuda:0`，并在 spec 中记录 command、server、GPU 型号、driver、data_path/data_count、seed、disk estimate、expected runtime、log/checkpoint/artifact 路径。\\n3. 建立统一评测协议：GATE RMSE、subgroup CATE bias、PEHE、CI coverage、CI width、bound tightness。所有指标必须能追溯到 registry exp_id。\\n4. 维护 `experiment_plan.yaml` 与 experiment matrix 映射：H1 claim、H2 claim、Stage 0 DGP grid、Stage 1 correction ablation、real-data feasibility 均必须有 plan entry 和 target/cell 映射。\\n5. 并行检查 real-data validation 可行性：Rohingya corpus 字段、LLM annotation、expert label source、subgroup variables、可用 split 与复现实验权限；未确认前不把 real-data 写成已完成结果。\\n\\n## Experiment Plan / Matrix 映射\\n\\n当前最低覆盖目标：\\n- `plan_001_h1_cpu_mvp` → `C_H1_GLOBAL_CORRECTION_WORSE`, `T_STAGE0_DGP_GRID`, registry `exp_001_bias_bound_mvp`。\\n- `plan_002_h1_gpu_dgp_grid` → `C_H1_GLOBAL_CORRECTION_WORSE`, `T_STAGE0_DGP_GRID`, registry `exp_002_gpu_dgp_grid`。\\n- `plan_003_stage1_correction_ablation` → `C_PARTIAL_POOLING_BETTER_LOW_BUDGET`, `T_STAGE1_CORRECTION_ABLATION`。\\n- `plan_004_realdata_feasibility` → `C_REALDATA_FEASIBILITY`。\\n\\n## 中期实验矩阵\\n\\nStage 0 机制验证：\\n- positive vs negative misclassification-CATE correlation\\n- high vs low misclassification heterogeneity\\n- high vs low CATE heterogeneity\\n- k=3 与 k=6 subgroup\\n- oracle global correction vs estimated global correction vs uncorrected\\n\\nStage 1 correction：\\n- uncorrected\\n- global confusion correction\\n- arm-specific correction\\n- per-subgroup independent correction\\n- hierarchical/partial-pooling correction\\n\\nStage 2 inference：\\n- naive CI\\n- sandwich-adjusted CI\\n- bootstrap CI\\n- empirical coverage 与 CI width 对比\\n\\nStage 3 allocation：\\n- uniform allocation\\n- misclassification-uncertainty-only\\n- CATE-magnitude-only\\n- joint criterion\\n- pilot ratio 10%、20%、30%\\n\\nReal-data validation：\\n- Rohingya interview corpus 上验证 LLM misclassification 是否随 refugee status、gender、education 差异化变化\\n- leave-expert-out calibration test\\n- diagnostic criterion operability demonstration\\n\\n## 工程产出\\n\\n- `scripts/`：可复现实验入口，包含 DGP、correction、estimation、evaluation。\\n- `configs/`：每个实验的 YAML/JSON 配置，记录 seed、DGP 参数、预算、method。\\n- `artifacts/`：实验表格、图、日志、registry 可追溯输出。\\n- `docs/`：技术报告素材与复现说明，由 Director 汇总。\\n- 部署代码：提供 diagnostic calculator 和 correction workflow 的最小可调用接口。\\n\\n## 决策规则\\n\\n- 任何负向结果必须先汇报 Director，不得默默跑同一方向的下一步。\\n- 如果 exp_001 未能复现 global correction worse than uncorrected，优先诊断 DGP、correction algebra、oracle-vs-estimated 拆分和 metric 定义，而不是直接推进 Stage 1。\\n- GPU 实验启动前必须确认项目白名单 GPU 可见，并记录 server、GPU 型号、driver、命令、数据路径、seed。\\n- 所有定量结论只引用 registry 中有 exp_id 的结果。\\n\", \"total_chars\": 5411, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
        }
      ],
      "structured_content": {
        "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/ec_hte_codex_a/ROADMAP.md\", \"content\": \"# ROADMAP\\n\\n> 最后更新: 2026-05-31 15:53 UTC | 更新原因: 量化 H1/exp_002 判据并新增 H2 partial-pooling claim\\n\\n## 项目目标\\n\\nEC-HTE 的内部研究目标是验证并实现一套面向 LLM 分类 effect modifier 误分类的 HTE/CATE 纠偏流程。最终产出是技术报告、可复现实验包和可部署代码，不走会议论文提交流程。\\n\\n核心问题：当 LLM 注释误分类率在 subgroup 间不同，并且误分类强度与真实 CATE/HTE 结构相关时，使用单一全局 confusion matrix 的纠偏可能放大 subgroup CATE bias，甚至比不纠偏更差。\\n\\n## 当前主线 Hypothesis\\n\\nH1: 在 misclassification rate 与真实 subgroup CATE magnitude 正相关的 DGP 中，全局 confusion-matrix correction 会 under-correct 高误差/高效应 subgroup，并 over-correct 低误差/低效应 subgroup，因此 GATE RMSE 可能高于 uncorrected。\\n\\nH2: subgroup-specific correction 能降低 H1 暴露的结构性偏差；当 expert label budget 较小时，partial pooling 会比 per-subgroup independent confusion matrix 更稳健。\\n\\nH3: naive CI 会低估 Stage 1 misclassification estimation uncertainty；sandwich 或 bootstrap variance adjustment 能改善 subgroup CATE coverage。\\n\\nH4: adaptive expert annotation allocation 应优先投向 misclassification uncertainty 与 CATE magnitude 同时较高的 subgroup，在固定预算下优于 uniform allocation。\\n\\n## Operational 判据\\n\\n`exp_001_bias_bound_mvp`：唯一 primary metric 是 GATE RMSE；mean subgroup CATE bias 与 max subgroup CATE bias 是 secondary diagnostics；最低 200 replications。\\n\\nH1 success for exp_001：在 positive-correlation high-misclassification/high-CATE-heterogeneity 设置中，`oracle_global - uncorrected` 的 GATE RMSE 差值大于 0，且 bootstrap 95% CI lower bound > 0。`estimated_global` 单独报告；`estimated_global - oracle_global` 用于量化 finite-sample confusion-estimation noise。如果 GATE RMSE 支持 H1 但 secondary bias diagnostics 方向相反，标记 mixed，先 Director 复核再推进 Stage 1。\\n\\nH1 negative for exp_001：如果 positive-correlation worst-case 中 oracle global 不劣于 uncorrected，则 H1 暂不支持；下一步先审计 DGP construction、correction algebra、metric definitions、subgroup weighting，而不是推进 Stage 1。\\n\\n`exp_002_gpu_dgp_grid`：primary metric 是 `global_worse_rate_difference_positive_minus_negative`；secondary metrics 是 `bias_bound_vs_global_worse_spearman` 与 `estimated_global_minus_oracle_global_gate_rmse`；每个 condition 最低 200 replications。\\n\\nH1 success for exp_002：positive-correlation conditions 的 oracle-global-worse rate 至少比 negative-correlation controls 高 20 percentage points，且 bootstrap 95% CI lower bound > 0；bias-bound diagnostic 对 oracle-global-worse conditions 的 Spearman rho >= 0.50，且 bootstrap 95% CI lower bound > 0。estimated-global 结果必须与 oracle-global 分开报告。\\n\\nH2 success for Stage 1：low expert-label budget 下，partial pooling 在 GATE RMSE 上优于 global correction，`partial_pooling_minus_global` bootstrap 95% CI upper bound < 0；相对 per-subgroup independent correction 满足 5% relative GATE RMSE non-inferiority。PEHE 和 mean subgroup CATE bias 是 secondary diagnostics。\\n\\n## 短期计划\\n\\n1. 完成 `exp_001_bias_bound_mvp` CPU-only 半合成 MVP simulation，验证 H1。必跑对照为 uncorrected、oracle global confusion correction、estimated global confusion correction、stratified/subgroup correction；必须拆开结构性 global-correction 偏差与 finite-sample confusion-estimation noise。\\n2. `exp_002_gpu_dgp_grid` 只能在 PENDING 审批、QUEUED、Director GPU allocation 后启动。GPU 实验必须使用项目白名单 `seetacloud-38274/root/cuda:0`，并在 spec 中记录 command、server、GPU 型号、driver、data_path/data_count、seed、disk estimate、expected runtime、log/checkpoint/artifact 路径。\\n3. 建立统一评测协议：GATE RMSE、subgroup CATE bias、PEHE、CI coverage、CI width、bound tightness。所有指标必须能追溯到 registry exp_id。\\n4. 维护 `experiment_plan.yaml` 与 experiment matrix 映射：H1 claim、H2 claim、Stage 0 DGP grid、Stage 1 correction ablation、real-data feasibility 均必须有 plan entry 和 target/cell 映射。\\n5. 并行检查 real-data validation 可行性：Rohingya corpus 字段、LLM annotation、expert label source、subgroup variables、可用 split 与复现实验权限；未确认前不把 real-data 写成已完成结果。\\n\\n## Experiment Plan / Matrix 映射\\n\\n当前最低覆盖目标：\\n- `plan_001_h1_cpu_mvp` → `C_H1_GLOBAL_CORRECTION_WORSE`, `T_STAGE0_DGP_GRID`, registry `exp_001_bias_bound_mvp`。\\n- `plan_002_h1_gpu_dgp_grid` → `C_H1_GLOBAL_CORRECTION_WORSE`, `T_STAGE0_DGP_GRID`, registry `exp_002_gpu_dgp_grid`。\\n- `plan_003_stage1_correction_ablation` → `C_PARTIAL_POOLING_BETTER_LOW_BUDGET`, `T_STAGE1_CORRECTION_ABLATION`。\\n- `plan_004_realdata_feasibility` → `C_REALDATA_FEASIBILITY`。\\n\\n## 中期实验矩阵\\n\\nStage 0 机制验证：\\n- positive vs negative misclassification-CATE correlation\\n- high vs low misclassification heterogeneity\\n- high vs low CATE heterogeneity\\n- k=3 与 k=6 subgroup\\n- oracle global correction vs estimated global correction vs uncorrected\\n\\nStage 1 correction：\\n- uncorrected\\n- global confusion correction\\n- arm-specific correction\\n- per-subgroup independent correction\\n- hierarchical/partial-pooling correction\\n\\nStage 2 inference：\\n- naive CI\\n- sandwich-adjusted CI\\n- bootstrap CI\\n- empirical coverage 与 CI width 对比\\n\\nStage 3 allocation：\\n- uniform allocation\\n- misclassification-uncertainty-only\\n- CATE-magnitude-only\\n- joint criterion\\n- pilot ratio 10%、20%、30%\\n\\nReal-data validation：\\n- Rohingya interview corpus 上验证 LLM misclassification 是否随 refugee status、gender、education 差异化变化\\n- leave-expert-out calibration test\\n- diagnostic criterion operability demonstration\\n\\n## 工程产出\\n\\n- `scripts/`：可复现实验入口，包含 DGP、correction、estimation、evaluation。\\n- `configs/`：每个实验的 YAML/JSON 配置，记录 seed、DGP 参数、预算、method。\\n- `artifacts/`：实验表格、图、日志、registry 可追溯输出。\\n- `docs/`：技术报告素材与复现说明，由 Director 汇总。\\n- 部署代码：提供 diagnostic calculator 和 correction workflow 的最小可调用接口。\\n\\n## 决策规则\\n\\n- 任何负向结果必须先汇报 Director，不得默默跑同一方向的下一步。\\n- 如果 exp_001 未能复现 global correction worse than uncorrected，优先诊断 DGP、correction algebra、oracle-vs-estimated 拆分和 metric 定义，而不是直接推进 Stage 1。\\n- GPU 实验启动前必须确认项目白名单 GPU 可见，并记录 server、GPU 型号、driver、命令、数据路径、seed。\\n- 所有定量结论只引用 registry 中有 exp_id 的结果。\\n\", \"total_chars\": 5411, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
      }
    },
    "error": null,
    "status": "completed"
  }
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "item.completed",
  "item": {
    "id": "item_5",
    "type": "agent_message",
    "text": "ROADMAP 明确 `plan_004_realdata_feasibility → C_REALDATA_FEASIBILITY`，且 real-data 只能验证 differential misclassification 与 leave-expert-out calibration，不报告真实 CATE accuracy。接下来核对 brief/matrix 里的具体 cell 名称和 artifact manifest 格式。"
  }
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "item.started",
  "item": {
    "id": "item_6",
    "type": "command_execution",
    "command": "/bin/bash -lc \"sed -n '1,240p' experiment_matrix.yaml\"",
    "aggregated_output": "",
    "exit_code": null,
    "status": "in_progress"
  }
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "item.completed",
  "item": {
    "id": "item_6",
    "type": "command_execution",
    "command": "/bin/bash -lc \"sed -n '1,240p' experiment_matrix.yaml\"",
    "aggregated_output": "version: 1\nupdated_at: '2026-05-31T15:52:41.437Z'\npaper_targets:\n- id: C_H1_GLOBAL_CORRECTION_WORSE\n  type: claim\n  location: 技术报告 Claim H1\n  description: 当 subgroup misclassification heterogeneity 与真实 CATE heterogeneity 正相关时，全局\n    confusion correction 可能比 uncorrected 产生更大的 subgroup CATE bias 或 GATE RMSE；该 claim\n    必须拆分 oracle global correction 与 estimated global correction，以区分结构性偏差和 finite-sample\n    confusion estimation noise。\n  provenance_id: H1\n  cells:\n  - row: exp_001_bias_bound_mvp\n    col: uncorrected_vs_oracle_global\n    status: planned\n    experiment_id: exp_001_bias_bound_mvp\n    metric_key: oracle_global_minus_uncorrected_gate_rmse\n  - row: exp_001_bias_bound_mvp\n    col: uncorrected_vs_estimated_global\n    status: planned\n    experiment_id: exp_001_bias_bound_mvp\n    metric_key: estimated_global_minus_uncorrected_gate_rmse\n  - row: exp_002_gpu_dgp_grid\n    col: grid_oracle_vs_estimated_mechanism_split\n    status: planned\n    experiment_id: exp_002_gpu_dgp_grid\n    metric_key: bias_bound_predicts_global_worse_rate_by_correction_type\n- id: T_STAGE0_DGP_GRID\n  type: table\n  location: 技术报告 Stage 0 机制验证表\n  description: Stage 0 半合成 DGP grid：按 misclassification-CATE correlation direction、misclassification\n    heterogeneity、CATE heterogeneity 比较 uncorrected、oracle global correction、estimated\n    global correction、stratified/subgroup correction。\n  provenance_id: STAGE0\n  cells:\n  - row: positive_corr_high_mis_high_cate\n    col: uncorrected_gate_rmse\n    status: planned\n    experiment_id: exp_001_bias_bound_mvp\n    metric_key: positive_corr_high_high.uncorrected_gate_rmse\n  - row: positive_corr_high_mis_high_cate\n    col: oracle_global_gate_rmse\n    status: planned\n    experiment_id: exp_001_bias_bound_mvp\n    metric_key: positive_corr_high_high.oracle_global_gate_rmse\n  - row: positive_corr_high_mis_high_cate\n    col: estimated_global_gate_rmse\n    status: planned\n    experiment_id: exp_001_bias_bound_mvp\n    metric_key: positive_corr_high_high.estimated_global_gate_rmse\n  - row: positive_corr_high_mis_high_cate\n    col: stratified_gate_rmse\n    status: planned\n    experiment_id: exp_001_bias_bound_mvp\n    metric_key: positive_corr_high_high.stratified_gate_rmse\n  - row: grid_all_conditions\n    col: bias_bound_auc_or_rank_corr\n    status: planned\n    experiment_id: exp_002_gpu_dgp_grid\n    metric_key: bias_bound_vs_global_worse_rank_corr\n  - row: grid_all_conditions\n    col: oracle_estimated_gap\n    status: planned\n    experiment_id: exp_002_gpu_dgp_grid\n    metric_key: estimated_global_minus_oracle_global_gate_rmse\n- id: T_STAGE1_CORRECTION_ABLATION\n  type: table\n  location: 技术报告 Stage 1 correction ablation 表\n  description: Stage 1 correction ablation：比较 global、arm-specific、per-subgroup independent、hierarchical/partial-pooling\n    correction 在相同 expert label budget 下的 subgroup CATE bias、GATE RMSE、PEHE。\n  provenance_id: STAGE1\n  cells:\n  - row: budget_low\n    col: global\n    status: planned\n    metric_key: gate_rmse\n  - row: budget_low\n    col: per_subgroup_independent\n    status: planned\n    metric_key: gate_rmse\n  - row: budget_low\n    col: partial_pooling\n    status: planned\n    metric_key: gate_rmse\n  - row: budget_mid\n    col: global\n    status: planned\n    metric_key: gate_rmse\n  - row: budget_mid\n    col: per_subgroup_independent\n    status: planned\n    metric_key: gate_rmse\n  - row: budget_mid\n    col: partial_pooling\n    status: planned\n    metric_key: gate_rmse\n- id: C_REALDATA_FEASIBILITY\n  type: claim\n  location: 技术报告 Real-data validation readiness\n  description: 在推进 real-data validation 前，必须确认 Rohingya corpus 的字段、LLM annotation、expert\n    label source、subgroup variables、可用 split 与复现实验权限；否则 real-data 部分只能作为设计方案而非结果。\n  provenance_id: REALDATA\n  cells:\n  - row: rohingya_corpus\n    col: fields_and_label_sources\n    status: planned\n    metric_key: data_schema_summary\n  - row: rohingya_corpus\n    col: expert_split_available\n    status: planned\n    metric_key: expert_split_status\n  - row: rohingya_corpus\n    col: subgroup_variables_available\n    status: planned\n    metric_key: subgroup_variable_coverage\n- id: C_PARTIAL_POOLING_BETTER_LOW_BUDGET\n  type: claim\n  location: 技术报告 Claim H2\n  description: 在 expert label budget 较低时，hierarchical/partial-pooling subgroup confusion\n    correction 应在 GATE RMSE 上优于 global correction，并相对 per-subgroup independent correction\n    满足 5% relative GATE RMSE non-inferiority；PEHE 与 mean subgroup CATE bias 作为 secondary\n    diagnostics。\n  provenance_id: H2\n  cells:\n  - row: low_budget\n    col: partial_pooling_vs_global\n    status: planned\n    metric_key: low_budget.partial_pooling_minus_global_gate_rmse\n  - row: low_budget\n    col: partial_pooling_vs_per_subgroup\n    status: planned\n    metric_key: low_budget.partial_pooling_minus_per_subgroup_gate_rmse\n  - row: low_budget\n    col: secondary_pehe_bias_diagnostics\n    status: planned\n    metric_key: low_budget.partial_pooling_secondary_diagnostics\n",
    "exit_code": 0,
    "status": "completed"
  }
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "item.started",
  "item": {
    "id": "item_7",
    "type": "command_execution",
    "command": "/bin/bash -lc \"sed -n '1,240p' docs/PROJECT_BRIEF.md\"",
    "aggregated_output": "",
    "exit_code": null,
    "status": "in_progress"
  }
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "item.completed",
  "item": {
    "id": "item_7",
    "type": "command_execution",
    "command": "/bin/bash -lc \"sed -n '1,240p' docs/PROJECT_BRIEF.md\"",
    "aggregated_output": "# EC-HTE Codex Scheme A\n\n## EC-HTE: Error-Corrected Heterogeneous Treatment Effect Estimation Under LLM Annotation Misclassification\n\n## Problem and Motivation\n\nWhen NLP researchers use LLM-generated annotations as effect modifiers in causal heterogeneous treatment effect (HTE) analysis, a previously unrecognized structural bias arises: LLM misclassification rates covary with the true conditional average treatment effect (CATE). Subgroups where LLMs err most in annotation (e.g., marginalized populations, linguistically complex cases) are often the same subgroups where treatment effects are largest. This creates a confounding between measurement error and causal heterogeneity that cannot be resolved by any global correction method—including arm-specific rectifiers (Mozer, arXiv:2603.19160), which address average treatment effect (ATE) bias but are algebraically incapable of correcting subgroup-level CATE distortions.\n\nThis problem is urgent. LLM-as-annotator has become the default pipeline for computational social science (Audinet de Pieuchon et al., EMNLP 2025, benchmarking DSL vs. PPI debiasing; StratPPI, Fisch et al., NeurIPS 2024, improving PPI via stratification), and researchers increasingly use LLM annotations not just for ATE estimation (where DSL and PPI provide corrections) but for subgroup analysis and effect modification—yet no correction method exists for this latter use case. Messing (arXiv:2604.11581) documents that hidden measurement error in LLM pipelines causes naive confidence intervals to under-cover by 40–60%, but this analysis remains at the aggregate level. Ashwin et al. (Sociological Methods & Research, 2025) provide direct empirical evidence that LLM coding errors in refugee interview transcripts correlate systematically with respondents' refugee status, gender, and education level—precisely the variables used as effect modifiers in downstream causal analysis. Any study using LLM-annotated text variables as moderators produces unreliable heterogeneity findings whenever annotation error rates differ across subgroups—and Ashwin et al. show this is the norm, not the exception.\n\n**Key anti-intuitive finding: global correction can actively worsen CATE estimates.** Consider a two-subgroup example. Subgroup A has high misclassification (25%) and large CATE (0.5 SD); Subgroup B has low misclassification (5%) and small CATE (0.1 SD). A global correction uses a pooled confusion matrix (~15% error), which under-corrects Subgroup A and over-corrects Subgroup B. The net effect: globally-corrected CATE estimates can have *larger* bias than uncorrected estimates. This is not an edge case—it occurs whenever the misclassification pattern and CATE structure are positively correlated, which empirical evidence suggests is common in practice.\n\n## Core Contributions\n\nThis paper makes four contributions:\n\n1. **Problem identification and formalization.** We identify and formalize measurement-error-induced CATE distortion—a new class of bias arising when LLM annotation errors in effect modifiers are differential across subgroups and correlated with the true heterogeneity structure. We show this is structurally distinct from: ATE-level debiasing (Mozer, arXiv:2603.19160; Egami et al., NeurIPS 2023 DSL; Zrnic & Candès, ICML 2024), CATE-to-GATE aggregation bias (Persson et al., arXiv:2602.20383, where bias originates from aggregation, not measurement error), and conditional inference with outcome prediction noise (Sui et al., arXiv:2603.05575 PPCI, which assumes the conditioning variable is correct). We prove that global correction can *increase* CATE bias relative to uncorrected estimates when misclassification and CATE heterogeneity are positively correlated.\n\n2. **Actionable diagnostic criterion (Bias Bound).** We derive a finite-sample bound: the bias of globally-corrected CATE estimates is proportional to the product of (a) misclassification heterogeneity across subgroups and (b) CATE heterogeneity across subgroups. This product yields a practical diagnostic: given pilot data, any researcher can compute this quantity *before* running full CATE analysis to determine whether global correction suffices or stratified correction is necessary. This diagnostic has standalone value independent of the EC-HTE framework—it applies to any CATE analysis using LLM-annotated effect modifiers. The bound implies that bias is worst when annotation is least accurate for subgroups where treatment effects are largest—empirically common (Ashwin et al., 2025).\n\n3. **EC-HTE: A three-stage correction framework** providing subgroup-specific misclassification correction, valid confidence intervals, and optimal annotation allocation (detailed below).\n\n4. **Empirical validation** via semi-synthetic benchmarks with controlled DGPs (including systematic variation of misclassification-CATE correlation direction) and a real-data misclassification pattern validation (Ashwin et al., 2025, Rohingya interview corpus).\n\n## Why Not Just Use Expert Labels?\n\nA natural objection: why not skip LLM annotation entirely and estimate CATEs using only expert-labeled data? The answer is a bias-variance tradeoff specific to CATE estimation. With a budget of ~2,000 expert labels distributed across k subgroups, each subgroup contains ~2,000/k observations. Honest causal forests (Wager & Athey, JASA 2018) split this further into estimation and splitting samples, leaving each cell with ~1,000/k observations—insufficient for detecting moderate heterogeneity when k ≥ 4.\n\nEC-HTE resolves this by using the full unlabeled corpus (potentially hundreds of thousands of LLM-annotated observations) for low-variance CATE estimation, with expert labels only for calibrating subgroup-specific misclassification. This extends the PPI/DSL paradigm—combining noisy large-scale with clean small-scale data—from ATE to CATE, where data demands make the combination even more critical.\n\n## Method: Three-Stage Framework\n\n**Stage 1: Hierarchical Bayesian Subgroup-Specific Misclassification Estimation.** For each effect-modifier subgroup g ∈ {1, …, k}, we estimate a confusion matrix C_g between LLM annotation and expert gold standard using a hierarchical Bayesian model with partial pooling. The hierarchy allows low-sample subgroups to borrow strength from the global structure while permitting genuine cross-subgroup variation. This addresses a key tension: per-subgroup independent estimation (high variance when subgroup expert-label counts are small) vs. single global estimation (biased when misclassification rates genuinely differ). For computational scalability in large-scale simulation studies, we use variational inference (VI) as the primary fitting method, with MCMC validation on representative configurations in the appendix.\n\n**Stage 2: Corrected CATE Estimation with Sandwich Variance Adjustment.** Corrected effect-modifier assignments are fed into an honest causal forest (Wager & Athey, JASA 2018). Because Stage 1 introduces nuisance parameter uncertainty, naive confidence intervals will under-cover. We derive a sandwich variance inflator propagating Stage 1 uncertainty into Stage 2 CIs, ensuring valid coverage. Bootstrap-based CIs serve as a robustness check.\n\n**Stage 3: Adaptive Expert Annotation Allocation.** Given a fixed expert budget B, we optimize allocation across subgroups by jointly minimizing misclassification estimation uncertainty and CATE estimation variance. The allocation criterion targets subgroups where the product of misclassification uncertainty and CATE magnitude is largest—precisely where annotation errors cause the most CATE distortion (as predicted by the bias bound).\n\n**Cold-start protocol.** Since Stage 3 requires initial estimates of both misclassification rates and CATE magnitudes, we employ a multi-batch protocol: (a) allocate 20–30% of B as a uniform pilot batch; (b) estimate initial confusion matrices and CATE values; (c) allocate remaining budget adaptively. We include pilot ratio sensitivity analysis (10%, 20%, 30%) in the experiments.\n\n## Related Work and Differentiation\n\n**Thread 1: LLM annotation debiasing (ATE-level).** DSL (Egami et al., NeurIPS 2023), PPI and its algebraic equivalence to survey-sampling difference estimators (Mozer, arXiv:2603.19160), active inference (Zrnic & Candès, ICML 2024), stratified PPI (StratPPI, Fisch et al., NeurIPS 2024), active multi-predictor PPI (AM-PPI, arXiv:2605.08429), and benchmarking thereof (Audinet de Pieuchon et al., EMNLP 2025). All locked to population-level estimands. Messing (arXiv:2604.11581) diagnoses hidden measurement error causing 40–60% CI under-coverage but does not extend to causal HTE correction.\n\n**Thread 2: HTE/CATE estimation methods.** Honest causal forests (Wager & Athey, JASA 2018), DR-learner, CATE-to-GATE aggregation bias correction (Persson et al., arXiv:2602.20383, shrinkage for aggregation-induced bias assuming clean covariates), and assumption-lean HTE detection under mismeasured modifiers (Boileau et al., arXiv:2512.03254, hypothesis testing for whether heterogeneity exists, not CATE estimation—complementary to EC-HTE). CATE evaluation standards established in \"Really Doing Great at Estimating CATE?\" (NeurIPS D&B 2021).\n\n**Thread 3: Conditional inference with ML predictions.** PPCI (Sui et al., arXiv:2603.05575) extends PPI to conditional functionals at fixed test points via kernel localization. Critical distinction: PPCI addresses outcome prediction noise at a correctly-specified conditioning point; EC-HTE addresses the situation where the conditioning variable (effect modifier) itself is misclassified. PPCI's localization anchors on correct covariate values—when the anchor itself is wrong (categorical misclassification), kernel localization cannot help.\n\n**Thread 4: Measurement error correction for ML-generated variables.** ForestIV (Bu et al., INFORMS JDS 2023) uses random forest tree tuples as instrumental variables, but requires IV exclusion restrictions and is limited to regression settings, not CATE with categorical effect modifiers. Jerzak et al. (arXiv:2509.12416, SRI framework) provide valid inference under noisy annotation but do not address effect modifier misclassification's impact on HTE. SIMEX handles continuous measurement error models but does not directly apply to categorical misclassification.\n\n**Thread 5: Causal inference with textual variables.** Feldman et al. (arXiv:2602.15730) address latent textual treatment estimation using SAE + residualization, assuming clean effect modifiers. Nwankwo et al. (arXiv:2502.10605, NeurIPS 2025 Workshop) optimize annotation allocation for doubly robust ATE with missing outcomes—different estimand (ATE vs. CATE), different error source (outcome missingness vs. effect modifier misclassification), different optimization landscape.\n\nEC-HTE sits at the intersection of Threads 1–4: correcting LLM misclassification specifically in effect modifiers for valid CATE estimation.\n\n## Validation Design\n\n### Semi-Synthetic Experiments\n\n**Corpus.** Political science text corpus with real-world linguistic variation (e.g., immigration framing data or partisan tweet datasets with known ideological annotations).\n\n**DGP Matrix.** Core factors:\n- Misclassification severity: high (25–30%) vs. low (5–10%)\n- CATE heterogeneity magnitude: large (>0.3 SD) vs. small (<0.1 SD)\n- Subgroup count: k=3 vs. k=6\n- **Misclassification-CATE correlation direction**: positive (high-error subgroups have high CATE, worst-case) vs. negative (high-error subgroups have low CATE, best-case)\n\nSelective design: 12–14 configurations covering all worst-case/best-case combinations for the key factors, rather than full 2⁴=16 factorial.\n\nTreatment assignment T ~ Bernoulli(0.5); potential outcomes Y(1), Y(0) generated with known ground-truth CATE τ(x) varying by subgroup.\n\n**Replications.** ≥ 200 per configuration.\n\n**Sample sizes.** N ∈ {2000, 5000, 10000}.\n\n**Expert label budget.** B ∈ {100, 500, 1000, 2000} to produce budget vs. performance curves. All methods compared under identical total budget.\n\n**LLMs.** Three annotators: GPT-4.1 (proprietary frontier), Qwen 3.5 (open-source large), Llama 3.3 (open-source, different family). Fourth LLM as appendix robustness check.\n\n### Comparison Methods (all under fixed expert annotation budget B)\n\n1. **Uncorrected**: LLM annotations used directly as effect modifiers in causal forest.\n2. **Globally-corrected**: Single confusion matrix → corrected annotations → causal forest.\n3. **Arm-specific (Mozer-style)**: Separate confusion matrices for treatment/control arms → causal forest.\n4. **SIMEX + causal forest**: SIMEX-based measurement error correction → causal forest.\n5. **Calibration-only + causal forest**: Platt scaling / temperature scaling → calibrated probabilities as soft effect modifiers → causal forest.\n6. **EC-HTE (full)**: Hierarchical Bayesian subgroup-specific correction → sandwich-adjusted causal forest → adaptive allocation.\n\n### Evaluation Metrics\n\n- **PEHE**: √E[(τ̂(x) − τ(x))²], overall and per-subgroup.\n- **Subgroup CATE bias**: |E[τ̂_g] − τ_g| for each subgroup g.\n- **CI empirical coverage**: Fraction of replications where true CATE falls within 95% CI (target: 0.95).\n- **CI width**: Efficiency measure at fixed coverage.\n- **GATE RMSE**: RMSE of group average treatment effect estimates.\n- **Bound tightness**: Observed bias vs. theoretical bound prediction.\n\n### Ablation Studies\n\n**Stage 1 ablation (partial pooling):**\n- (a) Hierarchical Bayesian with VI (partial pooling)\n- (b) Per-subgroup independent confusion matrices (no pooling)\n- (c) Single global confusion matrix (full pooling)\n- (d) Prior sensitivity: 2–3 prior settings (weakly informative, moderately informative, diffuse) on 1–2 representative DGP configurations\n\n**Stage 2 ablation (variance adjustment):**\n- (a) Sandwich variance-adjusted CIs\n- (b) Bootstrap-based CIs\n- (c) Naive CIs (no adjustment)\n→ Compare empirical coverage rates.\n\n**Stage 3 ablation (allocation strategy):**\n- (a) Joint criterion (misclassification uncertainty × CATE magnitude)\n- (b) Misclassification-uncertainty-only allocation\n- (c) CATE-magnitude-only allocation\n- (d) Uniform allocation\n- (e) Pilot ratio sensitivity: 10%, 20%, 30% of B as uniform pilot batch\n→ Compare PEHE at fixed total budget B.\n\n**Diagnostic validation:** Systematically vary misclassification heterogeneity and CATE heterogeneity (including correlation direction); produce heatmap of EC-HTE improvement over global correction vs. (product of heterogeneity measures). Verify that the theoretical bound predicts when global correction fails and when it suffices. Specifically demonstrate that global correction is worse than uncorrected in positive-correlation configurations.\n\n**CATE estimator robustness (appendix):** In 1–2 worst-case configurations, replace causal forest with DR-learner to verify EC-HTE's correction generalizes beyond a single CATE estimator.\n\n### Real-Data Application (Ashwin et al., 2025)\n\n**Dataset.** Rohingya refugee interview transcripts (Ashwin et al., Sociological Methods & Research 2025). This dataset's primary role is validating the premise of EC-HTE—that LLM misclassification is differential—rather than evaluating CATE estimation accuracy (the dataset lacks a natural causal structure).\n\n**Validation goals:**\n1. **Differential misclassification pattern confirmation**: Quantify and visualize how LLM error rates vary across subgroups defined by refugee status, gender, education.\n2. **Leave-expert-out calibration test**: Treat full human labels as ground truth, subsample B expert labels, evaluate whether EC-HTE's hierarchical confusion matrix estimates recover the true subgroup-specific error patterns better than global estimation.\n3. **Diagnostic criterion demonstration**: Compute the misclassification-heterogeneity × CATE-heterogeneity product on this dataset (constructing a plausible causal question from available variables) to demonstrate the diagnostic's operability.\n4. **Budget curve**: Accuracy of confusion matrix recovery vs. expert label budget B.\n\nCATE estimation accuracy is rigorously evaluated in the semi-synthetic experiments where ground-truth CATE is known.\n\n## Scope and Limitations\n\nEC-HTE targets **categorical effect modifiers** (stance, topic, sentiment, entity type, etc.)—the dominant use case when LLM annotations serve as moderators in computational social science. When the effect modifier is a continuous variable that has been discretized (binned), misclassification includes both LLM errors and discretization error; the current framework does not disentangle these sources. Extension to continuous effect modifiers with measurement error (where SIMEX-type approaches may be more natural) is future work.\n\n## Broader Applicability\n\nWhile our validation focuses on CSS, the same problem structure arises whenever ML-predicted categorical variables serve as effect modifiers: in medical research (ML-classified tumor subtypes as moderators of drug efficacy), education (NLP-coded classroom behaviors moderating intervention effects), and policy evaluation (automated classification of administrative characteristics). EC-HTE's framework and diagnostic criterion apply directly to these settings.\n\n## Expected Contributions\n\nEC-HTE provides (1) the first formal identification of measurement-error-induced CATE distortion in LLM-annotated pipelines, including the proof that global correction can worsen estimates; (2) an actionable diagnostic (the misclassification-heterogeneity × CATE-heterogeneity product) with standalone value for any CATE analysis; (3) a practical three-stage correction framework with valid inference; and (4) comprehensive empirical validation. The framework serves any study using LLM-annotated categorical text variables as effect modifiers in causal analysis.\n\n",
    "exit_code": 0,
    "status": "completed"
  }
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "item.started",
  "item": {
    "id": "item_8",
    "type": "command_execution",
    "command": "/bin/bash -lc \"sed -n '1,240p' artifacts/manifest.yaml\"",
    "aggregated_output": "",
    "exit_code": null,
    "status": "in_progress"
  }
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "item.completed",
  "item": {
    "id": "item_8",
    "type": "command_execution",
    "command": "/bin/bash -lc \"sed -n '1,240p' artifacts/manifest.yaml\"",
    "aggregated_output": "- id: art_20260531_baseline_protocol\n  name: baseline_protocol_research\n  type: report\n  description: EC-HTE 首批实验领域参考与 baseline protocol；覆盖 HTE/CATE metrics、PPI/DSL/StratPPI/AM-PPI/Mozer 适用边界、categorical misclassification correction baselines 和实验矩阵。\n  path: projects/ec_hte_codex_a/artifacts/research/baseline_protocol_20260531.md\n  url: null\n  project: ec_hte_codex_a\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-31T00:00:00+00:00'\n  tags:\n  - research\n  - protocol\n  - baseline\n  - cate\n  - misclassification\n",
    "exit_code": 0,
    "status": "completed"
  }
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "item.started",
  "item": {
    "id": "item_9",
    "type": "command_execution",
    "command": "/bin/bash -lc \"sed -n '1,220p' registry.yaml\"",
    "aggregated_output": "",
    "exit_code": null,
    "status": "in_progress"
  }
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "item.completed",
  "item": {
    "id": "item_9",
    "type": "command_execution",
    "command": "/bin/bash -lc \"sed -n '1,220p' registry.yaml\"",
    "aggregated_output": "baseline: null\nexperiments:\n  exp_001_bias_bound_mvp:\n    status: PREPARING\n    retry_count: 0\n    created_at: '2026-05-31T15:33:29.573Z'\n    updated_at: '2026-05-31T15:33:29.573Z'\n    hypothesis: When subgroup misclassification rates are positively correlated with\n      true subgroup CATE magnitudes, a pooled global confusion-matrix correction under-corrects\n      high-effect high-error groups and over-corrects low-effect low-error groups,\n      producing larger subgroup CATE bias than using the noisy annotations directly\n      in a controlled semi-synthetic DGP.\n  exp_002_gpu_dgp_grid:\n    status: PREPARING\n    retry_count: 0\n    created_at: '2026-05-31T15:44:35.644Z'\n    updated_at: '2026-05-31T15:44:35.644Z'\n    hypothesis: 'A GPU-vectorized DGP grid that systematically varies subgroup misclassification\n      heterogeneity and CATE heterogeneity will reproduce the EC-HTE bias-bound mechanism:\n      positive correlation between error and treatment effect should make global correction\n      worse than uncorrected annotations, while negative correlation should not show\n      the same degradation.'\n",
    "exit_code": 0,
    "status": "completed"
  }
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "item.started",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d14fdfc8191be818f99f8c924db",
    "type": "web_search",
    "query": "",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "item.completed",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d14fdfc8191be818f99f8c924db",
    "type": "web_search",
    "query": "Ashwin Chhabra Rao 2025 Rohingya Bengali host interviews dataset LLM qualitative analysis refugee status gender education",
    "action": {
      "type": "search",
      "query": "Ashwin Chhabra Rao 2025 Rohingya Bengali host interviews dataset LLM qualitative analysis refugee status gender education",
      "queries": [
        "Ashwin Chhabra Rao 2025 Rohingya Bengali host interviews dataset LLM qualitative analysis refugee status gender education",
        "\"Using Large Language Models for Qualitative Analysis Can Introduce\" Rohingya dataset",
        "Rohingya refugee interview transcripts Ashwin Chhabra Rao dataset"
      ]
    }
  }
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "item.started",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d18ecbc8191a0d2271c53776a83",
    "type": "web_search",
    "query": "",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "item.completed",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d18ecbc8191a0d2271c53776a83",
    "type": "web_search",
    "query": "https://journals.sagepub.com/doi/10.1177/00491241251338246",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "item.started",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d1ae91881919dbe69660706d332",
    "type": "web_search",
    "query": "",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "item.completed",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d1ae91881919dbe69660706d332",
    "type": "web_search",
    "query": "'## Data' in https://journals.sagepub.com/doi/10.1177/00491241251338246",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "item.started",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d1df3a481919060d16c9a07e5dc",
    "type": "web_search",
    "query": "",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "item.completed",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d1df3a481919060d16c9a07e5dc",
    "type": "web_search",
    "query": "https://journals.sagepub.com/doi/10.1177/00491241251338246",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "item.started",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d220008819187d1a1844f0beaaf",
    "type": "web_search",
    "query": "",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "item.completed",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d220008819187d1a1844f0beaaf",
    "type": "web_search",
    "query": "\"A Method to Scale-up Interpretative Qualitative Analysis\" Cox's Bazaar data code repository",
    "action": {
      "type": "search",
      "query": "\"A Method to Scale-up Interpretative Qualitative Analysis\" Cox's Bazaar data code repository",
      "queries": [
        "\"A Method to Scale-up Interpretative Qualitative Analysis\" Cox's Bazaar data code repository",
        "\"A Method to Scale-up Interpretative Qualitative Analysis\" \"Cox\" \"World Bank\" PDF",
        "\"Ashwin\" \"Rao\" \"Biradavolu\" \"Chhabra\" \"Haque\" \"Krishnan\" \"Khan\" \"iQual\""
      ]
    }
  }
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "item.started",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d27c2c081918ad8782bb18df226",
    "type": "web_search",
    "query": "",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "item.completed",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d27c2c081918ad8782bb18df226",
    "type": "web_search",
    "query": "\"Cox's Bazaar\" Rohingya host baseline survey 5020 households microdata World Bank 2019",
    "action": {
      "type": "search",
      "query": "\"Cox's Bazaar\" Rohingya host baseline survey 5020 households microdata World Bank 2019",
      "queries": [
        "\"Cox's Bazaar\" Rohingya host baseline survey 5020 households microdata World Bank 2019",
        "\"Bangladesh\" \"Cox's Bazaar\" \"Rohingya\" \"baseline survey\" \"5020\" \"microdata\"",
        "\"The baseline survey of 5,020\" \"Cox\" \"Rohingya\""
      ]
    }
  }
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "item.started",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d2cdb8c8191ba4f8af1de80cc5a",
    "type": "web_search",
    "query": "",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "item.completed",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d2cdb8c8191ba4f8af1de80cc5a",
    "type": "web_search",
    "query": "https://github.com/worldbank/iQual",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "item.started",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d2f6c888191a82c60c765a39223",
    "type": "web_search",
    "query": "",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "item.completed",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d2f6c888191a82c60c765a39223",
    "type": "web_search",
    "query": "https://raw.githubusercontent.com/worldbank/iQual/main/LICENSE.md",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "item.started",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d32d92c81919a9b62779f3842a8",
    "type": "web_search",
    "query": "",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "item.completed",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d32d92c81919a9b62779f3842a8",
    "type": "web_search",
    "query": "https://journals.sagepub.com/doi/10.1177/00491241251338246",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "item.started",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d35da608191816edefb5e0a6cb5",
    "type": "web_search",
    "query": "",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "item.completed",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d35da608191816edefb5e0a6cb5",
    "type": "web_search",
    "query": "",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "item.completed",
  "item": {
    "id": "item_20",
    "type": "agent_message",
    "text": "已核验论文页：数据确有访谈文本、human expert codes、LLM annotations 与 respondent covariates，但 transcript 公开性受隐私限制。现在补查补充材料、World Bank/UNHCR 数据页和 iQual 仓库，区分“代码/公开 survey data 可复现”和“文本/标签需申请”。"
  }
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "item.started",
  "item": {
    "id": "item_21",
    "type": "command_execution",
    "command": "/bin/bash -lc \"curl -L --fail --max-time 60 -o /tmp/rohingya_smr_supp.pdf 'https://journals.sagepub.com/doi/suppl/10.1177/00491241251338246/suppl_file/sj-pdf-1-smr-10.1177_00491241251338246.pdf' && pdfinfo /tmp/rohingya_smr_supp.pdf | sed -n '1,20p'\"",
    "aggregated_output": "",
    "exit_code": null,
    "status": "in_progress"
  }
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "item.completed",
  "item": {
    "id": "item_21",
    "type": "command_execution",
    "command": "/bin/bash -lc \"curl -L --fail --max-time 60 -o /tmp/rohingya_smr_supp.pdf 'https://journals.sagepub.com/doi/suppl/10.1177/00491241251338246/suppl_file/sj-pdf-1-smr-10.1177_00491241251338246.pdf' && pdfinfo /tmp/rohingya_smr_supp.pdf | sed -n '1,20p'\"",
    "aggregated_output": "  % Total    % Received % Xferd  Average Speed  Time    Time    Time   Current\n                                 Dload  Upload  Total   Spent   Left   Speed\n\r  0      0   0      0   0      0      0      0                              0\ncurl: (22) The requested URL returned error: 403\n",
    "exit_code": 22,
    "status": "failed"
  }
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "item.started",
  "item": {
    "id": "item_22",
    "type": "command_execution",
    "command": "/bin/bash -lc \"curl -L --fail --max-time 60 -o /tmp/ashwin_2022_iqual.pdf 'https://documents1.worldbank.org/curated/en/099759305162210822/pdf/IDU0a357362e00b6004c580966006b1c2f2e3996.pdf' && pdfinfo /tmp/ashwin_2022_iqual.pdf | sed -n '1,20p'\"",
    "aggregated_output": "",
    "exit_code": null,
    "status": "in_progress"
  }
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "item.started",
  "item": {
    "id": "item_23",
    "type": "command_execution",
    "command": "/bin/bash -lc \"curl -L --fail --max-time 60 -o /tmp/cbps_meta.html 'https://microdata.unhcr.org/index.php/catalog/822/study-description' && wc -c /tmp/cbps_meta.html && rg -n \\\"Data Collection|Access|Sampling|Questionnaires|strata|settlement_type|stratum|License|Citation\\\" /tmp/cbps_meta.html | head -60\"",
    "aggregated_output": "",
    "exit_code": null,
    "status": "in_progress"
  }
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "item.started",
  "item": {
    "id": "item_24",
    "type": "command_execution",
    "command": "/bin/bash -lc \"curl -L --fail --max-time 60 -o /tmp/iqual_tree.txt 'https://api.github.com/repos/worldbank/iQual/git/trees/main?recursive=1' && rg '\\\"path\\\"' /tmp/iqual_tree.txt | sed -n '1,160p'\"",
    "aggregated_output": "",
    "exit_code": null,
    "status": "in_progress"
  }
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "item.completed",
  "item": {
    "id": "item_24",
    "type": "command_execution",
    "command": "/bin/bash -lc \"curl -L --fail --max-time 60 -o /tmp/iqual_tree.txt 'https://api.github.com/repos/worldbank/iQual/git/trees/main?recursive=1' && rg '\\\"path\\\"' /tmp/iqual_tree.txt | sed -n '1,160p'\"",
    "aggregated_output": "\r100  14827   0  14827   0      0  48952      0                              0\r100  14827   0  14827   0      0  48936      0                              0\r100  14827   0  14827   0      0  48921      0                              0\n      \"path\": \".github\",\n      \"path\": \".github/workflows\",\n      \"path\": \".github/workflows/gh-pages.yml\",\n      \"path\": \".gitignore\",\n      \"path\": \"LICENSE.md\",\n      \"path\": \"README.md\",\n      \"path\": \"docs\",\n      \"path\": \"docs/_config.yml\",\n      \"path\": \"docs/_toc.yml\",\n      \"path\": \"docs/requirements.txt\",\n      \"path\": \"notebooks\",\n      \"path\": \"notebooks/Getting Started.ipynb\",\n      \"path\": \"notebooks/Model Training.ipynb\",\n      \"path\": \"notebooks/README.md\",\n      \"path\": \"notebooks/advanced\",\n      \"path\": \"notebooks/advanced/Model-Bootstrap.ipynb\",\n      \"path\": \"notebooks/advanced/Model-MultipleAnnotations.ipynb\",\n      \"path\": \"notebooks/advanced/Model-MultipleClassifiers.ipynb\",\n      \"path\": \"notebooks/advanced/Model-MultipleVectorizers.ipynb\",\n      \"path\": \"notebooks/advanced/README.md\",\n      \"path\": \"notebooks/basic\",\n      \"path\": \"notebooks/basic/Model-SavedDictionary.ipynb\",\n      \"path\": \"notebooks/basic/Model-SentenceTransformers.ipynb\",\n      \"path\": \"notebooks/basic/Model-Sklearn.ipynb\",\n      \"path\": \"notebooks/basic/Model-SpaCy.ipynb\",\n      \"path\": \"notebooks/basic/README.md\",\n      \"path\": \"notebooks/bias\",\n      \"path\": \"notebooks/bias/BiasTest.ipynb\",\n      \"path\": \"notebooks/bias/README.md\",\n      \"path\": \"notebooks/efficiency\",\n      \"path\": \"notebooks/efficiency/EfficiencyTest.ipynb\",\n      \"path\": \"notebooks/efficiency/README.md\",\n      \"path\": \"notebooks/interpretability\",\n      \"path\": \"notebooks/interpretability/InterpretabilityTest.ipynb\",\n      \"path\": \"notebooks/interpretability/Interpretability_Increasing_N_h.ipynb\",\n      \"path\": \"notebooks/interpretability/README.md\",\n      \"path\": \"notebooks/interpretability/RegressionCoefficientTest.ipynb\",\n      \"path\": \"requirements.txt\",\n      \"path\": \"setup.py\",\n      \"path\": \"src\",\n      \"path\": \"src/iqual\",\n      \"path\": \"src/iqual/__init__.py\",\n      \"path\": \"src/iqual/crossval.py\",\n      \"path\": \"src/iqual/estimation.py\",\n      \"path\": \"src/iqual/evaluation.py\",\n      \"path\": \"src/iqual/feature_transform.py\",\n      \"path\": \"src/iqual/iqualnlp.py\",\n      \"path\": \"src/iqual/preprocessing.py\",\n      \"path\": \"src/iqual/tests.py\",\n      \"path\": \"src/iqual/utils.py\",\n      \"path\": \"src/iqual/vectorizers.py\",\n",
    "exit_code": 0,
    "status": "completed"
  }
}
```

---

### Runtime record

_source line 49_

```json
{
  "type": "item.completed",
  "item": {
    "id": "item_22",
    "type": "command_execution",
    "command": "/bin/bash -lc \"curl -L --fail --max-time 60 -o /tmp/ashwin_2022_iqual.pdf 'https://documents1.worldbank.org/curated/en/099759305162210822/pdf/IDU0a357362e00b6004c580966006b1c2f2e3996.pdf' && pdfinfo /tmp/ashwin_2022_iqual.pdf | sed -n '1,20p'\"",
    "aggregated_output": "\r100  1.86M   0  1.86M   0      0  3.67M      0                              0\r100  1.86M   0  1.86M   0      0  3.66M      0                              0\r100  1.86M   0  1.86M   0      0  3.66M      0                              0\nTitle:           World Bank Document\nAuthor:          World Bank Group\nCreator:         LaTeX with hyperref\nProducer:        pdfTeX-1.40.23 / PDF PT 4.7.24.2 (pdf-tools.com)\nCreationDate:    Mon Feb 20 07:10:15 2023 UTC\nModDate:         Wed Feb 22 15:40:56 2023 UTC\nCustom Metadata: yes\nMetadata Stream: yes\nTagged:          no\nUserProperties:  no\nSuspects:        no\nForm:            none\nJavaScript:      no\nPages:           86\nEncrypted:       no\nPage size:       612 x 792 pts (letter)\nPage rot:        0\nFile size:       1959945 bytes\nOptimized:       yes\nPDF version:     1.4\n",
    "exit_code": 0,
    "status": "completed"
  }
}
```

---

### Runtime record

_source line 50_

```json
{
  "type": "item.completed",
  "item": {
    "id": "item_23",
    "type": "command_execution",
    "command": "/bin/bash -lc \"curl -L --fail --max-time 60 -o /tmp/cbps_meta.html 'https://microdata.unhcr.org/index.php/catalog/822/study-description' && wc -c /tmp/cbps_meta.html && rg -n \\\"Data Collection|Access|Sampling|Questionnaires|strata|settlement_type|stratum|License|Citation\\\" /tmp/cbps_meta.html | head -60\"",
    "aggregated_output": "\ncurl: (22) The requested URL returned error: 403\n",
    "exit_code": 22,
    "status": "failed"
  }
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "item.started",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d4adf6c8191874e0264018cd26d",
    "type": "web_search",
    "query": "",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "item.completed",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d4adf6c8191874e0264018cd26d",
    "type": "web_search",
    "query": "",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "item.started",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d4e10508191bc2a06f7974782b5",
    "type": "web_search",
    "query": "",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "item.completed",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d4e10508191bc2a06f7974782b5",
    "type": "web_search",
    "query": "site:dataverse.harvard.edu Cox's Bazar Panel Survey Baseline 2019 HARVARD_DATAVERSE_BGD_2019_CBPS_v2.1",
    "action": {
      "type": "search",
      "query": "site:dataverse.harvard.edu Cox's Bazar Panel Survey Baseline 2019 HARVARD_DATAVERSE_BGD_2019_CBPS_v2.1",
      "queries": [
        "site:dataverse.harvard.edu Cox's Bazar Panel Survey Baseline 2019 HARVARD_DATAVERSE_BGD_2019_CBPS_v2.1",
        "\"Cox's Bazar Panel Survey Baseline, 2019\" \"Harvard Dataverse\""
      ]
    }
  }
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "item.started",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d54799481919dbf857b3c3ac721",
    "type": "web_search",
    "query": "",
    "action": {
      "type": "other"
    }
  }
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "item.completed",
  "item": {
    "id": "ws_07d8fe17869e379d016a1c5d54799481919dbf857b3c3ac721",
    "type": "web_search",
    "query": "",
    "action": {
      "type": "other"
    }
  }
}
```

---
