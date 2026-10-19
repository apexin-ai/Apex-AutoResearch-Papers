# check precompute pipeline status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_precompute-pipeline-status_20260521T172145_result.json`
- **Structured JSON:** [`b81aebc4a594d4099d30.json`](../../sessions/b8/b81aebc4a594d4099d30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 关键结论

**所有 17 个 precompute 进程仍在跑**，但 pipeline-auto 有炸药桶在倒计时。

### 进度快照
| 服务器 | 进程数 | 进度 | ETA |
|---|---|---|---|
| bjb1-32546 (Obj s1–9) | 9/9 | 69–83% | 40–85 min |
| bjb2-40593 (Obj s0) | 1/1 | ~74%（bs=1，因 OOM 重启） | ~80–110 min |
| bjb2-28827 (Spa s0–5) | 6/6 | ~66% | ~110 min |
| bjb1-18228 (Spa s6) | 1/1 | **79%** | **~56 min** ⚠️ |

### 🚨 pipeline-auto 风险已确认
`crm-pipeline-auto.log` 每次轮询都报 `bjb1-32546=0 bjb2-40593=0 bjb2-28827=0 local=4 total=4`。远程 ssh+pipe 探测全失效，只靠 local=4（s6 包装进程）撑着。**spatial s6 结束的瞬间（约 02:18 CST / 18:18 UTC），local→0，TOTAL→0，立刻进入 Phase 2 清盘 + Phase 3 rsync + Phase 4 merge**，此时 object 目录是空的、spatial s0–5 还在 66%。

### Merge 状态
- bjb1-18228 `object/` 目录**空的**——0 个 partial、0 个 merged
- `spatial/` 只有本地 s6 的 13 个 partial
- 没有任何 manifest.json / obs_features.pt

### 建议下一步（按优先级）
1. **立刻 kill pipeline-auto（PID 790737）**，precompute 进程不要动。改用 sentinel-file 方案重启 monitor：每个远程 shard 退出时写 `done.s{id}` 文件，监视脚本数 17 个文件再 merge。
2. 退而求其次，干脆改成只 monitor、不自动 merge，全部完成后人工跑 merge。
3. 不动 = 等炸。

报告已注册：`art_20260521_6473b8`。

---
