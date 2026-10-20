# verify crescendo status check

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_crescendo-status-check_20260517T124535_result.json`
- **Structured JSON:** [`4986c62e41c545dfef55.json`](../../sessions/49/4986c62e41c545dfef55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Crescendo 生成状态：已完成 ✓

| 指标 | 结果 |
|------|------|
| **进度** | 250/250 (part1: 128, part2: 122) |
| **GPU** | 4x H800 全部空闲 (0% util, 0 MiB) |
| **Screen sessions** | 无（进程已正常退出） |
| **合并文件** | `crescendo_all.jsonl` (250 行) |

### 策略分布

| Playbook | 数量 |
|----------|------|
| Academic Disguise | 32 |
| Emotional Path | 32 |
| DAN Variant | 32 |
| Classic Crescendo | 32 |
| Obfuscation Path | 31 |
| Mixed Emotional | 31 |
| Full Spectrum | 30 |
| Role + Obfuscation | 30 |

- **平均 user turns**: 8.3（范围 5-12）
- **质量问题**: 0（无 `&lt;think>` 泄漏，无空 turn）

### Sanity Check (DeBERTa + LogReg)

- **F1 = 0.987 ± 0.004**
- 状态: **INVESTIGATE** — 远超目标范围 0.70-0.85

F1 过高说明 crescendo 对话与 benign 对话在表面特征上太容易区分（可能是 topic/style 差异过大，而非检测到了真正的 persuasion patterns）。这意味着：

1. **benign 数据与 jailbreak 数据的 topic 分布不匹配** — WildChat 日常对话 vs 安全相关 topic，DeBERTa 可能只是在做 topic classification
2. 需要更 hard 的 negative 样本（如正常安全讨论、红队研究讨论等）来让任务有意义

**建议下一步**: 检查是否需要构建 topic-matched benign 数据（如从 WildChat 中筛选涉及安全/技术话题的正常对话），或者直接用 turn-level 特征而非全对话嵌入来做 sanity check。

---
