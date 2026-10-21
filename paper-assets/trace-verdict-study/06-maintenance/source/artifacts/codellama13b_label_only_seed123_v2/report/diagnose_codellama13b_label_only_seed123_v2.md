# 诊断报告：codellama13b_label_only_seed123_v2

## 失败原因

**直接原因**：根分区磁盘满（30G/30G, 100% used），最终 checkpoint-444 保存失败。

```
safetensors_rust.SafetensorError: Error while serializing: I/O error: No space left on device (os error 28)
```

Traceback 路径：`trainer.train()` → `_maybe_log_save_evaluate` → `_save_checkpoint` → `save_pretrained` → `safe_save_file`

**注意**：错误发生在训练循环内部的 checkpoint 保存（epoch 3 结束后），不是 `&&` 链接的 `evaluate.py`。`evaluate.py` 从未执行。

## 训练是否完成

**训练本身完成了全部 444 steps（3 epochs）**，但最终 checkpoint 保存失败。

### Checkpoint 状态

| Checkpoint | 状态 | 大小 |
|-----------|------|------|
| checkpoint-148 (epoch 1) | 存在 | 未详查 |
| checkpoint-296 (epoch 2) | **完整** | ~738MB（含 optimizer.pt, adapter_model.safetensors 250MB） |
| checkpoint-444 (epoch 3) | **不完整** | 只有截断的 adapter_model.safetensors (151MB vs 正常 250MB) |

## 训练 Metrics（关键发现：模型 COLLAPSE）

整个 epoch 2-3 期间：

- **loss: 0.0**（完全 collapse）
- **grad_norm: ~1e-5 到 0.0**（梯度消失）
- **eval_loss: nan**（epoch 2 和 epoch 3 均为 nan）
- **eval_mean_token_accuracy: 0.117**（极低）
- **entropy: ~0.25**（退化到极低熵分布）

这与 seed42 的结果完全一致（seed42 = 28.5%, 全预测 fail）。

## 科学结论

**Label-only collapse 对 CodeLlama-13B 是 systematic 的。**

- seed42: collapsed（28.5%, 全预测 fail）
- seed123: collapsed（loss=0.0, eval_loss=nan, entropy=0.25）
- 与 DeepSeek collapse pattern 一致

结论支持假设："label-only collapse is systematic for non-Qwen architectures"。

## 恢复方案

### 短期
1. **清理磁盘空间**：根分区 30G 已满，需要清理（删除旧 checkpoint、移动大文件到 /root/autodl-tmp/）
2. **运行 evaluate.py on checkpoint-296**：虽然模型已 collapse，但为完整性可在 checkpoint-296 上跑 eval 拿正式数字

### 实际建议
鉴于模型已完全 collapse（loss=0.0 from epoch 2），**重跑 eval 科学意义不大**。训练日志中的 metrics 已足以证明 collapse 是 systematic 的。建议：
- 记录此结果到实验 report
- 不需要重跑这个实验
- **优先解决磁盘满问题**（影响后续所有实验）

## 环境状态

### 磁盘
```
overlay  30G  30G  300K  100%  /        ← 根分区已满！
/dev/sda2  439G  17G  400G  4%         ← 数据盘有大量空间
```

### GPU
2× NVIDIA RTX PRO 6000 Black (98GB each)，训练已结束，GPU 空闲。GPU 0 仍有 49GB 占用（残留 CUDA context），无活跃进程。
