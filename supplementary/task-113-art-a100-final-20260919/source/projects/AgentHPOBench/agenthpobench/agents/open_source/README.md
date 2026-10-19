# Compatibility package

The benchmark's model-family-neutral implementation lives in
`agenthpobench.agents.open_weight.LocalTransformersAgent`.

This package only preserves the `QwenAgent` import path used by the initial
public release. New code should import from `agenthpobench.agents.open_weight`.
