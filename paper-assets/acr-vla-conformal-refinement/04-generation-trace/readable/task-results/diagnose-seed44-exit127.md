# diagnose seed44 exit127

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_seed44-exit127_20260516T013243_result.json`
- **Structured JSON:** [`3ba3458e61d6c98c94ba.json`](../../sessions/3b/3ba3458e61d6c98c94ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是结果：

## 失败根因

三个日志内容完全一致：`bash: line 1: python: command not found`，EXIT_CODE=127。

**直接原因**：seed44 的提交命令使用了 `bash -c "cd ... && python -u ..."` 格式，而 `bash -c` 启动的是非交互 shell，不会 source `.bashrc`，因此 conda 未激活，`/root/miniconda3/bin/python` 不在 PATH 上。

**对比成功实验**：seed43 (eval-perdof-object-seed43) 的命令是直接传递 `python -u src/evaluate.py ...`，没有 `bash -c` 包装。`submit_training_job` 的 tmux backend 在创建 session 时会加载 shell profile，所以 conda 被正确激活。一旦外面套了 `bash -c`，就绕过了 tmux 的 shell 初始化。

## 三个实验的实际部署

| 实验 | 服务器 | GPU | 日志已确认 |
|------|--------|-----|-----------|
| eval-vla-only-object-seed44 | bjb2-40593 | cuda:0 | ✅ 同样错误 |
| eval-argmin-object-seed44 | **bjb1-18228** | cuda:3 | ✅ 同样错误 |
| eval-obs-only-object-norm02-seed44 | **bjb1-18228** | cuda:2 | ✅ 同样错误 |

注意：任务描述说三个都在 bjb2-40593，实际上只有 vla-only 在 bjb2，另外两个在 bjb1-18228。

## 服务器环境状态

两台服务器环境一致：
- **conda**：`/root/miniconda3/bin/python` → python3.12（正常）
- **PATH**（SSH session）：`/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:...`（不含 miniconda3）
- **.bashrc**：有 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（但非交互 shell 不加载）

## 修复建议

**方案 A（推荐）**：去掉 `bash -c` 包装，使用与 seed43 相同的直接命令格式：
```
python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_object_vla_only_seed44.json
```

**方案 B**：如果必须用 `bash -c`，在命令前加 conda 激活：
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py ..."
```

**系统层面**：`submit_training_job` 的 tmux backend 应该在检测到 `bash -c` 包装时自动注入 conda 激活，或者在文档中明确禁止 `bash -c` 包装格式。

---
