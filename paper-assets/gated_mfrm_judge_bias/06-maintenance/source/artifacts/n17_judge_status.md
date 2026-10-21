# N=17 Judge 评测进度报告

**检查时间**: 2026-05-23 ~21:45 UTC (服务器时间 May 24 05:45 +0800)

## 概要

评测**正在进行中**。9 个 judge 中有 8 个正在活跃写入数据，1 个（llama-shard2）已停止。3 个 vLLM 本地推理服务器正常运行。

## 配置

- **目标模型**: 18 个（原 9 个 + 新增 9 个）
- **问题数**: 500 (Arena Hard)
- **Position swap**: 开启（每对 x2）
- **每 judge 目标行数**: 18,000

### 9 个新增目标模型
claude-3-5-sonnet-20241022, gpt-4-turbo-2024-04-09, llama-3.1-70b-instruct, gemma-2-27b-it, claude-3-opus-20240229, llama-3-70b-instruct, mixtral-8x22b-instruct-v0.1, claude-3-haiku-20240307, llama-3-8b-instruct

## 各 Judge 完成度

| Judge | 类型 | 已完成行数 | /18,000 | 完成率 | 状态 |
|-------|------|-----------|---------|--------|------|
| claude-sonnet-4.6-proxy | API | 11,829 | 18,000 | 65.7% | 活跃运行 |
| qwen2.5-72b | Local | 9,953 | 18,000 | 55.3% | 活跃运行 |
| mistral-large-2 | Local | 9,441 | 18,000 | 52.5% | 活跃运行 |
| claude-opus-4.7-proxy | API | 9,431 | 18,000 | 52.4% | 活跃运行 |
| gpt-5.5-proxy | API | 8,758 | 18,000 | 48.7% | 活跃运行 |
| qwen3-235b-proxy | API | 8,667 | 18,000 | 48.2% | 活跃运行 |
| gemini-2.5-pro-proxy | API | 8,115 | 18,000 | 45.1% | 活跃运行 |
| llama-3.3-70b | Local | 7,172 | 18,000 | 39.8% | 活跃运行 |
| deepseek-v4-pro-proxy | API | 7,166 | 18,000 | 39.8% | 活跃运行 |
| llama-3.3-70b-shard2 | Local | 5,943 | 18,000 | 33.0% | 已停止（16h前） |

**总体完成率**: ~50%

## 运行中的进程

### vLLM 推理服务器（3 个，均正常）
- **llama-3.3-70b** (pid ~662563): 10 并发请求, KV cache 6-7%, ~24 tokens/s generation, prefix cache 40%
- **mistral-large-2** (pid ~664095): 10 并发请求, KV cache 63-71%, ~13 tokens/s generation, prefix cache 14%
- **qwen2.5-72b**: 运行中（结果文件持续写入）

### collect.py 评测进程
所有活跃 judge 的 collect.py 进程正在运行（结果文件最后修改时间 05:41-05:42 May 24 +0800）。

## 已知问题

### 1. Mistral 上下文长度错误
`n17_mistral_restart.log` 显示大量 4096 token 上下文长度错误：
```
Error code: 400 - This model's maximum context length is 4096 tokens.
However, you requested 1024 output tokens and your prompt contains at
least 3073 input tokens.
```
vLLM 服务器已用 fixed 配置重启（KV cache 71% 说明支持更长上下文），但 restart 运行中（进度 [110/9052]）的大量 items 因此错误被跳过。这些 items 后续需要重新收集。

### 2. llama-3.3-70b-shard2 已停止
最后修改时间 May 23 13:48 +0800，已停止约 16 小时。5,943 行数据。不清楚是独立分片还是已废弃的旧运行。

### 3. API 速度较慢
API judges 处理速度约 0.1 items/s。

## ETA 预估

| 场景 | 预计完成时间 |
|------|-------------|
| 最快 judge (sonnet) | ~17 小时后 (May 24 ~15:00 UTC) |
| 最慢 judge (deepseek) | ~30 小时后 (May 25 ~04:00 UTC) |
| 全部 judge 完成 | 约 24-36 小时 |

## 判断

**评测未完成，但正在正常推进。** 无需立即干预。

需要后续关注：
1. **Mistral 失败 items 需重跑**: restart 运行中因 4096 限制失败的 items 需在 fixed 服务器上重新收集
2. **llama-shard2 需确认**: 是否需要继续或合并到主 llama 结果
3. **API judge 持续跑即可**: resume-safe 机制保证中断后可续跑
