# code fix evaluate py d075 FINAL

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_evaluate_py_d075_FINAL_20260519T142424_result.json`
- **Structured JSON:** [`a24c259046dfb48df0fb.json`](../../sessions/a2/a24c259046dfb48df0fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

### 1. evaluate.py 修复前后关键行

**`teal_global_masks()` — 修复前（westd-41718 原始）：**
```
79:  hard_mask = (logits > 0).float()
80:  mag = intermediates[layer_idx].abs().float().to(pred_device)
81:  scores = (mag * hard_mask).mean(dim=(0, 1))
```

**修复后（两台服务器一致）：**
```
78:  scores = torch.sigmoid(logits).mean(dim=(0, 1))
```

**`_uniform_topk_masks()` — 新增 sparsity 断言（line 164-165）：**
```
164:  actual_sparsity = 1 - masks[li].float().mean()
165:  assert abs(actual_sparsity - sparsity_target) < 0.02, f"Layer {li}: ..."
```

### 2. 修改时间戳

| 服务器 | evaluate.py Modify | lm_eval_sparse_uniform.py Modify |
|--------|-------------------|----------------------------------|
| westd-34887 | **2026-05-19 22:22:11** ✅ | 2026-05-19 21:55:01 (未被本次修改) ✅ |
| westd-41718 | **2026-05-19 22:26:23** ✅ | 2026-05-19 21:56:07 (未被本次修改) ✅ |

### 3. lm_eval_sparse_uniform.py 未被触动 ✅

两台服务器上 `grep -n "hard_mask" evaluate.py` 均返回空（exit code 1）。

### 4. s42 eval 提交状态

- **exp_id**: `qwen14b_kl30_s42_eval_uniform_v3`
- **PID**: 114087（westd-34887 cuda:0）
- **状态**: RUNNING
- 日志显示 mask 已生成（model-level sparsity 0.296），正在评估 WikiText-2 PPL

---
