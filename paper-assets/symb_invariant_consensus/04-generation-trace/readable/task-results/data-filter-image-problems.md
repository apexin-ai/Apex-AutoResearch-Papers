# data filter image problems

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_filter-image-problems_20260515T114219_result.json`
- **Structured JSON:** [`a3fb49fbcd4ac27ac2ca.json`](../../sessions/a3/a3fb49fbcd4ac27ac2ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

替换完成，所有验证通过。

### 汇报

**1. 找到 6 个图形题**（问题文本含 `[asy]` Asymptote 绘图代码）

另有 4 个误报已排除：[17] "graph" 指函数连续性、[46] "image" 指矩阵像、[48][49] "graph" 指函数图像概念。

**2. 图形题清单**

| 索引 | 原 ID | Level | 原因 |
|------|-------|-------|------|
| 13 | test/geometry/248.json | 2 | 圆柱体图，半径仅在图中 |
| 19 | test/geometry/846.json | 2 | "In the diagram" + [asy] |
| 22 | test/prealgebra/631.json | 3 | 七巧板图 + [asy] |
| 29 | test/geometry/65.json | 3 | 四圆相切 "as shown" + [asy] |
| 30 | test/precalculus/1199.json | 4 | sin 函数图 + [asy]（已知问题） |
| 37 | test/geometry/465.json | 4 | 阴影区域图 + [asy] |

**3. 替换结果**

| 索引 | 旧题 → 新题 | Level | 新题摘要 | 答案 |
|------|------------|-------|---------|------|
| 13 | geometry/248 → number_theory/46 | 2 | 计算 $58_9 - 18_9$（九进制减法） | $40_9$ |
| 19 | geometry/846 → precalculus/779 | 2 | 复数 $7+2i$ 绕原点逆时针旋转 90° | $-2+7i$ |
| 22 | prealgebra/631 → intermediate_algebra/101 | 3 | 解嵌套根号方程 | $10$ |
| 29 | geometry/65 → algebra/1275 | 3 | 化简嵌套根号并有理化分母 | $\frac{\sqrt{3}}{3}$ |
| 30 | precalculus/1199 → counting_and_probability/430 | 4 | Bob 和 Alice 交换球的概率 | $\frac{1}{3}$ |
| 37 | geometry/465 → algebra/246 | 4 | 已知 $f(-3)=2$ 求 $f(3)$ | $8$ |

**4. 最终 Level 分布确认**

`{1: 10, 2: 10, 3: 10, 4: 10, 5: 10}` — 每级 10 题，共 50 题。无 Asymptote 代码残留。备份已保存至 `data/math500_subset_backup.json`。

---
