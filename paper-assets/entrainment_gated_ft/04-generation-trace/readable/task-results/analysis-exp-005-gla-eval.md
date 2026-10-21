# analysis exp 005 gla eval

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-005-gla-eval_20260522T154011_result.json`
- **Structured JSON:** [`3e42ff4612bcee8495dd.json`](../../sessions/3e/3e42ff4612bcee8495dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果如下：

```
GLA hybrid-3-1 (340M) eval 结果:
- 评估状态: ❌ 失败
- 失败原因: gla_eval.log 中 pretrained='' (空字符串)，模型路径未传入 lm_eval
- lambada_openai: 无结果
- arc_easy: 无结果
- per-example log_samples: 不存在（无结果目录 GLA_hybrid-3-1/）
- 模型路径: /root/entrainment_gated_ft/models/340M-20B-GLA-hybrid-3-1/
- 模型文件: ✅ 存在（model.safetensors + config.json 等完整）
```

**问题分析：**

1. `gla_eval.log` 不是由 `run_eval_p1.sh` 产生的——该脚本输出到 `eval_p1.log`，但 `eval_p1.log` 不存在，说明该脚本从未执行。

2. `gla_eval.log` 由某个单独的命令产生，该命令传了空的 `pretrained=''`，导致 HuggingFace 报 `HFValidationError: Repo id must use alphanumeric chars`。

3. `priority1_v4.log` 也失败了——卡在下载 DeltaNet 模型时网络断开（下载了 97MB/1.3GB 后连接被对端关闭）。

4. **模型本身没问题**，`340M-20B-GLA-hybrid-3-1/` 目录下 safetensors、config 等文件齐全，可以直接评估。

**需要重新运行评估。** 正确的命令应该是运行 `run_eval_p1.sh`（它的路径拼接逻辑是对的），或者手动执行：

```bash
python -m lm_eval --model hf \
  --model_args pretrained=/root/entrainment_gated_ft/models/340M-20B-GLA-hybrid-3-1,trust_remote_code=True \
  --tasks lambada_openai,arc_easy --device cuda:0 --batch_size auto --log_samples \
  --output_path /root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_hybrid-3-1/
```

要我现在重新运行 GLA 评估吗？

---
