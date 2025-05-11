## Configuration Setup

To use this project, you need to configure the properties file. Follow these steps:

1. Navigate to the `config/` directory:
   ```bash
   cd gen-graph/config
   ```

2. Copy the template file:
   ```bash
   cp properties.example.yaml properties.yaml
   ```

3. Open the `properties.yaml` file in a text editor:
   ```bash
   nano properties.yaml
   ```

4. Replace the placeholder values with your actual configuration details:
   ```yaml
   api_key: "YOUR_API_KEY_HERE"
   model_version: "gemini-1.5-flash"
   temperature: 0.1
   candidate_count: 1
   max_output_tokens: 300
   ```

5. Save the file. The project will now use the settings from `properties.yaml`.

> **Note:** Do not upload your `properties.yaml` file to the repository to keep your API keys and other sensitive information secure.