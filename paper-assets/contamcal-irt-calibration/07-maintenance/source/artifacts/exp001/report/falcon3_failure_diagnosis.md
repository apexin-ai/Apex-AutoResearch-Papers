# Falcon3-7B SFT 训练诊断报告

**日期**: 2026-05-22  
**实验**: sft_falcon3_7b_d100_s42  
**服务器**: cqa1-21977 (RTX 4090 D, 24GB)

## 结论：当前训练正在正常运行，未发现崩溃

### 当前状态

| 指标 | 值 |
|------|-----|
| PID | 666107 |
| GPU 显存 | 19582MiB / 24564MiB (79.7%) |
| GPU 利用率 | 100% |
| 训练进度 | step 185/4159 (~4.4%) |
| 吞吐量 | ~3.65-4.50 s/it |
| 预估剩余时间 | ~4.5 小时 |
| 启动时间 | 2026-05-22 15:48:56 |

### 根因分析

**"进程死了 5 次"大概率指的是此前不同 batch size 配置的尝试，不是当前运行：**

1. **日志中无任何 OOM/SIGKILL/crash 记录** — grep 确认零匹配
2. **"Loading tokenizer" 仅出现 1 次** — 证明日志中只有一次启动，无重启痕迹
3. **训练连续进行 12+ 分钟未中断** — 已超过所称的 "10 分钟内崩溃" 窗口
4. **全盘只有一个 falcon3 log 文件** — 无历史崩溃日志留存（每次重启覆写）

### 当前配置分析

**模型**: Falcon3-7B-Base (`LlamaForCausalLM` 架构)
- vocab_size=131072, hidden_size=3072, 28 layers
- GQA: 12 heads, 4 KV heads, head_dim=256
- bf16 权重 ~14.9GB

**训练配置**:
- bs=1, grad_accum=16 (effective batch=16)
- gradient_checkpointing=True
- bf16 训练
- LoRA: r=16, alpha=32, 7 target modules
- max_seq_length=2048
- attn_implementation="sdpa"
- **未使用 QLoRA** — 没有 "QLoRA mode" 日志，模型以 full bf16 加载

**显存预估**:
- 模型权重 (bf16): ~14.9 GB
- LoRA 参数 + 优化器: ~0.3 GB
- 激活值 (gradient checkpointing, bs=1, seq=2048): ~2-3 GB
- PyTorch 开销/碎片: ~1-2 GB
- **合计 ~18-20 GB，与观测值 19.1 GB 吻合**

### 非致命错误：bitsandbytes

```
[ERROR] bitsandbytes library load error: libnvJitLink.so.13: cannot open shared object file
```

这是 **非致命警告**。bitsandbytes 在 import 时尝试加载 CUDA JIT 库失败，但因为本次训练未使用 `--load-in-4bit`，所以不影响运行。如果未来需要 QLoRA，需先修复：

```bash
pip install nvidia-nvjitlink-cu12  # 或检查 CUDA toolkit 安装
```

### 风险评估

| 风险 | 严重度 | 说明 |
|------|--------|------|
| 长序列 OOM | 中 | 79.7% 显存占用，遇到接近 2048 token 的样本时显存可能尖峰超限 |
| 显存碎片 | 低 | `expandable_segments:True` 已设置，有效缓解 |
| bitsandbytes 缺失 | 无影响 | 当前配置不依赖 bitsandbytes |

### "5 次崩溃"的可能解释

1. **bs=4 → OOM（尝试 1-2）**: 7B bf16 + bs=4 需 ~30GB，远超 24GB
2. **bs=2 → OOM（尝试 3-4）**: ~24-25GB 边界值，随机长序列触发 OOM
3. **bs=1 无 gradient checkpointing → OOM（尝试 5）**: 无 checkpoint 时激活值 ~6-8GB，总计 ~23GB 临界
4. **bs=1 + gradient checkpointing（当前）**: ~19GB，余量 ~5GB，稳定运行

### 建议

1. **不需要干预** — 当前训练稳定运行，预计 ~4.5 小时完成
2. **监控长序列风险** — 可用 `nvidia-smi` 定期检查显存峰值
3. **如果后续仍 OOM** — 降低 max_seq_length 从 2048 到 1024，或启用 QLoRA (需先修复 bitsandbytes)
4. **提升效率（可选）** — 安装 flash-attn 替换 SDPA，可再节省 ~1-2GB 显存且提速 15-20%

### Falcon3-7B 在 24GB 4090D 上 SFT 可行性

**可行**，当前配置（bs=1 + grad_accum=16 + gradient_checkpointing + bf16 LoRA）已证明可运行。显存余量 ~5GB，足够应对正常变长输入。如需更大 batch size 或更长序列，QLoRA (4-bit) + gradient_checkpointing 可将显存降至 ~10-12GB。
