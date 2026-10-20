# code fix ar n50 hardcoded

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_ar_n50_hardcoded_20260522T231700_result.json`
- **Structured JSON:** [`4562e3d7c1278b15383c.json`](../../sessions/45/4562e3d7c1278b15383c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。汇报：

### 修改文件
`/root/turn_residual_gating/src/eval_attention_steering.py`，3 处改动：

### 改动内容

1. **新增 `--conversations-source` 参数**（`dataset` | `hardcoded`，默认 `dataset`）
2. **gen 模式数据加载逻辑**：
   - `--data-file` 显式指定 → 用指定文件（原有行为）
   - `--conversations-source dataset`（新默认）→ 自动加载 `data/ultrachat_eval_heldout.json`，`--max-convs` 控制数量
   - `--conversations-source hardcoded` → 原 5 条 hardcoded 对话（fallback）
3. **输出元数据** `conversations_source` 字段更新，正确记录 `"ultrachat_eval_heldout"`

### 数据格式对比

| | Hardcoded | UltraChat Heldout |
|---|---|---|
| 数量 | 5 | 50 |
| System prompt | 专属（5个不同角色） | 默认 "You are a helpful assistant." |
| User turns/对话 | 10 | 5-6 |
| 来源 | 手写 | ultrachat_200k heldout split |

### Dry-run 验证
- 加载 50 条 ✓，`max_convs=10` 取前 10 ✓
- 每条对话格式 `(sys_prompt, user_qs)` 正确
- Hardcoded fallback 仍可用 ✓

### 用法
```bash
# 新默认：50条 UltraChat 对话
python src/eval_attention_steering.py --mode gen --max-convs 50 ...

# 旧行为
python src/eval_attention_steering.py --mode gen --conversations-source hardcoded ...
```

无评估逻辑改动，仅数据来源切换。

---
