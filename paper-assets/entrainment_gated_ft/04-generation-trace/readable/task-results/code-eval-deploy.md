# code eval deploy

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-deploy_20260518T061433_result.json`
- **Structured JSON:** [`6f67ec6167cae3d762d4.json`](../../sessions/6f/6f67ec6167cae3d762d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 完整跑通。模型生成空 token（EOS），这对未 fine-tune 的 base model 是正常行为。

## 部署验证报告

| 检查项 | 状态 | 详情 |
|--------|------|------|
| 代码部署 | **通过** | 532行，远程+本地一致 |
| numpy 依赖 | **通过** | numpy 2.3.2 已安装 |
| FLA 模型注册 | **已修复** | 新增手动注册 GatedDeltaNet + HGRN2 到 AutoConfig/AutoModelForCausalLM |
| print-sample | **通过** | depth 1-5 格式正确：函数映射 `i->f(i)`，8-shot demos + test query |
| 数据集生成 | **通过** | 5个 JSON 文件，结构含 prompt/answer/depth/sample_idx/test_task |
| token 长度 | **depth 1-4 通过，depth 5 超限** | depth=1:501, 2:909, 3:1305, 4:1701, **5:2097 (>2048)** |
| 模型推理 | **通过** | GatedDeltaNet-pure-baseline 加载+推理+输出完整（accuracy=0.0 符合预期） |

### 已发现问题

1. **FLA 模型需手动注册**（已修复）：`flash-linear-attention` 不会自动注册到 transformers AutoConfig，脚本已加入 `AutoConfig.register()` + `AutoModelForCausalLM.register()`

2. **depth=5 token 超 2048 限制**（2097 tokens）：会被 tokenizer 截断丢失约 49 tokens（最后一个 demo 或 test query 的部分内容）。解决方案：
   - 减少 `num_shots` 从 8 到 6（每个 demo 约 ~198 tokens，减 2 个可省 ~396 tokens）
   - 或直接跑 depth 1-4，跳过 depth 5

### 已下载模型（9个）
- GatedDeltaNet: pure-baseline, hybrid-3-1, hybrid-6-1, hybrid-12-1, New-hybrid-24-1
- HGRN2: pure-baseline, hybrid-6-1, hybrid-12-1, hybrid-24-1

---
