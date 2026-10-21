# diagnose precompute pi05 spatial 2048 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_precompute-pi05-spatial-2048-r2_20260524T055509_result.json`
- **Structured JSON:** [`883474a5b38f9b278e82.json`](../../sessions/88/883474a5b38f9b278e82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

# 诊断报告：precompute-pi05-spatial-2048-r2

## 失败根因

**没有失败——spatial precompute 实际上已成功完成。** Cron 的告警是误判。

证据链：
- `train_crm.py:107-108` 在启动时检测 `manifest.json` 存在就直接跳过并退出（这正是"~17秒"的来源）
- spatial 缓存目录 `/root/autodl-tmp/crm_cache_pi05_2048/spatial/` 已含完整产出：
  - `manifest.json`：`{"benchmark": "spatial", "n_samples": 60250, "K": 10, "obs_dim": 2048, "h_eff": 5}`
  - `obs_features.pt` (494MB)、`k_samples.pt` (72MB)、`expert_actions.pt` (7.2MB)
  - 全部修改时间 May 24 13:32:50
- 原始 spatial 日志最后一行：`[merge] Saved 60250 samples + manifest to /root/autodl-tmp/crm_cache_pi05_2048/spatial` — 走完了 60250/60250，merge 阶段完成
- 原始 spatial 进程从 May 23 04:19 跑到 May 24 13:32，共 ~33h，全程无 traceback / OOM / CUDA error

Cron 的 "Process exited without valid W&B metrics" 检查不适用——precompute 是数据预处理脚本，**不会发出 W&B 指标**。-r2 重跑只是命中"manifest 已存在"分支，秒退后被 cron 误标为失败。

## 其他 3 个任务健康状态

均正常运行（无需干预）：

| benchmark | PID | GPU | 显存 | 日志最近写入 | 状态 |
|-----------|-----|-----|------|--------------|------|
| object    | 113456 | 0 | 9874MiB | 13:54 | 正常 |
| goal      | 114159 | 2 | 9874MiB | 13:53 | 正常 |
| long      | 114507 | 3 | 9874MiB | 13:55 | 正常 |

GPU 1 已空闲（spatial 完成后释放）。系统层面无 OOM、无 GPU 错误。

## 注意事项 & 建议

- **不要重跑 spatial**：缓存已完整，重跑会立即跳过。如果硬要重新生成，需先 `rm /root/autodl-tmp/crm_cache_pi05_2048/spatial/manifest.json`
- **更新 cron 告警逻辑**：precompute 任务应基于 `manifest.json` 存在 + 日志末尾包含 `[merge] Saved` 来判定成功，而非 W&B 指标
- **磁盘空间警告**：`/root/autodl-tmp` 已用 196G/250G (79%)，剩余 3 个 benchmark（object/goal/long）各会再写入 ~580MB 最终产物 + 大量 partial。建议 spatial 完成后 `rm /root/autodl-tmp/crm_cache_pi05_2048/spatial/partial_s*.pt`（约 570MB 可回收）；对其他 benchmark 完成后同样处理

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "benchmark": "spatial",
    "n_samples": 60250,
    "K": 10,
    "obs_dim": 2048,
    "h_eff": 5
  }
}
```

</details>

---
