# research webshop replication survey

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_webshop-replication-survey_20260516T023043_result.json`
- **Structured JSON:** [`cf0a4bec2a183664b6b6.json`](../../sessions/cf/cf0a4bec2a183664b6b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/webshop_replication_feasibility.md`。以下是核心结论：

---

## 调研结论

### 1. WebShop 环境
- **GitHub**: https://github.com/princeton-nlp/WebShop (NeurIPS 2022)
- Action space 极简：只有 `search[query]` 和 `click[element]` 两种动作
- 4 种页面类型（搜索/结果/商品/详情），两种渲染模式（HTML/text）
- Reward 是连续值 [0,1]（属性/类别/选项/价格匹配度），不是 ALFWorld 的二值成功率
- 安装需要 Java 11 + Lucene 搜索引擎 + ~16GB RAM，复杂度中等

### 2. Trajectory 收集
- 每条 trajectory 约 5-15 步（ALFWorld 10-50 步），但 observation 更长（商品列表）
- 预估 500 条成功 trajectory 需 ~850 次尝试，API 成本 ~$12-18
- 没有直接可用的现成数据集（AGENTBANK 有 WebShop 数据但格式不兼容）

### 3. Error Taxonomy 适配 — 核心问题
| Operator | WebShop 适用性 | 原因 |
|----------|--------------|------|
| P1 (step_order_swap) | **❌ 低** | 动作高度线性，swap 产生语法非法序列 |
| P2 (sub_goal_deletion) | ⚠️ 中 | 只能删 option selection（1-3步） |
| C1 (context_truncation) | ✅ 高 | 直接迁移 |
| C4 (observation_masking) | ✅ 高 | 直接迁移 |

**P1 几乎无法适配是最大障碍** — taxonomy 从 4 缩到 3，跨环境对比不对等。

### 4. 工作量
- 总计 ~12-17 天 / ~35 GPU-h / ~$15
- 占剩余 GPU 预算的 64%

### 5. 建议

**推荐方案 A：降级为 Discussion section**。在 limitation/future work 中用 1-2 段分析 WebShop 与 ALFWorld 的结构性差异，论证为什么跨环境复制不 trivial。成本为零，不挤占 Recovery-paired SFT (Claim 7) 和 multi-seed recovery eval 的资源。

完整复制的 ROI 较低：投入 15 天 + 35 GPU-h，产出可能只是"另一个环境上的相同 negative result"，且 P1 失效问题会给 reviewer 留把柄。

---
