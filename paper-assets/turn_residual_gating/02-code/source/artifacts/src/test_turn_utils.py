"""Mock-based tests for turn_utils.py with Qwen ChatML and Llama-3 formats."""
import unittest
from unittest.mock import MagicMock
import torch

from turn_utils import get_turn_markers, _get_special_token_ids, detect_turn_boundaries, build_turn_features


# --- Token ID constants for mocks ---
# Qwen ChatML
QWEN_IM_START = 151644
QWEN_IM_END = 151645
QWEN_NEWLINE = 198

# Llama-3
LLAMA_START_HEADER = 128006
LLAMA_END_HEADER = 128007
LLAMA_EOT = 128009
LLAMA_NEWLINE = 13


def _make_qwen_tokenizer():
    tok = MagicMock()
    tok.chat_template = (
        "{% for message in messages %}"
        "<|im_start|>{{ message.role }}\n{{ message.content }}<|im_end|>\n"
        "{% endfor %}"
    )

    token_map = {
        '<|im_start|>': [QWEN_IM_START],
        '<|im_end|>': [QWEN_IM_END],
        '\n': [QWEN_NEWLINE],
        'system': [9125],
        'user': [882],
        'assistant': [77091],
    }

    decode_map = {
        9125: 'system',
        882: 'user',
        77091: 'assistant',
    }

    def encode_fn(text, add_special_tokens=False):
        if text in token_map:
            return token_map[text]
        tokens = []
        for word in text.split():
            if word in token_map:
                tokens.extend(token_map[word])
            else:
                tokens.append(hash(word) % 100000)
        return tokens if tokens else [hash(text) % 100000]

    def decode_fn(token_ids):
        if isinstance(token_ids, int):
            token_ids = [token_ids]
        parts = []
        for tid in token_ids:
            if tid in decode_map:
                parts.append(decode_map[tid])
            else:
                parts.append(f'<tok_{tid}>')
        return ' '.join(parts)

    tok.encode = encode_fn
    tok.decode = decode_fn
    return tok


def _make_llama3_tokenizer():
    tok = MagicMock()
    tok.chat_template = (
        "{% for message in messages %}"
        "<|start_header_id|>{{ message.role }}<|end_header_id|>\n\n"
        "{{ message.content }}<|eot_id|>"
        "{% endfor %}"
    )

    token_map = {
        '<|start_header_id|>': [LLAMA_START_HEADER],
        '<|end_header_id|>': [LLAMA_END_HEADER],
        '<|eot_id|>': [LLAMA_EOT],
        '\n': [LLAMA_NEWLINE],
        'system': [1791],
        'user': [882],
        'assistant': [78191],
    }

    decode_map = {
        1791: 'system',
        882: 'user',
        78191: 'assistant',
    }

    def encode_fn(text, add_special_tokens=False):
        if text in token_map:
            return token_map[text]
        tokens = []
        for word in text.split():
            if word in token_map:
                tokens.extend(token_map[word])
            else:
                tokens.append(hash(word) % 100000)
        return tokens if tokens else [hash(text) % 100000]

    def decode_fn(token_ids):
        if isinstance(token_ids, int):
            token_ids = [token_ids]
        parts = []
        for tid in token_ids:
            if tid in decode_map:
                parts.append(decode_map[tid])
            else:
                parts.append(f'<tok_{tid}>')
        return ' '.join(parts)

    tok.encode = encode_fn
    tok.decode = decode_fn
    return tok


def _build_qwen_conversation():
    """Build: system + user + assistant + user + assistant (Qwen ChatML)."""
    sys_content = [1001, 1002]
    user1_content = [2001, 2002, 2003]
    asst1_content = [3001, 3002]
    user2_content = [4001]
    asst2_content = [5001, 5002, 5003]

    ids = []
    # system turn
    ids.append(QWEN_IM_START)
    ids.append(9125)        # "system"
    ids.append(QWEN_NEWLINE)
    ids.extend(sys_content)
    ids.append(QWEN_IM_END)
    # user turn 1
    ids.append(QWEN_IM_START)
    ids.append(882)         # "user"
    ids.append(QWEN_NEWLINE)
    ids.extend(user1_content)
    ids.append(QWEN_IM_END)
    # assistant turn 1
    ids.append(QWEN_IM_START)
    ids.append(77091)       # "assistant"
    ids.append(QWEN_NEWLINE)
    ids.extend(asst1_content)
    ids.append(QWEN_IM_END)
    # user turn 2
    ids.append(QWEN_IM_START)
    ids.append(882)
    ids.append(QWEN_NEWLINE)
    ids.extend(user2_content)
    ids.append(QWEN_IM_END)
    # assistant turn 2
    ids.append(QWEN_IM_START)
    ids.append(77091)
    ids.append(QWEN_NEWLINE)
    ids.extend(asst2_content)
    ids.append(QWEN_IM_END)

    return torch.tensor(ids, dtype=torch.long)


def _build_llama3_conversation():
    """Build: system + user + assistant + user + assistant (Llama-3)."""
    sys_content = [1001, 1002]
    user1_content = [2001, 2002, 2003]
    asst1_content = [3001, 3002]
    user2_content = [4001]
    asst2_content = [5001, 5002, 5003]

    ids = []
    # system turn
    ids.append(LLAMA_START_HEADER)
    ids.append(1791)             # "system"
    ids.append(LLAMA_END_HEADER)
    ids.append(LLAMA_NEWLINE)    # \n
    ids.append(LLAMA_NEWLINE)    # \n
    ids.extend(sys_content)
    ids.append(LLAMA_EOT)
    # user turn 1
    ids.append(LLAMA_START_HEADER)
    ids.append(882)              # "user"
    ids.append(LLAMA_END_HEADER)
    ids.append(LLAMA_NEWLINE)
    ids.append(LLAMA_NEWLINE)
    ids.extend(user1_content)
    ids.append(LLAMA_EOT)
    # assistant turn 1
    ids.append(LLAMA_START_HEADER)
    ids.append(78191)            # "assistant"
    ids.append(LLAMA_END_HEADER)
    ids.append(LLAMA_NEWLINE)
    ids.append(LLAMA_NEWLINE)
    ids.extend(asst1_content)
    ids.append(LLAMA_EOT)
    # user turn 2
    ids.append(LLAMA_START_HEADER)
    ids.append(882)
    ids.append(LLAMA_END_HEADER)
    ids.append(LLAMA_NEWLINE)
    ids.append(LLAMA_NEWLINE)
    ids.extend(user2_content)
    ids.append(LLAMA_EOT)
    # assistant turn 2
    ids.append(LLAMA_START_HEADER)
    ids.append(78191)
    ids.append(LLAMA_END_HEADER)
    ids.append(LLAMA_NEWLINE)
    ids.append(LLAMA_NEWLINE)
    ids.extend(asst2_content)
    ids.append(LLAMA_EOT)

    return torch.tensor(ids, dtype=torch.long)


class TestGetTurnMarkers(unittest.TestCase):

    def test_qwen_detected(self):
        tok = _make_qwen_tokenizer()
        markers = get_turn_markers(tok)
        self.assertEqual(markers['format'], 'chatml')
        self.assertEqual(markers['start'], '<|im_start|>')
        self.assertEqual(markers['end'], '<|im_end|>')

    def test_llama3_detected(self):
        tok = _make_llama3_tokenizer()
        markers = get_turn_markers(tok)
        self.assertEqual(markers['format'], 'llama3')
        self.assertEqual(markers['start'], '<|start_header_id|>')
        self.assertEqual(markers['end'], '<|eot_id|>')

    def test_unsupported_raises(self):
        tok = MagicMock()
        tok.chat_template = "some unknown template"
        with self.assertRaises(ValueError):
            get_turn_markers(tok)

    def test_no_chat_template(self):
        tok = MagicMock(spec=[])
        with self.assertRaises(ValueError):
            get_turn_markers(tok)


class TestGetSpecialTokenIds(unittest.TestCase):

    def test_qwen_ids(self):
        tok = _make_qwen_tokenizer()
        info = _get_special_token_ids(tok)
        self.assertEqual(info['start_id'], QWEN_IM_START)
        self.assertEqual(info['end_id'], QWEN_IM_END)
        self.assertEqual(info['format'], 'chatml')
        self.assertNotIn('end_header_id', info)

    def test_llama3_ids(self):
        tok = _make_llama3_tokenizer()
        info = _get_special_token_ids(tok)
        self.assertEqual(info['start_id'], LLAMA_START_HEADER)
        self.assertEqual(info['end_id'], LLAMA_EOT)
        self.assertEqual(info['format'], 'llama3')
        self.assertEqual(info['end_header_id'], LLAMA_END_HEADER)


class TestDetectTurnBoundariesQwen(unittest.TestCase):

    def setUp(self):
        self.tok = _make_qwen_tokenizer()
        self.input_ids = _build_qwen_conversation()

    def test_turn_count(self):
        result = detect_turn_boundaries(self.input_ids, self.tok)
        self.assertEqual(len(result['turns']), 5)

    def test_roles(self):
        result = detect_turn_boundaries(self.input_ids, self.tok)
        roles = [t['role'] for t in result['turns']]
        self.assertEqual(roles, ['system', 'user', 'assistant', 'user', 'assistant'])

    def test_assistant_last_positions(self):
        result = detect_turn_boundaries(self.input_ids, self.tok)
        self.assertEqual(len(result['assistant_last_token_positions']), 2)
        for pos in result['assistant_last_token_positions']:
            self.assertGreater(pos, 0)
            self.assertLess(pos, len(self.input_ids))

    def test_goal_positions_ours(self):
        result = detect_turn_boundaries(self.input_ids, self.tok, gar_variant="ours")
        self.assertGreater(len(result['goal_token_positions']), 0)

    def test_goal_positions_dongre(self):
        result = detect_turn_boundaries(self.input_ids, self.tok, gar_variant="dongre")
        goal = result['goal_token_positions']
        for t in result['turns']:
            if t['role'] == 'user':
                for pos in range(t['content_start'], t['content_end']):
                    self.assertNotIn(pos, goal)

    def test_content_boundaries(self):
        result = detect_turn_boundaries(self.input_ids, self.tok)
        for turn in result['turns']:
            self.assertLessEqual(turn['content_start'], turn['content_end'])
            self.assertGreaterEqual(turn['content_start'], turn['start'])
            self.assertLessEqual(turn['content_end'], turn['end'])

    def test_turn_index_map(self):
        result = detect_turn_boundaries(self.input_ids, self.tok)
        tim = result['turn_index_map']
        self.assertEqual(tim.shape[0], len(self.input_ids))
        self.assertTrue((tim >= 0).all())
        self.assertEqual(tim.max().item(), 4)

    def test_1d_required(self):
        with self.assertRaises(ValueError):
            detect_turn_boundaries(self.input_ids.unsqueeze(0), self.tok)


class TestDetectTurnBoundariesLlama3(unittest.TestCase):

    def setUp(self):
        self.tok = _make_llama3_tokenizer()
        self.input_ids = _build_llama3_conversation()

    def test_turn_count(self):
        result = detect_turn_boundaries(self.input_ids, self.tok)
        self.assertEqual(len(result['turns']), 5)

    def test_roles(self):
        result = detect_turn_boundaries(self.input_ids, self.tok)
        roles = [t['role'] for t in result['turns']]
        self.assertEqual(roles, ['system', 'user', 'assistant', 'user', 'assistant'])

    def test_assistant_last_positions(self):
        result = detect_turn_boundaries(self.input_ids, self.tok)
        self.assertEqual(len(result['assistant_last_token_positions']), 2)

    def test_content_start_skips_newlines(self):
        result = detect_turn_boundaries(self.input_ids, self.tok)
        ids_list = self.input_ids.tolist()
        for turn in result['turns']:
            if turn['content_start'] < turn['content_end']:
                self.assertNotEqual(ids_list[turn['content_start']], LLAMA_NEWLINE)

    def test_goal_positions_ours(self):
        result = detect_turn_boundaries(self.input_ids, self.tok, gar_variant="ours")
        self.assertGreater(len(result['goal_token_positions']), 0)

    def test_turn_index_map(self):
        result = detect_turn_boundaries(self.input_ids, self.tok)
        tim = result['turn_index_map']
        self.assertEqual(tim.shape[0], len(self.input_ids))
        self.assertEqual(tim.max().item(), 4)

    def test_turn_distance_resets_at_boundaries(self):
        result = detect_turn_boundaries(self.input_ids, self.tok)
        tdm = result['turn_distance_map']
        ids_list = self.input_ids.tolist()
        for i, tid in enumerate(ids_list):
            if tid == LLAMA_START_HEADER or tid == LLAMA_EOT:
                self.assertEqual(tdm[i].item(), 0)


class TestBuildTurnFeaturesQwen(unittest.TestCase):

    def setUp(self):
        self.tok = _make_qwen_tokenizer()
        self.input_ids = _build_qwen_conversation()

    def test_keys(self):
        result = build_turn_features(self.input_ids, self.tok)
        self.assertIn('turn_distance', result)
        self.assertIn('turn_index', result)
        self.assertIn('is_turn_boundary', result)

    def test_shapes(self):
        result = build_turn_features(self.input_ids, self.tok)
        seq_len = len(self.input_ids)
        self.assertEqual(result['turn_distance'].shape[0], seq_len)
        self.assertEqual(result['turn_index'].shape[0], seq_len)
        self.assertEqual(result['is_turn_boundary'].shape[0], seq_len)

    def test_boundary_at_special_tokens(self):
        result = build_turn_features(self.input_ids, self.tok)
        ids_list = self.input_ids.tolist()
        for i, tid in enumerate(ids_list):
            if tid == QWEN_IM_START or tid == QWEN_IM_END:
                self.assertTrue(result['is_turn_boundary'][i].item())
                self.assertEqual(result['turn_distance'][i].item(), 0)


class TestBuildTurnFeaturesLlama3(unittest.TestCase):

    def setUp(self):
        self.tok = _make_llama3_tokenizer()
        self.input_ids = _build_llama3_conversation()

    def test_shapes(self):
        result = build_turn_features(self.input_ids, self.tok)
        seq_len = len(self.input_ids)
        self.assertEqual(result['turn_distance'].shape[0], seq_len)
        self.assertEqual(result['turn_index'].shape[0], seq_len)

    def test_boundary_at_special_tokens(self):
        result = build_turn_features(self.input_ids, self.tok)
        ids_list = self.input_ids.tolist()
        for i, tid in enumerate(ids_list):
            if tid == LLAMA_START_HEADER or tid == LLAMA_EOT:
                self.assertTrue(result['is_turn_boundary'][i].item())
                self.assertEqual(result['turn_distance'][i].item(), 0)

    def test_turn_index_monotonic(self):
        result = build_turn_features(self.input_ids, self.tok)
        ti = result['turn_index']
        for i in range(1, len(ti)):
            self.assertGreaterEqual(ti[i].item(), ti[i - 1].item())


if __name__ == '__main__':
    unittest.main()
