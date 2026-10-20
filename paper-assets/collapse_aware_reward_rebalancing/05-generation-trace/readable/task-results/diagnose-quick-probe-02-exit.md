# diagnose quick probe 02 exit

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_quick-probe-02-exit_20260516T104259_result.json`
- **Structured JSON:** [`f55604774aba2d4b8089.json`](../../sessions/f5/f55604774aba2d4b8089.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：失败**

**退出原因：** ArmoRM 的 `score_quality` 在第 1 代（Generation 0/2）scoring 阶段崩溃。

**错误详情：**
- 位置：`score.py:101` → ArmoRM 自定义模型 `modeling_custom.py:50`
- 异常：`ValueError: Token pattern not found in the list.`
- ArmoRM 的 `find_token_for_gating` 函数在 `input_ids` 中找不到预期的 gating token pattern
- 已完成 quality scoring 2204/8000 条时崩溃
- 完成代数：0/3（第 1 代的 generation 完成，但 scoring 阶段失败）
- results.json 不存在

**根因分析：** 这不是之前的 `LLAMA_INPUTS_DOCSTRING` import 错误，而是 ArmoRM 推理时的数据问题——某些生成的 response 在 tokenize 后缺少 ArmoRM 期望的特殊 token pattern（通常是 chat template 的 assistant turn 结束标记）。大概率是某条生成结果为空或格式异常，导致 tokenize 后的 `input_ids` 不包含 gating token。

**日志最后 30 行：**

```
    Quality scored 1604/8000
    Quality scored 1804/8000
    Quality scored 2004/8000
    Quality scored 2204/8000
Traceback (most recent call last):
  File "/root/autodl-tmp/carr/run_quick_probe.py", line 115, in &lt;module>
    run_quick_probe()
  File "/root/autodl-tmp/carr/run_quick_probe.py", line 59, in run_quick_probe
    metrics_list, _ = run_condition(
                      ^^^^^^^^^^^^^^
  File "/root/autodl-tmp/carr/pipeline.py", line 54, in run_condition
    scores = score_all(generations, device=device)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/autodl-tmp/carr/score.py", line 30, in score_all
    quality = score_quality(generations, device)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/autodl-tmp/carr/score.py", line 101, in score_quality
    output = model(**inputs)
             ^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1776, in _wrapped_call_impl
    ...
  File ".../modeling_custom.py", line 155, in forward
    gating_token_positions = [find_token_for_gating(ids.tolist()) for ids in input_ids]
  File ".../modeling_custom.py", line 50, in find_token_for_gating
    raise ValueError("Token pattern not found in the list.")
ValueError: Token pattern not found in the list.
```

**修复方向：** 在 `score_quality` 中对 ArmoRM 的 `forward` 调用加 try-except，捕获此 ValueError 后给该样本一个默认低分（如 0.0），或在 tokenize 前过滤空/异常 response。

---
