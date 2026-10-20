# 实验失败诊断：llama_docred_full_s1_mt6144

## 失败根因

**`torch.AcceleratorError: CUDA error: invalid device ordinal`**

实验命令指定 `--device cuda:1`，传入 `AutoModelForCausalLM.from_pretrained(device_map="cuda:1")`。在 transformers 4.57.6 的 `caching_allocator_warmup()` 阶段（modeling_utils.py:6090），调用 `torch.cuda.cudart().cudaMemGetInfo(1)` 时 CUDA runtime 报告 device ordinal 1 无效。

**推断原因**：启动实验的 tmux session 中 `CUDA_VISIBLE_DEVICES` 被设为单卡（如 `CUDA_VISIBLE_DEVICES=0`），导致进程只能看到 `cuda:0`，`cuda:1` 不可见。`nvidia-smi` 在全局 shell 中显示 2 块 RTX PRO 6000（index 0, 1），硬件无问题。项目代码中未设置 `CUDA_VISIBLE_DEVICES`（grep 确认）。

## 完整 Traceback

```
Traceback (most recent call last):
  File "/root/schema_semantic_constrained_ie/run_constrained_extraction.py", line 752, in <module>
    main()
  File "/root/schema_semantic_constrained_ie/run_constrained_extraction.py", line 655, in main
    model = AutoModelForCausalLM.from_pretrained(
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/transformers/models/auto/auto_factory.py", line 604, in from_pretrained
    return model_class.from_pretrained(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/transformers/modeling_utils.py", line 277, in _wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/transformers/modeling_utils.py", line 5048, in from_pretrained
    ) = cls._load_pretrained_model(
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/transformers/modeling_utils.py", line 5432, in _load_pretrained_model
    caching_allocator_warmup(model, expanded_device_map, hf_quantizer)
  File "/root/miniconda3/lib/python3.12/site-packages/transformers/modeling_utils.py", line 6090, in caching_allocator_warmup
    device_memory = torch_accelerator_module.mem_get_info(index)[0]
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/cuda/memory.py", line 897, in mem_get_info
    return torch.cuda.cudart().cudaMemGetInfo(device)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
torch.AcceleratorError: CUDA error: invalid device ordinal
```

## 修复建议

1. **确认 CUDA_VISIBLE_DEVICES**：重新启动实验前检查 tmux session 环境变量 `echo $CUDA_VISIBLE_DEVICES`，确保包含目标 GPU
2. **推荐做法**：如果要用物理 GPU 1，设 `CUDA_VISIBLE_DEVICES=1` + `--device cuda:0`（重映射为逻辑 0 号）；或不设 `CUDA_VISIBLE_DEVICES` + `--device cuda:1`
3. **当前状态**：日志已被新运行覆盖，新运行使用 `cuda:0`，已在正常推理中（输出文件 34KB）。注意如果 unconstrained 实验仍在 cuda:0 上跑，两个实验共用同一 GPU 可能导致 OOM
