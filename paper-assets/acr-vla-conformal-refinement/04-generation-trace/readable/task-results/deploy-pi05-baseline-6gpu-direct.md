# deploy pi05 baseline 6gpu direct

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_pi05-baseline-6gpu-direct_20260521T080717_result.json`
- **Structured JSON:** [`466dce02a2d09e46758b.json`](../../sessions/46/466dce02a2d09e46758b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 6 个进程存活，GPU 全部占用，正在进行首轮 rollout（首次推理较慢）。部署完成。

---

**部署汇报**

| # | exp_id | GPU | PID | Benchmark | Seed | 状态 |
|---|--------|-----|-----|-----------|------|------|
| 1 | `eval-pi05-vla-only-object-seed42` | cuda:0 | 943180 | Object | 42 | RUNNING |
| 2 | `eval-pi05-vla-only-object-seed43` | cuda:1 | 943547 | Object | 43 | RUNNING |
| 3 | `eval-pi05-vla-only-object-seed44` | cuda:2 | 943899 | Object | 44 | RUNNING |
| 4 | `eval-pi05-vla-only-spatial-seed42` | cuda:3 | 944264 | Spatial | 42 | RUNNING |
| 5 | `eval-pi05-vla-only-spatial-seed43` | cuda:4 | 945459 | Spatial | 43 | RUNNING |
| 6 | `eval-pi05-vla-only-spatial-seed44` | cuda:5 | 946612 | Spatial | 44 | RUNNING |

**额外工作：**
- 模型下载：从 HuggingFace 下载 `lerobot/pi05_libero_finetuned`（7GB）到 bjb1
- Tokenizer 下载：`unsloth/gemma-2b` tokenizer 到 `/root/autodl-tmp/models/gemma-2b-tokenizer/`
- Bug 修复：前 4 个实验因 `torch._inductor` 的 `duplicate template name` 断言错误崩溃，添加 `TORCHDYNAMO_DISABLE=1` 后成功启动
- 代码同步：bjb1 上 `pi05_wrapper.py` 已有 `torch.flip` 修复，无需同步
- Registry：6 个实验全部注册为 RUNNING

---
