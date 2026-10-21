# diagnose eval stage1only k09

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_stage1only_k09_20260517T091047_result.json`
- **Structured JSON:** [`e88947234556871f7920.json`](../../sessions/e8/e88947234556871f7920.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 根因：监控系统误报（false positive），两个实验实际上都正常完成了

两个实验都跑完了全部 10 tasks × 50 episodes = 500 episodes，正常退出并写入了结果文件。Cron 监控报 "process dead 5× with no sentinel/W&B" 是因为 eval 脚本没有写 sentinel 文件或接入 W&B，进程正常退出后被监控系统误判为失败。

### 实验结果

| 实验 | 模式 | 结果 | 输出文件 |
|------|------|------|----------|
| eval_stage1only_k09 | acis_prune | **0/500 (0.0%)** | `eval_results/eval_stage1only_k09_object.json` ✅ |
| eval_random_prune_k05 | random_prune | **0/500 (0.0%)** | `eval_results/eval_random_prune_k05_object.json` ✅ |

所有 episode 都跑满 280 步后 FAIL，没有任何 task 有成功案例。

### 其他发现

- 没有 OOM、没有 traceback、没有 GPU 冲突报错
- Config 文件 `configs/libero_acis_stage1only_k09.yaml` 存在
- 日志末尾显示完成后立即有新一轮 eval 启动（"Reducing the number of VLM layers to 16..."），说明后续实验也在排队运行
- 日志写入位置不一致：stage1only_k09 的 log 在 `logs/` 目录，random_prune_k05 的 log 在 `eval_results/` 目录

### 真正需要关注的问题

实验没有 crash，但 **0% 成功率** 本身是实验层面的问题。Stage1-only checkpoint 配合 acis_prune (k=0.9) 和 random_prune (k=0.5) 两种剪枝模式都完全失效，说明这个 checkpoint 在剪枝后丧失了全部能力。可能需要检查：
1. `stage1_done/checkpoint.pt` 本身在不剪枝时的基线表现
2. k=0.9 / k=0.5 的剪枝比例是否过于激进
3. 剪枝 connector 是否正确加载和应用

---
