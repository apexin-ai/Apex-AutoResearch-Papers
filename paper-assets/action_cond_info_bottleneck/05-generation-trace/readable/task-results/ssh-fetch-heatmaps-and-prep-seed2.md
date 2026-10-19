# ssh fetch heatmaps and prep seed2

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fetch-heatmaps-and-prep-seed2_20260517T133632_result.json`
- **Structured JSON:** [`6a8815cbf4f0d1d365eb.json`](../../sessions/6a/6a8815cbf4f0d1d365eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

### Phase 1: Heatmap 下载 ✓

4 个 PNG 已下载到本地：
```
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/v72_heatmaps/
├── seed1_probe_A.png  (257 KB)
├── seed1_probe_B.png  (256 KB)
├── seed2_probe_A.png  (257 KB)
└── seed2_probe_B.png  (256 KB)
```

### Phase 2: Eval 进度

两个 eval 均为 **seed1** (`acib_v7.2_connector_scorer`)，都还在第一个 suite `libero_spatial`（共 4 个 suite）：

| Eval | PID | GPU | 当前 suite | Episodes | Success Rate |
|------|-----|-----|-----------|----------|-------------|
| alpha=0.0 | 40598 | GPU 0 (6581 MiB) | libero_spatial | ~47/50 (94%) | 74.5% |
| alpha=1.0 | 44022 | GPU 1 (6021 MiB) | libero_spatial | ~41/50 (82%) | 80.5% |

尚无已完成的 suite 结果文件。按 4 个 suite × 50 episodes 的节奏，预计还需较长时间。

### Phase 3: Seed2 eval 脚本 ✓

```
artifacts/run_v72_eval_seed2_alpha00.sh  (GPU 0, alpha=0.0, seed2 checkpoint)
artifacts/run_v72_eval_seed2_alpha10.sh  (GPU 1, alpha=1.0, seed2 checkpoint)
```

---
