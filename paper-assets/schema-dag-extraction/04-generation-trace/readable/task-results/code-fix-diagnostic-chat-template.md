# code fix diagnostic chat template

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-diagnostic-chat-template_20260515T165520_result.json`
- **Structured JSON:** [`17d13232bff896f08ef6.json`](../../sessions/17/17d13232bff896f08ef6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断脚本修复
- chat template: **已添加**（`tokenizer.apply_chat_template` 包装所有 prompts）
- syntax check: **PASS**

## run_extraction.py 补丁
- 需要修改的行: **272**（`llm.generate(prompts, sampling_params)` 前）
- diff 内容:

```diff
@@ -269,6 +269,19 @@
                     sample_indices.append(si)
 
             t0 = time.time()
+
+            # Apply chat template for instruct models (e.g. LLaMA-3.1-Instruct)
+            tokenizer = llm.get_tokenizer()
+            if hasattr(tokenizer, 'chat_template') and tokenizer.chat_template:
+                prompts = [
+                    tokenizer.apply_chat_template(
+                        [{"role": "user", "content": p}],
+                        tokenize=False,
+                        add_generation_prompt=True,
+                    )
+                    for p in prompts
+                ]
+
             outputs = llm.generate(prompts, sampling_params)
```

补丁脚本在 `/root/schema-dag-extraction/scripts/patch_chat_template.py`，仅输出 diff，未修改 `run_extraction.py`。补丁对非 instruct 模型（无 chat_template）安全跳过。

---
