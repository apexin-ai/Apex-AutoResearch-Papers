# Smoke tests for compound sparsity modules.
# Validates interfaces, GQA mapping, mask construction, and compound forward
# using mock models — no real 7B model needed.

import torch

from pacs.compound.head_selector import HeadSelector, HeadMask, group_heads_by_kv
from pacs.compound.kv_evictor import KVEvictor, KVMask


def test_gqa_grouping():
    groups = group_heads_by_kv(28, 4)
    assert len(groups) == 4
    assert groups[0] == [0, 1, 2, 3, 4, 5, 6]
    assert groups[3] == [21, 22, 23, 24, 25, 26, 27]
    all_q = []
    for qs in groups.values():
        all_q.extend(qs)
    assert sorted(all_q) == list(range(28))
    print("test_gqa_grouping PASSED")


def test_head_selection():
    selector = HeadSelector(num_q_heads=28, num_kv_heads=4)
    # Importance monotonically increases with index
    importance = torch.arange(28, dtype=torch.float)
    mask = selector.select(importance, keep_ratio=0.5)  # keep 14

    assert isinstance(mask, HeadMask)
    assert len(mask.active_q_heads) == 14
    assert mask.q_head_mask.sum().item() == 14
    # Top-14 (indices 14-27) should be kept
    assert 27 in mask.active_q_heads
    assert 26 in mask.active_q_heads
    assert 0 not in mask.active_q_heads
    # KV group 0 (Q 0-6) — all masked → KV head 0 skippable
    assert 0 not in mask.active_kv_heads
    # KV group 1 (Q 7-13) — all masked → KV head 1 skippable
    assert 1 not in mask.active_kv_heads
    # KV groups 2,3 (Q 14-27) — active
    assert 2 in mask.active_kv_heads
    assert 3 in mask.active_kv_heads
    print("test_head_selection PASSED")


def test_kv_eviction():
    evictor = KVEvictor(protect_positions=[0])
    attn = torch.rand(1, 4, 16, 16)
    importance = evictor.compute_kv_importance(attn)
    assert importance.shape == (16,)

    mask = evictor.select(importance, keep_ratio=0.5)
    assert isinstance(mask, KVMask)
    assert mask.position_mask.shape == (16,)
    assert mask.position_mask[0].item() is True  # BOS protected
    assert mask.active_positions.numel() == 8
    assert abs(mask.keep_ratio_actual - 0.5) < 1e-6
    print("test_kv_eviction PASSED")


def test_kv_bos_protection():
    """BOS should survive even with zero importance."""
    evictor = KVEvictor(protect_positions=[0])
    importance = torch.zeros(32)
    importance[1:] = torch.rand(31)

    mask = evictor.select(importance, keep_ratio=0.1)
    assert mask.position_mask[0].item() is True
    print("test_kv_bos_protection PASSED")


def test_head_mask_kv_group_skip():
    """When all Q heads in a KV group are masked, that KV head is skippable."""
    selector = HeadSelector(num_q_heads=28, num_kv_heads=4)
    # Only KV group 3 (Q 21-27) has nonzero importance
    importance = torch.zeros(28)
    importance[21:28] = torch.arange(1, 8, dtype=torch.float)

    mask = selector.select(importance, keep_ratio=0.25)  # keep 7
    assert set(mask.active_q_heads) == set(range(21, 28))
    assert mask.active_kv_heads == [3]
    assert mask.kv_head_mask[3].item() is True
    for i in range(3):
        assert mask.kv_head_mask[i].item() is False
    print("test_head_mask_kv_group_skip PASSED")


def test_compound_forward():
    """Verify compound forward produces valid logits with a mock model."""
    from pacs.compound.compound_forward import CompoundSparseForward

    # --- Mock model ---
    class MockAttention(torch.nn.Module):
        def __init__(self):
            super().__init__()
            # hidden_dim=56 → 28 Q heads × head_dim=2
            self.linear = torch.nn.Linear(56, 56)

        def forward(self, hidden_states, **kwargs):
            return (self.linear(hidden_states),)

    class MockLayer(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.self_attn = MockAttention()
            self.mlp = torch.nn.Linear(56, 56)

        def forward(self, hidden_states, **kwargs):
            attn_out = self.self_attn(hidden_states)[0]
            return (self.mlp(attn_out),)

    class MockConfig:
        num_hidden_layers = 2
        num_attention_heads = 28
        num_key_value_heads = 4

    class MockModel(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.layers = torch.nn.ModuleList([MockLayer() for _ in range(2)])
            self.lm_head = torch.nn.Linear(56, 100)
            self.config = MockConfig()

        def forward(self, input_ids, attention_mask=None, **kwargs):
            bsz, seq_len = input_ids.shape
            hidden = torch.randn(bsz, seq_len, 56)
            for layer in self.layers:
                hidden = layer(hidden)[0]
            logits = self.lm_head(hidden)

            class Output:
                pass

            out = Output()
            out.logits = logits
            return out

    model = MockModel()

    head_mask = HeadMask(
        active_q_heads=list(range(20)),
        active_kv_heads=[0, 1, 2],
        q_head_mask=torch.tensor([True] * 20 + [False] * 8),
        kv_head_mask=torch.tensor([True, True, True, False]),
    )
    kv_mask = KVMask(
        active_positions=torch.arange(8),
        position_mask=torch.tensor([True] * 8 + [False] * 8),
        keep_ratio_actual=0.5,
    )

    csf = CompoundSparseForward(model, device="cpu")
    input_ids = torch.randint(0, 100, (1, 16))
    logits = csf.forward(input_ids, head_mask=head_mask, kv_mask=kv_mask)

    assert logits.shape == (1, 16, 100), f"Expected (1, 16, 100), got {logits.shape}"
    assert torch.isfinite(logits).all(), "Logits contain non-finite values"

    # Without any masks — should also work
    logits_dense = csf.forward(input_ids)
    assert logits_dense.shape == (1, 16, 100)
    print("test_compound_forward PASSED")


def test_head_mask_effect():
    """Masking heads should produce different output than dense."""
    from pacs.compound.compound_forward import CompoundSparseForward

    class MockAttention(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.linear = torch.nn.Linear(28, 28)

        def forward(self, hidden_states, **kwargs):
            return (self.linear(hidden_states),)

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

    class MockModel(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.layers = torch.nn.ModuleList([MockLayer() for _ in range(1)])
            self.lm_head = torch.nn.Linear(28, 50)
            self.config = MockConfig()

        def forward(self, input_ids, attention_mask=None, **kw):
            torch.manual_seed(0)
            h = torch.randn(input_ids.shape[0], input_ids.shape[1], 28)
            for layer in self.layers:
                h = layer(h)[0]

            class Output:
                pass

            out = Output()
            out.logits = self.lm_head(h)
            return out

    model = MockModel()
    csf = CompoundSparseForward(model, device="cpu")
    ids = torch.randint(0, 50, (1, 8))

    logits_dense = csf.forward(ids)
    head_mask = HeadMask(
        active_q_heads=list(range(14)),
        active_kv_heads=[0, 1],
        q_head_mask=torch.tensor([True] * 14 + [False] * 14),
        kv_head_mask=torch.tensor([True, True, False, False]),
    )
    logits_sparse = csf.forward(ids, head_mask=head_mask)

    # Masked heads are zeroed → outputs must differ
    assert not torch.allclose(logits_dense, logits_sparse), "Head masking had no effect"
    print("test_head_mask_effect PASSED")


if __name__ == "__main__":
    test_gqa_grouping()
    test_head_selection()
    test_kv_eviction()
    test_kv_bos_protection()
    test_head_mask_kv_group_skip()
    test_compound_forward()
    test_head_mask_effect()
    print("\nAll tests PASSED")
