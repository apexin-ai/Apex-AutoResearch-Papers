# diagnose exp 001 eval 05B aligned batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_eval_05B_aligned_batch_20260514T144204_result.json`
- **Structured JSON:** [`617da5c48e53d2363841.json`](../../sessions/61/617da5c48e53d2363841.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

```json
{
  "completed_runs": ["d000_orig", "d000_para", "d005_orig", "d005_para"],
  "incomplete_runs": ["d100_orig", "d100_para"],
  "partial_results": "d100_aligned 目录已创建但为空（0文件），evaluate.py 被 timeout 杀死时未来得及写出结果。d100_para_aligned 目录不存在（从未启动）",
  "gpu2_status": "空闲 (0MiB / 24564MiB, 0% util, 无进程)",
  "timeout_setting": "脚本本身无 timeout。EXIT_CODE=124 来自 job runner 的 timeout_hours（默认 24h，实际用了约 6h，从 08:47 UTC 到 14:39 UTC = 5h52m）",
  "log_status": "/tmp/eval_05B_aligned_batch.log 不存在（已清理或未写入该路径）",
  "timeline": "d000_orig 18:52 → d000_para 19:15 → d005_orig 21:26 → d005_para 21:51 → d100_orig 开始 21:51 → killed 22:39（仅跑了48min）",
  "registry_correction": "registry notes 称仅 d000 8项指标已保存，但实际 d005 orig+para 也已完成（4项新指标可补录）",
  "fix_steps": [
    "单独重跑 d100：CUDA_VISIBLE_DEVICES=2 bash run_aligned_eval_05B.sh both，但修改脚本只跑 d100（或直接调 evaluate.py 两次）",
    "更简单：直接 ssh_execute 两条 python evaluate.py 命令，分别跑 d100_orig 和 d100_para，timeout_hours 设 3h 足够",
    "跑完后补录 d005 + d100 指标到 registry"
  ]
}
```

**关键发现**: 实际完成了 4/6 runs（不是 notes 说的 2/6）。d005 original + paraphrase 结果完整，需更新 registry。只差 d100 两个 run。每个 original eval 约 2h，paraphrase 约 25min，d100 单独跑 ~2.5h 即可完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "completed_runs": [
      "d000_orig",
      "d000_para",
      "d005_orig",
      "d005_para"
    ],
    "incomplete_runs": [
      "d100_orig",
      "d100_para"
    ],
    "partial_results": "d100_aligned 目录已创建但为空（0文件），evaluate.py 被 timeout 杀死时未来得及写出结果。d100_para_aligned 目录不存在（从未启动）",
    "gpu2_status": "空闲 (0MiB / 24564MiB, 0% util, 无进程)",
    "timeout_setting": "脚本本身无 timeout。EXIT_CODE=124 来自 job runner 的 timeout_hours（默认 24h，实际用了约 6h，从 08:47 UTC 到 14:39 UTC = 5h52m）",
    "log_status": "/tmp/eval_05B_aligned_batch.log 不存在（已清理或未写入该路径）",
    "timeline": "d000_orig 18:52 → d000_para 19:15 → d005_orig 21:26 → d005_para 21:51 → d100_orig 开始 21:51 → killed 22:39（仅跑了48min）",
    "registry_correction": "registry notes 称仅 d000 8项指标已保存，但实际 d005 orig+para 也已完成（4项新指标可补录）",
    "fix_steps": [
      "单独重跑 d100：CUDA_VISIBLE_DEVICES=2 bash run_aligned_eval_05B.sh both，但修改脚本只跑 d100（或直接调 evaluate.py 两次）",
      "更简单：直接 ssh_execute 两条 python evaluate.py 命令，分别跑 d100_orig 和 d100_para，timeout_hours 设 3h 足够",
      "跑完后补录 d005 + d100 指标到 registry"
    ]
  }
}
```

</details>

---
