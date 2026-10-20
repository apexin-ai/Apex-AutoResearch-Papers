# code prepare eval grpo

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-eval-grpo_20260514T124018_result.json`
- **Structured JSON:** [`64c97d0aff182955e7e6.json`](../../sessions/64/64c97d0aff182955e7e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息已齐全，结论如下：

---

## 分析结果

**evaluate.py `--mode` 参数**：支持 `base`、`sft`、`grpo` 三个值。代码逻辑上 `sft` 和 `grpo` 完全相同——都走 `else` 分支加载 checkpoint，自动检测 LoRA adapter（检查 `adapter_config.json` 是否存在）。

**GRPO checkpoint 格式**：与 SFT 一致，是 LoRA adapter（`grpo/` 的先例：`adapter_config.json` + `adapter_model.safetensors` + tokenizer 文件）。GRPO v2 最终保存路径为 `checkpoints/grpo_v2/`，当前为空（训练中）。

**evaluate.py 不需要修改**，`--mode grpo` 已原生支持。

---

## 确认的 eval 命令

```bash
cd /root/autodl-tmp/diagprobe && python src/evaluate.py \
  --mode grpo \
  --model-name /root/autodl-tmp/models/Qwen/Qwen3-8B \
  --checkpoint-path /root/autodl-tmp/diagprobe/checkpoints/grpo_v2 \
  --data-path data/eval.jsonl \
  --output-path results/eval_grpo_v2.json \
  --gpu 1 \
  --bf16
```

## 要点

| 项目 | 说明 |
|------|------|
| checkpoint 路径 | `checkpoints/grpo_v2/`（训练完成后会出现 `adapter_config.json` + `adapter_model.safetensors`） |
| checkpoint 格式 | LoRA adapter，base model = `Qwen3-8B`，r=16, alpha=32 |
| eval 脚本修改 | 不需要 |
| 预计耗时 | 202 样本，每样本需推理+沙箱执行，估计 30-60 分钟（参考 sft eval） |
| sentinel 文件 | eval 脚本本身不输出 `.done`。如需 cron 监控，跑完后手动 `touch results/.eval_grpo_v2.done` 即可 |
| 训练完成判断 | `checkpoints/grpo_v2/adapter_config.json` 存在即表示最终模型已保存 |

---
