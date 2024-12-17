BlackBox API Integration
========================

Overview
--------

The **BlackBox** class is a Python implementation that interacts with the BlackBox AI API to facilitate chat-based queries, image generation, and code generation. This class allows users to send queries and receive structured responses, including references, code snippets, and images.

Features
--------

*   **Chat Queries**: Send queries to the BlackBox AI and receive detailed responses.
    
*   **Image Generation**: Request image generation based on a query.
    
*   **Code Generation**: Generate code snippets in various programming languages based on user queries.
    
*   **References**: Automatically extract and format references from the responses.
    

Installation
------------

To use the **BlackBox** class, ensure you have Python installed on your machine. You will also need the **requests** library, which can be installed via pip:

```bash 
pip install requests
```

Usage
-----

### Step 1: Import the Class

First, import the **BlackBox** class into your Python script.

```python 
from blackAPI import BlackBox
```

### Step 2: Create an Instance

Create an instance of the **BlackBox** class.

```python 
bb = BlackBox()
```

### Step 3: Send a Query

You can send a query using the **get\_Response** method. This method takes the query string and optional parameters for maximum tokens and web search mode.

```python
response = bb.get_Response("What is the use of pg_scanf with an example?")  2print(response)
```

### Step 4: Generate Images

To generate images based on a query, use the **getImage\_Response** method. Specify the number of images you want (up to 2).

```python
image_response = bb.getImage_Response("CSK winning the IPL in 2025", 2)  2print(image_response)
```

### Step 5: Generate Code

To generate code snippets, use the **getCode\_Response** method. Provide a query that specifies the code you want to generate.

```python
code_response = bb.getCode_Response("Write a code in Python to generate random prime numbers from 1 to 100")  2print(code_response)
```

### Example

Here’s a complete example of how to use the **BlackBox** class:

```python
if __name__ == '__main__':
bb = BlackBox()
# Send a chat query
response = bb.get_Response("What is the use of pg_scanf with an example?")
print(response)
# Generate images
image_response = bb.getImage_Response("CSK winning the IPL in 2025", 2)
print(image_response)
# Generate code
code_response = bb.getCode_Response("Write a code in Python to generate random prime numbers from 1 to 100")
print(code_response)
```

Methods
-------

### **get\_Raw\_Response(query, max\_tokens=500, forced\_web\_search=False, image\_generation=False, web\_search\_mode=False)**

*   **Parameters**:
    
    *   **query**: The query string to send to the API.
        
    *   **max\_tokens**: Maximum number of tokens in the response (default is 500).
        
    *   **forced\_web\_search**: Boolean to enable forced web search (default is False).
        
    *   **image\_generation**: Boolean to enable image generation (default is False).
        
    *   **web\_search\_mode**: Boolean to enable web search mode (default is False).
        
*   **Returns**: Raw response content from the API.
    

### **get\_Response(query, max\_tokens=500, forced\_web\_search=False, web\_search\_mode=False)**

*   **Parameters**: Same as **get\_Raw\_Response**.
    
*   **Returns**: Formatted response string including references if available.
    

### **getImage\_Response(query, numberOfImages)**

*   **Parameters**:
    
    *   **query**: The query string for image generation.
        
    *   **numberOfImages**: The number of images to generate (maximum 2).
        
*   **Returns**: Links to the generated images.
    

### **getCode\_Response(query)**

*   **Parameters**:
    
    *   **query**: The query string for code generation.
        
*   **Returns**: A dictionary containing the programming language and the generated code.
    

Notes
-----

*   Ensure that you replace your chat id you can get from opening a new chat with black box web .
    *  **link**: https://www.blackbox.ai/chat/fXUwoqS
    *  **chatID** : fXUwoqs
    
*   The class is designed to handle various types of queries, but the quality of responses may vary based on the input provided.
    

License
-------

This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
------------

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

Contact
-------

For any questions or feedback, please reach out to the repository owner.
