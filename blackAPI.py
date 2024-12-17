import requests
import json
import re

class BlackBox:
    def __init__(self):
        self.url = 'https://www.blackbox.ai/api/chat'

        # Define the headers
        self.headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'cookie': 'sessionId=6e8e280c-ef9c-410d-a61e-2104cdb87e73; intercom-id-jlmqxicb=8504a3f5-8ff9-481b-af80-0cfc30db8a8d; intercom-device-id-jlmqxicb=70deede7-8309-4384-b7dc-4a0d56bfa7bb; __Host-authjs.csrf-token=dbf25c0808d90a39e748e43ec2b628709c5cec74cbb6dcbf740426a0a19ddba3%7C477f0feac46e15b1fac93cec899e9740365dfde2be4a53c51125d3211bc587f8; __Secure-authjs.callback-url=https%3A%2F%2Fwww.blackbox.ai',
            'origin': 'https://www.blackbox.ai',
            'pragma': 'no-cache',
            'referer': 'https://www.blackbox.ai/',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }
        self.query = None
        self.max_tokens = None
        self.forced_web_search = None
        self.image_generation = None
        self.web_search_mode = None
        self.references = []
        self.image_Links = []
        self.prog_Lang = None
        self.code = None


    def get_Raw_Response(self,query,max_tokens=500,forced_web_search=False,image_generation=False,web_search_mode=False):

        self.query = query
        self.max_tokens = max_tokens
        self.forced_web_search = forced_web_search
        self.image_generation = image_generation
        self.web_search_mode = web_search_mode
        # Define the payload
        payload = {
            "messages": [
                {
                    "id": {"Use Your chat_id"},
                    "content": f"in short {query}",
                    "role": "user"
                }
            ],
            "id": "Am8ruQb",
            "previewToken": None,
            "userId": None,
            "codeModelMode": True,
            "agentMode": {},
            "trendingAgentMode": {},
            "isMicMode": False,
            "userSystemPrompt": None,
            "maxTokens": max_tokens,
            "playgroundTopP": None,
            "playgroundTemperature": None,
            "isChromeExt": False,
            "githubToken": "",
            "clickedAnswer2": False,
            "clickedAnswer3": False,
            "clickedForceWebSearch": forced_web_search,
            "visitFromDelta": False,
            "mobileClient": False,
            "userSelectedModel": None,
            "validated": "00f37b34-a166-4efb-bce5-1312d87f2f94",
            "imageGenerationMode": image_generation,
            "webSearchModePrompt": web_search_mode
        }
        response = requests.post(self.url, headers=self.headers, json=payload)
        return response.content
    #function to praise response
    def get_Response(self,query,max_tokens=500,forced_web_search=False,web_search_mode=False):
        response = str(self.get_Raw_Response(query,max_tokens,forced_web_search,web_search_mode).decode("utf-8")).replace("\n","")
        print(response)
        if "$~~~$" in  str(response):#contains references
            #print(str(response).split("$~~~$")[1])
            response_json = json.loads(str(response).split("$~~~$")[1])
            print(response_json)
            for _json in response_json:
                title = str(_json['title']).split("-")[-1].strip()
                if title == str(_json['title']):#doesnot contains - Reference name then it should be
                    title = str(_json['title']).split("|")[-1].strip().split(".")[0].capitalize()
                #if the also title doesn't updateesss then use link to update
                if title == str(_json['title']) or len(title.split())>1:
                    title = str(_json['link']).split("/")[2].split(".")[0].capitalize()
                    if title == "Www":title = str(_json['link']).split("/")[2].split(".")[1].capitalize()
                if "." in title:
                    title = title.split(".")[0].capitalize()
                self.references.append(f"{title}: {str(_json['link'])}, {str(_json['snippet'])}")
            print(self.references)
            #return f"""References : {self.references}\nResponse : {str(response).split("$~~~$")[2]}"""
        if "```" in str(response):
            resp = self.getCode_Response(query=f"{query}")
        if self.references:
            if self.prog_Lang is not None:
                return f"References : {self.references}\nResponse :{str(response).split('$~~~$')[2].split("```")[0]+str(response).split('$~~~$')[2].split("```")[2]}\nProg_lang : {self.prog_Lang}\ncode : {self.code}"
            return f"References : {self.references}, Response : {str(response).split('$~~~$')[2]}"
        else:
            if self.prog_Lang is not None:
                return f"Response :{str(response).split("```")[0] + str(response).split("```")[2]}\nProg_lang : {self.prog_Lang}\ncode : {self.code}"
            return f"Response : {str(response)}"

    def getImage_Response(self,query,numberOfImages):
        if numberOfImages>2:
            return "error{50010}"#meaning image limit exhausted please try with a less number of images(<=2)
        # response = b'![](https://storage.googleapis.com/a1aa/image/797dba36-f212-4f53-8bc2-023345ead7cc.jpeg)'
        for i in range(numberOfImages):
            response = self.get_Raw_Response(query,image_generation=True)
            response_link = str(response.decode("utf-8")).split("(")[1].split(")")[0]
            self.image_Links.append(response_link)
        return f"Images :{self.image_Links}"

    def getCode_Response(self,query):
        #response = """```python['python': 'import random\n\n# Function to check if a number is prime\n\ndef is_prime(num):\n\tif num < 2:\n\t\treturn False\n\tfor i in range(2, int(num**0.5) + 1):\n\t\tif num % i == 0:\n\t\t\treturn False\n\treturn True\n\n# Generate a list of prime numbers from 1 to 100\nprimes = [num for num in range(1, 101) if is_prime(num)]\n\n# Function to generate a random prime number\n\ndef random_prime():\n\treturn random.choice(primes)\n\n# Example usage\nprint(random_prime())\n']```"""
        postTestCheat = "use comments and use \\n  for new line in code and \\t for tab space in code also put the code in like ['{Programming_language_used}' : '{code}'] and for any other charcter like #$ keep it as it is]"
        response = self.get_Raw_Response(f"{query},{postTestCheat}").decode("utf-8").replace('\n',"")
        print(response)

        programmingLanguage = response.split("['")[1].split("'")[0].lower()
        print("Programming Language:", programmingLanguage)
        # Corrected regex to split the code part
        code = re.split(fr"\[\s*'{programmingLanguage}'\s*:\s*", response, flags=re.IGNORECASE)[1].split("']")[
                   0].strip()[1:]

        self.prog_Lang = programmingLanguage
        self.code = code.encode().decode('unicode_escape')
        return {f"{self.prog_Lang}" : f"{self.code}"}

if __name__ == '__main__':
    bb = BlackBox()
    # response_bb = bb.get_Response("who won the ipl in 2025")
    # print(response_bb)
    # response_ii = bb.getImage_Response("csk winning the ipl in 2025",2)
    # print(response_ii)
    response_gg = bb.get_Response("what is the use pg scanf show with an example")
    print(response_gg)
    # response_cc = bb.getCode_Response("Write a code in python to generate random prime numbers from 1 to 100")
    # print(response_cc)
    # response_cc = bb.getCode_Response("Write a code in java to generate random prime numbers from 1 to 100")
    # print(response_cc)
    """OUTPUT :
        `pg_scanf` is a function in the PostgreSQL database system that allows you to read formatted input from a string, similar to the standard C `scanf` function. It is often used in PostgreSQL's procedural language (PL/pgSQL) or in custom C functions to parse strings into variables based on a specified format.### Example UsageSuppose you have a string that contains a date in the format "YYYY-MM-DD" and you want to extract the year, month, and day into separate variables. You can use `pg_scanf` to achieve this.Here's a simple example in a PostgreSQL function:```sqlCREATE OR REPLACE FUNCTION parse_date(input_text TEXT)RETURNS TABLE(year INT, month INT, day INT) AS $$DECLARE    date_string TEXT := input_text;BEGIN    -- Use pg_scanf to extract year, month, and day    PERFORM pg_scanf(date_string, '%d-%d-%d', year, month, day);    RETURN;END;$$ LANGUAGE plpgsql;```### How to Call the FunctionYou can call this function with a date string:```sqlSELECT * FROM parse_date('2023-10-05');```### OutputThis would return:``` year | month | day------+-------+----- 2023 |    10 |   05```### Note- `pg_scanf` is not a standard SQL function and is specific to PostgreSQL's internal C functions. The example above is illustrative; in practice, you might use other string manipulation functions available in PostgreSQL for similar tasks.- Always check the PostgreSQL documentation for the version you are using, as functions and their availability may vary.
        The `pg scanf` function is used in PostgreSQL to read formatted input from a string. It is similar to the standard `scanf` function in C, allowing you to extract data from a string based on a specified format.Here's a short example demonstrating its use:```['SQL' : '-- Example of using pg scanf in PostgreSQL-- Declare a variable to hold the input string\tDECLARE\t\tinput_string TEXT := ''John, 25, Developer'';\t\tname TEXT;\t\tage INT;\t\toccupation TEXT;-- Use pg scanf to extract values from the input string\tBEGIN\t\t-- The format string specifies how to parse the input\t\tSELECT pg_scanf(''%[^,], %d, %[^'']'', input_string, name, age, occupation);\t\t-- Output the extracted values\t\tRAISE NOTICE ''Name: %, Age: %, Occupation: %'', name, age, occupation;\tEND;']]```### Explanation:- The `input_string` variable contains a string with comma-separated values.- The `pg_scanf` function is used to parse the string according to the specified format:  - `%[^,]` reads a string until a comma is encountered.  - `%d` reads an integer.  - `%[^'']` reads a string until a single quote is encountered.- The extracted values are stored in the `name`, `age`, and `occupation` variables.- Finally, the `RAISE NOTICE` statement outputs the extracted values.
        Programming Language: sql
        Response :`pg_scanf` is a function in the PostgreSQL database system that allows you to read formatted input from a string, similar to the standard C `scanf` function. It is often used in PostgreSQL's procedural language (PL/pgSQL) or in custom C functions to parse strings into variables based on a specified format.### Example UsageSuppose you have a string that contains a date in the format "YYYY-MM-DD" and you want to extract the year, month, and day into separate variables. You can use `pg_scanf` to achieve this.Here's a simple example in a PostgreSQL function:### How to Call the FunctionYou can call this function with a date string:
        Prog_lang : sql
        code : -- Example of using pg scanf in PostgreSQL-- Declare a variable to hold the input string	DECLARE		input_string TEXT := ''John, 25, Developer'';		name TEXT;		age INT;		occupation TEXT;-- Use pg scanf to extract values from the input string	BEGIN		-- The format string specifies how to parse the input		SELECT pg_scanf(''%[^,], %d, %[^'  
    """