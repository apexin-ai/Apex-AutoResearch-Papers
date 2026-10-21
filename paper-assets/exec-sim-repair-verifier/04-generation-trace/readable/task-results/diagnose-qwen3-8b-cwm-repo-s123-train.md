# diagnose qwen3 8b cwm repo s123 train

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_qwen3-8b-cwm-repo-s123-train_20260519T222753_result.json`
- **Structured JSON:** [`8b3816302403246093bf.json`](../../sessions/8b/8b3816302403246093bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。PID 842756 已死但 GPU 3 内存未释放（26.7GB 泄漏），GPU 1 也有孤立计算上下文（100% util, 0 memory）。这是系统性的 OOM kill。

## 诊断结论

**根因：容器 cgroup OOM killer (SIGKILL)**

| 指标 | 值 |
|---|---|
| 容器内存上限 | 360GB (`memory.max`) |
| 当前使用 | 68.4GB |
| 历史 OOM 事件 | 18,115 次 |
| 历史 OOM 杀死进程 | **85 次** |

多个训练/eval 任务并发运行时，合计 RAM 超过 360GB 上限，cgroup OOM killer 选中 qwen3-8b 进程发送 SIGKILL。

**证据链**：
1. Python 日志无任何错误 → SIGKILL 无法被捕获
2. 无 EXIT_CODE、无 `.exit` 文件 → bash trap 也无法捕获 SIGKILL
3. dmesg 在容器内为空（OOM kill 仅记录在宿主机）
4. `memory.events` 显示 `oom_kill=85`
5. GPU 3 上 PID 842756 已死但显存未释放（26.7GB 泄漏）— 另一个 OOM kill 受害者
6. GPU 1 显示 100% util / 0 MiB — 孤立计算上下文

**其他同时死亡的实验也是同一原因**（D133-cwm-s42、deepseek-cwm-repo-s123 等均为 cgroup OOM kill 受害者）。

```json
{"root_cause":"cgroup OOM killer: memory.events shows oom=18115, oom_kill=85; container memory.max=360GB exceeded by concurrent GPU jobs; process received SIGKILL (no trap/log possible)","error_type":"resource","fix_steps":["清理 GPU 1 和 GPU 3 的孤立显存（kill 残留进程或 nvidia-smi --gpu-reset）","限制并发 GPU 任务数 ≤2，避免 RAM 超过 360GB 上限","从 checkpoint-300 恢复训练：添加 --resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cwm_8b_s123/checkpoint-300","启动前监控内存：watch -n 10 'cat /sys/fs/cgroup/memory.current | numfmt --to=iec'","考虑 SeetaCloud 升配或减少单任务 RAM 占用（如用 mmap 加载数据集）"],"can_auto_fix":true,"checkpoint_exists":true,"checkpoint_step":300}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "cgroup OOM killer: memory.events shows oom=18115, oom_kill=85; container memory.max=360GB exceeded by concurrent GPU jobs; process received SIGKILL (no trap/log possible)",
    "error_type": "resource",
    "fix_steps": [
      "清理 GPU 1 和 GPU 3 的孤立显存（kill 残留进程或 nvidia-smi --gpu-reset）",
      "限制并发 GPU 任务数 ≤2，避免 RAM 超过 360GB 上限",
      "从 checkpoint-300 恢复训练：添加 --resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cwm_8b_s123/checkpoint-300",
      "启动前监控内存：watch -n 10 'cat /sys/fs/cgroup/memory.current | numfmt --to=iec'",
      "考虑 SeetaCloud 升配或减少单任务 RAM 占用（如用 mmap 加载数据集）"
    ],
    "can_auto_fix": true,
    "checkpoint_exists": true,
    "checkpoint_step": 300
  }
}
```

</details>

---
