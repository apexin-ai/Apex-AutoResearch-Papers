# cpu plan006 full scalability

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_plan006_full_scalability_20260513T184410_result.json`
- **Structured JSON:** [`483b718ed6bd4d87392c.json`](../../sessions/48/483b718ed6bd4d87392c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已注册。以下是全量 M1 scalability 统计摘要：

---

## 全量 M1 Scalability 统计（123 repos, 44,173 instances）

### 1. 处理时间
| 指标 | Overall | Small (<50) | Medium (50-200) | Large (200-500) | XLarge (500+) |
|------|---------|-------------|-----------------|-----------------|---------------|
| Mean | 8.93s | 17.79s | 9.83s | 9.19s | 8.48s |
| Median | 0.0s | 16.61s | 7.81s | 0.0s | 0.0s |
| P95 | 31.95s | 23.16s | 26.24s | 33.93s | 32.26s |
| Max | 633.68s | 381.05s | 89.52s | 135.3s | 633.68s |
| Total | 109.58h | 2.47h | 11.18h | 34.80h | 61.13h |

Median=0 说明大量 instances 在大 repo 中因 error 而没有实际提取耗时。

### 2. Error Rate
| Tier | Total | Errors | Rate |
|------|-------|--------|------|
| Overall | 44,173 | 28,276 | **64.0%** |
| Small | 500 | 27 | 5.4% |
| Medium | 4,096 | 1,986 | 48.5% |
| Large | 13,628 | 8,714 | 63.9% |
| XLarge | 25,949 | 17,549 | 67.6% |

Error 率随 repo size 显著上升。所有 28,276 个 error 都归类为 "other"（非 timeout/OOM 关键词匹配）。

### 3. Per-Repo Instance 分布
| 区间 | Repo 数 |
|------|---------|
| <10 | 1 |
| 10-50 | 17 |
| 50-200 | 36 |
| 200-500 | 40 |
| 500+ | 29 |

Mean 359, Median 261, Max 1,770 (pylint-dev/astroid)。

### 4. 结构数据率
| Tier | With Struct | Total | Rate |
|------|-------------|-------|------|
| Overall | 15,153 | 44,173 | **34.3%** |
| Small | 405 | 500 | 81.0% |
| Medium | 1,935 | 4,096 | 47.2% |
| Large | 4,678 | 13,628 | 34.3% |
| XLarge | 8,135 | 25,949 | 31.4% |

结构数据率与 error rate 互补——小 repo 提取成功率高，大 repo 下降明显。

### 5. Connected-Not-Gold Ratio (Z%)
| Tier | Mean | Median | P25 | P75 |
|------|------|--------|-----|-----|
| Overall | 0.687 | 0.909 | 0.5 | 0.971 |
| Small | 0.284 | 0.0 | 0.0 | 0.667 |
| Medium | 0.444 | 0.5 | 0.0 | 0.833 |
| Large | 0.604 | 0.857 | 0.0 | 0.933 |
| XLarge | 0.812 | 0.960 | 0.889 | 0.976 |

大 repo 中 CodeQL 连接到的文件绝大多数（median 96%）不是 gold patch 文件——结构图噪声随 repo 规模急剧增大。这是 M2 需要解决的核心过滤问题。

JSON 已保存在服务器 `/root/autodl-tmp/structfuse/artifacts/plan006_full_scalability.json`。

---
