import torch


def get_turn_markers(tokenizer):
    chat_tpl = getattr(tokenizer, 'chat_template', '') or ''
    if 'im_start' in chat_tpl:
        return {'start': '<|im_start|>', 'end': '<|im_end|>', 'format': 'chatml'}
    elif 'start_header_id' in chat_tpl:
        return {'start': '<|start_header_id|>', 'end': '<|eot_id|>', 'format': 'llama3'}
    else:
        raise ValueError("Unsupported chat template for turn boundary detection")


def _get_special_token_ids(tokenizer):
    markers = get_turn_markers(tokenizer)
    fmt = markers['format']

    start_ids = tokenizer.encode(markers['start'], add_special_tokens=False)
    end_ids = tokenizer.encode(markers['end'], add_special_tokens=False)
    assert len(start_ids) == 1, f"Expected {markers['start']} to be a single token, got {start_ids}"
    assert len(end_ids) == 1, f"Expected {markers['end']} to be a single token, got {end_ids}"

    result = {
        'start_id': start_ids[0],
        'end_id': end_ids[0],
        'format': fmt,
    }

    if fmt == 'llama3':
        eh_ids = tokenizer.encode('<|end_header_id|>', add_special_tokens=False)
        assert len(eh_ids) == 1, f"Expected <|end_header_id|> to be a single token, got {eh_ids}"
        result['end_header_id'] = eh_ids[0]

    return result


def _find_all_positions(input_ids, token_id):
    if isinstance(input_ids, torch.Tensor):
        return (input_ids == token_id).nonzero(as_tuple=True)[0].tolist()
    return [i for i, t in enumerate(input_ids) if t == token_id]


def _parse_turns_chatml(ids_list, start_positions, end_positions, seq_len, tokenizer):
    newline_id = tokenizer.encode("\n", add_special_tokens=False)
    newline_id = newline_id[0] if len(newline_id) == 1 else None

    turns = []
    for i, start_pos in enumerate(start_positions):
        end_pos = end_positions[i] if i < len(end_positions) else seq_len - 1

        role_token_pos = start_pos + 1
        role_str = None
        content_start = role_token_pos

        scan_end = min(start_pos + 10, end_pos)
        for j in range(role_token_pos, scan_end):
            if newline_id is not None and ids_list[j] == newline_id:
                role_tokens = ids_list[role_token_pos:j]
                role_str = tokenizer.decode(role_tokens).strip()
                content_start = j + 1
                break

        if role_str is None:
            partial = tokenizer.decode(ids_list[role_token_pos:scan_end]).strip()
            for r in ("system", "user", "assistant"):
                if partial.startswith(r):
                    role_str = r
                    break
            if role_str is None:
                role_str = "unknown"
            content_start = role_token_pos + len(tokenizer.encode(role_str, add_special_tokens=False)) + 1

        content_start = min(content_start, end_pos)

        turns.append({
            "role": role_str,
            "start": start_pos,
            "end": end_pos,
            "content_start": content_start,
            "content_end": end_pos,
        })
    return turns


def _parse_turns_llama3(ids_list, start_positions, end_positions, seq_len, tokenizer, end_header_id):
    newline_id = tokenizer.encode("\n", add_special_tokens=False)
    newline_id = newline_id[0] if len(newline_id) == 1 else None

    turns = []
    for i, start_pos in enumerate(start_positions):
        end_pos = end_positions[i] if i < len(end_positions) else seq_len - 1

        eh_pos = None
        scan_end = min(start_pos + 10, end_pos)
        for j in range(start_pos + 1, scan_end):
            if ids_list[j] == end_header_id:
                eh_pos = j
                break

        if eh_pos is not None:
            role_tokens = ids_list[start_pos + 1:eh_pos]
            role_str = tokenizer.decode(role_tokens).strip()
            content_start = eh_pos + 1
            while content_start < end_pos and newline_id is not None and ids_list[content_start] == newline_id:
                content_start += 1
        else:
            role_str = "unknown"
            content_start = start_pos + 1

        content_start = min(content_start, end_pos)

        turns.append({
            "role": role_str,
            "start": start_pos,
            "end": end_pos,
            "content_start": content_start,
            "content_end": end_pos,
        })
    return turns


def detect_turn_boundaries(input_ids: torch.Tensor, tokenizer, gar_variant="ours") -> dict:
    if input_ids.dim() != 1:
        raise ValueError(f"Expected 1D input_ids, got shape {input_ids.shape}")

    seq_len = input_ids.size(0)
    token_info = _get_special_token_ids(tokenizer)
    start_id = token_info['start_id']
    end_id = token_info['end_id']
    fmt = token_info['format']
    ids_list = input_ids.tolist()

    start_positions = _find_all_positions(ids_list, start_id)
    end_positions = _find_all_positions(ids_list, end_id)

    if fmt == 'chatml':
        turns = _parse_turns_chatml(ids_list, start_positions, end_positions, seq_len, tokenizer)
    elif fmt == 'llama3':
        turns = _parse_turns_llama3(ids_list, start_positions, end_positions, seq_len, tokenizer, token_info['end_header_id'])

    goal_token_positions = []
    first_user_found = False
    for turn in turns:
        if turn["role"] == "system":
            goal_token_positions.extend(range(turn["content_start"], turn["content_end"]))
        elif turn["role"] == "user" and not first_user_found:
            if gar_variant == "ours":
                goal_token_positions.extend(range(turn["content_start"], turn["content_end"]))
            first_user_found = True

    assistant_last_token_positions = []
    assistant_all_token_positions = []
    for turn in turns:
        if turn["role"] == "assistant" and turn["content_end"] > turn["content_start"]:
            assistant_last_token_positions.append(turn["content_end"] - 1)
            if gar_variant == "dongre":
                assistant_all_token_positions.append(
                    list(range(turn["content_start"], turn["content_end"]))
                )

    boundary_positions = set()
    for pos in start_positions:
        boundary_positions.add(pos)
    for pos in end_positions:
        boundary_positions.add(pos)

    turn_distance_map = torch.zeros(seq_len, dtype=torch.long)
    dist = 0
    for i in range(seq_len):
        if i in boundary_positions:
            dist = 0
        turn_distance_map[i] = dist
        dist += 1

    turn_index_map = torch.zeros(seq_len, dtype=torch.long)
    current_turn = 0
    in_turn = False
    for i in range(seq_len):
        if ids_list[i] == start_id:
            if in_turn:
                current_turn += 1
            in_turn = True
        turn_index_map[i] = current_turn

    return {
        "turns": turns,
        "goal_token_positions": goal_token_positions,
        "assistant_last_token_positions": assistant_last_token_positions,
        "assistant_all_token_positions": assistant_all_token_positions,
        "turn_distance_map": turn_distance_map,
        "turn_index_map": turn_index_map,
    }


def build_turn_features(input_ids: torch.Tensor, tokenizer) -> dict:
    if input_ids.dim() != 1:
        raise ValueError(f"Expected 1D input_ids, got shape {input_ids.shape}")

    seq_len = input_ids.size(0)
    token_info = _get_special_token_ids(tokenizer)
    start_id = token_info['start_id']
    end_id = token_info['end_id']
    ids_list = input_ids.tolist()

    boundary_set = set()
    for i, tid in enumerate(ids_list):
        if tid == start_id or tid == end_id:
            boundary_set.add(i)

    turn_distance = torch.zeros(seq_len, dtype=torch.long)
    dist = 0
    for i in range(seq_len):
        if i in boundary_set:
            dist = 0
        turn_distance[i] = dist
        dist += 1

    turn_index = torch.zeros(seq_len, dtype=torch.long)
    current_turn = 0
    started = False
    for i in range(seq_len):
        if ids_list[i] == start_id:
            if started:
                current_turn += 1
            started = True
        turn_index[i] = current_turn

    is_turn_boundary = torch.zeros(seq_len, dtype=torch.bool)
    for pos in boundary_set:
        is_turn_boundary[pos] = True

    return {
        "turn_distance": turn_distance,
        "turn_index": turn_index,
        "is_turn_boundary": is_turn_boundary,
    }
