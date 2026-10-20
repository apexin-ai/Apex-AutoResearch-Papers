# diagnose exp 001 sft injection

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_sft_injection_20260513T191935_result.json`
- **Structured JSON:** [`dc61cf5c910470a14e8d.json`](../../sessions/dc/dc61cf5c910470a14e8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是完整分析：

---

## 诊断过程与发现

**各进程实际状态（与 cron 报告不符）：**

| Benchmark | 原 PID | 状态 | 说明 |
|-----------|--------|------|------|
| MMLU | 200967 | **已死** | vLLM 初始化失败 → transformers fallback 极慢 → 在 9% 处被 kill |
| GSM8K | 189375 | **仍在运行** | transformers 后端，已跑 30 分钟 |
| ARC | 190717 | **仍在运行** | transformers 后端，已跑 29 分钟 |
| HumanEval | 201102 | **已完成** | 产出文件存在 (489K, 2953 行) |

Cron 报告"process dead 5×"不准确——实际只有 MMLU 失败，HumanEval 正常完成，GSM8K/ARC 仍在跑。

**MMLU 失败链路：**
1. vLLM 初始化抛 pydantic 校验错误：`1 validation error for VllmConfig: Assertion failed, duplicate template name`
2. 代码 fallback 到 transformers 后端，速度从 ~8s/batch 降至 ~55s/batch（ETA 6+ 小时）
3. 在 batch 40/439 (9%) 处日志无 traceback 直接截断——被外部 kill（cron 监控或手动）

**MMLU v2 重试已在运行：** `phase1_paraphrase_v2.log` 显示 vLLM v0.20.2 成功初始化（EngineCore PID 204758），当前在 GPU 0 上以 ~8s/batch 速度生成中，进度 3%。

**根因分析：** vLLM 的 `duplicate template name` 错误是 Qwen2.5 模型 tokenizer_config.json 中的 chat template 与 vLLM 0.20.x 版本的 pydantic 校验冲突。HumanEval 的 vLLM 成功启动而 MMLU 失败，推测是两个 vLLM 进程同时启动时的竞争条件（vLLM 全局注册 template 时冲突）。v2 重试时 HumanEval 已完成释放资源，vLLM 单实例启动无冲突。

**资源状态：** GPU 0/1/2 活跃，GPU 3/4/5 空闲。磁盘 51%，空间充足。

---

```json
{"root_cause":"vLLM init failed: '1 validation error for VllmConfig: Assertion failed, duplicate template name [type=assertion_error]' — race condition when two vLLM instances initialize simultaneously, causing duplicate chat template registration in pydantic validator","error_type":"infrastructure","fix_steps":["1. 当前状态已部分恢复：MMLU v2 重试在跑(vLLM)，GSM8K/ARC 在跑(transformers)，HumanEval 已完成","2. 等待当前 3 个进程完成（MMLU v2 ETA ~1h, GSM8K/ARC ETA 取决于数据量）","3. 未来运行时错开 vLLM 进程启动时间（间隔 30s），避免 template 注册竞争","4. 或将所有 benchmark 改为串行使用同一 vLLM 实例（--tensor-parallel 多卡），避免多实例冲突","5. 固定 vLLM 版本并在 paraphrase_gen.py 的 fallback 逻辑中加重试（retry 1次 vLLM init 再 fallback）"],"can_auto_fix":false,"partial_output":"humaneval_paraphrases.json (489K, 2953行) 已完成; MMLU v2 重试中(3%); GSM8K/ARC transformers 生成中(~30min elapsed)"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "vLLM init failed: '1 validation error for VllmConfig: Assertion failed, duplicate template name [type=assertion_error]' — race condition when two vLLM instances initialize simultaneously, causing duplicate chat template registration in pydantic validator",
    "error_type": "infrastructure",
    "fix_steps": [
      "1. 当前状态已部分恢复：MMLU v2 重试在跑(vLLM)，GSM8K/ARC 在跑(transformers)，HumanEval 已完成",
      "2. 等待当前 3 个进程完成（MMLU v2 ETA ~1h, GSM8K/ARC ETA 取决于数据量）",
      "3. 未来运行时错开 vLLM 进程启动时间（间隔 30s），避免 template 注册竞争",
      "4. 或将所有 benchmark 改为串行使用同一 vLLM 实例（--tensor-parallel 多卡），避免多实例冲突",
      "5. 固定 vLLM 版本并在 paraphrase_gen.py 的 fallback 逻辑中加重试（retry 1次 vLLM init 再 fallback）"
    ],
    "can_auto_fix": false,
    "partial_output": "humaneval_paraphrases.json (489K, 2953行) 已完成; MMLU v2 重试中(3%); GSM8K/ARC transformers 生成中(~30min elapsed)"
  }
}
```

</details>

---
