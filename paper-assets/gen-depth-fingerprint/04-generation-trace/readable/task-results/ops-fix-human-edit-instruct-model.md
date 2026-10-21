# ops fix human edit instruct model

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-human-edit-instruct-model_20260515T170200_result.json`
- **Structured JSON:** [`0833fd699483294da9fe.json`](../../sessions/08/0833fd699483294da9fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

等待脚本正在运行。汇总当前状态：

---

## 执行总结

### 根因修正
用户诊断："模型是 Base 不是 Instruct" — **不准确**。Qwen3 系列没有单独的 Instruct 版本，`Qwen3-0.6B` 本身就是 instruct 模型（有完整 chat_template）。

**真正问题**：代码用原始文本 prompt 而不是 chat template，导致模型做 text continuation 而非 instruction following。

### 已完成

| Step | 状态 | 说明 |
|------|------|------|
| 模型验证 | ✅ | `Qwen3-0.6B` 已有 chat_template，就是 instruct 模型。HF/ModelScope 均不存在 `Qwen3-0.6B-Instruct` |
| 代码修复 | ✅ | `llm_rephrase_batch` 改用 `apply_chat_template(enable_thinking=False)` + `temperature=1.0, top_p=0.95` |
| 3-seed 验证 | ✅ | **100% 文本有变化**，23% fallback（vs 旧方法的 continuation 垃圾），改写质量好 |
| 本地同步 | ✅ | 本地 `experiments/human_edit_robustness.py` 已同步修复 |
| 重跑提交 | ✅ | PID 228872 等待旧进程(223500, ETA ~20min)结束后自动在 cuda:1 重跑全部条件 |

### 待进行
- 旧进程完成后可检查其 fallback 比例（`/tmp/human_edit_robustness.log`）
- 重跑预计耗时 ~90 分钟（rephrase 阶段 ~85min + 特征提取 + 评估）
- 结果输出到 `/root/gen-depth-fingerprint/results/human_edit_robustness.json`
- 旧结果备份到 `human_edit_robustness_old_no_chat_template.json`

### 监控命令
```bash
tail -20 /tmp/human_edit_rerun.log   # 重跑进度
tail -5 /tmp/human_edit_robustness.log  # 旧进程进度
```

---
