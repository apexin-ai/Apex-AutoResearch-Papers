# diagnose alpha3 sft failures westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_alpha3_sft_failures_westb_20260522T084932_result.json`
- **Structured JSON:** [`d050d6d8898d4cb96ba7.json`](../../sessions/d0/d050d6d8898d4cb96ba7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到确凿证据了。

```
根因: 磁盘满（数据盘 /root/autodl-tmp/ 100% 使用，250G/250G，剩余 528K）

证据: /tmp/alpha3p0_pipeline.log 末尾完整错误链：
  1. SFT 训练到 epoch 1 结束（step 935/1870），触发 save_strategy="epoch" 保存 checkpoint
  2. model.safetensors（12GB）写入成功
  3. 写 optimizer.pt（11GB）时磁盘空间耗尽：
     - torch.serialization: "RuntimeError: basic_ios::clear: iostream error"
     - "RuntimeError: [enforce fail at inline_container.cc:668] unexpected pos 11135879360 vs 11135879256"
  4. 进程崩溃退出

sft_recovery.py 修复状态: 已修（无 CUDA_VISIBLE_DEVICES 硬编码）
checkpoint-935 完整性: 部分完整——model.safetensors(12GB)、config.json、tokenizer 文件存在；
                       optimizer.pt(11GB) 写入时崩溃，可能损坏
GPU 当前状态: GPU 0 空闲；GPU 1 被 PID 164710 (train_grpo_v5.py cka_only GRPO) 占用(58GB/98GB)
磁盘: /root/autodl-tmp/ 250G/250G (100%)，项目占 235G
```

**根因分析**：数据盘 250G 被 ~20 个模型/checkpoint 目录填满（各 11-22GB）。SFT 训练本身正常运行到 epoch 1 结束，保存 checkpoint 时 model.safetensors 刚好写完，但紧接着写 optimizer.pt 时磁盘彻底满了，进程崩溃。这解释了为什么三次都在差不多的位置停——每次都是 epoch 边界触发 checkpoint 保存时爆盘。

**恢复建议**：

1. **清理磁盘**——至少需要释放 ~25GB 才能保存完整 checkpoint（model 12GB + optimizer 11GB）。候选清理对象：
   - 已完成且不再需要的中间 pruned/sft 目录（每个 11-12GB）
   - checkpoint-935 中损坏的 optimizer.pt（11GB）

2. **从 checkpoint-935 恢复训练**——model.safetensors 完整，可以 resume（optimizer state 会丢失，从 epoch 2 开始 lr warmup 会有轻微偏差，但影响不大）

3. **防止复发**——在 SFT 脚本中加 `save_total_limit=2`，避免 checkpoint 无限堆积

要我清理磁盘并重启 SFT 吗？

---
