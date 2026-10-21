# investigation deepseek ft v3 reproducibility

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigation_deepseek_ft_v3_reproducibility_20260516T020725_result.json`
- **Structured JSON:** [`5eecf5870269b30ff78e.json`](../../sessions/5e/5eecf5870269b30ff78e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

还在加载模型。等一下再检查。但我已经有足够的证据来得出结论了。前 20 个样本的直接实验已经证明了根因。

---

## 调查结论

### 1. evaluate.py 的 git 修改历史

| Commit | 时间 (UTC) | 变更 |
|--------|-----------|------|
| `42bad40` | 2026-05-15T17:10 | 首版：添加 `truncation=True, max_length=2048`（右截断） |
| `0836dd4` | 2026-05-15T17:25 | v2 fix：改为 content-aware 截断，保留 chat template 结构 |
| `e404237` | 2026-05-15T23:32 | 仅添加 debugbench condition choices，无逻辑变更 |

### 2. 训练内置 eval vs evaluate.py

- **训练 SFTTrainer** 只计算 `eval_loss` 和 `eval_mean_token_accuracy`（98.0%），**没有** verdict classification accuracy
- **79.16%** 来自训练完成后，Worker 自动用 **evaluate.py v2 + 默认 max_length=2048** 运行的 eval

### 3. 79.16% 的来源和为什么无法复现

**根因：`run_missing_predictions.sh` 用了 `--max_length 16384`（不截断）重跑 eval。**

- 训练时：full_trace input 被 `to_chat_text()` 截断到 2048 tokens（94.1% 的样本被截断，mean=2732→截至~1976 tokens content）
- 原始 eval：max_length=2048（content-aware 截断）→ 模型看到与训练相同的 truncated input → **79.16%**
- 重跑 eval：max_length=16384（不截断）→ 模型看到完整的 ~2700 tokens input（OOD）→ **28.5%**（全预测 fail）

### 4. 直接实验验证

对同一 checkpoint 的前 20 个样本：
- `max_length=2048`：**18/20 = 90% correct**，正常的 pass/fail 分布
- `max_length=16384`：**5/20 = 25% correct**，全部预测 fail

### 5. 两套 eval 的具体差异

唯一差异是 `--max_length` 参数：
- 产出 79.16% 的 eval：`--max_length 2048`（默认值，匹配训练截断）
- 产出 28.5% 的 eval：`--max_length 16384`（`run_missing_predictions.sh` 中指定）

### 6. 复现方案

**用 `--max_length 2048` 重跑即可复现 79.16%。** 后台已提交完整 1190 样本的重跑任务（PID 229417），预计 ~20 分钟完成。

### 影响

- 79.16% 数据是真实的、可复现的
- 但这意味着模型严重依赖训练时的截断 pattern：它学会了对**截断后的 input** 做判断，而不是对**完整 trace** 做判断
- `deepseek_vota` 的 84.45% 用 max_length=16384 可复现，是因为 VOTA 的 input 虽然也超 2048 tokens，但模型从 VOTA 格式中学到了更鲁棒的 pass/fail 信号
- 论文中 79.16% 数据有效，但需要注明 eval 条件是 max_length=2048（匹配训练）

---
