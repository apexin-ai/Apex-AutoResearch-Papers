# analysis structural v3 deep

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_structural_v3_deep_20260515T092549_result.json`
- **Structured JSON:** [`92ebf072fa3377894820.json`](../../sessions/92/92ebf072fa3377894820.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已生成。以下是完整分析结果：

---

## 1. Subset A / B 实例列表

**Subset A (keep>0, 15 实例):**
`black_1`, `cookiecutter_1/2/3`, `fastapi_1/2`, `luigi_5`, `sanic_2`, `scrapy_2/7`, `tornado_2`, `youtube-dl_1/2/5/20`

**Subset B (keep=0, 18 实例):**
`httpie_1/2`, `luigi_1/2/10/14`, `sanic_1`, `scrapy_1/3/4`, `thefuck_1/2/4`, `tornado_1/4/5/7`, `youtube-dl_10`

## 2. Keep segment 类型分布 (41 segments)

| Type | Count | Pct |
|------|-------|-----|
| call_subtree | 25 | 61.0% |
| exception_chain | 12 | 29.3% |
| loop_iteration | 4 | 9.8% |
| basic_block | 0 | 0% |

**basic_block 从未被 keep** — 这在论文叙事中很有价值：纯执行行序列缺乏诊断信息。

## 3. 关键发现

**什么区分 keep>0 vs keep=0：**

1. **exception_chain 是最"可 keep"的类型**：占 keep 的 29.3%，但在 Subset A 的 drop 中仅占 ~2%。异常链天然包含错误上下文，诊断价值高。

2. **实例规模有差异但不大**：Subset A median events=193, tokens=16769；Subset B median events=126, tokens=9732。更大的 trace 产生更多 keepable 段，但差异不如预期大。

3. **Token 长度不区分 keep vs drop**：keep median=438, drop median=428。segment 是否被保留取决于内容相关性而非长度。

4. **Subset B 的 drop 是高置信度的**：81.5% 的 confidence ≥ 0.95，模型非常确信这些段无诊断价值。

5. **项目级模式明显**：
   - cookiecutter (3/3) 和 fastapi (2/2) 100% 有 keep — bug 涉及明确的函数调用链/异常
   - thefuck (0/3) 和 httpie (0/2) 完全没有 keep — trace 内容与 bug 描述关联弱
   - luigi (1/5)、tornado (1/5) 很少有 keep — trace 多为框架内部调度，不直接暴露 bug

6. **极端值**：youtube-dl_1 有一个 3.35M token 的 exception_chain（41K events），拉高了均值。去掉前 5 个极端值后，keep 平均 token = 688。

## 4. 产出文件

`/root/trace_distill_repair/pipeline_output/structural_v3_analysis.json` (17.7KB) — 包含逐实例的 keep/drop/error 分布、keep_segment_types、subset 标签，以及 Subset A/B 的 summary stats，可直接用于 Phase 3 conditional analysis。

---
