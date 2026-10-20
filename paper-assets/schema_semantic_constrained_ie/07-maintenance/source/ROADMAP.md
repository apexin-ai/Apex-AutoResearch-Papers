# schema_semantic_constrained_ie — Research Dashboard

> 最后更新: 2026-05-24 07:39 UTC | 更新原因: DDL 前最终状态更新：页数修复、camera-ready 检查完成、PDF 交付

> **阶段: Submission-ready** | DDL: 2026-05-25

## 核心方向
OntoCoDec: 两层约束解码（grammar + semantic）将 IE schema 翻译为 token-level constraints，消除 LLM-based IE 的 type violations。**目标: EMNLP 2026 ARR May 25 提交**。详见 paper_framing.md。

## 当前进展
**论文已就绪，等待提交。**

- ✅ 164 实验完成（133 成功 / 15 阴性 / 11 failed+killed）
- ✅ 正文 8 页（Section 7 压缩修复页数超限）
- ✅ Abstract 134 words（≤200 限制）
- ✅ 60 条参考文献格式统一，无 orphan
- ✅ 15 个阴性结果覆盖度 Reviewer PASS
- ✅ 0 critical warnings，0 undefined refs/citations
- ✅ 匿名代码仓库已 push（README + code + requirements）
- ✅ _anonymous_repo.json 持久化 + .gitignore
- ✅ LoRA adapters 从 westd-21461 备份
- ✅ 服务器审计完成（westd-16980 + westd-21461 均可释放）

## 近期任务
- [x] R26 全部修复 + Reviewer 验证
- [x] 实验收尾（70B PS / r16 / p1 清理）
- [x] 匿名仓库推送 + URL 持久化
- [x] 页数超限修复（Section 7 压缩 5 行）
- [x] Camera-ready 检查（claims 对齐、引用格式、TODO 残留、阴性覆盖）
- [x] 最终 PDF 上传给用户
- [ ] Final freeze + ARR 提交（运维手动提交表单）

## GPU 预算
westd-21461 cuda:0,1 — 空闲（可释放，已通知 Manager）
westd-16980 cuda:0,1 — 空闲（可释放，已通知 Manager）
所有计划实验已完成。

## 时间线
- **May 23**: R26 修复验证通过 + 实验收尾
- **May 24 AM**: 页数超限修复 + camera-ready 检查 + 最终 PDF 交付
- **May 25**: EMNLP 2026 ARR 提交（运维操作）

## 遗留低优先级（post-submission）
- M2: CF bootstrap CI（info severity）
- M4: Visual density（info severity）

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D087 | 2026-05-23 | DocRED FT Semantic-only DR 重验后修正叙事：去掉 "39-72%" ran | w8_llama_docred_ft_semantic_only, w8_qwen_docred_ft_semantic_only |
| D086 | 2026-05-23 | R25 审稿报告全面修复：14 项 Action Matrix，全部为写作层面修改 | — |
| D085 | 2026-05-22 | Dream dream_20260522T052642 分析完成：Best=2.5, Median= | — |
| D084 | 2026-05-22 | D084: 撤回 D083，恢复使用 70B DocRED ZS 数据（DR 14.98%→0%,  | r16_70b_docred_zs_s1 |
| D083 | 2026-05-22 | D083: 放弃 70B DocRED ZS 重跑，从论文移除该数据点。70B feasibilit | r16_70b_docred_zs_s1, r16_70b_lora_scierc, r16_70b_lora_docred |
| D082 | 2026-05-22 | D082: 70B LoRA DocRED 推理改用 200-doc 子集 + DocRED ZS  | r16_70b_lora_docred, r16_70b_docred_zs_s1 |
| D081 | 2026-05-21 | D081: 评估用户 5 项补充建议——downstream KG 扩展 Task E、beam=C | — |
| D080 | 2026-05-21 | D080: 采纳用户 3 项审稿建议——GoLLIE head-to-head + 下游 tripl | — |
| D079 | 2026-05-21 | D079: R16 Action Matrix——MF1 trie-based GCD-equiva | — |
| D078 | 2026-05-21 | D078: R15 Action Matrix 定稿——MF1 §5 显式对比, MF2 guara | — |




