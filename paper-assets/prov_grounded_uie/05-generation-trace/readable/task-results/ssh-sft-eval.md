# ssh sft eval

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_sft-eval_20260512T150055_result.json`
- **Structured JSON:** [`1cda21d53ff6061b63c9.json`](../../sessions/1c/1cda21d53ff6061b63c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估仍在全力运行中（GPU0 100%、34GB 显存）。24B 模型对 985 条样本逐条推理需要较长时间——预计总共约 60-120 分钟。

**当前状态总结：**
- PID 17835 后台运行中
- GPU0 利用率 100%，显存 34198 MiB
- 日志因 Python stdout 缓冲（nohup 导致）暂无进度输出
- 结果文件 `eval_results.json` 尚未生成（脚本结束才写入）

评估正在正常推理中。你可以稍后用以下命令检查结果：
```bash
# 检查是否完成
ls -la /root/autodl-tmp/prov_grounded_uie/outputs/sft/eval_results.json

# 查看日志
tail -20 /tmp/sft_eval.log

# 查看结果
cat /root/autodl-tmp/prov_grounded_uie/outputs/sft/eval_results.json | python3 -m json.tool | head -20
```

需要我继续轮询等待结果，还是稍后手动检查？

---
