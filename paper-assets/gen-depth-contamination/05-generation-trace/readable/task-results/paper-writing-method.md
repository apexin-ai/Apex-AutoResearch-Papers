# paper writing method

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_20260513T090523_result.json`
- **Structured JSON:** [`7bc0d8a44524532f17f7.json`](../../sessions/7b/7bc0d8a44524532f17f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Method section 已写入 `docs/paper/method.tex` 并注册为 artifact。

**内容摘要：**

6 个子节，~1500 words，2 个表格：

| 子节 | 核心内容 |
|------|---------|
| §3.1 Problem Formulation | 递归生成 → Markov chain → DPI → $K^*_{\text{theory}}$ 上界 → $K^*_{\text{empirical}}$ operational 定义（bootstrap CI + θ） |
| §3.2 Feature Extraction | 15D 特征表（Table 1），5 组特征的动机，hand-crafted vs learned 的三条理由 |
| §3.3 OBD Classifier | OBD-LightGBM 分解为 K 个 cumulative binary classifiers；与 multiclass LightGBM（MAE 更高）和 ordinal logreg（AUC 0.4883 vs 0.6095，中心坍缩病理）的对比 |
| §3.4 Operationalizing K* | θ=0.60 基于 permutation null 95th pctl < 0.55；四阈值敏感性分析（θ=0.60 时 K*=2 全配置一致） |
| §3.5 Experimental Setup | 4 configs × 3 model families（Table 2），C4 seed，5-fold CV，AUC 为主指标 |
| §3.6 Generation Mode Control | Continuation vs Rewrite；canonical condition 选择基于 transfer retention（80-92% vs 61-63%）和 cont→rw 89% vs rw→cont 82% 不对称性 |

**数据溯源：** 所有定量 claim 均来自 registry（exp-010 OBD 对比、exp-007 bootstrap CI、exp-013 cross-transfer、exp-017/001/002 pairwise AUC）。θ 敏感性分析如实报告：θ=0.65 时仅 rewrite 保持 K\*=2，continuation 降为 1。

---
