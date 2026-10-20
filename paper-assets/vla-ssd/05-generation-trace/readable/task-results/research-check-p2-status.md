# research check p2 status

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check_p2_status_20260516T102243_result.json`
- **Structured JSON:** [`6b67e00d39b18b7c6863.json`](../../sessions/6b/6b67e00d39b18b7c6863.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整输出：

**1. tmux sessions**
```
ablation_p2_demo_sensitivity: 1 windows (created Sat May 16 18:17:16 2026)
```

**2. GPU 利用率**
```
0, 0 %, 0 MiB, 97887 MiB
1, 0 %, 1739 MiB, 97887 MiB
```

**3. P2 脚本**
```
-rw-r--r-- 1 root root 13029 May 16 18:14 /root/vla-ssd/scripts/ablations/demo_sensitivity.py
SCRIPT_EXISTS
```

**4. P2 结果文件**
```
-rw-r--r-- 1 root root 716 May 16 18:16 /root/autodl-tmp/vla-ssd/results/ablations/demo_sensitivity_25.json
RESULT_EXISTS
```

**5. P2 log**
```
(空输出 — 文件存在但 tail -10 返回空)
```

总结：tmux session `ablation_p2_demo_sensitivity` 存在但 GPU 利用率为 0%，结果文件已生成（716 bytes），log 文件为空。看起来 P2 任务可能已完成或未实际启动运行。

---
