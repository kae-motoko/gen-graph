import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold


def initialize_gemini_model(api_key, version="gemini-1.5-flash"):
    """
    Initialize the Gemini model configuration.

    Args:
        api_key (str): Your Google API key for accessing Gemini.
        version (str): The version of the Gemini model to use. Default is "gemini-1.5-flash".

    Returns:
        genai.GenerativeModel: Configured Gemini model.
    """
    # Configure the API key
    genai.configure(api_key=api_key)

    # Initialize the model
    model = genai.GenerativeModel(version)
    return model


def get_generation_config(temperature=0.1, candidate_count=1, max_output_tokens=300):
    """
    Define the generation configuration for the Gemini model.

    Args:
        temperature (float): Controls randomness of the output. Default is 0.1.
        candidate_count (int): Number of candidates to generate. Default is 1.
        max_output_tokens (int): Maximum tokens in the output. Default is 300.

    Returns:
        genai.types.GenerationConfig: Configuration object for generation.
    """
    return genai.types.GenerationConfig(
        temperature=temperature,
        candidate_count=candidate_count,
        max_output_tokens=max_output_tokens,
    )


def get_safety_settings():
    """
    Define safety settings for the Gemini model to allow or block certain categories of content.

    Returns:
        dict: Safety settings configuration.
    """
    return {
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    }