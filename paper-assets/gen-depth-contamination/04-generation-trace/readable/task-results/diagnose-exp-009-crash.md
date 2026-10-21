# diagnose exp 009 crash

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_009_crash_20260516T230909_result.json`
- **Structured JSON:** [`cf373e08ae4d7239a0ef.json`](../../sessions/cf/cf373e08ae4d7239a0ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三组实验全部正常启动，已进入训练阶段。

## 汇报

| 项目 | 状态 |
|------|------|
| **exp-009 crash 原因** | `lm_eval.simple_evaluate` 下载 MMLU/HellaSwag 数据集时，HuggingFace Hub 网络不稳定导致 httpx client 关闭 (`RuntimeError: Cannot send a request, as the client has been closed.`) |
| **修复方案** | 1) 脚本顶部添加 `HF_ENDPOINT=https://hf-mirror.com` 使用国内镜像；2) `evaluate_model` 函数添加 3 次重试+指数退避 |
| **重启状态** | 3 组 v2 已启动，训练正在进行：&lt;br>- `exp_009_dose_10pct_v2` (cuda:1, PID 86049, 5555 samples)&lt;br>- `exp_009_dose_30pct_v2` (cuda:2, PID 86196, 7142 samples)&lt;br>- `exp_009_dose_50pct_v2` (cuda:3, PID 86342, 10000 samples) |
| **exp-008 v2** | cuda:0 正常运行中，Generation 0→1 生成阶段 ~44% (278/625)，预计还需 ~20 分钟完成当前 generation |

---
