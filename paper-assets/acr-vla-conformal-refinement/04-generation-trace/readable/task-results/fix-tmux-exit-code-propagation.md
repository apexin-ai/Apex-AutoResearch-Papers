# fix tmux exit code propagation

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_tmux-exit-code-propagation_20260517T145516_result.json`
- **Structured JSON:** [`a5a900466e0aaf4c23ea.json`](../../sessions/a5/a5a900466e0aaf4c23ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 台服务器验证通过。

**部署结果：**

| 服务器 | 脚本 | 目录 | SUCCESS 测试 | FAILED 测试 |
|---|---|---|---|---|
| bjb2-28827 | ✓ | ✓ | ✓ | ✓ |
| bjb1-18228 | ✓ | ✓ | ✓ | ✓ |
| bjb1-32546 | ✓ | ✓ | ✓ | ✓ |
| bjb2-40593 | ✓ | ✓ | ✓ | ✓ |

**使用方式：** 在 tmux send-keys 中把原始命令包装为：
```bash
bash /root/acr-vla-conformal-refinement/scripts/tmux_wrapper.sh &lt;exp_id> "&lt;original_command>"
```

Sentinel 文件写入 `/root/acr-vla-conformal-refinement/logs/sentinels/&lt;exp_id>.sentinel`，内容为 `SUCCESS`/`FAILED` + 时间戳 + EXIT_CODE。

---
