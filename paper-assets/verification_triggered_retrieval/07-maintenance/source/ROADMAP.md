# verification_triggered_retrieval — Research Dashboard

> 最后更新: 2026-05-17 10:14 UTC | 更新原因: D002: 项目 KILLED，记录终局结论和教训

## 核心方向
~~训练单一 LLM 通过 GRPO/RL 生成目的分化的检索 query（answer-seeking vs. verification）~~

**状态：KILLED (D002)**

## 终局结论

核心假设"NLI-style verification queries 检索到更好 evidence"被两轮 MVP 决定性反驳：
- mvp_001 (distractor ~2000 passages): 无差异 (-0.74pp, p=0.106)
- mvp_002 (Wikipedia 21M passages): verification 显著更差 (-3.28pp, p=0.005)

**根因**：assertion-form queries 在 BM25 上引入 noise tokens（日期/地名/专有名词），检索偏向表面词汇匹配而非语义相关文档。FEVER 中 claim-as-query 有效因 claims 短且 corpus 针对性强，multi-hop 推理产生的复杂 claims 不满足此条件。

## 教训
1. Multi-hop CoT claims 长而复杂（含日期/地名等），不等于 FEVER 短 claims
2. BM25 对 query 表面形式高度敏感——长 query 中的冗余 token 是 noise 不是 signal
3. "某方法在相关领域有效"不等于"在目标场景有效"——需要先验证前提条件是否匹配

## 实验记录
- mvp_001: HotpotQA distractor, 200Q, N=1598 claims → FAIL (无区分力)
- mvp_002: Wikipedia BM25 21M, 50Q, N=402 claims → KILL (显著反向 p=0.005)

## GPU 预算
westd-46807 cuda:0 → 待释放

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D002 | 2026-05-17 | KILL: 核心假设被两轮 MVP 决定性反驳，终止项目 | mvp_001, mvp_002 |
| D001 | 2026-05-17 | MVP distractor-corpus 结果 FAIL 但不 kill：追加 Wikipedia | mvp_001 |


