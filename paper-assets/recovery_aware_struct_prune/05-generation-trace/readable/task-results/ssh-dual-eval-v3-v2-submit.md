# ssh dual eval v3 v2 submit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_dual_eval_v3_v2_submit_20260521T045331_result.json`
- **Structured JSON:** [`9c80805a1e31176f2df7.json`](../../sessions/9c/9c80805a1e31176f2df7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **命令 1** PID=322438 (CKA-only 25% eval, cuda:0)
- **命令 2** PID=322606 (Random 20% eval, cuda:1)

**验证输出：**

CKA-only 25% log 尾部：
```
2026-05-21 12:53:53,278 [INFO] Loading model from /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25
2026-05-21 12:53:53,876 [INFO] Non-uniform MLP detected: intermediate_size range [8128, 18944]
```

Random 20% log 尾部：
```
2026-05-21 12:54:24,716 [INFO] Non-uniform MLP detected: intermediate_size range [11508, 17592]
2026-05-21 12:54:24,716 [INFO] Non-uniform attention detected: heads range [7, 28], kv_heads range [1, 4]
```

nvidia-smi：
```
0, 88 %, 12519 MiB   ← cuda:0 已在工作
1, 0 %, 0 MiB        ← cuda:1 模型尚在加载中
2, 0 %, 0 MiB
3, 0 %, 0 MiB
```

两个 eval 均已启动。cuda:0 上 CKA-only 25% 已加载模型开始推理；cuda:1 上 Random 20% 模型加载稍慢，尚未占用显存。

---
