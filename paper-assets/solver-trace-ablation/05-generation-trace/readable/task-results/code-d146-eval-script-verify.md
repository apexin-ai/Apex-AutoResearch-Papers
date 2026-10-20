# code d146 eval script verify

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-eval-script-verify_20260520T003800_result.json`
- **Structured JSON:** [`58b81814acaa0d5d6d7f.json`](../../sessions/58/58b81814acaa0d5d6d7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果：

### 1. 脚本结构：7 个 eval — **完整**
- Step 0: Base model (`/root/autodl-tmp/models/Qwen3-4B`) ✅
- Step 1-6: 循环遍历 6 个实验 (`d146_pf_exec_s42/s43/s44`, `d146_pf_isr_s42/s43/s44`) ✅
- 每个 eval 包含 `eval_sta.py` + `classify_h7.py` 两步 ✅
- 最后有 batch summary 汇总 ✅

### 2. model_path — **正确**
- Base: `/root/autodl-tmp/models/Qwen3-4B` ✅
- 实验: 指向 `$OUT/$EXP` 即 final model 目录（检查 `model.safetensors.index.json` 存在性） ✅
- 脚本有防护：若目录不存在或无 final model 则 SKIP ✅

### 3. 数据路径 — **正确**
- `data/prooffol_eval_100.jsonl` — 存在，100 行 ✅
- `--logic_type fol` ✅

### 4. 依赖文件 — **全部存在**
- `eval_sta.py` ✅
- `classify_h7.py` ✅
- Base model 目录 ✅

### 5. Checkpoint 状态

| 实验 | Final Model | 状态 |
|------|-------------|------|
| d146_pf_exec_s42 | ✅ | ready |
| d146_pf_exec_s43 | ✅ | ready |
| d146_pf_exec_s44 | ✅ | ready |
| d146_pf_isr_s42 | ✅ | ready |
| d146_pf_isr_s43 | ✅ | ready |
| **d146_pf_isr_s44** | **❌** | **训练中，仅 checkpoint-150** |

`d146_pf_isr_s44` 尚未完成训练（只有 checkpoint-150），脚本会自动 SKIP 它。其余 5 个实验 + 1 个 base = 6 个 eval 可正常执行。等 isr_s44 训练完成后重跑即可覆盖全部 7 个。

---
