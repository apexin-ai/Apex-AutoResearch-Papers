# paper supplementary check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_supplementary-check_20260529T132039_result.json`
- **Structured JSON:** [`0e7b2863f22f61b2a527.json`](../../sessions/0e/0e7b2863f22f61b2a527.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完成。结果总结：

**交叉引用**：主论文 6 个指向附录的 `\ref{}` 全部正确解析，无悬空引用。

**数字一致性**：全部一致。逐项验证了 Claim 1-3 中所有关键数值（CAR/TSR/dfCAR 均值、标准差、per-seed 值、置换检验 p 值、per-task 聚合计算），appendix 表格的算术均与主论文吻合。

**内容覆盖**：ablation 详表、多 seed 数据、实现细节、oracle 变体说明均齐全。两个 stub section（displacement §A.2、SSR §A.6）只有一行重定向到主论文，无额外分析。

**建议改进**（非必须）：
1. claim3.tex 讨论 TSR 下降和 per-task CAR 排序时应分别引用 `sec:appendix_tsr_collapse` 和 `sec:appendix_pertask_car`
2. 去掉或充实两个 stub section
3. 删除未使用的 `sec:appendix_pertask` 重复 label
4. `experimental_framework.tex` 未被 main.tex 引入，可归档

---
