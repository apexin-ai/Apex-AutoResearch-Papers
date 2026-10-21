# eval smart compress m96 seed43 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_smart_compress_m96_seed43_v2_20260518T213050_result.json`
- **Structured JSON:** [`005fdb76c18162658cc5.json`](../../sessions/00/005fdb76c18162658cc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 1. eval_smart_compress_libero.py 参数格式

关键参数：`--n_queries`（M 值，required）、`--checkpoint_path`（required）。不需要 `--config`，脚本内部硬编码加载 `configs/smart_compress.yaml` 作为基础配置。

## 2. m96_seed43 v2 eval 启动成功

- tmux session: `eval_smart_compress_m96_seed43_v2`，GPU 2
- 日志确认 `SmartCompressWrapper loaded: M=96, compressor params=22241280`
- checkpoint 完整匹配，无 missing/unexpected keys
- 前 2 个 episode 已 SUCCESS（steps=137, 131），说明模型在正常工作（之前错误的 eval 全部 timeout 280 步）
- 输出写入 `eval_results/eval_smart_compress_m96_seed43_v2.json`

## 3. m32/m64 seed43 eval 命令已保存

文件：`/root/autodl-tmp/importance_margin_vla_compress/pending_eval_commands.txt`

与之前错误命令的关键差异：使用 `eval_smart_compress_libero.py`（加载 SmartCompressWrapper）而非 `eval_success_rate_libero.py --mode baseline`（不加载 compressor），并通过 `--n_queries` 指定正确的 M 值。

---
