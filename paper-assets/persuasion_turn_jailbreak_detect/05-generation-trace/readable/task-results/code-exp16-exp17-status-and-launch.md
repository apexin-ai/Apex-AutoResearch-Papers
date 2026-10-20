# code exp16 exp17 status and launch

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp16-exp17-status-and-launch_20260519T231145_result.json`
- **Structured JSON:** [`37497d1c65159d7684ab.json`](../../sessions/37/37497d1c65159d7684ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果文件正常生成（F1=0.8146 for vanilla seed42 mixed_test）。`F1=?` 是脚本解析字段名不匹配，不影响实际数据。

---

**最终状态汇报：**

```
exp16 MLM 完成度: 6/6 checkpoints ✅
exp16 eval: started, vanilla seed42 已完成 7 个 test sets，继续剩余 variants/seeds
exp17 数据: jailbreak 250/250 ✅, benign 250/250 ✅
exp17 合并: done (1000条, 700/150/150 split) ✅
exp17 训练: 
  - vanilla 3 seeds: ✅ done
  - MLM stage1 seed42: running (Epoch 1, step 320/385, loss 6.09↓)
  - 9-class stage2 seed42: running (pre-computing embeddings)
  - 待完成: MLM seeds 123,456 + MLM stage2 all + 9-class seeds 123,456
GPU 使用: 0=exp16_eval(切换中), 1=idle, 2=MLM(20.6GB), 3=9-class(10.3GB)
```

**修复的问题：**
1. 首次 tmux 杀进程误杀了 tmux server，连带终止了 exp17 两个会话
2. resume 脚本缺少 `TRANSFORMERS_OFFLINE=1` + `HF_HUB_OFFLINE=1`，导致 transformers import 联网超时卡死
3. Python 输出重定向到文件时缺少 `PYTHONUNBUFFERED=1`，看不到实时日志

三个 tmux 会话 (`exp16_eval`, `exp17_gpu2`, `exp17_gpu3`) 均正常运行中。

---
