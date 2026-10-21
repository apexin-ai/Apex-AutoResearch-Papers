# deploy redeploy crashed v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_redeploy_crashed_v2_20260524T145208_result.json`
- **Structured JSON:** [`a039ef39c9506758e7c7.json`](../../sessions/a0/a039ef39c9506758e7c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。最终部署状态：

```
westd-41074 GPU 0: eval_pi05_l2norm_k09_long_seed43_postfix_v2  PID=474396 ✅ (k=0.9, 230/256 tokens, 刚开始 T0)
westd-41074 GPU 1: eval_pi05_l2norm_k085_long_seed43_postfix_v2 PID=474471 ✅ (k=0.85, 217/256 tokens, 刚开始 T0)
westd-41074 GPU 2: eval_l2norm_k03_long                         PID=402927 🔄 (进行中, Task 5, SR~48.8%)
westd-41074 GPU 3: eval_pi05_l2norm_k07_long_seed43_postfix     PID=467274 🔄 (已在运行, T0 ep10=60%)
westd-38929 GPU 0: eval_pi05_l2norm_k03_long_seed42_postfix_v2  PID=568641 ✅ (k=0.3, 76/256 tokens, 刚开始评估)
```

关键信息：
- 3 个崩溃实验已修复重部署（根因：tmux 默认 shell 没有 conda 环境，加了 `source conda.sh && conda activate base`）
- GPU 3 的 k07 seed43 已由前次操作部署，无需重复
- GPU 2 正在跑 `eval_l2norm_k03_long`（非空闲），l2norm_k085_long_seed42 已完成被替换
- 两台服务器全部 GPU 满载运行

---
