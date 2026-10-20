# ops submit detach ln evals

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_detach_ln_evals_20260524T074047_result.json`
- **Structured JSON:** [`e708f4060bb2da8bc91f.json`](../../sessions/e7/e708f4060bb2da8bc91f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 eval tmux session 全部运行中。

**提交结果：**

| Eval | GPU | PID | tmux session |
|------|-----|-----|-------------|
| detach_ln_s0_eval | cuda:0 | 585626 | detach_ln_s0_eval |
| detach_ln_s1_eval | cuda:1 | 585894 | detach_ln_s1_eval |
| detach_ln_s2_eval | cuda:2 | 586100 | detach_ln_s2_eval |

日志路径：`~/runs/occsafe_vla/detach_ln_s{0,1,2}_eval.log`

GPU 进程尚在模型加载阶段（nvidia-smi 暂未显示占用），属正常行为，加载完成后会出现显存占用。

---
