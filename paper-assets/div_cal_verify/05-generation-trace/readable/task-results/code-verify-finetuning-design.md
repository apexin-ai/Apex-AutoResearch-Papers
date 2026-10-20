# code verify finetuning design

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify_finetuning_design_20260513T092410_result.json`
- **Structured JSON:** [`4406fe8c0af32e38bc56.json`](../../sessions/44/4406fe8c0af32e38bc56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：Cumulative，设计正确。**

关键代码流程：

### 1. 模型初始化（仅一次）— `run_mvp.py:217-219`
```python
student_model = AutoModelForCausalLM.from_pretrained(
    args.student_model, torch_dtype=dtype, trust_remote_code=True
).to(student_device)
```
`student_model` 在 `main()` 入口加载一次 pretrained GPT-2，之后**整个 generation loop 中不再重新加载**。

### 2. Self-iterate 绑定 — `run_mvp.py:229`
```python
generator_model = student_model  # 同一个对象引用
```

### 3. 每代训练 — in-place 修改 — `run_mvp.py:318`
```python
avg_loss = run_training(student_model, tokenizer, selected_data, str(ckpt_dir),
                        student_device, args)
```

`run_training`（`run_mvp.py:130-152`）直接在传入的 `student_model` 对象上创建 optimizer 并 step，**不从 checkpoint 重新加载**：
```python
def run_training(student_model, tokenizer, selected_data, checkpoint_dir, device, args):
    ...
    optimizer = torch.optim.AdamW(student_model.parameters(), lr=args.train_lr, ...)
    for epoch in range(args.train_epochs):
        avg_loss = train_one_epoch(student_model, dataloader, optimizer, scheduler, device, args)
    student_model.save_pretrained(checkpoint_dir)  # 保存但不重加载
    return avg_loss
```

### 4. Generation loop 中无 re-load
`for gen in range(args.num_generations):` 循环体内没有任何 `from_pretrained` 调用。每代结束后 checkpoint 保存到磁盘（并删除前一代的 checkpoint 节省空间），但模型对象在内存中持续累积权重变化。

### 流程链
```
Gen 0: pretrained GPT-2 → generate → select → train(in-place) → M_0
Gen 1: M_0 → generate → select → train(in-place) → M_1
Gen 2: M_1 → generate → select → train(in-place) → M_2
...
```

**`run_phase2.sh` 和 `run_ext_seed123.sh`** 均使用相同的 `--self_iterate` 参数调用 `run_mvp.py`，配置一致（8 generations, seed 42/123），设计无差异。

---
