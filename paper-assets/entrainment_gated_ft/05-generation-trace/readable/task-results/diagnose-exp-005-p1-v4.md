# diagnose exp 005 p1 v4

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-005-p1-v4_20260522T150706_result.json`
- **Structured JSON:** [`83ece910411859201679.json`](../../sessions/83/83ece910411859201679.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论**：实验**没有以 EXIT_CODE=1 退出** — 进程仍在运行，但 DeltaNet `model.safetensors` 的 HF 下载**卡死**了。

关键事实：
- PID 870648 及整个进程树（tmux → bash → timeout → run_p1_v4.sh → python3 snapshot_download）全部存活
- `.incomplete` 文件停在 60MB (62,914,560 bytes)，自 23:07 起不再增长（距今已超 2 分钟）
- 预期模型文件约 1.33GB（参考 GLA 的 `model.safetensors` = 1,332,498,184 bytes），当前仅完成 ~4.5%
- 日志警告 `unauthenticated requests to the HF Hub`，未设置 `HF_TOKEN`
- GLA 模型此前在 21:51 成功下载，说明网络本身可达，但 AutoDL 代理对大文件不稳定

```json
{"root_cause":"HF snapshot_download for model.safetensors stalled at 60MB/1.33GB — unauthenticated HF download via AutoDL proxy hanging (Warning: unauthenticated requests)","error_type":"infrastructure","fix_steps":["Kill current stalled process: tmux kill-session -t exp-005-p1-v4","Set HF_TOKEN in script for authenticated access (higher rate limits), OR switch to ModelScope download per CLAUDE.md recommendation","Clean up incomplete file: rm -rf /root/entrainment_gated_ft/models/340M-20B-DeltaNet-hybrid-3-1/.cache/","Re-run experiment"],"can_auto_fix":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "HF snapshot_download for model.safetensors stalled at 60MB/1.33GB — unauthenticated HF download via AutoDL proxy hanging (Warning: unauthenticated requests)",
    "error_type": "infrastructure",
    "fix_steps": [
      "Kill current stalled process: tmux kill-session -t exp-005-p1-v4",
      "Set HF_TOKEN in script for authenticated access (higher rate limits), OR switch to ModelScope download per CLAUDE.md recommendation",
      "Clean up incomplete file: rm -rf /root/entrainment_gated_ft/models/340M-20B-DeltaNet-hybrid-3-1/.cache/",
      "Re-run experiment"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
