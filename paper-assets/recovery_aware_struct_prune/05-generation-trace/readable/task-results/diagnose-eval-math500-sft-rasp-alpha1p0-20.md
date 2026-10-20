# diagnose eval math500 sft rasp alpha1p0 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_math500_sft_rasp_alpha1p0_20_20260522T175155_result.json`
- **Structured JSON:** [`40458864f328ddc28d31.json`](../../sessions/40/40458864f328ddc28d31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```json
{"status":"crashed", "progress":"304/500", "accuracy":"N/A", "root_cause":"进程在304/500处被kill，日志无traceback/错误信息，最后写入01:44:43后停止。1分钟后(01:45) alpha3p0 eval (PID 66827)在同一cuda:0上启动——大概率被手动kill让位", "gpu0_current_user":"PID 66827 (eval_math500_sft_rasp_alpha3p0_20, 16492 MiB)"}
```

补充：results JSON 不存在，需要重跑。当前 4 张 GPU 全部被占用（cuda:0=alpha3p0, cuda:1=alpha2p0, cuda:2=alpha0p5, cuda:3=alpha4p0），alpha1p0 需等其中一个完成后才能重启。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "status": "crashed",
    "progress": "304/500",
    "accuracy": "N/A",
    "root_cause": "进程在304/500处被kill，日志无traceback/错误信息，最后写入01:44:43后停止。1分钟后(01:45) alpha3p0 eval (PID 66827)在同一cuda:0上启动——大概率被手动kill让位",
    "gpu0_current_user": "PID 66827 (eval_math500_sft_rasp_alpha3p0_20, 16492 MiB)"
  }
}
```

</details>

---
