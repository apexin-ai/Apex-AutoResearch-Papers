# check api key location

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_api_key_location_20260515T091327_result.json`
- **Structured JSON:** [`16d6fd4ba0bc2f3c1a93.json`](../../sessions/16/16d6fd4ba0bc2f3c1a93.json)

## Before a recorded user message

1 recorded events

### Log line

_source line 1_

{
  "raw": "结果如下：\n\n**找到位置：`/root/.bashrc`**\n\n`.bashrc` 中有一行 `export OPENROUTER_API_KEY=[REDACTED]"tum_XXB3sZ...\"` —— key 已存在。\n\n**问题原因：**\n\n`teacher_scorer.py:52` 读取逻辑是 `os.environ.get(\"OPENROUTER_API_KEY\", \"\") or os.environ.get(\"DEEPSEEK_API_KEY\", \"\")`。但当前 SSH session 的 `env` 输出中没有 `OPENROUTER_API_KEY`，说明 `.bashrc` 中的 export 在非交互式 SSH 登录时未被 source。\n\n**其他检查结果：**\n- `.env` 文件：不存在\n- `.bash_profile` / `.zshrc`：不存在\n- tmux session：无法通过 read_only 检查（命令被拦截）\n- 当前 shell 环境变量中不含任何 API_KEY\n\n**结论：** key 在 `/root/.bashrc` 里，但非交互式 shell 不会加载 `.bashrc`。启动 v4 时需要在脚本前手动 `source /root/.bashrc`，或者把 export 移到 `/root/.profile` 中。"
}

---
