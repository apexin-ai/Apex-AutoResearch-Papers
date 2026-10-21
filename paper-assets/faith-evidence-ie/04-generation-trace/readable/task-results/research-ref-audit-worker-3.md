# research ref audit worker 3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-audit-worker-3_20260526T103541_result.json`
- **Structured JSON:** [`5de9638b17ccdc9d611e.json`](../../sessions/5d/5de9638b17ccdc9d611e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计报告已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/ref_audit_worker3.md`。

**结果概要：52 条引用全部验证，11 条有问题，0 条虚构。**

**高优先级修正（4 条）：**
1. **gulcehre2023rest** — 两个作者名错误（Dyer→Doucet, Grangier→de Freitas）+ @inproceedings 应为 @article
2. **wang2025relprior** — 标题虚构了 "RelPrior:" 前缀，真实标题是 "Relation as a Prior: A Novel Paradigm for..."
3. **tang2025rsftppo** — venue 名称虚构（"Practical Aspects of Unlearning..." → 实际是 "2nd Workshop on Test-Time Adaptation: Putting Updates to the Test"）
4. **ma2023dreeam** — venue 错误：不是 Findings EACL 2023，是 EACL 2023 主会议

**中优先级（2 条）：**
5. **xu2024lmrc** — cite key "xu" 但首作者是 Li，\citet 渲染不受影响但 key 误导
6. **li2026qurl** — 已被 ICLR 2026 接收，应更新 venue

**所有 2026 年引用（7 条）均已验证为真实存在的论文。** 另有 17 条 bib 条目未在正文中被 \cite，不会出现在编译后的 PDF 中。

---
