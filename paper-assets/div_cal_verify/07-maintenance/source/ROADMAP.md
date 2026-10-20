# div_cal_verify — Research Dashboard

> 最后更新: 2026-05-14 07:28 UTC | 更新原因: seed=456 两卡并行部署确认，修正时间线从 02:15→22:30 CST

> 最后更新: 2026-05-14 | 更新原因: seed=456 两卡并行部署确认，修正时间线

## 核心方向
迭代自训练中，模型内部嵌入的几何多样性与内容多样性系统性失对齐（Embedding Alignment Gap），导致基于内部表征的 diversity selection 灾难性加速 model collapse。详见 paper_framing.md (D014 revised)。

## 当前进展
- **阶段**: Research + 审稿进行中（Group C 独立处理）
- **MVP**: PASS (D009)
- **Core claims**: C1 (ratio 退化) 强 ✅ | C3 (RGDS > Random 同 budget) 强 ✅ 跨 scale | C2-revised (内部嵌入特异性) 定性强 ✅
- **125M 完成**: 4 方法 × 3 seed 完整，3-seed t-test 就绪
- **355M 进展**: seed=42 四方法完成 ✅ | seed=123 运行中（2/4完成，2卡并行）| seed=456 脚本就绪+两卡chain部署完毕
- **355M seed=42 完整排序**: Random 70.25 < External 77.74 < RGDS 82.84 < Uncurated 91.66 → C3 成立
- **Scaling narrative (D020)**: 双假说共存（表征冗余缓冲 + ceiling effect），ratio 作为鉴别指标，已加 limitation 句
- **论文写作**: Results 355M + Discussion scaling narrative 已完成（D020 patch）。全文 Provenance 18/19。

## 运行中实验
| 实验 | GPU | 状态 | 预计完成 |
|------|-----|------|----------|
| medium_random50_seed123 | cuda:0 | Gen 3/7 训练中 | ~16:15 CST |
| medium_external_seed456 | cuda:1 | Gen 0/7 训练中 | ~16:45 CST |

## 自动衔接（两卡并行）
- cuda:0: random50_seed123 (~16:15) → chain_cuda0_seed456: **uncurated→rgds** (~6-7h → ~22:30 CST)
- cuda:1: external_seed456 (~16:45) → chain_cuda1_seed456: **random50** (~3h → ~19:45 CST)
- **seed=456 全部完成：~22:30 CST（两卡并行，比单卡串行提前 ~4h）**

## 近期任务
- [x] seed=456 脚本准备（4 方法 + 2 chain 脚本 + registry 预注册）
- [x] seed=456 两卡并行 chain 部署（cuda:0: uncurated→rgds, cuda:1: random50）
- [x] Paper Agent Results 355M + Discussion 深化（seed=42 数据）
- [x] 因果性语言修正（D017 降级 S3 相关表述）
- [x] paper_framing.md 同步：S3 降级 (D017) + External scaling nuance + scaling narrative (D020)
- [x] Scaling narrative 定稿：双假说共存框架 (D020)
- [ ] seed=123 剩余两方法完成（random50 ~16:15, external_s456 ~16:45）
- [ ] 补全数据缺口：rgds_seed123 全 gen ratio + uncurated_seed123 逐代数据
- [ ] seed=456 四方法执行（auto-chain 已部署，~22:30 全部完成）
- [ ] 355M 3-seed 统计检验脚本打磨中（ratio 汇总 + LaTeX 格式）
- [ ] Paper Agent patch: 填入 355M 统计检验数据 + ratio 鉴别结果
- [ ] 论文质量打磨：Intro/Related Work/Ablation（Reviewer 审查中）

## GPU 预算
- 分配: westd-11235 2×RTX PRO 6000 98GB
- DDL: EMNLP 2026 ARR **2026-05-25**（还有 **11 天**）
- seed=123 剩余: ~1h（今天 ~16:15/16:45 完成）
- seed=456: ~7h wall（两卡并行）→ 预计今天 ~22:30 CST 完成
- 总剩余到 DDL: 充裕

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D024 | 2026-05-14 | Selection ratio 定义修复：论文改为 sel/rej 匹配代码实现 | — |
| D023 | 2026-05-14 | D021: Scaling narrative 措辞降级——"selective attenuati | medium_rgds_seed42, medium_rgds_seed123, medium_external_seed42 |
| D022 | 2026-05-14 | D021: Scaling narrative 主攻证据改为不对称 gap 模式，ratio 降级为 | medium_rgds_seed42, medium_rgds_seed123, medium_external_seed42 |
| D021 | 2026-05-14 | Scaling narrative 证据策略调整：不对称 gap 模式为主攻，ratio 降级为辅证 | medium_rgds_seed42, medium_rgds_seed123 |
| D020 | 2026-05-14 | 355M scaling narrative 采用修正版 B：双假说共存（表征冗余缓冲 + ceil | medium_external_seed42, medium_rgds_seed42 |
| D019 | 2026-05-14 | 追加 355M seed=456 实验（4 方法），使 355M 与 125M 同为 3-seed  | medium_external_seed42, medium_external_seed123 |
| D018 | 2026-05-13 | Reviewer 独立评估确认三核心 claim 跨 seed 稳健：C1 STRONG (rati | phase2_3method_selfit, phase2_seed123_remaining, random_50_seed456, uncurated_seed456 |
| D017 | 2026-05-13 | D017: S3 (random pruning as regularizer) 降级为 direc | random_50_seed123, random_50_seed456, phase2_random50_v2 |
| D016 | 2026-05-13 | D016: random_50 三 seed 确认 random < external（非 nois | random_50_seed123, random_50_seed456, phase2_random50_v2 |
| D015 | 2026-05-13 | D015: Claim 层级确认——C1/C3 强，C2-revised 定性强但定量弱化，S3 暂 | phase2_3method_selfit, phase2_seed123_remaining |

