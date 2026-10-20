# diagnose quick probe exit

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_quick-probe-exit_20260516T093950_result.json`
- **Structured JSON:** [`653fa850d46e403f4e11.json`](../../sessions/65/653fa850d46e403f4e11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Quick Probe 诊断报告

### 1. 退出原因：**错误崩溃**

进程在 Generation 0（第1代）的 scoring 阶段崩溃，未完成任何一代。

### 2. 错误信息

```
ImportError: cannot import name 'LLAMA_INPUTS_DOCSTRING' from 
'transformers.models.llama.modeling_llama'
```

**根因**：ArmoRM 模型的自定义代码（`modeling_custom.py`）依赖 `LLAMA_INPUTS_DOCSTRING`，该符号在当前安装的 transformers 版本中已被移除/重命名。这是 transformers 版本不兼容问题。

### 3. 崩溃位置

- 文件：`/root/autodl-tmp/carr/score.py:62` → `score_quality()` → 加载 ArmoRM-Llama3-8B-v0.1 模型时
- 阶段：Generation 0/2, Step 2 (Scoring)
- 生成已完成 2000/2000 prompts 的候选，但 scoring 阶段加载 reward model 失败

### 4. 完成进度

- Generation 0: 生成完成 ✓，评分失败 ✗
- Generation 1: 未开始
- Generation 2: 未开始
- 结果文件：不存在

### 5. 日志最后 20 行

```
  File "/root/autodl-tmp/carr/run_quick_probe.py", line 115, in &lt;module>
    run_quick_probe()
  File "/root/autodl-tmp/carr/run_quick_probe.py", line 59, in run_quick_probe
    metrics_list, _ = run_condition(
  File "/root/autodl-tmp/carr/pipeline.py", line 54, in run_condition
    scores = score_all(generations, device=device)
  File "/root/autodl-tmp/carr/score.py", line 30, in score_all
    quality = score_quality(generations, device)
  File "/root/autodl-tmp/carr/score.py", line 62, in score_quality
    model = AutoModelForSequenceClassification.from_pretrained(
  File ".../transformers/dynamic_module_utils.py", line 616, in get_class_from_dynamic_module
    ...
  File ".../transformers_modules/ArmoRM_.../modeling_custom.py", line 9, in &lt;module>
    from transformers.models.llama.modeling_llama import LLAMA_INPUTS_DOCSTRING
ImportError: cannot import name 'LLAMA_INPUTS_DOCSTRING' from 'transformers.models.llama.modeling_llama'
```

### 修复方向

需要降级 transformers 到兼容 ArmoRM 自定义代码的版本（`LLAMA_INPUTS_DOCSTRING` 在 transformers ~4.42 左右被移除），或者 patch ArmoRM 的 `modeling_custom.py` 去掉对该符号的依赖。

---
