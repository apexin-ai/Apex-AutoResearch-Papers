# writing experiments results

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_experiments-results_20260513T214557_result.json`
- **Structured JSON:** [`5476a015a8205b888748.json`](../../sessions/54/5476a015a8205b888748.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

草稿完成。报告如下：

---

**字数统计**: 1,441 词（约 2.5 页，符合 2.5-3 页要求）

**占位符** (7 处):
| 行 | 内容 | 等待数据 |
|---|---|---|
| L25 | External s456 PPL & Mean±Std | seed=456 External Gen 6-7 完成 |
| L29 | RGDS s456 PPL & Mean±Std | seed=456 RGDS 未启动 |
| L38 | +84% 和 78.32 (2-seed mean) | 3-seed mean 后更新为精确值 |
| L108 | Medium RGDS "in progress" | Medium RGDS 实验完成后填入 |

**需要的 Figures**:
| ID | 内容 |
|---|---|
| `fig:ppl_trajectory` | 4 方法 × 8 代 PPL 折线图 (§5.2 引用) |
| `fig:ratio_trajectory` | RGDS vs External Selection Ratio 折线图 (§5.3 引用) |

**需要的 Tables** (已内联):
| ID | 内容 | 状态 |
|---|---|---|
| `tab:gen7_summary` | Gen 7 全方法汇总 (Table 1) | ✓ 已写 |
| `tab:sr_trajectory` | RGDS SR 逐代轨迹 (Table 2) | ✓ 已写 |
| `tab:scale` | 125M vs 355M 对比 (Table 3) | ✓ 已写 |

**需要的 Citations**:
| cite key | 用途 |
|---|---|
| `goodhart1984problems` | Goodhart's Law 理论锚点 (§5.3) |
| 已在 methodology 中定义的 `shumailov2024ai`, `jing2022understanding` 等 | 交叉引用即可 |

---
