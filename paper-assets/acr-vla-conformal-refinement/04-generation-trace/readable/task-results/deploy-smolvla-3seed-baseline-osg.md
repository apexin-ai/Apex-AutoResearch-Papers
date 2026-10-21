# deploy smolvla 3seed baseline osg

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_smolvla-3seed-baseline-osg_20260522T184725_result.json`
- **Structured JSON:** [`032e497939f7c809bd13.json`](../../sessions/03/032e497939f7c809bd13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。状态汇总：

**已启动 (5/6)**：
| Suite | Seed | GPU | tmux session | 状态 |
|-------|------|-----|------|------|
| Object | 43 | cuda:0 | eval-smolvla-object-s43 | RUNNING, 模型加载中 |
| Object | 44 | cuda:1 | eval-smolvla-object-s44 | RUNNING, 模型加载中 |
| Spatial | 43 | cuda:2 | eval-smolvla-spatial-s43 | RUNNING, 模型加载中 |
| Spatial | 44 | cuda:4 | eval-smolvla-spatial-s44 | RUNNING, 模型加载中 |
| Goal | 43 | cuda:5 | eval-smolvla-goal-s43 | RUNNING, 模型加载中 |

**待启动 (1/6)**：
| Goal | 44 | - | - | QUEUED, 等前5个中任一完成 |

**关键修复**：
- 需要 `--env.type=libero` 让 draccus 解析 env config
- 需要 `--rename_map='{"observation.images.image": "observation.images.camera1", "observation.images.image2": "observation.images.camera2"}'` 修正 LIBERO↔SmolVLA 相机名映射

**监控**：已设 cron 每 5 分钟检查。eval 完成后自动更新 registry 并在释放的 GPU 上启动 goal-seed44。预计 Object/Spatial 约 15-20min，Goal 约 20-25min。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "observation.images.image": "observation.images.camera1",
    "observation.images.image2": "observation.images.camera2"
  }
}
```

</details>

---
