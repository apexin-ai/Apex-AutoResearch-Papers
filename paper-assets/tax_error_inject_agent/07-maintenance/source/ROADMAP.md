# tax_error_inject_agent — Research Dashboard

> 最后更新: 2026-05-16 15:50 UTC | 更新原因: LLaMA 3-seed 数据齐全，framing 升级为跨模型训练不稳定性，dream 评估中

## 核心方向
Error injection 对 embodied planning agent 训练的影响：结构化注入(TaxEI)跨模型导致训练不稳定，Random 注入跨模型稳定，taxonomy 标签零收益。详见 paper_framing.md。

## 当前进展
**阶段**: Research → 写作准备（实验主体完成，等 dream 评估新 framing）

**核心实验完成度**:
- Qwen3-8B 5-seed 主实验: ✅ 完成（V=67.3%, T=R=58.3%）
- Qwen3-8B 5-seed 剂量响应(10/25/50/Full): ✅ 完成
- LLaMA-3.1-8B 3-seed 跨模型验证: ✅ 完成（D047）
- Recovery-paired injection (TaxEI-RP): ✅ 4-seed 完成（47.9%，D043）
- Recovery eval multi-seed: 7/15 完成，剩余 8 个进行中
- Scale-up datagen: ~405/1000，状态待确认

**关键发现**:
- TaxEI 跨模型不稳定: Qwen -9pp 一致退化; LLaMA SD=8.6%, 1/3 seed catastrophic
- Random 跨模型稳定: Qwen -9pp; LLaMA 稳定甚至微提升(+3.5pp)
- Taxonomy 标签跨模型零收益: TaxEI≈Random（均值层面）
- 结构化注入的方差 >> 随机注入方差（跨模型成立）

**Claims 支撑状态**: 9 个 claims，7 个有完整实验支撑，Claim 8 已取消，Claim 9 新增已完成

## 近期任务
- [ ] Dream dream_20260516T153939 完成 → 分析审稿反馈
- [ ] Recovery eval 剩余 8/15 完成
- [ ] Scale-up datagen 状态确认（~405/1000）
- [ ] Dream 通过后 → 启动 Paper Agent 写作
- [ ] 统计检验补充：LLaMA 跨模型 Levene's test / bootstrap

## GPU 预算
**分配**: autodl-5090 cuda:0/1/2/3（4× RTX 5090）
**当前占用**: Recovery eval multi-seed 4 GPU 并行
**累计**: ~150+ GPU-h（训练+eval+dose-response+cross-model）

## 投稿目标
EMNLP 2026 Findings, 8-page long paper, Budapest Oct 22-29

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D048 | 2026-05-16 | Dream #2 结果：3/6 跨档一致 Weak/Borderline Reject。核心行动项： | dream_20260516T153939 |
| D047 | 2026-05-16 | LLaMA 3-seed 完成：TaxEI 跨模型不稳定确认，paper framing 升级为"结 | llama31-vanilla-s123, llama31-taxei-s123, llama31-random-s123 |
| D046 | 2026-05-16 | D046: 撤销 D044 scale-up 暂停——9.3% 成功率是统计口径错误（714 exc | scale-up-data |
| D045 | 2026-05-16 | D045: Scope 最终判断——当前 scope 含 LLaMA 3-seed + recove | llama-cross-model, recovery-eval-multiseed, scale-up-data |
| D044 | 2026-05-16 | D044: Scale-up 数据收集暂停——成功率从 70% 崩到 9.3%，1000 目标不可行 | scale-up-data |
| D043 | 2026-05-16 | D043: TaxEI-RP (recovery-paired) 4-seed 结果: 47.9±7 | recovery-paired-injection, multiseed-taxei, multiseed-vanilla |
| D042 | 2026-05-16 | D042: Scope 扩展——加 LLaMA-3.1-8B 跨模型验证 + scale-up 25 | llama-cross-model, scale-up-data |
| D041 | 2026-05-16 | D041: Recovery rate ≈ normal eval rate — 模型是 "resi | recovery-eval, recovery-eval-multiseed |
| D040 | 2026-05-16 | D040: WebShop replication 降级为 Discussion section 分 | webshop-replication |
| D039 | 2026-05-16 | D039: Recovery-paired SFT 启动 (Claim 7)。数据设计: TaxEI | recovery-paired-injection, dose-response-5seed |

