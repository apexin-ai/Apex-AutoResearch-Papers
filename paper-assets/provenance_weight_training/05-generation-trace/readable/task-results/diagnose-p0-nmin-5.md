# diagnose p0 nmin 5

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_p0_nmin_5_20260524T170405_result.json`
- **Structured JSON:** [`18052837b9e122bbc7b8.json`](../../sessions/18/18052837b9e122bbc7b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**根因：checkpoint 保存时磁盘 I/O 错误**

训练本身正常运行到 step 500（8%），但在保存 checkpoint 时崩溃：

```
torch.save(self.optimizer.state_dict(), ...) 
→ RuntimeError: [enforce fail at inline_container.cc:668] . unexpected pos 86016 vs 85908
→ RuntimeError: basic_ios::clear: iostream error
```

模型权重（safetensors 格式）写入成功，但 optimizer state（PyTorch zip 格式）写入失败。输出目录里无任何 checkpoint 文件留存（只有 config.json、metrics、log）。

**排除的原因：**
- 非 OOM：GPU 1 内存用量 45GB/97GB，充裕
- 非磁盘满：109G 可用，inode 1% 使用
- 非代码逻辑 bug：训练 500 步 metrics 正常

**可能的底层原因：**
- `/dev/md0`（软 RAID）的瞬时 I/O 错误
- PyTorch zipfile 序列化在该 RAID 阵列上的已知兼容性问题

**重试建议：**

值得重试，但需调整：
1. **加 `--save_safetensors_optimizer true`**（transformers ≥4.46）或 **`--save_strategy steps --save_steps 1000`** 降低保存频率
2. 或在训练脚本中设置 `trainer.args.save_only_model = True` 跳过 optimizer state 保存（0.6B 模型重新 warmup 代价很低）

**另外注意一个参数问题：** `n_min=5` 但 `batch_size=4`，导致 n_min 约束永远满足（batch 内所有样本都被保留），加权退化为均匀加权（日志中 `weighted_loss == unweighted_loss` 始终相等）。如果要让 adaptive weighting 实际起作用，需要 `n_min < batch_size`。

---
