# Repo-Level 实验失败诊断报告

**日期**: 2026-05-12
**实验**: repo-level-cls, repo-level-cwm
**服务器**: seetacloud-westd-4x5090

## 错误摘要

两个实验错误完全相同，在训练第一个 step 即崩溃：

```
KeyError: 'sample_weight'
```

### repo-level-cls Traceback

```
File "/home/sonny/exec-sim-repair-verifier/train_repo_verifier.py", line 124, in compute_loss
    sample_weights = inputs.pop("sample_weight")
KeyError: 'sample_weight'
```

### repo-level-cwm Traceback

```
File "/home/sonny/exec-sim-repair-verifier/train_repo_cwm.py", line 122, in compute_loss
    sample_weights = inputs.pop("sample_weight")
KeyError: 'sample_weight'
```

## 根因分析

HF `Trainer` 默认设置 `remove_unused_columns=True`。在构建 DataLoader 前，Trainer 会检查模型 `forward()` 的签名参数，自动删除 Dataset 中不在签名里的列。

数据流：
1. `preprocess_split()` 构建 Dataset，包含 `input_ids`, `labels`, `attention_mask`, `sample_weight` 四列
2. Trainer 初始化时检测到 Qwen3 模型的 `forward()` 不接受 `sample_weight` 参数
3. Trainer 自动从 Dataset 中移除 `sample_weight` 列
4. DataLoader + DataCollatorForSeq2Seq 构建 batch 时已经没有 `sample_weight`
5. `WeightedCausalLMTrainer.compute_loss()` 尝试 `inputs.pop("sample_weight")` → KeyError

**不是** OOM、依赖缺失或数据问题。纯粹是 Trainer 的 `remove_unused_columns` 默认行为与自定义 loss 的 `sample_weight` 字段冲突。

## 修复方案

在两个文件的 `TrainingArguments` 字典 `ta` 中加一行：

```python
"remove_unused_columns": False,
```

### 具体修改

**train_repo_verifier.py** (~line 240, `ta` 字典内):
```python
ta = {
    ...
    "gradient_checkpointing": True,
    "dataloader_num_workers": 4,
    "remove_unused_columns": False,   # ← 添加此行
}
```

**train_repo_cwm.py** (~line 238, `ta` 字典内):
```python
ta = {
    ...
    "gradient_checkpointing": True,
    "dataloader_num_workers": 4,
    "remove_unused_columns": False,   # ← 添加此行
}
```

无需其他改动。`DataCollatorForSeq2Seq` 会将 `sample_weight`（标量列表）正常 collate 为 tensor 传入 `compute_loss`。

## 环境确认

- 训练代码存在：`train_repo_verifier.py` (9890B), `train_repo_cwm.py` (9742B)
- 数据目录完整：`swebench_train.jsonl` (413MB), `swebench_val.jsonl` (67MB), `swebench_test.jsonl` (60MB)
- 数据加载成功：train=70748, val=9335
- 模型加载成功：Qwen3-4B, LoRA trainable 0.29%
- GPU 未涉及（第一个 step 前向还没跑完就崩了）
