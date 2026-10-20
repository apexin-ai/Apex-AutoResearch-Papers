# research evidence chain audit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_evidence-chain-audit_20260514T055852_result.json`
- **Structured JSON:** [`6cbe65ba2823f2e2c5fa.json`](../../sessions/6c/6cbe65ba2823f2e2c5fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已写入 `artifacts/_project/report/evidence_audit.md`。核心发现：

**Table 1 数据问题（3 个需立即处理）：**

1. **plan001-s43 PR 应为 14% 而非 13%** — registry 记录 `eval_sampling_n_proved=14`，所有引用 "13%" 的地方需修正
2. **plan001-s43 评估方法不一致** — s43 用 `eval_sampling` (temperature=0.7)，其他 5 组全用 `eval_sta.py full STA`。论文 Table 1 需统一，建议对 s43 checkpoint 重跑 eval_sta.py
3. **3/6 组缺少 component count 的 registry 来源** — plan001-s42 (6.58)、plan013 (2.04)、plan002 (10.67) 的 n_components 不在 registry 中，需追溯来源或重新评估后补入

**证据覆盖度：**
- Claim 1 (ISR 诊断): ✅ 充分，1 处需补充 (s43 评估方法统一)
- Claim 2 (GRPO 饱和): ✅ 充分，5 组实验全部可追溯
- Claim 3 (跨逻辑泛化): ❌ 无证据，plan006 未启动

**可立即启动写作的章节**：Introduction、Method、Results §4.1-4.3、Discussion (ISR boundary)、Related Work。仅 §4.4 Cross-Logic 和 Extended Training 依赖未完成实验。

---
