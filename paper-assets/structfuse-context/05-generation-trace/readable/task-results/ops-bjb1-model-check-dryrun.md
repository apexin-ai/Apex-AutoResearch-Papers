# ops bjb1 model check dryrun

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1-model-check-dryrun_20260513T032947_result.json`
- **Structured JSON:** [`aebc13a66206befa7614.json`](../../sessions/ae/aebc13a66206befa7614.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完成。汇报结果：

```
=== 模型下载 ===
Qwen2.5-Coder-3B: 完成 ✓
  路径: /root/autodl-tmp/models/Qwen/Qwen2.5-Coder-3B/Qwen/Qwen2.5-Coder-3B/
  大小: 5.8G (2个safetensors + tokenizer + config 齐全)
  注意: ModelScope 下载，路径嵌套了一层 Qwen/Qwen2.5-Coder-3B/

StarCoder2-3B: 下载中 (53%, 5.98G/11.3G, ~6min)
  PID 2821 运行中

flash-attn: 编译中
  PID 3106 运行中

=== 训练数据 ===
路径: /root/autodl-tmp/structfuse/m2_early_pilot_data/ (脚本引用路径)
存在: NO
  - /root/autodl-tmp/structfuse/ 目录不存在
  - 整个服务器上未找到任何 .jsonl 文件
  - 代码 scp 过来时只复制了 /root/structfuse/ 源码，数据未同步

=== Dry-run ===
train.py 路径: /root/structfuse/training/train.py
dry-run 支持: 无 (无 --dry-run 参数)
执行: 跳过 — 训练数据缺失
结论: BLOCKED

=== 阻塞项 ===
1. 训练数据缺失: 需从 cqa1 服务器 scp 数据目录 m2_early_pilot_data/ 到 /root/autodl-tmp/structfuse/m2_early_pilot_data/
2. 模型路径不匹配: 脚本引用 /root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B，
   实际下载到 /root/autodl-tmp/models/Qwen/Qwen2.5-Coder-3B/Qwen/Qwen2.5-Coder-3B/
   需要创建 symlink 或更新脚本路径
```

---
