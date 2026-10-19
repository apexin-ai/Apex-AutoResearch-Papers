# Model Download Fix Report — 2026-05-21 10:48 UTC

## Llama4 (RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized.w4a16)

- **旧进程 PID 51303**: 已 kill（下载到错误路径 `Llama-4-Scout-W4A16`）
- **错误目录 `Llama-4-Scout-W4A16`**: 已删除
- **正确目录 `Llama4-Scout-W4A16`**: 已有 7/14 shards, 43GB
- **新进程 PID 53308**: 已启动，续传模式，`HF_HUB_DISABLE_XET=1` + `HF_ENDPOINT=hf-mirror.com`
- 日志: `/tmp/download_llama4.log`

## Qwen3 (Qwen/Qwen3-235B-A22B-GPTQ-Int4)

- **旧进程 PID 51304**: 已 kill（xet 超时错误，反复 `The read operation timed out`，无进展）
- **目录 `Qwen3-235B-GPTQ-Int4`**: 已有 5.4GB
- **新进程 PID 53359**: 已启动，续传模式，`HF_HUB_DISABLE_XET=1` + `HF_ENDPOINT=hf-mirror.com`
- 日志: `/tmp/download_qwen3.log`

## 磁盘空间

| 路径 | 大小 | 总容量 | 可用 | 使用率 |
|------|------|--------|------|--------|
| `/root/autodl-tmp/` | — | 350G | 215G | 39% |
| `Llama4-Scout-W4A16/` | 43G | — | — | — |
| `Qwen3-235B-GPTQ-Int4/` | 5.4G | — | — | — |

预计总需 ~103G (Llama4 ~43G + Qwen3 ~60G)，磁盘剩余 215G，空间充足。

## 根因

两个下载都受 xet (xethub) 超时影响。Llama4 还有路径错误（连字符 vs 无连字符）。修复：`HF_HUB_DISABLE_XET=1` 禁用 xet 协议，走标准 HTTP。
