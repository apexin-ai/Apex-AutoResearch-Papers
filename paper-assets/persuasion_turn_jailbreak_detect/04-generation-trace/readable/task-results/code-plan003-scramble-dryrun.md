# code plan003 scramble dryrun

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan003-scramble-dryrun_20260517T214849_result.json`
- **Structured JSON:** [`34962a6d9cdc679fa85d.json`](../../sessions/34/34962a6d9cdc679fa85d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完成，结果汇报：

## 脚本验证结果

**数据概况**: 336 conversations (175 jailbreak, 161 benign), 1444 jailbreak user turns, 1053 benign user turns

### 分布对比 (shuffle 前后完全一致)

| Strategy | Before | After |
|----------|--------|-------|
| 0 (benign) | 1053 | 1053 |
| 1 | 157 | 157 |
| 2 | 110 | 110 |
| 3 | 112 | 112 |
| 4 | 136 | 136 |
| 5 | 94 | 94 |
| 6 | 575 | 575 |
| 7 | 104 | 104 |
| 8 | 156 | 156 |

### 验证项

| 检查项 | 结果 |
|--------|------|
| 分布保持不变 | **True** |
| Benign turns 被修改数 | **0** (正确) |
| Jailbreak turns 被打乱数 | **924/1444 (64.0%)** |
| `intended_strategy` 被修改数 | **0/1444** (未触碰) |

### 结论

脚本功能正确，无 bug：
- 只 shuffle jailbreak 对话内的 `persuasion_strategy`，benign 完全不动
- 分布精确保持
- 64% 的 turn-strategy pair 被打乱（合理 — shuffle 是 per-conversation 的，短对话中重复 strategy 可能回到原位）
- `intended_strategy` 字段未被触碰 — 这是设计如此（保留原始标注供参考，只打乱训练用的 `persuasion_strategy`）

无需修改，可直接用于 ablation 实验。

---
