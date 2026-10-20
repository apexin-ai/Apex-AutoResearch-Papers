# diagnose eval gsm8k grpo cka only 15

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_gsm8k_grpo_cka_only_15_20260520T231118_result.json`
- **Structured JSON:** [`7dc9793f079ad1e538e6.json`](../../sessions/7d/7dc9793f079ad1e538e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

关键发现：**两个进程实际上没有被 kill，仍在运行。** 当前进度：

- **seed123** (PID 285682): 810/1319 (61.4%), acc@800=0.7250, 仍在推进
- **seed456** (PID 285821): 795/1319 (60.3%), 仍在推进

同时发现 4 个 eval 进程共存导致周期性 ~6 分钟 GPU stall（从 ~3s/it 跳到 ~110s/it），所有进程均受影响：

| 进程 | GPU | 启动时间 | 当前进度 |
|------|-----|----------|----------|
| cka_only_15_seed123 | cuda:0 | 05:36 | 810/1319 |
| cka_only_15_seed456 | cuda:1 | 05:36 | 795/1319 |
| standard_15_seed123_v3 | cuda:2 | 06:58 | 191/1319 |
| standard_15_seed456_v3 | cuda:3 | 06:58 | 161/1319 |

`eval_std15` 进程同样在 sample 71 处出现 6 分钟 stall，确认是系统级问题（PCIe 带宽争抢 / 4 进程 30GB 模型同时做 generation）。

```json
{"root_cause":"进程未被kill，仍在运行。4个eval进程(每个~30GB GPU)同时在4张RTX PRO 6000上做generation，导致周期性~6分钟PCIe/系统级stall（所有进程在相近wall-clock时间同时卡顿，从~3s/it跳到~110s/it）。日志看似截断是因为progress bar只在tmux pane刷新，log文件每50 sample才写一条。","error_type":"resource","fix_steps":["无需修复——进程仍在运行，等待完成即可（预计再需~1-2小时）","如需加速：kill掉eval_std15的2个进程(PID 293079, 293153)减少资源争抢，待cka_only_15完成后再重跑","未来避免同时运行4个eval：每次最多2个进程并发"],"can_auto_fix":false,"partial_results":{"seed123_acc_at_750":0.7320,"seed456_acc_at_750":0.7253,"seed123_acc_at_800":0.7250,"results_files_exist":false,"processes_alive":true,"current_progress_seed123":"810/1319","current_progress_seed456":"795/1319"}}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "进程未被kill，仍在运行。4个eval进程(每个~30GB GPU)同时在4张RTX PRO 6000上做generation，导致周期性~6分钟PCIe/系统级stall（所有进程在相近wall-clock时间同时卡顿，从~3s/it跳到~110s/it）。日志看似截断是因为progress bar只在tmux pane刷新，log文件每50 sample才写一条。",
    "error_type": "resource",
    "fix_steps": [
      "无需修复——进程仍在运行，等待完成即可（预计再需~1-2小时）",
      "如需加速：kill掉eval_std15的2个进程(PID 293079, 293153)减少资源争抢，待cka_only_15完成后再重跑",
      "未来避免同时运行4个eval：每次最多2个进程并发"
    ],
    "can_auto_fix": false,
    "partial_results": {
      "seed123_acc_at_750": 0.732,
      "seed456_acc_at_750": 0.7253,
      "seed123_acc_at_800": 0.725,
      "results_files_exist": false,
      "processes_alive": true,
      "current_progress_seed123": "810/1319",
      "current_progress_seed456": "795/1319"
    }
  }
}
```

</details>

---
