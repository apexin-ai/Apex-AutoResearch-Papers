# eval cls8b s42 ckpt1000 test mutation home

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls8b-s42-ckpt1000-test-mutation-home_20260515T220616_result.json`
- **Structured JSON:** [`bce0bc6491c00cabf9b0.json`](../../sessions/bc/bce0bc6491c00cabf9b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**home-1x5090 不可达。** DNS 解析正常（`implicit5638.xyfu.me` → `73.241.206.183`），但 SSH 端口 22 无响应。服务器可能关机或端口转发未配置。

已确认的信息：
- **westd 上 ckpt-1000 位置**: `/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1000/`（176MB，LoRA adapter）
- **文件内容**: adapter_config.json, adapter_model.safetensors (61MB), optimizer.pt (123MB), trainer_state.json 等

需要你检查：
1. home 服务器是否已开机
2. 路由器是否正确转发 22 端口到该机器
3. 如果端口/IP 有变化，更新 resources.yaml 中的 host/port

服务器恢复后我可以继续执行 eval 任务。或者，如果你想改在 westd 上运行这个 eval，也可以——westd 上已有 ckpt 和模型。

---
