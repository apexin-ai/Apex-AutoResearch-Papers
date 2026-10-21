# diagnose pi05 adaptive crash and kill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pi05-adaptive-crash-and-kill_20260525T101526_result.json`
- **Structured JSON:** [`90089b2af3ac5ecf131e.json`](../../sessions/90/90089b2af3ac5ecf131e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Critical re-read: the **first 3 tasks ran FINE** (75%, 95%, 75%) before OOM hit. Memory leak accumulates, then OOMs from task 4 onward. The final JSON showing 0/200 for all tasks is a separate bug (likely error-recovery path clobbering per_task dict). 399 OOM lines in the log.

cqa1-32758 already verified clean: all GPUs at 0% utilization, no π0.5/adaptive processes.

---

## 诊断报告

### 根因：**CUDA OOM 内存泄漏**，**不是** CRM 修正破坏 action

**关键证据**（log 头部）：
```
open_the_middle_drawer_of_the_cabinet:     75% (15/20)  ✓
put_the_bowl_on_the_stove:                 95% (19/20)  ✓
put_the_wine_bottle_on_top_of_the_cabinet: 75% (15/20)  ✓
open_the_top_drawer_and_put_the_bowl_inside: 7/10 中途 OOM 开始
... 之后所有 rollout 在 step 0 OOM 失败
```

`grep -c "out of memory" = **399 次**` OOM 报错，全部在 `pi05_wrapper.py:159 torch.flip(img, dims=[2, 3])` 图像预处理阶段。

### 回答四个问题

1. **trigger_rate**：log 中**未输出**（adaptive_conformal_crm 没记录此统计；需要去看 K=10 的 conformal threshold 是否真的在工作，但前 3 个 task 75-95% SR 说明触发逻辑没有破坏 action）
2. **mean_l2 / uncertainty**：log 中**未输出**任何 mean_l2/uncertainty/correction_norm 行
3. **运行命令**（完整参数）：
   ```
   python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm \
     --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt \
     --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 \
     --benchmark goal --seed 42 --n_rollouts 20 --max_correction_norm 0.2
   ```
   args 中 `K=10`, `n_action_steps=10`, `max_steps=300`（goal benchmark）
4. **根因判断**：
   - ❌ τ=0.25 太低：**否**。前 3 task 75-95% SR 与 VLA-only (98%) 相近，说明 conformal+CRM 没系统性破坏 action
   - ❌ CRM checkpoint 错误：**否**。能跑出 75-95% 不可能加载错
   - ❌ obs_dim 配置错误：**否**。CRM 前 60 个 rollout 正常工作
   - ✅ **CUDA OOM 内存泄漏 + JSON 序列化 bug**：K=10 samples × 300 max_steps 累积显存未释放，从 task 4 中段开始 OOM。最终写出的 JSON 把所有 task 标 0/20（per_task dict 在 exception 路径被清零或覆写），掩盖了真实结果

### Kill 确认

| 服务器 | PID | 任务 | 状态 |
|---|---|---|---|
| bjb2-28827 | 732023 | goal s43 | ✅ killed (force) |
| bjb2-28827 | 732469 | object s42 | ✅ killed (force) |
| bjb2-28827 | 733346 | object s43 | ✅ killed (force) |
| bjb1-18228 | 484291 | spatial s42 r2 | ✅ killed (force) |
| cqa1-32758 | — | 无 π0.5/adaptive 进程 | ✅ 干净 |

### 修复方向（不修，仅建议）
1. evaluate.py 在每个 rollout 后 `torch.cuda.empty_cache()` + `gc.collect()`
2. K 从 10 降到 2-5 减少显存占用
3. 修 JSON 写入逻辑：保留中途 task 的累积统计，OOM 时不要清零
4. 重跑前需确认 GPU 剩余显存 ≥ 模型本身 + K × forward pass 内存

---
