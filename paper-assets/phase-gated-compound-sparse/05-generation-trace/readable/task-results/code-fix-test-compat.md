# code fix test compat

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-test-compat_20260513T210249_result.json`
- **Structured JSON:** [`8172862e906c8571d7fa.json`](../../sessions/81/8172862e906c8571d7fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。改动摘要：

**改之前**（3 处 `type()` 动态类创建）：
```python
self.layers = torch.nn.ModuleList([
    type("L", (torch.nn.Module,), {
        "__init__": lambda s: (super(type(s), s).__init__(),
                              setattr(s, "self_attn", MockAttention())),
        "forward": lambda s, h, **kw: (s.self_attn(h)[0],),
    })() for _ in range(1)
])
self.config = type("C", (), {...})()
out = type("O", (), {"logits": self.lm_head(h)})()
```

**改之后**（标准类定义，与 `test_compound_forward` 风格一致）：
```python
class MockLayer(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.self_attn = MockAttention()
    def forward(self, h, **kw):
        return (self.self_attn(h)[0],)

class MockConfig:
    num_hidden_layers = 1
    num_attention_heads = 28
    num_key_value_heads = 4

# MockModel 中：
self.layers = torch.nn.ModuleList([MockLayer() for _ in range(1)])
self.config = MockConfig()

# forward 中：
class Output:
    pass
out = Output()
out.logits = self.lm_head(h)
```

其余 6 个测试函数未改动，`__main__` 入口不变。

---
