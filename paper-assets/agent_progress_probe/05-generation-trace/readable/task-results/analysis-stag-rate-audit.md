# analysis stag rate audit

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_stag-rate-audit_20260514T222656_result.json`
- **Structured JSON:** [`785f8a09a253a2fe1fd4.json`](../../sessions/78/785f8a09a253a2fe1fd4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Audit complete. Here are the results:

---

## Task 1: SWE Stag Rate 溯源

**验证数据（从服务器直接读取）：**

| 数据源 | Stag | Total | Rate |
|--------|------|-------|------|
| embeddings.pt (all conf) | 15,600 | 54,809 | **28.46%** |
| WL (excl abstain) | 15,600 | 54,809 | **28.46%** |
| conf≥2 subset | 5,846 | 15,401 | **37.96%** |
| conf≥3 subset | 513 | 792 | 64.77% |

**36% 来源：** `cross-agent-eval` registry 中 `swe_agent_stag_ratio=0.36` 不匹配任何精确计算。最接近的是 conf≥2 rate (37.96%)，可能是粗略近似。同时在 `cross_agent_distribution_analysis.py:674` 中被硬编码为 `"~36%"`。

**结论：** 36% 是错误数字。正确值：整体 28.5%，conf≥2 子集 38.0%。论文正文正确写了 28.5%，但 writing_plan 和 registry 错写了 36%。

---

## Task 2: Registry 审计

| 条目 | OH 标签源 | 状态 |
|------|-----------|------|
| **cross-agent-eval** | embeddings.pt (6.56%) | **[INVALID]** — `openhands_stag_ratio: 0.066` 来自旧标签；`swe_agent_stag_ratio: 0.36` 也是错的 |
| **openhands-fewshot-probe** | embeddings.pt (6.56%) | **[INVALID]** — 所有 few-shot 结果基于旧标签 |
| **oh-full-finetune** | embeddings.pt (6.56%) | **[INVALID]** — 0.751 训练/评估均在旧标签上 |
| **oh-cmdrep-ablation** | emb (旧) + WL (新) 混合 | **[PARTIAL]** — 2-LF 结果内部一致，但 3-LF baseline 比较跨标签集 |
| **cross-agent-no-cmdrep** | OH eval 用旧 embeddings | **[INVALID]** — SWE 训练结果 OK，OH 跨域评估无效 |
| **cross-agent-structural** | windows_labeled.jsonl (20.87%) | **[VALID]** — 结构特征直接从当前 WL 计算 |
| **bootstrap-crossdomain-fix** | — | **N/A** — 未找到 |
| **non-nlp-baseline** | SWE only | **[VALID]** — 无 OH 依赖 |

**核心问题：** Table 1 中 structural cross-agent (0.967) 用的是 20.87% 标签，probe cross-agent (0.751 FT) 用的是 6.56% 标签。**两种方法在不同标签集上比较。**

---

## Task 3: 论文数字核对

| 论文位置 | 当前数字 | 数据源 | 状态 |
|----------|----------|--------|------|
| Abstract/Intro | SWE 28.5% stag | emb_001 | ✅ CORRECT |
| Abstract/Intro | OH 6.6% stag | OH emb (旧) | ❌ WRONG → 应为 20.87% |
| Abstract | 0.751 probe OH FT | oh-full-finetune | ❌ INVALID — 旧标签 |
| Abstract | 21.6pp struct vs probe | 混合标签集 | ⚠️ SUSPECT |
| Abstract | 17.6pp cmd_rep removal | oh-cmdrep-ablation | ⚠️ PARTIAL |
| Experiments Tab | OH Stag% = 6.6 | OH emb (旧) | ❌ WRONG |
| Experiments | N=1824 (485 stag) | split_info | ⚠️ 实测 454 stag |
| Writing plan | SWE "36% stag" | cross-agent-eval | ❌ WRONG → 应为 28.5% |
| Registry | swe_agent_stag_ratio=0.36 | 未知 | ❌ WRONG → 应为 0.2846 |

---

**必须修复：**
1. 重新生成 OH embeddings.pt（从当前 WL）
2. 重跑所有 probe-based OH 实验
3. 更新论文所有 OH 6.6% → 新 rate
4. 修正 writing_plan 中 SWE "36%" → "28.5%"
5. 修正 cross-agent-eval registry `swe_agent_stag_ratio`

完整 JSON 已保存至 `bjb2-23165:/root/autodl-tmp/agent_progress_probe/results/stag_rate_audit.json`。

---
