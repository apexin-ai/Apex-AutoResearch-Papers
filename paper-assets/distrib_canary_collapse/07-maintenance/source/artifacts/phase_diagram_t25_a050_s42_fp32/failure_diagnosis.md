# Failure Diagnosis: phase_diagram_t25_a050_s42_fp32

**Server**: westd-17855  
**EXIT_CODE**: 1  
**Runtime**: ~5.76 GPU hours  

## 1. 失败原因

```
safetensors_rust.SafetensorError: Error while serializing: I/O error: No space left on device (os error 28)
```

磁盘 100% 满：`/dev/md0  350G  350G  1.2M  100%  /root/autodl-tmp`

崩溃点：`iterative_train.py:316` → `model.save_pretrained(ckpt_path)` — gen_14 训练完成（5000/5000 steps, loss=1.069），但保存 checkpoint 时磁盘空间耗尽。

## 2. 实验进度

- **完成**: gen_0 ~ gen_13（14/25 generations），全部有完整 metrics.json 和 checkpoint
- **失败**: gen_14 — 训练完成但 checkpoint 截断（model.safetensors 293MB vs 正常 1.6GB），无 metrics.json，无 tokenizer 文件
- **未开始**: gen_15 ~ gen_24

## 3. Partial Results

gen_0 ~ gen_13 的数据完整可用：
- 每个 generation 有 metrics.json（含 token_entropy, self_bleu, ece, effective_rank, perplexity, distinct_1/2/3, mauve）
- 每个 generation 有完整 checkpoint（~1.6GB model.safetensors + tokenizer）
- 总占用 3.5GB（实验目录），phase_diagram 整体占 36GB

gen_14 的训练指标可从日志提取（train_loss=1.069），但 checkpoint 不可用需删除重建。

## 4. 重试方案

### 必须修复
1. **释放磁盘空间**：350G 已满，phase_diagram 目录占 36GB。可考虑：
   - 清理已完成实验的中间 checkpoint（只保留 metrics.json）
   - 或转移到更大容量服务器
2. **删除 gen_14 损坏 checkpoint**：`rm -rf results/phase_diagram/t25_a050_s42_fp32/gen_14/`
3. **添加 HF_HOME 三件套**（M060 硬约束）：原始命令缺失，需加上：
   ```
   HF_HOME=/root/autodl-tmp/.hf_cache
   HF_HUB_CACHE=/root/autodl-tmp/.hf_cache
   TRANSFORMERS_CACHE=/root/autodl-tmp/.hf_cache
   ```

### 重试策略
- 如果 iterative_train.py 支持 `--resume_from_gen 14`：从 gen_13 checkpoint 恢复，只需跑剩余 11 个 generation
- 如果不支持断点续跑：需要从头跑，但可复用 gen_0~gen_13 数据
- 预估剩余空间需求：11 gen × ~250MB（metrics+data，不含 checkpoint 清理时）≈ 2.7GB；含 checkpoint 约 11 × 1.6GB ≈ 17.6GB

### 根因
与 C007 约束一致——提交实验前未 `df -h` 确认空间。350G 总容量对 T=25 实验（25 gen × ~1.6GB checkpoint ≈ 40GB 仅 checkpoint）本就紧张。
