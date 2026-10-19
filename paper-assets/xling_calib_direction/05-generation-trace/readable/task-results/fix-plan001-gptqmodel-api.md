# fix plan001 gptqmodel api

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_plan001_gptqmodel_api_20260521T142431_result.json`
- **Structured JSON:** [`3d3cc54fc83cc6e68385.json`](../../sessions/3d/3d3cc54fc83cc6e68385.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**gptqmodel 版本**: 7.0.0

**代码修改 (4 处)**:
1. `parse_args()`: `--quantization` 增加 `"gptq"` 选项
2. `load_model()`: 新增 GPTQ 分支 — `GPTQModel.from_quantized()` 原生 API，在 multimodal 检测之前短路返回，不影响 Llama4 逻辑
3. `get_layer_modules()`: 新增 `model.model.model.layers` 路径（GPTQModel 多包一层 wrapper）
4. `get_final_norm()`: 新增 `model.model.model.norm` 路径

**Dry run 结果**: 成功
- MarlinLinear kernel，4 卡分布加载，94 层
- 5 样本 en，~2.2s/样本，model_acc=1.000
- GPU 峰值占用: ~31GB/卡（总 ~123GB），运行后已清零
- 输出文件: layer0_en.pt (82K), layer93_en.pt (82K)

**Git commit**: `3a0524e` on master

---
