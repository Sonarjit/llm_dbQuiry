from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from src.few_shots import few_shots

def build_dynamic_prompt() -> FewShotPromptTemplate:
    """Builds the dynamic few-shot prompt using Chroma and Hugging Face."""
    
    # 1. Initialize local embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # 2. Build the Example Selector (Vector Store)
    example_selector = SemanticSimilarityExampleSelector.from_examples(
        examples=few_shots,
        embeddings=embeddings,
        vectorstore_cls=Chroma,
        k=2,
        input_keys=["Question"]
    )

    # 3. Define single example format
    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery"],
        template="User Input: {Question}\nSQL Query: {SQLQuery}"
    )

    # 4. Assemble the master dynamic template
    return FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=(
            "You are a highly accurate MySQL data analyst agent.\n"
            "CRITICAL RULES:\n"
            "1. Map sizes: 'extra small' -> 'XS', 'small' -> 'S', 'medium' -> 'M', 'large' -> 'L'.\n"
            "2. Case Insensitivity: Always use LOWER() for brand and color matching.\n"
            "3. Only execute read-only SELECT queries.\n\n"
            "Here are examples of how to structure your queries:"
        ),
        suffix="\n\nUser Input: {Question}\nSQL Query:",
        input_variables=["Question"],
    )