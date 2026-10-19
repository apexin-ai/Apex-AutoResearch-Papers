# ops gpt4omini final and cleanup

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpt4omini_final_and_cleanup_20260520T065640_result.json`
- **Structured JSON:** [`70bb3d87c3ba8dd85f28.json`](../../sessions/70/70bb3d87c3ba8dd85f28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

## 完整摘要

### gpt-4o-mini 标注结果
| 指标 | 值 |
|------|-----|
| 总标注数 | 388/520 |
| Jailbreak | 99 (25.5%) |
| CP mean/median | 10.3 / 10.0 |
| CP range | 0–40 |

### IAA（Qwen3 vs gpt-4o-mini）
| 指标 | 值 |
|------|-----|
| 共同样本 | 388 |
| **is_jailbreak κ** | **0.6063**（moderate） |
| Agreement | 87.4% |
| Qwen3 JB / gpt4omini JB | 52 / 99 |
| TP/TN/FP/FN | 51 / 288 / 48 / 1 |

gpt-4o-mini 明显更激进——把 48 个 Qwen3 认为非 jailbreak 的样本判为 jailbreak（FP=48），而 Qwen3 几乎没有独判的（FN=1）。

**CP 位置一致性**（51 个双方均判 jailbreak 的样本）：
- Exact match: 37%
- Within 2 steps: 39%
- Within 5 steps: 47%
- Mean abs diff: 8.5 steps

### API key 清理
3 个脚本中的硬编码 key 已全部替换为 `REMOVED_KEY`，grep 确认 `ALL_CLEAN`。

---
