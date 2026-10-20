# infra p1 qwen3 fix verify

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_p1-qwen3-fix-verify_20260521T182023_result.json`
- **Structured JSON:** [`36b9a6dfeb7effc17e04.json`](../../sessions/36/36b9a6dfeb7effc17e04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture.

---

## 汇报

### (1) 修复进程

**两个相关进程在跑：**
- **PID 414515**: 主实验 `exp_d126_crossmodel_sica.py --phase all`，当前 154/204 题，仍在跑（但它的 Qwen3 extraction 有 bug）
- **PID 473120**: 修复脚本 `reextract_qwen3_fixed.py --direction both --max-workers 4`，02:15 UTC 启动，正在覆盖 buggy 结果

两者共享 Qwen3 vLLM (port 8001)，存在 GPU 竞争。

### (2) 根因确认

**`extra_body` 包装导致 `chat_template_kwargs` 没传到 vLLM。** Qwen3 的 thinking mode 没被关闭，输出带 `&lt;think>...&lt;/think>` 块，extraction parser 找不到 JSON → `error: "no JSON"` → 0 constraints。

修复方案：`reextract_qwen3_fixed.py` 把 `chat_template_kwargs: {enable_thinking: False}` 直接放 payload 顶层，并加 `strip_thinking()` fallback。

### (3) 修复后质量对比（同一文件 ProofWriter_AttNeg-OWA-D5-1015_Q3）

| 版本 | 文件大小 | trace 结果 |
|------|---------|-----------|
| **buggy** | 89 行 | 绝大多数 trace → `constraints: [], error: "no JSON"`，仅个别侥幸提取到 4 个 |
| **fixed** | 713 行 | 每个 trace 7+ constraints，含完整 `z3_formula`、`type`、`source_step` |

主实验日志也佐证：同一题 Mistral same-model 提取 58 constraints，Mistral→Qwen3 提取 93 constraints，但 **Qwen3→Mistral 只有 11 constraints**（bug 未修前）。

### (4) 进度与预计完成时间

- `extraction_qwen3_cross_mistral`: **11/152 文件**（~7%），正在处理
- `extraction_qwen3_same`: 尚未开始（脚本先做 cross 再做 same）
- 速率：~6 分钟完成 11 文件（~0.55 min/file）
- **预计**：cross 剩余 ~140 文件 ≈ 77 min，same 152 文件 ≈ 84 min，**总计约 2.5-3 小时**（考虑与主实验争抢 Qwen3 GPU 可能更慢）

---
