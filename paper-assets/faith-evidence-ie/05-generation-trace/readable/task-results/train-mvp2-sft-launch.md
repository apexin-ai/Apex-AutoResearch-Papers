# train mvp2 sft launch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_mvp2-sft-launch_20260514T061031_result.json`
- **Structured JSON:** [`1b088f45499ba2aa9907.json`](../../sessions/1b/1b088f45499ba2aa9907.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练确认正常运行，第一个 loss 已输出：**

- **Step 10/144**: loss=1.2741, grad_norm=0.079, lr=2e-4, token_accuracy=75.9%, epoch=0.21
- 速度 ~8.1s/step, 预计总训练时间 ~20 分钟

## 任务完成总结

| 步骤 | 状态 |
|------|------|
| 1. 终止残留进程 | ✅ |
| 2. 部署 sft_trainer.py | ✅（修复了 TRL 1.1.0 兼容性：`max_seq_length`→`max_length`, `tokenizer`→`processing_class`, 加入 `device_map` per-rank） |
| 3. 数据加载验证 | ✅ Train=3027, Dev=985 |
| 4. 提交 SFT 训练 | ✅ 4×RTX 5090, DeepSpeed ZeRO-2 + QLoRA |
| 5. 验证训练启动 | ✅ loss=1.2741 @ step 10 |
| 6. 更新 registry | ✅ RUNNING，完整 spec 已记录 |

修复的 3 个 TRL 1.1.0 兼容性问题：
1. `SFTConfig.max_seq_length` → `max_length`
2. `SFTTrainer(tokenizer=...)` → `SFTTrainer(processing_class=...)`
3. accelerate config 改为 `MULTI_GPU` + 代码加 `device_map={"": local_rank}` 解决多 GPU 模型加载冲突

---
