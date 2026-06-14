from src.prompts import build_dynamic_prompt
from src.agent import create_sql_reasoning_agent

def main():
    # 1. Initialize core components
    print("Initializing Agent and Vector Store...")
    agent_executor = create_sql_reasoning_agent()
    dynamic_prompt_template = build_dynamic_prompt()

    # 2. Capture user input
    user_question = "What is the total revenue we would generate if we sold all remaining extra large black Levi shirts at their final discounted price?"

    # 3. Format the prompt dynamically (Triggers Vector Search)
    system_instructions = dynamic_prompt_template.format(Question=user_question)

    # 4. Execute the agent
    print(f"\nUser: {user_question}")
    print("Agent is reasoning...\n")
    
    response = agent_executor.invoke({
        "messages": [
            ("system", system_instructions),
            ("user", user_question)
        ]
    })  

    # 5. Output the final result
    print("Final Answer:")
    print(response["messages"][-1].content)

if __name__ == "__main__":
    main()