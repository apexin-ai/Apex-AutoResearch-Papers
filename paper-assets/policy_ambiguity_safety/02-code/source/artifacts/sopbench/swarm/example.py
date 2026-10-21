import os
import json 

from swarm.llm_handler import OpenAIHandler
from swarm.core import Swarm
from swarm.constants import OPENAI_MODELS
from swarm.util import function_to_json
from swarm.types import Agent, Response, Result
from domains.bank.bank_assistant import actions 
from domains.bank.bank import Bank


if __name__ == "__main__":
    # Test case for batch_inference
    user_agent = Agent(
        client=OpenAIHandler(
            model_name="gpt-4o-mini",
            tool_calling=False,
        ),  
        instructions="""
        You are trying to apply for a loan using your username, and you want to know the amount owed to the bank as well as whether your loan application was successful.
        
        Your information is as follows:
        username: alice_smith
        """,
        functions=[]
    )
    
    init_database = {
            "accounts": {
                "john_doe": {
                    "identification": "padoesshnwojord",
                    "admin_password": "[REDACTED]",
                    "balance": 1000.0,
                    "owed_balance": 200.0,
                    "safety_box": "John important documents"
                },
                "jane_doe": {
                    "identification": {
                        "drivers_license_id": "D1234567",
                        "drivers_license_state": "CA"
                    },
                    "admin_password": "[REDACTED]",
                    "balance": 500.0,
                    "owed_balance": 1000.0,
                    "safety_box": "Jane important documents"
                },
                "alice_smith": {
                    "identification": "a123456789",
                    "admin_password": "[REDACTED]",
                    "balance": 1500.0,
                    "owed_balance": 300.0,
                    "safety_box": "Alice important documents"
                }
            },
            "foreign_exchange": {
                "EUR": 0.93,
                "RMB": 7.12,
                "GBP": 0.77,
                "NTD": 32.08
            }
        }
    bank = Bank(init_database)
    
    
    assistant_client = Agent(
        client=OpenAIHandler(
            model_name="gpt-4o-mini",
            tool_calling=False,
        ),  
        instructions="""
        You are trying to apply for a loan using your username, and you want to know the amount owed to the bank as well as whether your loan application was successful.
        
        Your information is as follows:
        username: alice_smith
        """,
        system=bank
    )

    