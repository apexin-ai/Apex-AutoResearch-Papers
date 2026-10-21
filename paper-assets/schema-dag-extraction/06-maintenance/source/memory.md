# Memory — schema-dag-extraction

## DocRED expanded: interaction reversed, R² increased (2026-05-19)
- 原 n=5 per condition: interaction=+5.7pp CI[-1.6, 13.0], R²=0.525 (count16)
- 扩展 n=15 per condition (n=55 per count level): interaction=-9.4pp CI[-12.9, -6.0], R²=0.653 (count16), R²=0.614 (count32)
- **方向翻转**: 从不确定(+5.7pp, CI 含零)变为确定 sub-additive(-9.4pp, CI 不含零)
- BCS effect 从 -25.0pp (count16) 衰减到 -15.7pp (count32)，符合 floor compression
- **教训**: 小样本(n=5)的交互估计极不稳定，符号都可以翻转
- 论文范围从 "22-53%" 更新为 "22-65%"

## MAVEN SDGD: merge amplification 跨任务确认 (2026-05-19)
- Single-pass F1=0.207 > SDGD-zero F1=0.123 > random-batch F1=0.111
- Precision collapse 0.287→0.091 (-19.6pp), pred_count inflation 3.7×
- 与 Few-NERD NER 一致：分解策略在所有 span-based tasks 上因 merge amplification 失败
- SDGD-zero 略优于 random (+1.2pp F1)，但均远低于 single-pass

## exp_schema_intervention: renaming 不是有效干预手段 (2026-05-17, negative)
- Renaming 降低两组 accuracy：high-BCS -8.83pp, low-BCS -2.96pp (both p<0.001)
- Interaction 显著 (-5.88pp, p<0.001)：high-BCS 受损更大，但方向是 renaming 损害而非改善
- 根因：LLM 对 original type names 有 strong prior，renaming 引入 label unfamiliarity confound
- Solo sanity check 11/12 通过，但 multi-type batch 中 compound effect 出现 (r=-0.625)
- **教训**：post-hoc renaming 无法分离 SCS 降低效果与 label unfamiliarity，不可用作因果干预
- D059 (Greedy auto-renaming) 基于相同逻辑，也已停止

## TUM proxy 不是运行中的服务 (2026-05-17)
- TUM 是飞书 key 收集机制，不是 API proxy server
- localhost:8001 没有进程监听
- `tum_` 前缀的 token 不是有效的 Google/OpenAI API key
- 本机能直连 Google API（需要真实 Gemini key, 格式 AIza...）
- **教训**：API 实验前必须先验证 (a) proxy 是否运行 (b) key 格式是否匹配目标 API

## Q3 held-out validation: FewRel val-origin SCS-confusion (2026-05-17, CORRECTED)
- 从 80-type confusion matrix 提取 16 val-origin types 的 C(16,2)=120 pairs
- 16 val types 与 64 train types PIDs 完全不重叠
- Val-only Spearman ρ = 0.216, p = 0.018 (显著)
- All-80 Spearman ρ = 0.218, p = 2.2e-35
- Val-only 与全集几乎一致，排除 training-set contamination
- Nonzero subset: val ρ = 0.600 (n=11, p=0.051), all-80 ρ = 0.128 (n=272, p=0.035)
- Top confused val pairs: child↔mother (500, SCS=0.84), child↔spouse (100, SCS=0.71), member of↔part of (100, SCS=0.90)
- 数据源: `/root/schema-dag-extraction/artifacts/q3_val_scs_confusion/q3_val_scs_confusion.json`
- **教训**: 第一个 Q3 worker 做错了（做了 SCS 分布对比而非 confusion correlation），第二个 worker 才做对

## 跨模型 appendix 数据必须同 seed 同批次 (2026-05-17)
- d051 Qwen3 FewRel 有 3 seeds (s42/s123/s456)，每个 seed 不同的 960 samples 和 batch compositions
- 70B 只有 s42。论文 appendix 曾错用三 seed 平均值与 70B s42 并列
- **修正**: 统一用 s42 单 seed（确保同 samples 同 batches）
- 数据源: `artifacts/d051_fewrel_n25_s42/count_curve_summary.json`

## exp_fewshot_bcs_v2 结论 (2026-05-17)
- Few-shot 不缓解 confusability：BCS gap 从 +18.5pp (0-shot) 扩大到 +22.8pp (5-shot)
- High-BCS 组 5-shot vs 0-shot: 0.4875 vs 0.4975 (p=0.483, NS)，demonstrations 完全无效
- Low-BCS 组获益 +3.33pp (p=0.002)，差异增益 4.33pp (p=0.014)
- 0-shot gap 18.5pp vs exp_fewrel_v2_n25 的 25.5pp 差异源于不同 test split，不可直接比较

## NER batch-level BCS-F1 is NULL — r=+0.50/+0.58 was spurious (2026-05-17)
- eval_exp2 的 27 个 batch（seed=54）恰好产生 BCS↔type_frequency 高相关（r=0.53），制造虚假路径 BCS→freq→F1
- 控制 frequency 后，eval_exp2 partial r=0.28 (p=0.16, NS)，d051 partial r=-0.12 (p=0.29, NS)
- d051 数据（75 batches, 3 seeds）的 NER batch-level BCS-F1: r=0.003, p=0.982
- **教训**：25-27 个 random batches 不足以产生可靠相关性估计

## Q5: BCS unique R² after controlling type composition (2026-05-17)
- BCS unique R²=0.259 (36.8%), composition unique=0.298 (42.3%), shared=0.147 (20.9%)
- BCS partial R²=0.467 controlling composition (p=6.8e-15)
- 适用场景：回应审稿人"BCS R² 是否只是 type composition 的 proxy"

## Q3: Logit-scale TOST 灵敏度 (2026-05-17)
- Linear TOST passes (p=0.003), logit TOST inconclusive (p=0.209)
- TOST inconclusive 因 power 不足 (n=69, wide CI)，非 effect size 大

## SDGD Routing 策略全面失败（2026-05-17）
- 所有 practical routing 策略都比 single-pass 更差
- 根因：structured decoding (enum constraint) 在 sub-schema 中强制预测
- **教训**：confidence-based/none-aware routing 在 structured decoding 下不可行

## exp-018 结果与经验（2026-05-16）
- confusability_aware 0.8021 > random 0.7877±0.0178，+1.44pp
- FLASHINFER_DISABLE_VERSION_CHECK=1 需要设置

## exp-017 GPT-4o-mini（2026-05-16, 放弃）
- TUM proxy 不可达，闭源模型验证缺失写入 limitations
- 教训：API 实验需预先确认 proxy 可达性

## 实验数据一致性 (2026-05-17)
- Few-NERD full schema = 66 types (非 64)
- FewRel count levels 包含 count_40
- count=1 是独立 solo baseline

## MAVEN per-type BCS 正相关是 artifact（2026-05-16）
- 控制 log_freq + degree_centrality 后相关消失
- 同质 schema 下 per-type BCS 聚合失效
