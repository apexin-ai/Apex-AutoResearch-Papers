# Memory — agent_progress_probe

> 非 metrics 性质的决策原因、约束、经验教训

## Cycle Detector Cross-Agent Collapse (2026-05-16, 重大)
- Cycle detector (n-gram) 在 SWE gold 上与 GB 打平 (0.841 vs 0.839)，但跨 agent (OH) 彻底失败
- OH 上 3-gram F1=0.530 (all) / 0.592 (conf≥2)，f1_stag 仅 0.19/0.28
- Oracle 调参天花板: 0.552 / 0.614——即使完美 threshold 也无法救
- Structural GB OH: 0.967 / 0.992，差距 43.7pp
- **结论**: cycle detection 只捕捉表面重复，structural features 的 30-dim representation 编码了 cycle detector 无法表示的跨 agent 泛化信号
- 这确认了 paper headline: cross-agent transfer IS the genuine contribution

## ACR Adapted LF 发现 (2026-05-16)
- action_entropy 是 ACR 上唯一有效的 stag 触发器 (88.3% sole trigger)
- output_stagnation 和 error_repetition 在 ACR 上零覆盖——search-based agent 不产生这类模式
- RF 从 adapted labels 获益 +10.4pp, GB 反而退化 -3.6pp (过拟合原始分布)
- 启示: LF portability 是 cross-agent transfer 的关键维度，不同模型对 label shift 敏感度不同

## Non-SE Domain Transfer (2026-05-16)
- ALFWorld (household robot): 23/30 features 可迁移, 6 个 SE-specific (file_diff 类)
- 核心方法是 domain-general，不限于 SE 场景
- ToolBench 和 ATBench 有 parsing issues (conversations field / key mismatch)，需 fix 后才能评估

## C3 TLM Conditional Finding (2026-05-16, 重大)
- **原 C3 "TLM 全部 negative" 已推翻。** 6-LF regime (42% conflict) 下 HMM gold F1=0.784, +6.46pp over MV (0.719)
- 关键洞察：TLM 价值取决于 LF 多样性/冲突率。3-LF 15% conflict → MV 足够；6-LF 42% conflict → HMM 显著优于 MV
- 6-LF MV gold F1 (0.719) 低于 3-LF MV (0.798)——更多 LF 不自动改善 MV，但为 TLM 提供消歧信号
- 3-LF vs 6-LF 的 conf≥2 对比方法学不完全可比（cross-eval vs 直接对齐），但 gold F1 对比同口径
- 论文 narrative: "practitioners should design diverse LFs before applying TLM"

## LLM Judge Cross-Agent Collapse (2026-05-16)
- LLM few-shot-CoT on OH: 0.470 (SWE 上 0.799, -32.9pp)。SWE few-shot examples 在 OH 上是 negative transfer
- Zero-shot (0.491) 反而比 CoT (0.470) 好——示例 misleading
- f1_stag 近乎 random (0.134/0.055)——LLM 几乎无法检测 OH stagnation
- Structural GB OH: 0.967, advantage +47.6pp

## ACR Third Agent Architecture Gap (2026-05-16)
- AutoCodeRover (AST-based search agent) 与 SWE-Agent/OpenHands 架构差异大
- file_diff_delta LF 在 ACR 上 0% 触发（search agent 不编辑文件）
- GB SWE→ACR: 0.608 (-38.7pp)，LR 更鲁棒 (0.671)
- ACR stag rate 极低 (10.1%), conf≥2 仅 5 stag samples

## Gold 3-Annotator 最终结果 (2026-05-15, canonical)
- 3 annotators, N=512 total, 3 subsets: Set A (conf≥3, N=52), Set B (conf≥2, N=505), Set C (all, N=512)
- Set A 太小无法产生显著性结果（全部 p>0.25）——最小可用 gold set 需 N~500
- Set B 和 Set C 高度一致（<0.3pp 差异），conf≥2 是合理的 primary evaluation scope
- **Silver-Gold gap**: GB silver 0.9919 → gold 0.8394 = 15.3pp gap，量化了 LF noise floor
- **Gold 上排序变化**: TWV Probe (0.854) > GB (0.839) 但 p=0.056 不显著。Silver 上 GB 显著领先——gold 上 embedding 方法更有竞争力
- 这意味着 silver eval 系统性低估了 embedding-based 方法（TWV Probe）相对于 structural methods 的竞争力

## Gold Set 评估 3-Bug 修复 (2026-05-15)
修复了三个导致 gold set 数字不可信的 bug，全部在 `evaluate_gold_set.py` 和 `gold_bootstrap_ci.py` 中：
1. **超参数不匹配**：GB lr=0.1→0.05, RF n_estimators=200→100（canonical 值来自 `bootstrap_table2_matched.py`）
2. **训练集数据泄漏**：structural 模型训练未排除 gold windows（39 个），通过 `wid_to_noabs_idx` 映射排除
3. **OH 轨迹缺失**（仅 bootstrap）：`gold_bootstrap_ci.py` 只加载 SWE 轨迹，OH windows 特征全零 → GB 预测 progress 碰巧匹配 → F1 膨胀 3.8pp
- **教训**：跨脚本复制评估逻辑时必须确保数据加载路径一致（eval 有 OH，bootstrap 缺 OH）

## LLM Structural Input 实验教训 (2026-05-15)
给 LLM 提供 30 维 structural features 作为 prompt 输入（0.688）反而不如纯 few-shot（0.751）。LLM 无法将数值型结构特征转化为有效判断——支持 "structural signal requires feature engineering, not NL reasoning" 论点。

## CMI=0 不适合直接引用 (2026-05-15)
CMI(X_residual; Y | X_LF) = 0 是数学必然（Y = MV(LFs)），不是实验发现。若写入论文会被审稿人误读为 "residual features 没有信息"。应改用 feature-overlap-ablation (11/19 split) 来回应 circularity。

## OH 数据口径 (2026-05-15)
- JSONL: 150,652 windows, 43,376 conf≥2, stag rate 20.87%（非 abstain 口径）
- embeddings_fixed.pt: 143,057 windows, 43,366 conf≥2, stag rate 21.45%
- Paper 用 JSONL 口径: 150,652 / 20.9% / 43,376

## Structural GB 0.998 vs 0.9919 (2026-05-15)
Registry 中 0.9984 实际是 RF f1_progress，不是 GB macro_f1。Canonical GB conf≥2 macro_f1 = 0.9919。

## Camera-Ready BibTeX 修复清单 (2026-05-15, 低优先级)
- `ratner2017snorkel`: key 含 2017 但 year=2018，需统一
- `dawid1979em`: 缺 volume/pages
- 多处 "and others" 需补全完整作者列表
