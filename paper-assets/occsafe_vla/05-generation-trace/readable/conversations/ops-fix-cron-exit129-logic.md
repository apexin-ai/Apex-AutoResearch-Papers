# ops fix cron exit129 logic

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_ops_fix-cron-exit129-logic_20260528T070507.jsonl`
- **Structured JSON:** [`6ae78155ab1f9d50055f.json`](../../sessions/6a/6ae78155ab1f9d50055f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-28T07:06:12.401419+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_fix-cron-exit129-logic_20260528T070507",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-28T07:06:12.401759+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_fix-cron-exit129-logic_20260528T070507",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-28T07:06:12.401929+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "cat /root/poll_eval_detach_ln_v2_s2.sh",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_fix-cron-exit129-logic_20260528T070507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "cat /root/poll_eval_detach_ln_v2_s2.sh",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-28T07:06:12.402062+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "cat /root/poll_eval_vanilla_object_s1.sh",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_fix-cron-exit129-logic_20260528T070507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "cat /root/poll_eval_vanilla_object_s1.sh",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-28T07:06:12.402214+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\nCHKPT_DIR=\\\"/root/autodl-tmp/checkpoints/detach_ln_v2_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s2--50000_chkpt\\\"\\nTRAIN_PID=47162\\nLOG=\\\"/root/poll_eval_detach_ln_v2_s2.log\\\"\\n\\necho \\\"$(date -u): Polling started for detach_ln_v2_s2\\\" >> $LOG\\n\\nwhile true; do\\n    if [ -d \\\"$CHKPT_DIR\\\" ] && [ -f \\\"$CHKPT_DIR/lora_adapter/adapter_config.json\\\" ]; then\\n        echo \\\"$(date -u): 50000_chkpt detected! Waiting 60s for save to complete...\\\" >> $LOG\\n        sleep 60\\n        echo \\\"$(date -u): Killing training PID $TRAIN_PID\\\" >> $LOG\\n        kill $TRAIN_PID 2>/dev/null\\n        sleep 5\\n        ps -p $TRAIN_PID -o pid= 2>/dev/null && kill -9 $TRAIN_PID 2>/dev/null\\n        echo \\\"$(date -u): Starting eval on cuda:0...\\\" >> $LOG\\n        source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe\\n        cd /root/occsafe_vla/openvla-oft\\n        MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python3 vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_v2_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s2--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42 >> $LOG 2>&1\\n        echo \\\"$(date -u): Eval completed with exit code $?\\\" >> $LOG\\n        break\\n    fi\\n    sleep 60\\ndone\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.24}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_fix-cron-exit129-logic_20260528T070507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-28T07:06:12.402388+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\nLOG=\\\"/root/poll_eval_vanilla_object_s1.log\\\"\\nTRAIN_PID=798980\\nCHKPT_BASE=\\\"/root/autodl-tmp/checkpoints/vanilla_object_s1\\\"\\n\\necho \\\"$(date -u): Polling started for vanilla_object_s1\\\" >> $LOG\\n\\nwhile true; do\\n    CHKPT_DIR=$(ls -d ${CHKPT_BASE}/*50000_chkpt 2>/dev/null | head -1)\\n    if [ -n \\\"$CHKPT_DIR\\\" ] && [ -f \\\"$CHKPT_DIR/lora_adapter/adapter_config.json\\\" ]; then\\n        echo \\\"$(date -u): 50000_chkpt detected at $CHKPT_DIR! Waiting 60s for save to finish...\\\" >> $LOG\\n        sleep 60\\n        if ps -p $TRAIN_PID -o pid= 2>/dev/null; then\\n            echo \\\"$(date -u): Training still running, waiting for natural exit...\\\" >> $LOG\\n            for i in $(seq 1 10); do\\n                sleep 60\\n                if ! ps -p $TRAIN_PID -o pid= 2>/dev/null; then\\n                    echo \\\"$(date -u): Training process exited naturally\\\" >> $LOG\\n                    break\\n                fi\\n            done\\n            if ps -p $TRAIN_PID -o pid= 2>/dev/null; then\\n                echo \\\"$(date -u): Killing training PID $TRAIN_PID\\\" >> $LOG\\n                kill $TRAIN_PID 2>/dev/null\\n                sleep 5\\n                kill -9 $TRAIN_PID 2>/dev/null\\n            fi\\n        fi\\n        echo \\\"$(date -u): Starting eval on cuda:0...\\\" >> $LOG\\n        source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe\\n        cd /root/occsafe_vla/openvla-oft\\n        CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python3 vla-scripts/evaluate_safelibero.py \\\\\\n            --pretrained_checkpoint \\\"$CHKPT_DIR\\\" \\\\\\n            --task_suite_name libero_object \\\\\\n            --num_rollouts 50 \\\\\\n            --seed 42 >> $LOG 2>&1\\n        echo \\\"$(date -u): Eval completed with exit code $?\\\" >> $LOG\\n        break\\n    fi\\n    sleep 60\\ndone\\n\", \"stderr\": \"\", \"
…[truncated 80 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_fix-cron-exit129-logic_20260528T070507",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T07:06:12.402675+00:00_

两个脚本都已读取完毕。分析如下：

**westd-34685 `poll_eval_detach_ln_v2_s2.sh`** 和 **westd-10894 `poll_eval_vanilla_object_s1.sh`** 的逻辑都是：
1. 轮询检测 `50000_chkpt` 目录 + `adapter_config.json` 存在
2. 等待 60s 确保写入完成
3. `kill` 训练进程（不依赖其退出码）
4. 启动 eval
5. `break` 退出循环

两个脚本都**不使用训练进程的退出码做任何判断**。`$?` 只在日志中记录的是 eval 的退出码，不是训练的。脚本最终通过 `break` 退出 while 循环，自身退出码为 0（最后执行的 `echo` 成功）。

**结论：脚本本身无问题，问题在 cron 监控层。**

cron 监控系统独立追踪训练进程的 PID，当训练进程被轮询脚本 kill 后以 exit 129 (128 + SIGHUP) 退出时，cron 系统将其判定为 `conclusion=failed`。这是 cron 监控系统的退出码判定逻辑问题——它没有区分"被外部 kill 导致的非零退出"和"训练本身失败导致的非零退出"。

按要求，不修改 cron 监控代码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_fix-cron-exit129-logic_20260528T070507"
}
```

</details>

---
