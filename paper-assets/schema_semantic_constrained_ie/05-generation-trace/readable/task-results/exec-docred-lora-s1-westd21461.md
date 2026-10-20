# exec docred lora s1 westd21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_docred-lora-s1-westd21461_20260522T052720_result.json`
- **Structured JSON:** [`e196b03b8ef3bd5df354.json`](../../sessions/e1/e196b03b8ef3bd5df354.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

推理已成功启动。总结：

**Checkpoint 传输**: westd-21461 通过 SSH 直接从 westd-16980 拉取，2秒完成（内网直连）。传输了 adapter_model.safetensors (251MB)、adapter_config.json、tokenizer 文件。

**启动过程遇到的问题及修复**:
1. `--lora_path` 参数不存在 → 改用 monkey-patch `AutoModelForCausalLM.from_pretrained` 注入 LoRA 加载
2. `compiler` 模块找不到 → 添加 sys.path 和 os.chdir
3. `AwqGEMMQuantLinear` 导入失败 → 给 gptqmodel 添加别名
4. AWQ 模型不支持 `merge_and_unload()` → 改为不合并，直接用 PeftModel 推理

**运行状态**:
- PID: 11466
- GPU: cuda:0, 86-90% 利用率, 39.6GB/97.9GB 显存
- 输出: `/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_200_s1_constrained.jsonl`（已写入 1 条，第 2 条生成中）
- 日志: `/tmp/constrained_inference.log`

**注意**: PEFT 报 `Unsupported layer type AwqMarlinLinear` warning — LoRA adapter 可能未实际应用到 AWQ 量化层。如果最终结果与 base model 无显著差异，需要确认 LoRA 是否生效。

---
