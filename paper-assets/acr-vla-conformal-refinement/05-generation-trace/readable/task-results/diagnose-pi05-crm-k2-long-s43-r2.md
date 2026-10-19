# diagnose pi05 crm k2 long s43 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pi05-crm-k2-long-s43-r2_20260526T125148_result.json`
- **Structured JSON:** [`ac3bbdd0f870232dd4ba.json`](../../sessions/ac/ac3bbdd0f870232dd4ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 根因：误报（False Positive）— 实验实际已成功完成

实验 `pi05-crm-k2-long-s43-r2` **并未失败**，而是被监控系统误判为失败。

**原因**：监控系统在 `/root/autodl-tmp/acr-vla-conformal-refinement/` 下查找 sentinel/日志文件，但项目实际路径是 `/root/acr-vla-conformal-refinement/`。连续 5 次检测不到 sentinel/W&B 信号后自动标记为 failed。

### 实验结果

- **状态**：10 个任务 × 20 rollouts = 200 rollouts 全部完成
- **Overall success rate**：**76.0%** (152/200)
- **结果文件**：`/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed43_pi05_K2.json`（写入时间 May 26 20:22）
- **日志文件**：同目录下 `.log` 文件，末尾显示正常结束

### Per-task 成绩

| Task | Success Rate |
|------|-------------|
| cream_cheese_box_and_butter | 95% |
| stove_and_moka_pot | 95% |
| white_mug_left_yellow_right | 95% |
| yellow_white_mug_microwave | 90% |
| alphabet_soup_tomato_sauce | 75% |
| black_bowl_cabinet | 75% |
| book_in_caddy | 75% |
| alphabet_soup_cream_cheese | 75% |
| white_mug_chocolate_pudding | 60% |
| both_moka_pots_stove | 25% |

### GPU 状态

- **cuda:1 空闲**（1MiB / 24564MiB, 0% util）
- cuda:0, cuda:3 也空闲
- cuda:2 有进程占用（11238MiB）

### 结论

无需重跑。结果已完整写入 JSON 文件，可直接使用。监控系统的路径配置需要修正（`/root/autodl-tmp/` → `/root/`）。

---
