# diagnose ridge startup verify

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_ridge_startup_verify_20260521T052500_result.json`
- **Structured JSON:** [`73ba5e50c6f4876f21a2.json`](../../sessions/73/73ba5e50c6f4876f21a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Raw output：

```
=== PROCESSES ===
   PID %CPU %MEM     ELAPSED COMMAND
EXIT=1
=== TMUX ===
=== CUDA:0 LOG ===
  File "/root/miniconda3/lib/python3.12/site-packages/transformers/processing_utils.py", line 974, in from_pretrained
    args = cls._get_arguments_from_pretrained(pretrained_model_name_or_path, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/transformers/processing_utils.py", line 1020, in _get_arguments_from_pretrained
    args.append(attribute_class.from_pretrained(pretrained_model_name_or_path, **kwargs))
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/transformers/models/auto/image_processing_auto.py", line 539, in from_pretrained
    image_processor_class = get_class_from_dynamic_module(class_ref, pretrained_model_name_or_path, **kwargs)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/transformers/dynamic_module_utils.py", line 541, in get_class_from_dynamic_module
    final_module = get_cached_module_file(
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/transformers/dynamic_module_utils.py", line 345, in get_cached_module_file
    resolved_module_file = cached_file(
                           ^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/transformers/utils/hub.py", line 446, in cached_file
    raise EnvironmentError(
OSError: We couldn't connect to 'https://huggingface.co' to load this file, couldn't find it in the cached files and it looks like openvla/openvla-7b is not the path to a directory containing a file named processing_prismatic.py.
Checkout your internet connection or see how to run the library in offline mode at 'https://huggingface.co/docs/transformers/installation#offline-mode'.
EXIT_CODE=1
=== CUDA:1 LOG ===
[13:24:19]     1100/5000
[13:24:24]     1200/5000
[13:24:29]     1300/5000
[13:24:34]     1400/5000
[13:24:40]     1500/5000
[13:24:40]   Task 3/10: put_the_bowl_on_the_plate
[13:24:45]     1600/5000
[13:24:50]     1700/5000
[13:24:55]     1800/5000
[13:25:01]     1900/5000
[13:25:06]     2000/5000
[13:25:06]   Task 4/10: put_the_bowl_on_the_stove
[13:25:11]     2100/5000
[13:25:16]     2200/5000
[13:25:22]     2300/5000
[13:25:27]     2400/5000
[13:25:32]     2500/5000
[13:25:32]   Task 5/10: put_the_bowl_on_top_of_the_cabinet
[13:25:38]     2600/5000
[13:25:43]     2700/5000
=== NVIDIA-SMI ===
533679, 8522 MiB
```

**状态：**
- **CUDA:0 (object_pipeline_ridge)** — 已崩溃。进程 533530 不存在。报错：无法连接 HuggingFace 下载 `processing_prismatic.py`，`openvla/openvla-7b` 本地缓存也没找到该文件。
- **CUDA:1 (nora_goal_pipeline_v3)** — 正常运行中，PID 533679 占用 8522 MiB，正在跑 Task 5/10 (2700/5000)。
- **tmux** — 无活跃 session。

---
