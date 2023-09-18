### Flask API

#### Hosted API Link - http://ankur36.pythonanywhere.com/

#### Usage
- Route `/`
    - Headers: Authorization/{'token': 'API_KEY'}
    - method: GET
    - Response: {'msg': 'Hello, world'}

- Route `/data`
    - Headers: Authorization/{'token': 'API_KEY'}
    - method: GET
    - Response: [
        {
            "age": 45,
            "city": "abc",
            "name": "xyz",
            "salary": 45000
        },
        {
            "age": 47,
            "city": "abcd",
            "name": "abc",
            "salary": 450000
        }
    ]