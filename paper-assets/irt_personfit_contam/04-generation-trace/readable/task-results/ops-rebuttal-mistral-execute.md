# ops rebuttal mistral execute

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_rebuttal-mistral-execute_20260524T035531_result.json`
- **Structured JSON:** [`927546d45fc2c5edb536.json`](../../sessions/92/927546d45fc2c5edb536.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务都已正常启动并在加载模型/数据。

---

**执行结果汇总：**

### 代码修改 (diff)

**prepare_data.py:**
- 添加 `n_5 = int(n_mmlu * 0.05)` → 702, `n_25 = int(n_mmlu * 0.25)` → 3510
- 添加 `indices_5`, `indices_25`（取自同一 seed=999 shuffle 的前 N 个，嵌套子集关系: 5%⊂15%⊂25%⊂50%）
- conditions dict 新增 `"contam_5"` 和 `"contam_25"`
- 输出 `seen_items_5pct.json` 和 `seen_items_25pct.json`

**train.py:**
- SEED_MAP 新增 `"contam_5": 42`, `"contam_25": 42`

**eval_lz.py:**
- 替换硬编码的 15%/50% seen_items 逻辑为通用 `SEEN_ITEMS_MAP` 字典查找

### 数据验证

| 条件 | 行数 | 预期 | 状态 |
|------|------|------|------|
| clean | 5000 | 5000 | ✓ |
| contam_5 | 5702 | 5702 | ✓ |
| contam_15 | 7106 | 7106 | ✓ |
| contam_25 | 8510 | 8510 | ✓ |
| contam_50 | 12021 | 12021 | ✓ |

seen_items: 5pct=702, 25pct=3510, 子集关系验证通过。

### 训练提交

| 任务 | GPU | PID | tmux session | 状态 |
|------|-----|-----|------|------|
| mistral_contam_5 | cuda:0 | 185062 | mistral_contam_5 | 模型加载中 ✓ |
| mistral_contam_25 | cuda:1 | 185140 | mistral_contam_25 | 已开始 tokenize ✓ |

---
