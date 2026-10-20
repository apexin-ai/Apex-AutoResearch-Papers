import json
from swarm.util import (
    _generate_random_id, 
    ChatCompletion, 
    ChatCompletionMessage, 
    ChatCompletionMessageToolCall, 
    Function
)

ReAct_FORMAT_INSTRUCTIONS_SYSTEM_FUNCTION = """
Always attempt to solve tasks by leveraging the available tools. You have access to the following tools:

{func_str}

## RESPONSE ACTION FORMAT
For every response, please adhere strictly to the following format:
Thought: Describe your reasoning before taking any action.
Action: Specify the action to execute. This must be one of {func_list} (include only the function name).
Action Input: Provide the input arguments for the action in JSON format. For example: {{"arg1": "value1", "arg2": "value2"}}
<End Action>

**Example Response Format:**
Thought: [Your reasoning here]  
Action: [one of {func_list}]  
Action Input: [Arguments in JSON format]  
<End Action>

## Important: 
- Your response must be in the format of Thought, Action, Action Input, <End Action> without any other information.
- You can use at most ONE function per response.
- If you decide not to take any action, use Action: N/A and Action Input: N/A.
"""

ReAct_Verify_FORMAT_INSTRUCTIONS_SYSTEM_FUNCTION = """
Always attempt to solve tasks by leveraging the available tools. You have access to the following tools:

{func_str}

## RESPONSE ACTION FORMAT
For every response, please adhere strictly to the following format:
Thought: Describe your reasoning before taking any action.
Eligibility: Check if it is eligible to take the planned action under the current context.
Action: Specify the action to execute. This must be one of {func_list} (include only the function name).
Action Input: Provide the input arguments for the action in JSON format. For example: {{"arg1": "value1", "arg2": "value2"}}
<End Action>

**Example Response Format:**
Thought: [Your reasoning here]  
Eligibility: [Yes/No]  
Action: [one of {func_list}]  
Action Input: [Arguments in JSON format]  
<End Action>

## Important: 
- Your response must be in the format of Thought, Eligibility, Action, Action Input, <End Action> without any other information.
- You can use at most ONE function per response.
- If the planned action is not eligible, or you decide not to take any action, use Eligibility: No and Action: N/A and Action Input: N/A.
"""

ReAct_wo_REASON_FORMAT_INSTRUCTIONS_SYSTEM_FUNCTION = """
Always attempt to solve tasks by leveraging the available tools. You have access to the following tools:

{func_str}

## RESPONSE ACTION FORMAT
For every response, please adhere strictly to the following format:
Action: Specify the action to execute. This must be one of {func_list} (include only the function name).
Action Input: Provide the input arguments for the action in JSON format. For example: {{"arg1": "value1", "arg2": "value2"}}
<End Action>

**Example Response Format:**
Action: [one of {func_list}]  
Action Input: [Arguments in JSON format]  
<End Action>

## Important: 
- Your response must be in the format of Action, Action Input, <End Action> without any other information.
- You can use at most ONE function per response.
- If you determine no action is needed, respond with Action: None and Action Input: None.
"""

ReAct_TOOL_CALL_TEMPLATE = """
Thought: {content}
Action: {function_name}
Action Input: {function_args}
<End Action>
"""

ReAct_Verify_TOOL_CALL_TEMPLATE = """
Thought: {content}
Action: {function_name}
Action Input: {function_args}
<End Action>
"""

Act_ONLY_TOOL_CALL_TEMPLATE = """
{content}Action: {function_name}
Action Input: {function_args}
<End Action>
"""

TOOL_RESPONSE_TEMPLATE = """
Observation ({function_call}):
{content}
"""

def convert_assistant_message(message, called_tools, response_template):
    """
    Input OpenAI assistant message:
        {
        "content": null,
        "refusal": null,
        "role": "assistant",
        "audio": null,
        "function_call": null,
        "tool_calls": [
        {
            "id": "call_S0HG9X1tquIb0gnnhnmXumwI",
            "function": {
            "arguments": "{\"username\":\"alex_smith\"}",
            "name": "internal_check_username_exist"
            },
            "type": "function"
        }
        ],
        "sender": "bank assistant"
    }
    """
    assert message["role"] == "assistant"
    content = message["content"]
    if message.get("tool_calls", []):
        tool_call_id = message["tool_calls"][0]["id"]
        function_name = message["tool_calls"][0]["function"]["name"]
        function_args = message["tool_calls"][0]["function"]["arguments"]
        # record the tool call
        called_tools[tool_call_id] = {"function_name": function_name, "function_args": function_args}
        text = response_template.format(content=content, function_name=function_name, function_args=function_args)
    else:
        # use N/A if no tool call
        text = response_template.format(content=content, function_name="N/A", function_args="N/A")
    return {"role": "assistant", "content": text}, called_tools

def convert_tool_message(message, called_tools):
    assert message["role"] == "tool"
    tool_call_id = message["tool_call_id"]
    function_name = called_tools[tool_call_id]["function_name"]
    function_args = called_tools[tool_call_id]["function_args"]
    function_call = {function_name: function_args}
    function_call_str = json.dumps(function_call)
    tool_response = message["content"]
    text = TOOL_RESPONSE_TEMPLATE.format(function_call=function_call_str, content=tool_response)
    return {"role": "user", "content": text}

def merge_user_messages(messages):
    """
    If there are consecutive user messages, merge them into one user message.
    Args:
        messages: List of message dictionaries with 'role' and 'content' keys
    Returns:
        new_messages: List of messages with consecutive user messages merged
    """
    new_messages = []
    current_user_content = []
    
    for message in messages:
        if message["role"] == "user":
            current_user_content.append(message["content"])
        else:
            # If we have accumulated user messages, merge them before adding non-user message
            if current_user_content:
                new_messages.append({
                    "role": "user",
                    "content": "\n".join(current_user_content)
                })
                current_user_content = []
            new_messages.append(message)
    
    # Handle any remaining user messages at the end
    if current_user_content:
        new_messages.append({
            "role": "user",
            "content": "\n".join(current_user_content)
        })
    
    return new_messages

def convert_ReAct_into_openai_format(completion: ChatCompletion) -> ChatCompletion:
    """
    Convert the response from the ReAct tool calling format into the openai format.
    
    Args:
        completion: ChatCompletion object containing ReAct format response
        
    Returns:
        ChatCompletion object in OpenAI format with tool calls
        
    Example ReAct format:
    Thought: I need to check the username
    Action: internal_check_username_exist
    Action Input: {"username":"alex_smith"}
    <End Action>
    """
    # Get the message content from the first choice
    message = completion.choices[0].message
    content = message.content
    
    if not content:
        return completion
        
    # Check if this is a ReAct format response (has Action and Action Input)
    if "Action:" not in content or "Action Input:" not in content:
        return completion
        
    # Parse the ReAct format
    try:
        # Extract Thought, Action and Action Input sections
        # print(content)
        thought_match = content.split("Action:")[0].replace("Thought:", "").strip()
        action_match = content.split("Action:")[1].split("Action Input:")[0].strip()
        action_input_match = content.split("Action Input:")[1].split("<End Action>")[0].strip()
        
        # Additional validation - if any section is empty, return original completion
        if not action_match or not action_input_match:
            return completion
        
        # Create tool call
        tool_call = ChatCompletionMessageToolCall(
            id=f"call_{_generate_random_id()}",
            function=Function(
                name=action_match,
                arguments=action_input_match
            ),
            type="function"
        )
        
        # Create new message with thought as content and tool call
        new_message = ChatCompletionMessage(
            content=thought_match,
            role="assistant",
            tool_calls=[tool_call]
        )
        
        # Update the completion object
        completion.choices[0].message = new_message
        completion.choices[0].finish_reason = "tool_calls"
        
    except (IndexError, AttributeError):
        # If parsing fails, return original completion
        return completion
        
    return completion 

def ReAct_tool_calling(chat_completion_func, 
                       chat_completion_params, 
                       messages, 
                       tools, 
                       reasoning=True,
                       verification=False):
    """
    Receive the messages in the openai function calling format, and convert it into the format of chat completion messages.
    Return the converted messages.
    1. Add the ReAct format instructions to the system message.
    2. Convert the assistant tool call into text (Thought and Action)
    3. Convert the tool role message into user message (Observation)
    """
    called_tools = {}
    if not reasoning:
        input_template = ReAct_wo_REASON_FORMAT_INSTRUCTIONS_SYSTEM_FUNCTION
        response_template = ReAct_wo_REASON_TOOL_CALL_TEMPLATE
    elif verification:
        input_template = ReAct_Verify_FORMAT_INSTRUCTIONS_SYSTEM_FUNCTION
        response_template = ReAct_Verify_TOOL_CALL_TEMPLATE
    else:
        input_template = ReAct_FORMAT_INSTRUCTIONS_SYSTEM_FUNCTION
        response_template = ReAct_TOOL_CALL_TEMPLATE
    
    tool_list = [tool["function"]["name"] for tool in tools]
    tool_str = json.dumps(tools, indent=4)
    new_messages = []
    for message in messages:
        if message["role"] == "system":
            system_message = message["content"]
            system_message_w_func_doc = system_message + "\n\n" + input_template.format(func_str=tool_str, func_list=tool_list)
            new_messages.append({"role": "system", "content": system_message_w_func_doc})
        elif message["role"] == "assistant":
            converted_message, called_tools = convert_assistant_message(message, called_tools, response_template)
            new_messages.append(converted_message)
        elif message["role"] == "tool":
            # change the tool message into user message
            converted_message = convert_tool_message(message, called_tools)
            new_messages.append(converted_message)
        elif message["role"] == "user":
            # change the user message into assistant message
            new_messages.append(message)
        else:
            raise ValueError(f"Unknown message role: {message['role']}")

    # merge consecutive user messages into one user message
    new_messages = merge_user_messages(new_messages)
    
    # call the func to get the response
    chat_completion_params["messages"] = new_messages
    completion = chat_completion_func(**chat_completion_params)
    
    # change the response into the openai format
    new_completion = convert_ReAct_into_openai_format(completion)
    return new_completion


if __name__ == "__main__":
    """
    Test the ReAct_tool_calling function with a sample conversation.
    """
    # Define test tools
    tools = [
        {
            "name": "check_balance",
            "description": "Check the balance of a user's account",
            "parameters": {
                "type": "object",
                "properties": {
                    "username": {"type": "string"}
                },
                "required": ["username"]
            }
        }
    ]

    # Define test messages
    test_messages = [
        {
            "role": "system",
            "content": "You are a bank assistant."
        },
        {
            "role": "user",
            "content": "What's my balance?"
        },
        {
            "role": "assistant",
            "content": "Let me check your balance.",
            "tool_calls": [
                {
                    "id": "call_test123",
                    "function": {
                        "name": "check_balance",
                        "arguments": "{\"username\":\"test_user\"}"
                    },
                    "type": "function"
                }
            ]
        },
        {
            "role": "tool",
            "tool_call_id": "call_test123",
            "content": "$1000.00"
        },
        {
            "role": "user",
            "content": "Thanks!"
        },
        {
            "role": "user",
            "content": "Have a great day!"
        }
    ]