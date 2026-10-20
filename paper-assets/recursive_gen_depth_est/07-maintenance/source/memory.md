# Project Memory

## Paper Placeholder Values (2026-05-15)

Computed from experimental data for paper XX.X% placeholders:

### 1. d0-excluded 3-class accuracy range (abstract.tex L5)
- **58.8%–82.6%** across 9 cells
- Source: `granularity_ablation_rf_001` registry entry, per_cell 3class acc
- Min: pythia_topk50 = 58.83%, Max: gpt2xl_temp09 = 82.60%

### 2. Cross-strategy LOO d1-d3 accuracy (generalization.tex L95)
- **45.9%** (mean across 9 folds)
- Source: confusion matrices in `w6_cross_strategy_per_class_recall.json`
- Method: (d1_correct + d2_correct + d3_correct) / 15000 per fold, then averaged
- Note: 4-class mean was 59.1%; d0's near-perfect accuracy inflates it. Excluding d0 drops to 45.9%.
- Range across folds: 35.4% (pythia_topk50) to 59.1% (pythia_nucleus)

### Artifact
- `artifacts/placeholder_values.json` — full breakdown with per-fold numbers

## Downstream Curation PoC Insights (2026-05-15)

### Oracle ≤ Unfiltered（反直觉发现）
- 完美 depth 筛选（oracle）反而不优于 unfiltered 全量数据：oracle_strict PPL 15.879 vs unfiltered 15.776（p=0.22）
- 原因推测：纯按 depth 筛选过度移除了有用的多样性，RF 的分类误差反而保留了有价值的变异
- **Framing 含义**：不能 claim "RF approximates oracle"，应 claim "data efficiency"（RF 用 44% 数据 ≈ 全量 PPL）

### rf_moderate 统计检验偏差
- 我们的 t=-3.77 (p=0.02) vs Reviewer 手算 t=-5.58 (p=0.005)
- 其余 3 组对比偏差 <8%，此组偏差较大，以原始数据直接计算为准
- 定性结论一致（均显著），不影响 claim

## ⚠️ Wild Data 解读约束 C004 (2026-05-17)

**硬约束**：wild data RF 分类结果的 d1+ 预测是 OOD 假阳性率（FPR），不是 AI contamination 证据。
- C4 FPR 34%、FineWeb FPR 17%：差异来自 FineWeb 质量过滤去除了特征异常文本，不代表 C4 有更多 AI 内容
- C4 采集于 2019 年 Common Crawl，彼时几乎不存在 LLM 生成内容
- 论文中**禁止**说 "contamination"、"AI-generated content detected"
- 正确 framing：method limitation + calibration gap
- 教训：不要将分类器在 OOD 数据上的预测当作真实标签解读

## Downstream Benchmark v2 结论 (2026-05-17)

- d0_only 并非最优训练数据（PPL 5.65），d1_only 最低（5.55）
- PPL 差异极小（max 0.12），500 条训练不足以达到统计显著性
- **论文 framing**：exploratory/pilot analysis，放 Discussion 或 Appendix，claim 强度为 "we observe that..."
- 确定信号：train_loss 单调递减（d0 2.558 > d1 1.920 > d2 1.286），支持 "递归生成降低信息量"
- 不是 main contribution

## Learned Estimator 结论翻转 (2026-05-17)

- learned_estimator_001 (negative) → learned_estimator_002 (success)
- 根因：Proto NaN 导致 gpt2xl holdout 结果损坏，修复后 proto gpt2xl 68.35% > RF 66.4%
- XGBoost mean 67.18% 最强，Proto 单项最高（olmo 70.01%）
- Pythia holdout 对所有方法最难（61-64%），可能因 Pythia 文本分布与 olmo/gpt2xl 差异较大
- 教训：NaN/Inf 在距离度量中静默传播，需要在 cdist/softmax 管道中添加防御性 clamp

## Feature Importance & RF Stability (2026-05-17)

### RF Seed Robustness
- 3 seeds (42/123/456) mean 4-class accuracy: **66.48% ± 0.06%** — 种子对结果几乎无影响，RF 高度稳定

### Feature Importance Ablation
- **Perplexity 组 (9 features) 单独达到 66.0%**，仅比全 19 特征低 0.5pp — 是绝对主导特征组
- Entropy/Surprisal 组 (5 features): 63.2%，贡献中等
- Repetition/Diversity 组 (5 features): 53.0%，最弱但仍显著高于 25% chance
- **Top-2 特征占总 importance 41%**：p90_ppl (22.4%) + var_surprisal (18.8%)
- mean_ppl 和 var_ppl importance 接近零（被 percentile 特征替代）
- **论文含义**：perplexity degradation is the dominant signal — 与 feature bottleneck 结论一致，更复杂分类器无法显著超越 RF 因为信息集中在少数 perplexity 特征

## Wild Data Calibration 跨数据集一致性 (2026-05-16)

- Web-crawl FPR ~20% 是跨数据集一致的现象（C4=20.2%, FineWeb=19.5%, Δ<1pp），由模板/SEO 内容驱动
- 编辑质量文本（WikiText）FPR 稳定 0%
- 所有 web-crawl 误分类均为 d1（无 d2/d3 false positives），误分类程度温和
- AutoDL 代理下 HF streaming/大文件下载不可靠，改用 hf-mirror.com 下载 parquet 可绕过（FineWeb 2GB/114s）

## LLM Zero-Shot Failure Modes (2026-05-16)

- 两个 LLM（DeepSeek-v3.2 36.2%, Qwen2.5-7B 30.4%）均远低于 RF 78.2%，验证 zero-shot 一般性劣势
- 不同 LLM 的 failure mode 截然不同：DeepSeek 几乎全猜 d0（recall 95.2%），Qwen 偏向 d1（recall 55.2%）但 d0 recall 仅 26.4%
- 共同点：都无法捕获深层递归信号（d2/d3 recall 均很低）
- 论文叙事：两个模型的不同 failure pattern 说明这不是 prompt 偏差问题，而是 LLM zero-shot 根本无法访问 depth 所需的统计特征（surprisal distribution）

## Multi-τ Ablation 关键洞察 (2026-05-16)

### Memorization-as-prerequisite 机制
- τ=1.1 崩溃的根因不是"特征变了"而是"特征消失了"：高温使 token 分布过于随机，模型无法学习自身输出模式，depth-dependent 的 memorization 效应不再发生
- 训练 loss 是直接证据：τ=0.5 时 loss 2.27→0.42→0.16（快速 memorization），τ=1.1 时 loss 2.27→1.91→1.85（几乎不降）
- **论文含义**：depth signal 的存在前提是递归训练会改变模型——当温度太高时训练数据等同于随机噪声，模型不变，depth 无可探测

### τ 鲁棒性范围
- τ ∈ [0.5, 0.9] 均 d1v2 AUC > 0.80，depth signal 不是单一温度伪影
- τ=0.7 是 d1v2 AUC 峰值（0.851），接近 nucleus p=0.95 的 0.861
- 这回答了 Reviewer R2-W3 的关切：depth signal 跨温度鲁棒，但有上界

### Cross-τ 不可迁移性
- Cross-τ LOO mean acc=46.7%，与 cross-strategy LOO (59.1%) 一致但更差
- 原因：不同 τ 产生不同的 surprisal distribution 形状，feature space 不可直接对齐
- 与论文现有 "strategy-dependent feature space" 叙事一致，multi-τ 提供了同一 strategy（temperature）内部的细粒度证据

## Instruction-Tuning 正则化发现 (2026-05-16)

### 核心发现（D032）
- 原假设错误：以为 IT 引入 U-shape → 实际 BASE 本身就有 U-shape
- 正确解读：IT **正则化** depth signal（使 AUC 单调递减），而非引入伪影
- 证据对比：BASE AUC d2v3=0.6815 (dip) → d3v4=0.73 (recovery) = U-shape; Instruct AUC 单调递减 0.949→0.877→0.771→0.716→0.618
- **论文含义**：IT 不是 confound 而是有利条件，移除了关于"所有实验用 IT 模型是否引入系统偏差"的审稿顾虑

### EDD Bug 教训
- `llama3_eval.py` 硬编码阈值 0.55 而非项目标准 0.70，导致初始 EDD 报告为 ">5" 而非正确的 EDD=3
- **规则**：任何 eval 脚本中的 EDD 阈值必须参数化并默认 0.70，不得硬编码
- 影响范围：仅 BASE 实验的 eval 路径受影响；cross_scale_llama3_8b_003 使用了正确阈值（验证通过）

## Text Length Sensitivity Analysis (2026-05-17)

### 实验配置
- 3 models (pythia, olmo, gpt2xl) × 3 strategies (nucleus, temp09, topk50) = 9 cells
- 50 samples/depth/cell, 4 depths, total 1800 samples
- Tokenizer/model: pythia-1.4b (CPU, float32)
- 截断长度: 50, 100, 200, 500 tokens
- RF 5-fold CV, 200 estimators, seed=42

### 结果摘要

| Truncation | 4-class Acc | 3-class Acc | d0 recall | d1 recall | d2 recall | d3 recall |
|-----------|------------|------------|-----------|-----------|-----------|-----------|
| 50 tokens | 51.5% | 65.0% | 82.9% | 47.2% | 28.0% | 47.8% |
| 100 tokens | 56.3% | 72.8% | 89.8% | 54.3% | 27.5% | 53.4% |
| 200 tokens | 60.4% | 74.9% | 92.0% | 56.0% | 35.3% | 57.0% |
| 500 tokens | 61.0% | 78.9% | 93.8% | 66.9% | 42.7% | 55.2% |

### 关键洞察
- **50 tokens 已可检测 depth signal**：4-class 51.5% 显著高于 chance (25%)，d0 recall 82.9%
- **收益递减**：50→200 tokens 提升 ~9pp（51.5→60.4%），200→500 仅 +0.7pp（60.4→61.0%）
- **3-class（排除 d0）持续提升**：50→500 从 65.0% 到 78.9%，说明更长文本对区分深层 depth 更有价值
- **d2 始终最难**：即使 500 tokens 也仅 42.7% recall，是分类瓶颈
- **实用意义**：200 tokens 是性价比拐点，足够用于实际 depth estimation pipeline

## qwen25_14b_scale_002 诊断 (2026-05-17)
- 失败原因：模型下载阶段 aria2 遇到 SSL/TLS handshake failure，shard 5/8 下载中断导致脚本 EXIT_CODE=1
- 详细错误：`[SocketCore.cc:1018] errorCode=1 SSL/TLS handshake failure: The TLS connection was non-properly terminated.` — 下载 model-00005-of-00008.safetensors 时与 cas-bridge.xethub.hf.co 的 TLS 连接被异常终止
- 当前状态：shards 1-3 完整，shard 4 下载中（有 .aria2 控制文件），shards 5-8 缺失；磁盘空间充足（103GB 可用）
- 修复建议：重新提交实验即可，脚本已有 skip-existing 逻辑会跳过已下载的 shards；或在脚本中为 aria2 添加 `--max-tries=5 --retry-wait=10` 重试参数防止瞬态网络故障

## ⚠️ Table 2 数据口径不一致 (2026-05-18)

### 排查结论
- Table 2 主表 4-class 数字实际来自 **80/20 split + 100 trees + StandardScaler**，但 caption 声称 "5-fold CV, 200 trees"
- Table 2 括号 d1-d3 数字**无单一 JSON 来源**——在项目开发不同阶段分批计算，各 cell 可能用了不同 RF 配置
- Abstract 71.1% 使用口径 A（4-class RF, 5-fold CV, 200 trees 的 d1-d3 balanced accuracy），与 Table 2 实际口径不一致

### 统一重跑（RF-200, 5-Fold CV, No Scaler）
- 全 9 cells 重跑完成，存于 `results/table2_rerun_5foldcv.json`
- Mean 4-class: 78.44% | Mean d1-d3 BalAcc: 71.63%
- 与旧 Table 2 主表差异 <1pp（大部分），最大差异 olmo_nucleus d1-d3 -2.4pp
- 待 Director 决策是否替换

## 21-Feature Augmented RF 洞察 (2026-05-18)

### Min-K% 是互补特征，DetectGPT 是冗余特征
- Min-K% K=20 score 加入 19-feature RF 后 rank #3（importance 0.0952），仅次于 p90_ppl 和 var_surprisal
- 说明 token-level log-prob 最低 K% 均值捕获了 passage-level 统计特征未完全覆盖的信息
- DetectGPT perturbation discrepancy rank #17/21（importance 0.0255），几乎无增量贡献
- **论文含义**：统计特征已捕获绝大部分 depth 判别信息；Min-K% 提供温和互补（+0.48pp），DetectGPT 完全冗余——强化 "depth estimation ≠ binary detection" 论点
- **决策待定**：是否将 20-feature (+Min-K%) 作为正式配置，还是保持 19-feature 并将此结果放 ablation

## ⚠️ Accumulation 实验方法论错误 M008/M009 (2026-05-19)

### 错误描述
accum_mix50 和 accum_mix25 两次实现都犯了**同一个根本性错误**：在特征空间做混合（把 d0 的 features 直接塞进 d1/d2/d3 类，保留 depth label）。这不是 accumulation，是标签污染。
- 结果（35.5% / 67.2%）是标签污染的伪影，不反映真实 accumulation degradation
- 两个实验 registry 已标记 conclusion=failed, notes=INVALIDATED

### 正确 accumulation pipeline
真正的 accumulation 需要在**文本层面**混合，每个 depth 都需要完整的：
1. 构造混合训练语料（raw text: human + 前一 depth 的 synthetic text）
2. LoRA 微调 GPT-2 XL（从 base model 重新开始）
3. 用微调后模型生成新文本
4. 提取 19 个统计特征
5. 预计每个 depth ~2-3h（LoRA + generation），3 depths ≈ 6-9h

### 教训
- **"accumulation" 不是特征空间操作**——它是训练数据层面的操作，涉及模型重新训练
- 如果实验 <1h 完成且不需要 GPU，说明实现有误
- 关键操作（accumulation、fine-tuning 等）的实现方案必须经 Reviewer 审查后再执行

## Accumulation v3 结果 (2026-05-19)

### mix25 与 mix50 结果 comparable
- mix25（25% human + 75% synthetic）70.1% 4-class，mix50（50% human + 50% synthetic）69.1%
- **1.0pp 差异在 seed 噪声范围内**（跨 seed 方差 2.04pp），不应做方向性解读
- 两者均为 ~69-70%，comparable
- 两者均显著低于 full-replacement baseline **84.2%**（GPT-2 XL nucleus seed42），delta 约 -15.1pp / -14.1pp
- **论文含义**：Discussion §6 可报告 accumulation 降低了约 14-15pp 的分类精度，但 mix ratio 的影响在统计上不可区分
- **d2 是跨所有 accumulation 比例的一致瓶颈**（~42% recall），与 full-replacement 实验中 d2 最难的 pattern 一致，说明 d2 困难性是 depth signal 的内禀属性而非 accumulation 引入

## MDD 计算发现 (2026-05-19)
- MDD = EDD 在所有 12 个 profile 上成立（AUC 严格单调递减，无 U 型）
- MDD 不提供超越 EDD 的额外信息——depth signal 衰减是纯累积性的
- 唯一非单调 profile: Qwen2.5-1.5B-Instruct（atlas 外），但所有 pairs < 0.70，MDD=EDD=0
- d4v5 AUC 跨模型收敛到 0.681-0.684（range 仅 0.003）→ signal 消失边界

## DeBERTa vs RF: "Simple Features Beat Neural" (2026-05-19)

### 核心结果
- DeBERTa-v3-base (LoRA, r=8, query_proj+value_proj) on gpt2xl_temp09: **53.1% ± 2.0%** (5-fold CV)
- RF + 19 statistical features on same cell: **78.2%**
- Gap: **25.1pp** — hand-crafted perplexity features 远优于 end-to-end neural representations

### DeBERTa 失败模式
- 极端类容易：d0 recall 81.2%, d3 recall 94.2%
- 中间类崩塌：d1 recall 28.8%, d2 recall 8.4%
- 主要错误模式：d1→d3 (2221/5000), d2→d3 (4274/5000) — 模型只学会 "极端 vs 非极端"
- **解读**：DeBERTa 的文本表征能区分 "human vs heavily recursive" 但无法捕捉中间 depth 的细微 perplexity distribution 差异

### 论文含义
- "RF ≥ DeBERTa" 不是 RF 的局限——是 paper insight："depth signal 藏在 perplexity 分布的统计特征里，不在表面文本 pattern 里"
- DeBERTa 中间类崩塌 + RF 全类相对均衡 = feature engineering 本身就是方法贡献
- 写入 §5 Results 或 Discussion，~2-3 句 + 一行对比数据

## ⚠️ Worker 远程脚本部署失败教训 (2026-05-19)

### 问题
Worker spawn 写远程脚本连续两次声称 "部署成功+验证通过"，但文件实际不存在于目标服务器。根因：Worker 在 worktree 隔离环境中执行 ssh_execute，工具可能未真正连接到远程服务器，或 heredoc 写入被隔离环境拦截。

### 正确做法
- **关键脚本部署用 scp**：本地写好脚本 → `scp` 到远程 → ssh 验证（ls + py_compile + --help）
- 不依赖 Worker 的 ssh_execute + heredoc 写文件——这条路径不可靠
- 部署后必须独立验证（ssh 直连确认文件存在 + 可编译 + 可运行）

### 额外发现
- westd-48862 上 transformers 5.8.1 的 `from_pretrained()` 不接受绝对路径（`/root/...`），报 `HFValidationError`
- 解决：用 HuggingFace model ID (`microsoft/deberta-v3-base`) + `HF_ENDPOINT=hf-mirror.com` + `HF_HOME=/root/autodl-tmp/.hf_cache`
- westd-48862 上无 DeBERTa 模型缓存，首次运行需在线下载（~500MB）

## ⚠️ Binoculars Ordinal Depth: 假设被证伪 (2026-05-19)

### 核心发现
- **假设**：Binoculars cross-perplexity (observer=pythia-1.4b, performer=pythia-410m) 在 4-class ordinal depth 上接近 chance (25%)
- **实际结果**：假设被证伪。Binoculars 包含强 ordinal depth 信号

### 9-cell 平均 accuracy（5 种 calibration 方法）
| Method | 4-class Acc | d1-d3 BalAcc |
|--------|------------|-------------|
| equal_width (no learning) | 48.8% | 41.7% |
| CORAL (ordinal regression) | 38.1% | 50.8% |
| threshold (learned) | 69.8% | 60.2% |
| RF_single (Bino score only) | 63.7% | 53.4% |
| RF_multi (11 features) | 78.1% | 71.2% |

### 与其他 baselines 对比
- Random chance: 25%
- DetectGPT: 29.1% (near chance)
- Min-K%: 33.2% (slightly above chance)
- **Binoculars equal_width: 48.8%** — 几乎 2x chance
- **Binoculars RF_multi: 78.1%** — 与我们的 RF-19 (78.4%) 相当

### 关键洞察
- Cross-perplexity ratio 编码 depth 信息：递归生成的 distributional drift 导致 observer/performer PPL 比值系统性变化
- RF_multi 用 11 个 perplexity 统计特征（bino_score, ppl_mean/var/median/p10/p90/skew, xppl_mean/var/median, bino_score_median），本质上是另一种 perplexity-based feature engineering
- **RF_multi 78.1% ≈ 我们的 RF-19 78.4%**：Binoculars-derived features 几乎追平了我们的方法

### 论文含义
- **不能** claim "binary detection methods can't do ordinal depth"
- 必须调整 narrative："Binoculars partially succeeds at ordinal depth when augmented with calibration, but requires a specific model pair (observer/performer) — our 19 statistical features are model-agnostic and don't need a second reference model"
- Binoculars 是 strongest baseline — 论文 Table 中需要如实对比
- topk50 cells 是 Binoculars 最弱的方向（pythia_topk50 68.1%、olmo_topk50 70.5%、gpt2xl_topk50 73.5%），可能是因为 top-k 截断使 perplexity ratio 信息丢失
