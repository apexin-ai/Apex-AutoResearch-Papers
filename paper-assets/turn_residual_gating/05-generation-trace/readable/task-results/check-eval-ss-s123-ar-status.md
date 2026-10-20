# check eval ss s123 ar status

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval_ss_s123_ar_status_20260523T174705_result.json`
- **Structured JSON:** [`d43101d1530f3c117a07.json`](../../sessions/d4/d43101d1530f3c117a07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### AR eval PID 110052: **运行中**（已跑 ~20 分钟）
- 命令：`eval_attention_steering.py --checkpoint runs/d048_ss_s123/epoch_2 --beta 0 3 5 --max-convs 50`
- 输出文件 `ss_s123_ar_n50.json` 尚未生成
- AR eval 完成后还需跑 `base_ar_n50`（Step AR 2/2），然后是 Bootstrap CI

### GPU 状态
- 利用率 49%，显存 30.4 / 97.9 GiB（A100 80G）
- 仅 PID 110052 在使用 GPU

### GPU chain 进度：**Step 1/7**（SS s123 eval）
- Phase 1 TF eval（4 个子任务）：**已完成** ✓
- Phase 2 AR eval（AR 1/2 SS s123）：**运行中**
- 后续 AR 2/2 + Bootstrap CI 待跑
- Step 2/7（SS s456 resume training）**未启动**

### 已完成的 TF 结果

| 配置 | GAR-variant | turn1_avg_gar | avg_ppl |
|------|-------------|---------------|---------|
| Base | ours | 0.1008 | 3.9586 |
| Base | dongre | 0.0075 | 3.9586 |
| SS s123 | ours | 0.5536 | 2.6123 |
| SS s123 | dongre | 0.4106 | 2.6123 |

SS s123 在 TF eval 下 GAR-ours 从 0.1008→0.5536（+0.453），PPL 从 3.96→2.61，效果显著。AR eval 结果需等 PID 110052 完成后查看。

---
